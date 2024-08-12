'''
You have two piles of cards: one has 1 deck (total of 52 cards), the other has 2 decks mixed together (total of 104 cards). You pick two cards separately from the same pack. If both of two cards are red, you win. Which pack will you choose?



Calculation to demonstrate convergence to .25:

x <- num of total cards

(x/2)/x * (x/2-1)/(x-1)
x/2 - 1/ 2x - 2
x- 2/ 4x - 4
x-2/ 2(x + x-2)
1/2(x/x-2 + 1) -> .5 * .5  = .25



'''
import random

def got_2_reds(num_decks):
    num_reds = num_blacks = 26*num_decks
    first_draw = random.randint(1, num_reds+num_blacks)
    second_draw = random.randint(1, num_reds+num_blacks - 1)
    return first_draw < num_reds and second_draw < num_reds

def get_num_of_times_you_get_2_reds(num_trials, num_decks):
    random.seed(10)
    num_times_get_2_reds = 0
    for _ in range(num_trials):
        if got_2_reds(num_decks):
            num_times_get_2_reds += 1
    return num_times_get_2_reds / num_trials


if __name__ == "__main__":
    max_num_decks = 10
    for num_decks in range(1, max_num_decks+1):
        for num_trials in [1000000]:
            prob_2_reds = get_num_of_times_you_get_2_reds(num_trials, num_decks)
            print(f"For {num_trials} trials and {num_decks} decks, proportion with no empty bins is {prob_2_reds}")

