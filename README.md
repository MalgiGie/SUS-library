# SUS-Lib
## Introduction
The System Usability Scale Library is a software package designed to streamline the process of computing usability scores using the Software Usability Scale. SUS-Lib simplifies the evaluation of software usability by allowing users to input survey data and automatically generating SUS scores along with detailed graphical representations. The package is designed to be user-friendly, requiring minimal knowledge of Python or command line tools.

## Motivation
Evaluating software usability is crucial for improving user experience, yet many existing tools require advanced technical skills or significant resources. The decentralized nature of usability studies, conducted across varied platforms and user groups, presents challenges in data consistency and accessibility. SUS-Lib addresses these issues by offering a user-friendly, open-source tool that simplifies the calculation of SUS scores. By reducing the technical barriers and resource demands, SUS-Lib ensures that usability evaluations can be easily integrated into various research and testing environments, making the process more accessible and efficient.

## Usage
To use the sus_lib library, ensure you have Python 3.6 or above installed. First, install the required dependencies. Navigate to the directory where setup.py is located and run:

```
pip install .
```

The sus_lib package provides various functions for importing answers from a CSV file, calculating SUS values, generating statistics, and displaying charts.
* `import_from_csv`: Imports answers from a CSV file.
* `calculate_sus_values`: Computes SUS values based on user answers.
* `show_statistics`: Displays various SUS-related statistics, including mean, standard deviation, and quartiles.
* `sus_value_histogram`: Plots a histogram of SUS values.
* `acceptability_bar_chart`: Generates a bar chart for SUS acceptability categories.
* `grade_bar_chart`: Generates a bar chart showing the distribution of grades.
* `adjective_bar_chart`: Plots a bar chart for adjective ratings.

## Usage examples
### import_from_csv
Input:

`answers`: Optional parameter. If provided, it should be either None or a string representing the path to a CSV file. In other cases, the input remains unchanged and is returned as the result.

Output: 

Returns a list of lists where each sublist represents a row from the CSV file, with each value converted to an integer.

```
from sus_lib import import_from_csv

import_from_csv()

import_from_csv("path_to_your_file.csv")
```

### calculate_sus_values
Input: 

`answers`: Optional parameter. Can be None, a string representing the path to a CSV file with data, a single list of 10 integers from 1 to 5 representing SUS responses or a list of them.

Output: 

Returns the SUS score as a float or a list of floats if answers is a list of lists.

```
from sus_lib import calculate_sus_values

values = calculate_sus_values()

values = calculate_sus_values("path_to_your_file.csv")

values = calculate_sus_values([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])

values = calculate_sus_values([[1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
                               [2, 3, 4, 5, 1, 2, 3, 5, 3, 3],
                               [3, 4, 5, 1, 2, 3, 4, 1, 1, 2]])
```

### show_statistics
Input:

`answers`: Optional parameter. Can be None, a string representing the path to a CSV file with data, a single list of 10 integers from 1 to 5 representing SUS responses or a list of them.

`output_path`: Optional parameter. Can be a string.

Output: 

Displays statistics to the console and saves them to a specified text file.

```
from sus_lib import show_statistics

show_statistics()

show_statistics("path_to_your_file.csv")

show_statistics([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])

show_statistics([[1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
                 [2, 3, 4, 5, 1, 2, 3, 5, 3, 3],
                 [3, 4, 5, 1, 2, 3, 4, 1, 1, 2]])
```

### sus_value_histogram
Input: 

`answers`: Optional parameter. Can be None, a string representing the path to a CSV file with data, a single list of 10 integers from 1 to 5 representing SUS responses or a list of them.

Output: 

Displays a histogram of SUS values.

```
from sus_lib import sus_value_histogram

sus_value_histogram()

sus_value_histogram("path_to_your_file.csv")

sus_value_histogram([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])

sus_value_histogram([[1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
                     [2, 3, 4, 5, 1, 2, 3, 5, 3, 3],
                     [3, 4, 5, 1, 2, 3, 4, 1, 1, 2]])
```
### acceptability_bar_chart
Input: 

`answers`: Optional parameter. Can be None, a string representing the path to a CSV file with data, a single list of 10 integers from 1 to 5 representing SUS responses or a list of them.

Output: 

Displays a bar chart of the acceptability ranges.

```
from sus_lib import acceptability_bar_chart

acceptability_bar_chart()

acceptability_bar_chart("path_to_your_file.csv")

acceptability_bar_chart([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])

acceptability_bar_chart([[1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
                         [2, 3, 4, 5, 1, 2, 3, 5, 3, 3],
                         [3, 4, 5, 1, 2, 3, 4, 1, 1, 2]])
```

### grade_bar_chart
Input: 

`answers`: Optional parameter. Can be None, a string representing the path to a CSV file with data, a single list of 10 integers from 1 to 5 representing SUS responses or a list of them.

Output: 

Displays a bar chart of the SUS grades.

