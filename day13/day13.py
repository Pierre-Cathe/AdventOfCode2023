from tqdm import tqdm

FILENAME = './input'
# FILENAME = './example'


def parse_data(filename):
    patterns = []
    with open(filename) as data:
        pattern = []
        for raw_line in data:
            line = raw_line.rstrip()
            if line == '':
                patterns.append(pattern)
                pattern = []
            else:
                pattern.append(line)
    patterns.append(pattern)
    return patterns


def get_horizontal_reflection_line(pattern, skip_index=None):
    previous_line = pattern[0]
    for i in range(1, len(pattern)):
        if skip_index is not None and skip_index == i:
            continue
        current_line = pattern[i]
        if current_line == previous_line:
            max_reflection_length = min(i, len(pattern) - i)
            if all([pattern[(i-j)-1] == pattern[i+j] for j in range(max_reflection_length)]):
                return i
        previous_line = current_line
    return None


def transpose(pattern):
    new_pattern = []
    for y in range(len(pattern[0])):
        line = ''.join([pattern[x][y] for x in range(len(pattern))])
        new_pattern.append(line)
    return new_pattern


def find_reflection_line(pattern, skip_line=None):
    skip_index, skip_vertical = None, None
    if skip_line is not None:
        skip_index, skip_vertical = skip_line

    if skip_line is not None and not skip_vertical:
        reflection_line_index = get_horizontal_reflection_line(pattern, skip_index=skip_index)
    else:
        reflection_line_index = get_horizontal_reflection_line(pattern)
    is_vertical = False

    if reflection_line_index is None:
        if skip_line is not None and skip_vertical:
            reflection_line_index = get_horizontal_reflection_line(transpose(pattern), skip_index=skip_index)
        else:
            reflection_line_index = get_horizontal_reflection_line(transpose(pattern))
        is_vertical = True

    return reflection_line_index, is_vertical


def unsmudge(pattern, x, y):
    new_char = '#' if pattern[x][y] == '.' else '.'
    new_pattern = pattern.copy()
    new_pattern[x] = new_pattern[x][:y] + new_char + new_pattern[x][y+1:]
    return new_pattern


def find_smudged_reflection_line(pattern):
    default_reflection_line = find_reflection_line(pattern)
    for x in range(len(pattern)):
        for y in range(len(pattern[0])):
            new_pattern = unsmudge(pattern, x, y)
            new_reflection_line = find_reflection_line(new_pattern, skip_line=default_reflection_line)
            if new_reflection_line[0] is not None and new_reflection_line != default_reflection_line:
                return new_reflection_line
    return None


def run():
    patterns = parse_data(FILENAME)
    reflection_lines = []
    for i in range(len(patterns)):
        pattern = patterns[i]
        # reflection_line_index, is_vertical = find_reflection_line(pattern)  # part 1 solution
        reflection_line = find_smudged_reflection_line(pattern)
        reflection_line_index, is_vertical = reflection_line
        reflection_lines.append((reflection_line_index, is_vertical))
    summary = 0
    for reflection_line_index, is_vertical in reflection_lines:
        factor = 100 if not is_vertical else 1
        summary += factor * reflection_line_index
    print(summary)


if __name__ == '__main__':
    run()
