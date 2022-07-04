import random
from termcolor import colored, cprint


trials = 0

sum_results = 0.0

rolls = []

def roll_dice(s,d):

    rolls.clear()

    i = d

    while i > 0:
        roll_n = int(random.random()*s)+1
        rolls.append(roll_n)

        i -= 1

        
def calc():

    num_sides = int(input("How many side are on your die? "))
    s = num_sides
    num_dice = int(input("How many dice are you rolling? "))
    d = num_dice
    sum_results = 0.0

    trials = 0

    while trials < 10**6:
        roll_dice(s,d)
        #print(rolls)

        sum_results += max(rolls)

        trials += 1


    
    cprint("Average result of rolling two and taking the highest is about {0}".format(sum_results/trials), 'red')

    loops()


def loops():
    print("Would you like to try again? Y/N")

    user_input = (input())

    if user_input == "y":
        calc()
    elif user_input == 'n':
        return


cprint('******************************************************************************', 'green')
cprint('***            Higher of n Rolls | https://github.com/jibatsu              ***', 'green')
cprint('*Based on the code written by StandUpMaths | https://github.com/standupmaths *', 'green')
cprint('******************************************************************************', 'green')

cprint('This script will calculate the average higest roll when rolling multiple dice.', 'green')
calc()
