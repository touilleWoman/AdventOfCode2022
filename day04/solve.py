from pathlib import Path
import re

def fully_contains(sections) -> bool:
    if sections[0] <= sections[2] and sections[1] >= sections[3]:
        return True
    elif sections[0] >= sections[2] and sections[1] <= sections[3]:
        return True
    else:
        return False
    
def overlap(sections) -> bool:
    pair_one = [x for x in range(sections[0], sections[1] + 1)]
    pair_two = [x for x in range(sections[2], sections[3] + 1)]
    for x in pair_one:
        if x in pair_two:
            return True
    return False
    
def solve():
    with open(Path(__file__).with_name('adventofcode.com_2022_day_4_input.txt'), 'r') as fd:
        counter = 0
        counter_part_two = 0
        for line in fd:
            sections = re.split(r'[,-]', line)
            sections = [int(x) for x in sections]
            if fully_contains(sections):
                counter += 1
            if overlap(sections):
                counter_part_two += 1
        print(f"There are {counter} paires where one fully contains the other")
        print(f"There are {counter_part_two} paires with range overlap")
                    
if __name__ == "__main__":
    solve()