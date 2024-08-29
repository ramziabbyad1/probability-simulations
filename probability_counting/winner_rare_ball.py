'''
A & B are alternately picking balls from a bag without replacement. The bag has k black balls and 1 red ball. The winner is the one who picks the red ball. Who is more likely to win, the one who starts first, or second?

Solution: 
   Draw out the event tree, you will see that the probability of the winning round being any of the possible k+1 rounds is actually 1/k+1, i.e. a uniform distribution.
   This is evidenced by the output provided below.  From the fact that the distribution is uniform regardless of k, we see that when k is even, there k+1 possible round which is an odd number, and hence the 1st player is more likely to win.  When k is odd, the probability of winning is the same for both players.
'''
import random

def get_winning_round_distribution(k, trials):
    random.seed(10)
    number_of_red_balls = k
    number_of_black_balls = 1
    total_balls = number_of_red_balls + number_of_black_balls
    winning_rounds = [0]*total_balls
    for _ in range(trials):
        round_i = get_winning_round_number(number_of_red_balls)
        winning_rounds[round_i-1] += 1

    return [round_count/trials for round_count in winning_rounds]

def get_winning_round_number(number_of_red_balls):
        outcome = ''
        round_i =1
        while outcome != 'BLACK':
            outcome = draw_random_ball(number_of_red_balls)
            #print(outcome)
            #print(outcome != 'BLACK')
            number_of_red_balls -= 1
            round_i += 1

        return round_i-1

def draw_random_ball(number_of_reds_left):
    #print(number_of_reds_left)
    black_ball_position  = 1
    draw = random.randint(1, number_of_reds_left+1)
    if draw == 1:
        return 'BLACK'
    else:
        return 'RED'

if __name__ == "__main__":
    for k in range(2, 11):
        for num_trials in [10, 100, 1000, 10000, 100000, 1000000]:
            prob_distribution = get_winning_round_distribution(k, num_trials)
            print(f"For {num_trials} trials and {k} red balls and 1 black ball, distribution is {prob_distribution}")
