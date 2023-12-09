

FILENAME = './input'
# FILENAME = './example'


def parse_data(filename):
    sequences = []
    with open(filename) as data:
        for line in data:
            sequences.append([int(x) for x in line.rstrip().split(' ') if x != ''])
    return sequences


def get_next_term(sequence, look_forward):
    difference_sequence = []
    for i in range(len(sequence) - 1):
        difference_sequence.append(sequence[i+1] - sequence[i])
    if all([item == 0 for item in difference_sequence]):
        return sequence[-1]
    else:
        if look_forward:
            return sequence[-1] + get_next_term(difference_sequence, look_forward)
        else:
            return sequence[0] - get_next_term(difference_sequence, look_forward)


def run():
    oasis_sequences = parse_data(FILENAME)
    next_terms = []
    previous_terms = []
    for sequence in oasis_sequences:
        next_terms.append(get_next_term(sequence, True))
        previous_terms.append(get_next_term(sequence, False))
    print(sum(next_terms))
    print(sum(previous_terms))


if __name__ == '__main__':
    run()