```
from sus_lib import grade_bar_chart

grade_bar_chart()

grade_bar_chart("path_to_your_file.csv")

grade_bar_chart([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])

grade_bar_chart([[1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
                 [2, 3, 4, 5, 1, 2, 3, 5, 3, 3],
                 [3, 4, 5, 1, 2, 3, 4, 1, 1, 2]])
```

### adjective_bar_chart
Input: 

`answers`: Optional parameter. Can be None, a string representing the path to a CSV file with data, a single list of 10 integers from 1 to 5 representing SUS responses or a list of them.

Output: 

Displays a bar chart of adjective ratings based on SUS values.

```
from sus_lib import grade_bar_chart

adjective_bar_chart()

adjective_bar_chart("path_to_your_file.csv")

adjective_bar_chart([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])

adjective_bar_chart([[1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
                     [2, 3, 4, 5, 1, 2, 3, 5, 3, 3],
                     [3, 4, 5, 1, 2, 3, 4, 1, 1, 2]])
```

### calculate_acceptability
| Input               | Output           |
|---------------------|------------------|
| `value` < 50        | 'NOT ACCEPTABLE' |
| 50 ≤ `value` < 62.5 | 'LOW MARGINAL'   | 
| 62.5 ≤ `value` < 70 | 'HIGH MARGINAL'  | 
| `value` ≥ 70        | 'ACCEPTABLE'     | 

Input: 

`value`: A single SUS value as a float.

Output: 

Returns a string representing the acceptability range (e.g., 'NOT ACCEPTABLE', 'ACCEPTABLE').


```
from sus_lib import calculate_acceptability

acceptability = calculate_acceptability(78.7)
```

### calculate_acceptabilities

Input: 

`answers`: Optional parameter. Can be None, a string representing the path to a CSV file with data, a single list of 10 integers from 1 to 5 representing SUS responses or a list of them.

Output: 

Returns a list of acceptability ranges corresponding to the SUS values.

```
from sus_lib import calculate_acceptabilities

acceptabilities = calculate_acceptabilities()

acceptabilities = calculate_acceptabilities("path_to_your_file.csv")

acceptabilities = calculate_acceptabilities([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])

acceptabilities = calculate_acceptabilities([[1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
                                             [2, 3, 4, 5, 1, 2, 3, 5, 3, 3],
                                             [3, 4, 5, 1, 2, 3, 4, 1, 1, 2]])
```

### calculate_grade
| Input             | Output |
|-------------------|-------|
| `value` < 60      | 'F'   |
| 60 ≤ `value` < 70 | 'D'   | 
| 70 ≤ `value` < 80 | 'C'   | 
| 80 ≤ `value` < 90 | 'B'   | 
| `value` ≥ 90      | 'A'   | 

Input: 

`value`: A single SUS value as a float.

Output: 

Returns a string representing the grade ('A', 'B', 'C', 'D', 'F').

```
from sus_lib import calculate_grade

grade = calculate_grade(78.7)
```

### calculate_grades

Input: 

`answers`: Optional parameter. Can be None, a string representing the path to a CSV file with data, a single list of 10 integers from 1 to 5 representing SUS responses or a list of them.

Output: 

Returns a list of acceptability ranges corresponding to the SUS values.

```
from sus_lib import calculate_grades

grades = calculate_grades()

grades = calculate_grades("path_to_your_file.csv")

grades = calculate_grades([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])

grades = calculate_grades([[1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
                           [2, 3, 4, 5, 1, 2, 3, 5, 3, 3],
                           [3, 4, 5, 1, 2, 3, 4, 1, 1, 2]])
```
### calculate_adjective
| Input             | Output             |
|-------------------|--------------------|
| `value` < 25      | 'WORST IMAGINABLE' |
| 25 ≤ `value` < 39 | 'POOR'             | 
| 39 ≤ `value` < 52 | 'OK'               | 
| 52 ≤ `value` < 73 | 'GOOD'             | 
| 73 ≤ `value` < 85 | 'EXCELLENT'        | 
| `value` ≥ 85      | 'BEST IMAGINABLE'  | 

Input: 

`value`: A single SUS value as a float.

Output: 

Returns a string representing the adjective rating (e.g., 'WORST IMAGINABLE', 'BEST IMAGINABLE').

```
from sus_lib import calculate_adjective

adjective = calculate_adjective(78.7)
```

### calculate_adjectives

Input: 

`answers`: Optional parameter. Can be None, a string representing the path to a CSV file with data, a single list of 10 integers from 1 to 5 representing SUS responses or a list of them.

Output: 

Returns a list of acceptability ranges corresponding to the SUS values.

```
from sus_lib import calculate_adjectives

adjectives = calculate_adjectives()

adjectives = calculate_adjectives("path_to_your_file.csv")

adjectives = calculate_adjectives([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])

adjectives = calculate_adjectives([[1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
                                   [2, 3, 4, 5, 1, 2, 3, 5, 3, 3],
                                   [3, 4, 5, 1, 2, 3, 4, 1, 1, 2]])
```

# License
The SUS-Lib is provided under the MIT License.