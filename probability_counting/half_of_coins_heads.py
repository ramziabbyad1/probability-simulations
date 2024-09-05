'''
Here we have he intuition that since half of the coins come up heads that this happens half of the time.
Why?  For each coin there are 2 possible equally likely outcomes.  

Let's count it anyway:  there are a total of 2^10 possible outcomes, and 10_choose_5 of these are half heads.
10_choose_5 = 10*9*8*7*6/5*4*3*2*1 = 9*8*7*6/4*3 = 3*2*7*6 = 36*7 = 210+42 = 252.
2^10 = 1024

Answer = 252/1024


'''
import random

def get_prob_half_heads(trials):
    random.seed(10)
    NUMBER_OF_COINS = 10
    count_of_half_heads = 0
    for _ in range(trials):
        head_count = 0
        for _ in range(NUMBER_OF_COINS):
            head_count += random.randint(0,1)
        if head_count == NUMBER_OF_COINS/2:
            count_of_half_heads += 1

    return count_of_half_heads/trials

if __name__ == '__main__':
    for num_trials in [10, 100, 1000, 10000, 100000, 1000000]:
        prob_half_heads = get_prob_half_heads(num_trials)
        print(f"For {num_trials} trials, proportion with half of the coins heads is {prob_half_heads}")

    print(f'Theoretical probability is {252/1024}')
