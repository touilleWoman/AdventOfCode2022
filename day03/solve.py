from pathlib import Path
import string

def priority(input):
    items = string.ascii_letters
    return items.index(input) + 1

def calculate(line):
    cutpoint =len(line)//2
    first = line[0: cutpoint]
    second = line[cutpoint:]
    for letter in first:
        if letter in second:
            return priority(letter)
    raise ValueError("Wrong input, there shold be a shared item in two compartments")

def solve():
    with open(Path(__file__).with_name('adventofcode.com_2022_day_3_input.txt'), 'r') as fd:
        line_gen = (line for line in fd)
        sum = 0
        for line in line_gen:
            sum += calculate(line)
        print(f"the sum of priorities is {sum}")
        return sum

def common_item_value(group):
    for x in group[0]:
        if x in group[1] and x in group[2]:
            return priority(x)
    raise ValueError("There shold have common item in group")

def solve_part_two():
    with open(Path(__file__).with_name('adventofcode.com_2022_day_3_input.txt'), 'r') as fd:
        line_gen = (line for line in fd)
        sum = 0
        while True:
            group = [next(line_gen, None) for _ in range(3)]
            if None in group:
                break
            sum += common_item_value(group)
        print(f"Part Two: The sum of priorities is {sum}")

if __name__ == "__main__":
    solve()
    solve_part_two()