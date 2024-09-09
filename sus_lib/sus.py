import matplotlib.pyplot as plt
import csv
import numpy as np
from tkinter import filedialog
NUMBER_OF_INTERVALS = 10
ACCEPTABILITY_RANGES = ['NOT ACCEPTABLE', 'LOW MARGINAL', 'HIGH MARGINAL', 'ACCEPTABLE']
GRADES = ['A', 'B', 'C', 'D', 'F']
ADJECTIVE_RATINGS = ['WORST IMAGINABLE', 'POOR', 'OK', 'GOOD', 'EXCELLENT', 'BEST IMAGINABLE']

def import_from_csv(answers = None):
    if answers is None or isinstance(answers, str):
        if isinstance(answers, str):
            csv_file = answers
        else:
            csv_file = filedialog.askopenfilename(filetypes=[(".csv files", "*.csv")])
        try:
            with open(csv_file, 'r') as file:
                answers = [[int(item) for item in answer] for answer in  list(csv.reader(file, delimiter=';'))]
        except FileNotFoundError:
            raise ValueError("File not found")
    return answers

def calculate_sus_values(answers = None):
    answers = import_from_csv(answers)

    if not isinstance(answers, list):
        raise TypeError("Input must be a list")

    if all(isinstance(item, list) for item in answers):
        return [calculate_sus_values(item) for item in answers]
    
    if not (all(isinstance(item, int) and 1 <= item <= 5 for item in answers) and len(answers) == 10):
        raise TypeError("Input must be a list of 10 integers from range <1, 5>")
        
    even = 0
    odd = 0
    for i, answer in enumerate(answers):
        if i % 2 == 0:
            odd += answer
        else:
            even += answer
    value = 2.5 * (20 + odd - even)
    return value

def show_statistics(answers = None, output_path: str = None):
    answers = import_from_csv(answers)

    sus_values = calculate_sus_values(answers)
    if isinstance(sus_values, float):
        statistics = (
            f"{'Statistic':<20}{'Value':<20}\n"
            f"{'-' * 40}\n"
            f"{'SUS value':<20}{sus_values:<20.2f}\n"
            f"{'Acceptability':<20}{calculate_acceptability(sus_values):<20}\n"
            f"{'Grade':<20}{calculate_grade(sus_values):<20}\n"
            f"{'Adjective':<20}{calculate_adjective(sus_values):<20}\n"
        )
    else:
        np_sus_values = np.array(sus_values)
        mean_value = np.mean(np_sus_values)
        std_deviation = np.std(np_sus_values, ddof=1)
        q1 = np.percentile(np_sus_values, 25)
        median_value = np.median(np_sus_values)
        q3 = np.percentile(np_sus_values, 75)

        acceptabilities = calculate_acceptabilities(answers)
        grades = calculate_grades(answers)
        adjectives = calculate_adjectives(answers)

        accept_count = [calculate_acceptabilities(answers).count(range) for range in ACCEPTABILITY_RANGES]
        grade_count = [calculate_grades(answers).count(grade) for grade in GRADES]
        adjective_count = [calculate_adjectives(answers).count(adjective) for adjective in ADJECTIVE_RATINGS]

        statistics = (
            f"{'Statistic':<20}{'Value':<20}\n"
            f"{'-'*40}\n"
            f"{'Mean':<20}{mean_value:<20.2f}\n"
            f"{'Standard Deviation':<20}{std_deviation:<20.2f}\n"
            f"{'First Quartile (Q1)':<20}{q1:<20.2f}\n"
            f"{'Median (Q2)':<20}{median_value:<20.2f}\n"
            f"{'Third Quartile (Q3)':<20}{q3:<20.2f}\n"
            f"\n\n"
            f"{'Acceptability':<20}{'Number':<20}\n"
            f"{'-'*40}\n"
        )
        for i, label in enumerate(ACCEPTABILITY_RANGES):
            statistics += f"{label:<20}{accept_count[i]:<20}\n"
        statistics += (
            f"\n\n"
            f"{'Grades':<20}{'Number':<20}\n"
            f"{'-'*40}\n"
        )
        for i, label in enumerate(GRADES):
            statistics += f"{label:<20}{grade_count[i]:<20}\n"
        statistics += (
            f"\n\n"
            f"{'Adjectives':<20}{'Number':<20}\n"
            f"{'-'*40}\n"
        )
        for i, label in enumerate(ADJECTIVE_RATINGS):
            statistics += f"{label:<20}{adjective_count[i]:<20}\n"
        statistics += (
            f"\n\n"
            f"{'SUS Value':<15}{'Acceptability':<15}{'Grade':<15}{'Adjective':<15}\n"
            f"{'-'*60}\n"
        )
        for i in range(len(sus_values)):
            statistics += f"{sus_values[i]:<15.2f}{acceptabilities[i]:<15}{grades[i]:<15}{adjectives[i]:<15}\n"

    
    print(statistics)
    if not isinstance(output_path, str):
        output_path = filedialog.asksaveasfilename(initialfile="results.txt",defaultextension=".txt", filetypes=[("Text files", "*.txt"),("All files", "*.*")])
    try:
        with open(output_path, "w") as file:
            file.write(statistics)
        print("Results have been saved to results.txt")
    except Exception as e:
        print(f"Could not save results to file: \n{e}")

