from tqdm import tqdm

FILENAME = './input'
# FILENAME = './example'


def get_map_value(map_to_read, index):
    for numbers in map_to_read:
        dest_range_start, source_range_start, range_length = numbers
        if index >= source_range_start and index < source_range_start + range_length:
            delta = index - source_range_start
            return dest_range_start + delta
    return index


def clean_up_numbers(raw_numbers):
    return [int(number) for number in raw_numbers.split(' ') if number != '']


def parse(filename):
    seeds = []
    maps = [[], [], [], [], [], [], []]
    current_map = -1
    with open(filename) as data:
        for raw_line in data:
            line = raw_line.rstrip()
            if 'seeds' in line:
                seed_ids = line.split(':')[1]
                seeds = clean_up_numbers(seed_ids)
            elif 'map' in line:
                current_map += 1
            elif line == '':
                pass
            else:
               maps[current_map].append(clean_up_numbers(line))

    return seeds, *maps

def get_key_from_map(map_to_read, value):
    for numbers in map_to_read:
        dest_range_start, source_range_start, range_length = numbers
        if value >= dest_range_start and value < dest_range_start + range_length:
            delta = value - dest_range_start
            return source_range_start + delta
    return value


def is_seed_in_seeds(seed, seeds):
    for i in range(0, len(seeds), 2):
        if seed >= seeds[i] and seed < seeds[i] + seeds[i+1]:
            return True
    return False


def run():
    seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location = parse(FILENAME)
    locations = []
    for seed in seeds:
        soil = get_map_value(seed_to_soil, seed)
        fertilizer = get_map_value(soil_to_fertilizer, soil)
        water = get_map_value(fertilizer_to_water, fertilizer)
        light = get_map_value(water_to_light, water)
        temperature = get_map_value(light_to_temperature, light)
        humidity = get_map_value(temperature_to_humidity, temperature)
        location = get_map_value(humidity_to_location, humidity)
        locations.append(location)
    print(min(locations))

    for location in tqdm(range(0, 100000000, 1)):
        humidity = get_key_from_map(humidity_to_location, location)
        temperature = get_key_from_map(temperature_to_humidity, humidity)
        light = get_key_from_map(light_to_temperature, temperature)
        water = get_key_from_map(water_to_light, light)
        fertilizer = get_key_from_map(fertilizer_to_water, water)
        soil = get_key_from_map(soil_to_fertilizer, fertilizer)
        seed = get_key_from_map(seed_to_soil, soil)
        if is_seed_in_seeds(seed, seeds):
            print(location)
            break





if __name__ == '__main__':
    run()
