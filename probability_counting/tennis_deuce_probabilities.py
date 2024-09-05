'''
Two players are at deuce in a tennis match — player 1 has 60 percent of winning the point and player 2 has 40 percent chance. What are the odds of player 1 winning?

First, how does deuce work?  after winning a deuce, the second player has a chance to reenter deuce, otherwise the point goes to the player that wins 2 in a row.

There is a state diagram to manage this interaction.  But it is difficult to draw out here.

X = proabibiity of p1 winning deuce

=> X = (.6)(.6) + 2*(.6)(.4)X
=> X = .6923

'''
import random
def get_probability_p1_wins_deuce(trials):
    random.seed(10)
    number_of_p1_wins = 0
    for _ in range(trials):
        no_winner_yet = True
        previous_2_winners = []
        while no_winner_yet:
            random_variable = random.randint(1,10)
            current_victor = ''
            if random_variable <= 6:
                current_victor = 'P1'
            else:
                current_victor = 'P2'
            if len(previous_2_winners) == 2:
                previous_2_winners[0] = previous_2_winners[1]
                previous_2_winners[1] = current_victor
            else:
                previous_2_winners.append(current_victor)

            # Player 1 won this deuce
            if previous_2_winners == ['P1', 'P1']:
                number_of_p1_wins += 1
                break
            # Player 2 won this deuce
            if previous_2_winners == ['P2', 'P2']:
                break

            # Return to deuce if alternated victories
            if previous_2_winners == ['P1', 'P2'] or previous_2_winners == ['P2', 'P1']:
                previous_2_winners = []  # Reset to go back to deuce

    return number_of_p1_wins / trials

if __name__ == '__main__':
    for num_trials in [10, 100, 1000, 10000, 100000, 1000000]:
        prob_p1_wins = get_probability_p1_wins_deuce(num_trials)
        print(f"For {num_trials} trials, proportion of p1 winning deuce is {prob_p1_wins}")
        #break


        
