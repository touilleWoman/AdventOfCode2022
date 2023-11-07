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


if __name__ == "__main__":
    solve()