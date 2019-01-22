##import re
##
##example_string = "Salil is 22 years old. Pep is 45 years old."
##
##names = re.findall(r'[A-Z][a-z]*', example_string)
##ages = re.findall(r'\d{1,2}', example_string)
##
##print names,ages

import re

example_string = 'Salil is 22 years old. Lionel is 30 years old. Cristiano is 33 years old'

names = re.findall(r'[A-Z][a-z]*',example_string)
ages = re.findall(r'\d{1,3}', example_string)

print names, ages
