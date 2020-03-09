import itertools
import collections

def verify_set(test_set, num_plants, num_days, num_barrels, debug=False):
    """
    Verifier test set by checking whether each combination of poison barrels result in a unique outcome
    :return: tuple of (number of unique outcomes, total unique outcomes required)
    """
    def print_debug(s):
        if debug:
            print(s)

    result_sets = collections.defaultdict(list)
    n = 0

    # Tests each combination of poisonous barrels
    for poison_combi in itertools.combinations('ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:num_barrels], 2):
        n += 1
        print_debug('===Set ' + str(n) + ' Poisonous: ' + '+'.join(poison_combi) + '===')
        outcome_str = ''
        for i in range(len(test_set)):  # B.DG
            print_debug('Plant ' + str(i))
            days = test_set[i]
            is_dead = False
            for day in days:  # DG
                for barrel in day:  # D
                    if barrel in poison_combi:
                        is_dead = True
                        break
                if is_dead:
                    print_debug(day + ': Dead')
                    outcome_str += 'D'
                else:
                    print_debug(day + ': Alive')
                    outcome_str += 'A'
            print_debug('')

        # Represent outcome by a string of Ds (dead) and As (alive)
        # Each outcome is a dictionary key, where the value is a list of poison combinations that cause it
        result_sets[outcome_str].append('+'.join(poison_combi))  # 'DADDADAD': A+B

    # As long as an outcome has more than one poison combination that causes it, test is a failure
    for k, v in result_sets.items():
        if len(v) > 1:
            k_str = []
            for i in range(int(len(k) / num_days)):
                k_str.append('.'.join(k[i * num_days:i * num_days + num_days]))
            print('Cases ' + str(v) + ': ' + '; '.join(k_str))

    return len(result_sets.keys()), n


num_barrels = 11
num_plants = 4
num_days = 3

test_set = [
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I'],
    ['J', 'K', 'L']
]

result = verify_set(test_set, num_plants, num_days, num_barrels, debug=True)
print(f"Testing combination {test_set}")
print(f"{result[0]}/{result[1]} {'(PASS)' if result[0] == result[1] else '(FAIL)'}")
