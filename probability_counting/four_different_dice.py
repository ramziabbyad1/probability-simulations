'''

	
Imagine you have 4 6-sided dice. What is the probability that you roll a different number on each die?

one can approach this problem through counting.

if the first die has 6 possible states, then each of those is associated with 5 possible states for the second, and so on, until only 3 states are left.

Hence there are 6*5*4*3 such configurations, out of a total of 6^4.

Anser: 6*5*4*3/6*6*6*6 = 5*2/6*6 = 5/18.

'''

import random

def get_prob_4_different_dice(trials):
    random.seed(10)
    NUMBER_OF_DICE = 4
    unique_count = 0
    for _ in range(trials):
        unique_outcomes = set()
        for _ in range(NUMBER_OF_DICE):
            unique_outcomes.add(random.randint(1,6))
        if len(unique_outcomes) == NUMBER_OF_DICE:
            unique_count += 1

    return unique_count/trials


if __name__ == '__main__':
    for num_trials in [10, 100, 1000, 10000, 100000, 1000000]:
        prob_unique = get_prob_4_different_dice(num_trials)
        print(f"For {num_trials} trials, proportion with unique outomes {prob_unique}")
        print(f"The true probability is {5/18}")

        
