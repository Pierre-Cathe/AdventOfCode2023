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
        for i in range(4):
            new_numbers.extend(numbers)
        unfolded.append((spring_rep, new_numbers))
    return unfolded


def run():
    springs = parse_data(FILENAME)
    springs = unfold(springs)
    possible_arrangements = []
    for spring in tqdm(springs):
        possible_arrangements.append(enumerate_number_of_possible_arrangements(spring))
    print(sum(possible_arrangements))


if __name__ == '__main__':
    run()
