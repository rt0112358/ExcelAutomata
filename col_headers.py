import pandas
#########################################
# Column/Feature Name Grabber
#
# Loads a user given csv file.
#
# Grabs the column names in order to,
#   setup the column names for a mysql
#   database. 
# 
# Meant to be a helper for,
#   xlsx/csv/mysql parsering programs.
#
# Usage:
#   $ python
#   >>> import col_headers
#   >>> col_headers.get_filename()
#########################################

# Setup user input for the filename
def get_filename():
    print("Enter csv file: ")
    filename = input()
    filename += '.csv'
    return filename

# Load the given csv file
def load_data(filename):
    csv_data = pandas.read_csv(filename, delimiter=',')
    print("\n\nLoaded data from " + str(filename))
    return csv_data

# Displays column names
def print_col_names(csv_data):
    print(csv_data.columns) # prints the column names via pandas data object.

    # Iterates through all of the column names.
    for feature in csv_data.columns:
        print(feature)

# Displays all csv data overview
def print_csv_data(csv_file):
    print(csv_file)




