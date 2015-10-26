#Choose-your-own-adventure fantasy RPG.
#Choose your weapon, follow your own path, and retrieve the water to save the kingdom!
#Will take a lot of time to finish.
#Wish ya boy some luck!

import os
from PATH_FOR_PRIME import path_prime
from PATH_FOR_PRIME import path_prime_2
from PATH_FOR_PRIME import path_1_a
from PATH_FOR_PRIME import path_1_1
from PATH_FOR_PRIME import path_1_2
from PATH_FOR_PRIME import path_prime_3
from PATH_FOR_PRIME import path_prime_4
from PATH_FOR_PRIME import path_prime_5
from PATH_FOR_PRIME import path_f_1
from PATH_FOR_PRIME import path_f_1_1
from PATH_FOR_PRIME import path_f_1_2
from PATH_FOR_PRIME import path_f_1_3
from PATH_FOR_PRIME import path_f_1_4
from PATH_FOR_PRIME import path_f_1_5
from PATH_FOR_PRIME import path_f_1_6
from PATH_FOR_PRIME import path_f_2_1
from PATH_FOR_PRIME import path_f_2_2
from PATH_FOR_PRIME import path_f_2_3
from PATH_FOR_PRIME import path_f_2_4
from PATH_FOR_PRIME import path_f_2_5
from PATH_FOR_PRIME import path_f_2_6


os.system('clear')

print "T H E  Q U E S T  F O R  T H E  S A C R E D  W A T E R"
path_prime()

continue_1=raw_input("Enter 'y' to continue, 'n' to end game. ")
if continue_1==("n"):
    print "Thanks for playing!"
    exit()
elif continue_1==("y"):
    os.system('clear')
    print "Welcome to your Quest!"

path_prime_2()

choiceweapon=raw_input ("You have three choices: 'sword and shield,' 'bow and dagger,' 'or staff and tome.' Choose wisely... ")
if choiceweapon=="sword and shield":
    path_1_a() #prints out path 1's stories
else:
    if choiceweapon=="bow and dagger":
        path_1_1()
    else:
        if choiceweapon=="staff and tome":
            path_1_2()

raw_input ("Enter 'y' to continue. ")
if continue_1==("y"):
    os.system('clear')
    path_prime_3()
    print " "


choice=raw_input ("You look on your mother one last time. Do you embrace her? Or do you turn and go? Enter 'turn and go' or 'embrace.' ")
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
path_prime_4()

continue_2=raw_input ("Enter 'y' to continue, 'n' to end game. ")
if continue_2==("n"):
    print "Thanks for playing!"
    exit()
elif continue_2==("y"):
    os.system('clear')

path_prime_5()

answer_1=raw_input("What will you do? Enter 'go into the light' or 'continue.' ")
if (answer_1=="continue"):
    print "You ignore the light, heeding your mother's warning about the dangers of the forest."

elif (answer_1=="go into the light"):
    path_f_1()
    path_f_1_1()
    if choiceweapon=="sword and shield":
        path_f_1_2()
    elif choiceweapon=="staff and tome":
        path_f_1_3()
    elif choiceweapon=="bow and dagger":
        path_f_1_4()

continue_3=raw_input ("Enter 'y' to continue, 'n' to end game. ")
if continue_3==("n"):
    print "Thanks for playing!"
    exit()
elif continue_3==("y"):
    os.system('clear')

print "THE FOREST-PART II"
print " "
print " "

if answer_1=="continue":
    path_f_1_5()
elif answer_1=="go into the light":
    path_f_1_6()

fightorflight=raw_input("What shall you do? 'stay and fight,' or 'flee?'Choose one... ")

os.system('clear')
print " "
print " "

if fightorflight=="flee":
    print "You flee the scene, leaving some of your gear behind in your excitement,"
    print "back into the forest's maw."

elif fightorflight=="stay and fight":
    print "You prepare yourself, readying your weapon once again; you fear nothing!"
    if choiceweapon=="sword and shield":
        path_f_2_1()
    if choiceweapon=="staff and tome":
        path_f_2_2()
    if choiceweapon=="bow and dagger":
        path_f_2_3()

if choiceweapon=="sword and shield" or choiceweapon=="staff and tome":
    path_f_2_4()
elif choiceweapon=="bow and dagger":
    path_f_2_5()

    stealthchoice=raw_input("What will you do? 'flee,' or 'face the wolf?' ")

    if choiceweapon=="bow and dagger" and stealthchoice==("flee"):
        print "You flee back into the woods, the wolf none the wiser."

    elif choiceweapon=="bow and dagger" and stealthchoice==('face the wolf'):
        path_f_2_6()
