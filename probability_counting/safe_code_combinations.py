'''
An electronic safe has a three digit passcode. You are given three constraints regarding the code. Firstly, the code is not an odd number. Secondly, the code does not contain the number six. Lastly, one of the digits appears more than once. How many possible three digit entries satisfy these three requirements?

1) code not odd -> last digit is 0,2,4,8 (4 possible)
2) no sixes
3) 2 of same number

third*second*First

2 cases
The duplicate is in the last 2
The duplicate contains the third

For case 1, there are 9 possible values for the remaining 2
meaning 4*9 = 36


For case 2, position 1 or 2 is the same as the third and the other can take nine values, hence again 9*4

Overall, we sum them to get 9*4*3.

But we have overcounted, note that 2,2,2 belongs to both cases

There are 4 cases where all three are the same, hence we should subtract 8 of these, since we counted them 3 times.

(e,e,e) -> complete overlap
(e, o, o) -> no overlap
(e, o, e) -> no overlap

Overall, get 9*4*3 - 8 = 108 - 8 = 100
'''

def get_possible_safe_combos():
    combos = set()
    for i in range(10):
        if i != 6 and i%2 == 0:
            for j in range(10):
                if j != 6:
                    for k in range(10):
                        if k != 6 and i==j or i == k or j == k:
                            combos.add((i,j,k))

    print(f'{combos = }')
    return len(combos)

print(get_possible_safe_combos() == 100)
