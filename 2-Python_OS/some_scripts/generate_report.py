#!/usr/bin/env python3
import csv
import os

parent_dir = os.path.dirname(os.getcwd())
os.chdir(parent_dir)
os.chdir("data")
file_path = "employees.csv"

def read_employees(csv_file_location):
        file = open(csv_file_location)
        """DictReader creates an object that operates like a regular reader (an object that iterates over lines in the given CSV file),
	but also maps the information it reads into a dictionary where keys are given by the optional fieldnames parameter.
	If we omit the fieldnames parameter, the values in the first row of the CSV file will be used as the keys. So, in this case,
	the first line of the CSV file has the keys and so there's no need to pass fieldnames as a parameter."""
        #The main purpose of this dialect is to remove any leading spaces while parsing the CSV file.
        csv.register_dialect('empDialect',skipinitialspace=True,strict=True)
	#DictReader is used to read a  csv file and at the same time it maps the data (key, values) to a dictionary
        employee_file = csv.DictReader(open(csv_file_location),dialect = 'empDialect')
        employee_list = []
        for data in employee_file:
                employee_list.append(data)
        return employee_list

employee_list = read_employees(file_path)

def process_data(employee_list):
        department_list = []
        for employee_data in employee_list:
                department_list.append(employee_data['Department'])
        department_data = {}
        for department_name in set(department_list):
                department_data[department_name] = department_list.count(department_name)
        return department_data

dictionary = process_data(employee_list)

def write_report(dictionary, report_file):
        with open(report_file, "w+") as f:
                for k in sorted(dictionary):
                        f.write(str(k)+':'+str(dictionary[k])+'\n')
                f.close()

os.chdir(parent_dir)
os.chdir("script")
os.chdir("data_generated")
write_report(dictionary, os.path.abspath("report.txt"))
