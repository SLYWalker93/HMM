import os
from PATH_FOR_PRIME import path_prime
from PATH_FOR_PRIME import path_prime_2
from PATH_FOR_PRIME import path_1_a
from PATH_FOR_PRIME import path_1_1
from PATH_FOR_PRIME import path_1_2
from PATH_FOR_PRIME import path_prime_3

os.system('clear')

print "T H E  Q U E S T  F O R  T H E  S A C R E D  W A T E R"
path_prime()

continue_1=raw_input("Enter 'y' to continue, 'n' to end game.")
if continue_1==("n"):
    print "Thanks for playing!"
    exit()
elif continue_1==("y"):
    os.system('clear')
    print "Welcome to your Quest!"

path_prime_2()

choiceweapon=raw_input ("You have three choices: 'sword and shield,' 'bow and dagger,' 'or staff and tome.' Choose wisely...")
if choiceweapon=="sword and shield":
    path_1_a() #prints out path 1's stories
else:
    if choiceweapon=="bow and dagger":
        path_1_1()
    else:
        if choiceweapon=="staff and tome":
            path_1_2()

raw_input ("Enter 'y' to continue.")
if continue_1==("y"):
    os.system('clear')
    path_prime_3()
    print " "


choice=raw_input ("You look on your mother one last time. Do you embrace her? Or do you turn and go? Enter 'turn and go' or 'embrace.'")
if choice=="embrace":
    print " "
    print "You embrace your sick mother, kissing her on the cheek, then rise to face the challenges ahead of you."
    print " "
    print " "
elif choice=="turn and go":
    print " "
    print "You know your mother is ill, and it's too risky to endanger your own life. You turn to face the challenges ahead."

    print " "
    print " "
