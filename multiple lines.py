# Ray Allessandra D. Pacis | BSCPE 1-5 
# Write a method in python to write multiple line of text contents into a text file mylife.txt. 

import pyfiglet
from termcolor import colored, cprint

print_yellow = lambda x: cprint(x, 'yellow')

# open mylife.txt(write)
with open("mylife.txt", 'w') as input_file:

    # create loop
    while True:
        # ask user for input
        user_input = input("Enter something: ")
        # write user's input to mylife.txt
        input_file.write("Enter something: " + str(user_input) + '\n')
        # ask the user if they want to add more lines
        reply = input("\n DO YOU WANT TO PUT ANOTHER LINE? YES/No? ")

        # write user's input to mylife.txt
        input_file.write("DO YOU WANT TO PUT ANOTHER LINE? YES/No? " + str(reply) + '\n')
        # if yes:
        if reply == "Y" or reply == "Yes" or reply == "YES" or reply == "yes":
             continue
        # if no:
        if reply == "N" or reply == "No" or reply == "NO" or reply == "no":
                exit("\n\tHave a great day!")
        # if user input is invalid
        else:
            print("\tYou can type either YES, Yes, yes, Y or NO, No, no, N.") #These are the only acceptable inputs
            break
# end of program