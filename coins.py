import random
import math

def heads_or_tails(toss):
    h_counter = 0
    t_counter = 0
    for number in range(1, toss+1, 1):
        coin = round(random.random())
        if number == toss:
            print "End of program. Bye!"
        elif number < toss and coin == 0:
            h_counter+= 1
            print "Attempt number {}. Got heads. Heads({}) and tails({})".format(number, h_counter, t_counter)
        elif number < toss and coin == 1:
            t_counter+= 1
            print "Attempt number {}. Got tails. Heads({}) and tails({})".format(number, h_counter, t_counter)

heads_or_tails(500)


# Flip a coin and keep track of which side it landed on and how many times