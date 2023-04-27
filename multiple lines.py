# Ray Allessandra D. Pacis | BSCPE 1-5 
# Write a method in python to write multiple line of text contents into a text file mylife.txt. 

import pyfiglet
from termcolor import colored, cprint

print_green = lambda x: cprint(x, 'green')
print_yellow = lambda x: cprint(x, 'yellow')
print_red = lambda x: cprint(x, 'red')
print_magenta = lambda x: cprint(x, 'magenta')

print_yellow('\n' + '-' * 100)
intro = pyfiglet.figlet_format("Hello User!", font = 'starwars', width = 100, justify = 'center')
print_magenta(intro)
welcome = "You can enter multiple messages and I'll save it in a file for you. You're welcome!"
welcome_center = welcome.center(100)
print_green(welcome_center)
print_yellow('-' * 100)

# open mylife.txt(write)
with open("mylife.txt", 'w') as input_file:

    # create loop
    while True:
        # ask user for input
        user_input = input("\033[0;32m" +"\nEnter something: \033[0m")
        import time
        print_magenta("...")
        time.sleep (2)

        # write user's input to mylife.txt
        input_file.write("Enter something: " + str(user_input) + '\n')
        # ask the user if they want to add more lines
        reply = input('\033[1m' + "\n DO YOU WANT TO PUT ANOTHER LINE? YES/No? ")

        # write user's input to mylife.txt
        input_file.write("\nDO YOU WANT TO PUT ANOTHER LINE? YES/No? " + str(reply) + '\n')
        # if yes:
        if reply == "Y" or reply == "y" or reply == "Yes" or reply == "YES" or reply == "yes":
            continue
        # if no:
        if reply == "N" or reply == "n" or reply == "No" or reply == "NO" or reply == "no":
            exit(cprint('-' * 100 + "\n\tHave a great day!", "yellow"))
            print_yellow('-' * 100)
                    
        # if user input is invalid
        else:
            invalid_txt = "INVALID!"
            invalid = pyfiglet.figlet_format(invalid_txt, font = "starwars", width = 100, justify = "center")
            print_red(invalid + "\t\tYou can only type either YES, Yes, yes, Y or NO, No, no, N.") #These are the only acceptable inputs
            continue

# end of program