### CHARTS ###

def sus_value_histogram(answers = None):
    answers = import_from_csv(answers)
    sus_values = calculate_sus_values(answers)
    plt.xlabel('SUS values')
    plt.ylabel('Number of responses')
    plt.title('Number of responses with a given SUS value')
    plt.hist(sus_values, bins= NUMBER_OF_INTERVALS, range=[0, 100], edgecolor='white')
    plt.show()

def acceptability_bar_chart(answers = None):
    answers = import_from_csv(answers)
    sus_acceptabilities = calculate_acceptabilities(answers)

    plt.xlabel('Acceptabilities')
    plt.ylabel('Number of responses')
    plt.title('Number of responses with a given acceptability range')
    plt.bar(ACCEPTABILITY_RANGES, [sus_acceptabilities.count(acceptability) for acceptability in ACCEPTABILITY_RANGES])
    plt.show()

def grade_bar_chart(answers = None):
    answers = import_from_csv(answers)
    sus_grades = calculate_grades(answers)

    plt.xlabel('Grades')
    plt.ylabel('Number of responses')
    plt.title('Number of responses with a given grade')
    plt.bar(GRADES, [sus_grades.count(grade) for grade in GRADES])
    plt.show()

def adjective_bar_chart(answers = None):
    answers = import_from_csv(answers)
    sus_adjectives = calculate_adjectives(answers)

    plt.xlabel('Adjectives')
    plt.ylabel('Number of responses')
    plt.title('Number of responses with a given adjective ratings')
    plt.bar(ADJECTIVE_RATINGS, [sus_adjectives.count(adjective) for adjective in ADJECTIVE_RATINGS])
    plt.show()


### METRICS ###

def calculate_acceptability(value: float):
    if not isinstance(value, float):
        raise TypeError("Input must be a float")
    if value < 0 or value > 100:
        raise ValueError("Invalid SUS value")

    if value < 50:
        return 'NOT ACCEPTABLE'
    elif value < 62.5:
        return 'LOW MARGINAL'
    elif value < 70:
        return 'HIGH MARGINAL'
    else:
        return 'ACCEPTABLE'

def calculate_acceptabilities(answers = None):
    sus_values = calculate_sus_values(answers)
    if isinstance(sus_values, float):
        sus_values = [sus_values]
    return [calculate_acceptability(sus_value) for sus_value in sus_values]

def calculate_grade(value: float):
    if not isinstance(value, float):
        raise TypeError("Input must be a float")
    if value < 0 or value > 100:
        raise ValueError("Invalid SUS value")

    if value < 60:
        return 'F'
    elif value < 70:
        return 'D'
    elif value < 80:
        return 'C'
    elif value < 90:
        return 'B'
    else:
        return 'A'
    
def calculate_grades(answers = None):
    sus_values = calculate_sus_values(answers)
    if isinstance(sus_values, float):
        sus_values = [sus_values]
    return [calculate_grade(sus_value) for sus_value in sus_values]

def calculate_adjectives(answers = None):
    sus_values = calculate_sus_values(answers)
    if isinstance(sus_values, float):
        sus_values = [sus_values]
    return [calculate_adjective(sus_value) for sus_value in sus_values]

def calculate_adjective(value: float):
    if not isinstance(value, float):
        raise TypeError("Input must be a float")
    if value < 0 or value > 100:
        raise ValueError("Invalid SUS value")
    
    if value < 25:
        return 'WORST IMAGINABLE'
    elif value < 39:
        return 'POOR'
    elif value < 52:
        return 'OK'
    elif value < 73:
        return 'GOOD'
    elif value < 85:
        return 'EXCELLENT'
    else:
        return 'BEST IMAGINABLE'
