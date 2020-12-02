# __file__ contains this file's filename, e.g. aoc_01_a.py when run from this
# directory or C:\code\aoc\python\2019\aoc_01_a.py when run from elsewhere.
# We want to replace the "_a.py" at the end with "_input" to get the correct
# input file name, e.g. aoc_01_input
input_file = __file__[:-5] + "_input"

# Open the input file
with open(input_file) as f:
    # Read the inputs line by line into variable "inputs"
    inputs = list(f)

# First steps: output _anything_ to check that things are running as expected
print('this is fine')
print(len(inputs))
 
# Example inputs: 4-5 t: ftttttrvts

import re

#match = re.match(r"(\d+)-(\d+)", line)
#int_range1 = int(match.group(1))
#int_range2 = int(match.group(2))
#var_char = 't'
#var_string = 'ftttttrvts'

for line in inputs:
    pattern = r"(\d+)-(\d+)"
    match = re.match(pattern, line)
    str_group1 = match.group(1)
    str_group2 = match.group(2)
    int_range1 = int(str_group1)
    int_range2 = int(str_group2)
    print(str_group1, type(str_group1), int_range1, type(int_range1))


if int_range1 <= var_string.count(var_char) <= int_range2:
    print('pass')

for line in inputs:    
    print(re.match(r"(\d+)", line))