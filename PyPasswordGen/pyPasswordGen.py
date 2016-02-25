""" 
	Python Password Generator
			Version 1.0
	Created by CodeBarbarian

My goal was to port a C++ application I saw years ago, and it works.

"""
import os
import time

""" 
SPECIFIC APPLICATION VARIABLES
"""
# Filename
file_name = "password"
# File extension
file_extension = "txt"
# Minimum size of password
min_size = 1
# Maximum size of password
max_size = 5
# DEBUG?
debug = False

# Opens the file stream
f = open(str(file_name) + "." + str(file_extension), 'w')

"""
ASCII DEFINITIONS
"""
# All the numbers 0 - 9 on the ASCII TABLE
numbers = range(48, 58)
# All the upper case letters in the alphabet on the ASCII TABLE
upperAlpha = range(65, 91)
# All the lower case letters in the alphabet on the ASCII TABLE
lowerAlpha = range(97, 123)

menu_item = 0

while int(menu_item) not in range(1,5):
	menu_item = input(''' 
		[1] - Numbers
		[2] - Upper Case Letters
		[3] - Lower Case Letter
		[4] - Numbers, Upper and Lower case Letters
		
		Selection: ''')

selection = []
if menu_item == 1:
	# Appending the numbers to the selection
	selection += numbers
elif menu_item == 2:
	# Appending the Uppercase Characters to the selection
	selection += upperAlpha
elif menu_item == 3:
	# Appending the Lowercase Characters to the selection
	selection += lowerAlpha
elif menu_item == 4:
	# Appending the numbers to the selection
	selection += numbers
	# Appending the Uppercase Characters to the selection
	selection += upperAlpha
	# Appending the Lowercase Characters to the selection
	selection += lowerAlpha

charList = []
for i in selection:
	charList.append(str(chr(i)))

def nrOfSelections(items, seq):
	if seq == 0: 
		yield []
	else:
		for item in xrange(len(items)):
			for rec in nrOfSelections(items, seq-1):
				yield [items[item]]+rec


# To keep track of how many passwords are created
count = 0

# When we begin generating passwords
start_time = time.time()

# The main generation loop
for i in range(min_size, max_size+1):

    for s in nrOfSelections(charList, i):
        # Increasing the count
        count += 1
        # Writing the password to the file
        f.write(''.join(s) + '\n')
        # If the debug is set to true, display passwords(By turning this on, everything slows down)
        if debug:
        	print s
# Closing the file stream
f.close()

# When we are finished generating passwords
end_time = time.time()

# Information output
print "It took " + str(end_time - start_time) + " seconds to compute " + str(count) + " passwords!"








