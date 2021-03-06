# Computing summary statistics on the Iris dataset
# ================================================

# Task
# ----
#   - Load the Iris dataset (`data/iris.data`)
#   - Answer the following questions:
#     * What is the mean `sepal length` for Iris Setosa?
#     * What is the median `petal length` for Iris Virginica?
#     * What is the range of `sepal width` for Iris Versicolour?
#     * Which class (Setosa/Versicolour/Virginica) shows the highest variance in `petal width`?
#     * What is the 70% percentile for `sepal length` and `sepal width` (for all classes together)?
#     * Compute Absolute Average Deviation (AAD), Median Absolute Deviation (MAD), and Interquartile
#       Range (IQR) for `petal length` (for all classes together).

# Hint: you can exploit the fact that the input is ordered by class: the first 50 records are Iris Setosa,
# records 51-100 are Iris Versicolour, and records 101-150 are Iris Virginica.

# Solution
# --------

# This standard import changes the default behavior of division to always
# return a floating point value.
from __future__ import division

# We will use the **csv** module for reading in data from a file.
import csv

# The data set is stored in a comma-separated text file.
# We read it and store it as a list of records, where each record is represented using a dict.
def load_iris_data(filename):
    records = []
    with open(filename, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            if len(row) == 5:  # if we have 4 fields in that line
                records.append({
                    "sepal_length": float(row[0]),
                    "sepal_width": float(row[1]),
                    "petal_length": float(row[2]),
                    "petal_width": float(row[3]),
                    "class": row[4]
                })
    return records

iris_data = load_iris_data("../data/iris.data")

# Hints:
# Get a slice of the list, e.g., all Iris Versicolour records: iris_data[50:100]
# Get a given attribute as a list, e.g., sepal with: attr = [x['sepal_width'] for x in iris_data]
