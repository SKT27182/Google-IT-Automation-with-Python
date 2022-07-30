#!/usr/bin/env python3
import sys
import os
import re
from to_parent import change_dir_to_parent


change_dir_to_parent()
os.chdir("data")


def error_search(log_file):
  error = input("What is the error? ")
  returned_errors = []
  with open(log_file, mode='r',encoding='UTF-8') as file:
    for log in  file.readlines():
      error_patterns = ["error"]
      for i in range(len(error.split(' '))):
        error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
      if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
        returned_errors.append(log)
    file.close()
  return returned_errors
  
def file_output(returned_errors):
  change_dir_to_parent()
  os.chdir("script")
  os.chdir("data_generated")
  with open('errors_found.log', 'w') as file:
    for error in returned_errors:
      file.write(error)
    file.close()



def new_func(error_search, file_output):
    log_file = sys.argv[1]  #fishy.log
    returned_errors = error_search(log_file)
    file_output(returned_errors)
    sys.exit(0)

if __name__ == "__main__":
  new_func(error_search, file_output)

  