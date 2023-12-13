from tqdm import tqdm

FILENAME = './input'
# FILENAME = './example'


def compute_test_string(spring_rep, unknowns, is_broken):
    res = [char for char in spring_rep]
    for i in range(len(unknowns)):
        if is_broken[i]:
            res[unknowns[i]] = '#'
        else:
            res[unknowns[i]] = '.'
    return ''.join(res)


def string_respects_group_constraints(test_string, numbers):
    numbers_index = 0
    previous_was_broken = False
    current_group_size = 0
    found_groups = []
    for char in test_string:
        if char == '#':
            previous_was_broken = True
            current_group_size += 1
        else:
            if previous_was_broken:
                previous_was_broken = False
                if numbers_index >= len(numbers) or numbers[numbers_index] != current_group_size:
                    return False
                numbers_index += 1
                found_groups.append(current_group_size)
                current_group_size = 0
    if previous_was_broken:
        if numbers_index >= len(numbers) or numbers[numbers_index] != current_group_size:
            return False
        found_groups.append(current_group_size)
    return len(found_groups) == len(numbers) and all([found_groups[i] == numbers[i] for i in range(len(found_groups))])


def enumerate_number_of_possible_arrangements(spring):
    spring_rep, numbers = spring
    unknowns = []
    for i in range(len(spring_rep)):
        if spring_rep[i] == '?':
            unknowns.append(i)

    arrangements = 0
    is_broken = [False for _ in unknowns]
    keep_testing = True
    while keep_testing:
        if all(is_broken):
            keep_testing = False
        test_string = compute_test_string(spring_rep, unknowns, is_broken)
        string_respects_group_constraints(test_string, numbers)
        if string_respects_group_constraints(test_string, numbers):
            arrangements += 1

        # update boolean array to test all possibilities
        for i in range(len(is_broken)):
            if is_broken[i]:
                is_broken[i] = False
            else:
                is_broken[i] = True
                break
    return arrangements


def parse_data(filename):
    springs = []
    with open(filename) as data:
        for raw_line in data:
            line = raw_line.rstrip()
            springs_rep, numbers = line.split(' ')
            springs.append((springs_rep, [int(number) for number in numbers.split(',')]))
    return springs


def unfold(springs):
    unfolded = []
    for spring_rep, numbers in springs:
        spring_rep = f'{spring_rep}?{spring_rep}?{spring_rep}?{spring_rep}?{spring_rep}'
        new_numbers = []
        for i in range(5):
            new_numbers.extend(numbers)
        unfolded.append((spring_rep, new_numbers))
    return unfolded


# Compute all legal arrangements by the following method :
# Take the last group and try placing it at all available positions and then do the next group
def compute_number_of_possible_arrangements_greedy_match(spring, memo):
    spring_rep, numbers = spring
    if sum(numbers) + sum([1 for number in numbers]) - 1 > len(spring_rep):
        return 0
    if len(numbers) == 0:
        if '#' in spring_rep:
            return 0
        return 1
    if len(spring_rep) == 0:
        return 0
    if len(spring_rep) >= 0 and len(numbers) >= 0:
        number_of_arrangements = 0
        if (spring_rep, tuple(numbers)) in memo:
            return memo[(spring_rep, tuple(numbers))]
        # find all places in spring_rep where the last group can be placed
        for i in range(len(spring_rep)-1, -1, -1):
            is_index_available = True
            for j in range(numbers[-1]):
                if i + 1 < len(spring_rep) and spring_rep[i+1] == '#':
                    is_index_available = False
                    break
                if i-j >= 0:
                    if spring_rep[i-j] == '.':
                        is_index_available = False
                        break
                else:
                    is_index_available = False
                    break
            if (i-j) - 1 >= 0 and spring_rep[(i-j)-1] == '#':  # account for the fact that groups must be separated by a '.'
                is_index_available = False
            if '#' in spring_rep[i+1:]:  # check that i'm not skipping a #
                is_index_available = False
            if is_index_available:
                new_string_index = (i-j)-1   # -1 to account for the fact that groups must be separated by 1 character
                if new_string_index < 0:
                    new_string_index = 0
                new_spring_rep = spring_rep[:new_string_index]
                new_numbers = numbers[:-1]
                number_of_arrangements += compute_number_of_possible_arrangements_greedy_match((new_spring_rep, new_numbers), memo)
        if len(numbers) < 30:
            memo[spring_rep, tuple(numbers)] = number_of_arrangements
        return number_of_arrangements


def run():
    springs = parse_data(FILENAME)
    springs = unfold(springs)
    possible_arrangements = []
    i = 0
    for spring in tqdm(springs, miniters=1):
        i += 1
        # possible_arrangements = enumerate_number_of_possible_arrangements(spring)   # Enumeration method, not good enough for part 2
        value = compute_number_of_possible_arrangements_greedy_match(spring, {})
        # print((spring, value))
        possible_arrangements.append(value)
    print(possible_arrangements)
    print(sum(possible_arrangements))


if __name__ == '__main__':
    run()
