import numpy as np

# Board size +1 because player starts from space outside the board
NUM_SQUARES = 100 + 1

def verify_set(ladders):
    # Construct dictionary of snake/ladders where the key is the starting space, and the value the ending space
    ladder_dict = {}
    for ladder in ladders:
        ladder_dict[ladder[0]] = ladder[1]

    """
    References:   - http://web.mit.edu/18.06/www/Spring17/Chutes-and-Ladders.pdf
                  - https://math.stackexchange.com/questions/1695191/markov-chain-snakes-and-ladders
                  - https://www.quora.com/What-is-the-expected-number-of-moves-required-to-finish-a-snakes-and-ladders-game
    """

    # Create X by X matrix
    a = np.zeros((NUM_SQUARES, NUM_SQUARES))
    for i in range(NUM_SQUARES):
        # For start of snake/ladder, leave as empty row (all zero)
        if i in ladder_dict:
            continue

        # For each result of die roll
        for roll in range(1, 7):
            sum = i + roll

            # If exceed final space, stay in current space
            if sum > NUM_SQUARES - 1:
                a[i][i] += 1

            # If die roll lands on start of snake/ladder, land on the ending space instead
            elif sum in ladder_dict:
                a[i][ladder_dict[sum]] += 1

            # Else, just land on that tile
            else:
                a[i][sum] += 1

    # Remove first column and row to get transient matrix
    a = a[:-1, :-1]

    # Change values to represent chance out of each die outcome
    a = a / 6

    # Formula for obtaining expected number of moves: (𝐼−𝑄)−1, then sum the first row of the result
    i = np.identity(NUM_SQUARES - 1)
    sub = np.subtract(i, a)
    inverse = np.linalg.inv(sub)

    return inverse[0].sum()

test_set = [
    [1,38], [4,14],
    [9,31], [21,42],
    [28,84], [36,44],
    [51,67], [71,91],
    [80,100], [16,6],
    [47,26], [49,11],
    [56,53], [62,19],
    [64,60,],[87,24],
    [93,73],[95,75],
    [98,78]
]

# Given example, expected outcome 39.225122
print(verify_set(test_set))