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
 
# Example inputs:
#4-5 t: ftttttrvts
#7-8 k: kkkkkkkf
#4-6 k: gqjkkk
#1-2 t: rttb

int_range1 = 4
int_range2 = 8
var_char = 't'
var_string = 'ftttttrvts'

#print(var_string.count(var_char))

#if 10000 <= 12345 <= 30000:
#    print("pass")

#if 5 <= var_string.count(var_char) <= 9:
#   print("pass")

if int_range1 <= var_string.count(var_char) <= int_range2:
    print('pass')


parts = inputs.split("-")
print(parts[0])
print(parts[1])