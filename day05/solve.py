from pathlib import Path
import re

def parse():
    with open(Path(__file__).with_name("adventofcode.com_2022_day_5_input.txt")) as fd:
        data = fd.readlines()
    crates_lines = []
    nb_of_stacks = 0
    instructions = []
    for line in data:
        if line.startswith('['):
            crates_lines.append(line)
        elif line.startswith(' 1'):
            nb_of_stacks = int(line.strip().split(' ')[-1])
        elif line.startswith('move'):
            instructions.append(line)
    return crates_lines, nb_of_stacks, instructions

def build_stacks(crates_lines, nb_of_stacks):
    stacks = [str(index) for index in range(1, nb_of_stacks + 1)]
    while crates_lines:
        line = crates_lines.pop()
        for index in range(nb_of_stacks):
            crate = line[index * 4 + 1]
            if crate.isalpha():
                stacks[index] += crate
    print("original stacks's horizontal view :")
    for line in stacks:
        print(line)
    return stacks
        

def grep_instructions(line):
    match = re.match(r'^move (\d+) from (\d+) to (\d+)$', line)
    if match:
        return map(lambda x :int(x), match.groups())
    else:
        raise ValueError("Wrong instruction line")


def main(part_two=False):
    crates_lines, nb_of_stacks, instructions = parse()
    stacks = build_stacks(crates_lines, nb_of_stacks)
    for line in instructions:
        nb_of_crates, from_stack, to_stack = grep_instructions(line)
        unmoved, moved = stacks[from_stack - 1][:-nb_of_crates], stacks[from_stack - 1][-nb_of_crates:]
        stacks[from_stack - 1] = unmoved
        if part_two == False:
            stacks[to_stack - 1] += ''.join(reversed(moved))
        else:
            stacks[to_stack - 1] += moved
            
    ends_of_crates = ''
    for line in stacks:
        ends_of_crates += line[-1]
    print(f"\nThe crates that end up on the top of each stack is {ends_of_crates}")
    


if __name__ == "__main__":
    main()
    main(part_two=True)