'''
We flip a fair coin until we obtain our firt head.  If the first head occurs on the kth flip, we are given k balls.  We put them into 3 bins labeled 1,2  and 3 at random. Find the probability that none of the three bins are empty.

Solution:
    We first seek the probability that at least 1 bin remains empty.  We use the inclusion-exclusion principle.  We assume that 1 of the bins is empty, hence there is a 2/3 probability for each placement of balls that it will go into the other 2 bins.  For example we might have k = 4, and the outcome Bin1, Bin2, Bin1, Bin1, or Bin1, Bin1, Bin1, Bin1 when Bin3 is always empty.  Similarly when Bin2 is always empty, we could get the outcome Bin1, Bin1, Bin1, Bin1.  So these outcomes have been duplicated when we iterate over the 3 bins.
    Hence we seek to exclude (subtract) those outcomes where exactly 2 bins are empty, once for each iteration over the bins.
    p1(k) = choose(1, 3)*(2/3)^k - choose(2,3)*(1/3)^k
    And finally,
    P(k) = 1 - p1(k)
    P = sum(1, infinity) {P(k)} = 1/10
    where the final sum has been computed using geometric series.
'''

import random
from functools import reduce

def get_num_bins_from_coin():
    num_flips = 1
    while random.randint(0,1) == 0:
        num_flips += 1
    return num_flips

def get_bin_ball_distribution(k):
    bins = [0]*3
    for _ in range(k):
        bin_index = random.randint(0,2)
        bins[bin_index] += 1
    return bins

def get_prob_no_empty_bins(num_trials):
    random.seed(10)
    num_cases_with_no_empty_bins = 0
    for _ in range(num_trials):
        k = get_num_bins_from_coin()
        bin_ball_distribution = get_bin_ball_distribution(k)
        bin_prod = reduce(lambda x,y: x*y, bin_ball_distribution, 1)
        if bin_prod > 0:
            num_cases_with_no_empty_bins += 1

    return num_cases_with_no_empty_bins / num_trials

if __name__ == "__main__":
    for num_trials in [10, 100, 1000, 10000, 100000, 1000000]:
        prob_no_empty = get_prob_no_empty_bins(num_trials)
        print(f"For {num_trials} trials, proportion with no empty bins is {prob_no_empty}")

