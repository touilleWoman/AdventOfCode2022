from pathlib import Path
import re

def fully_contains(line) -> bool:
    sections = re.split(r'[,-]', line)
    sections = [int(x) for x in sections]
    if sections[0] <= sections[2] and sections[1] >= sections[3]:
        print(sections)
        
        return True
    elif sections[0] >= sections[2] and sections[1] <= sections[3]:
        print(sections)
        
        return True
    else:
        return False
    

def solve():
    with open(Path(__file__).with_name('adventofcode.com_2022_day_4_input.txt'), 'r') as fd:
        counter = 0
        for line in fd:
            if fully_contains(line):
                counter += 1
        print(f"There are {counter} paires where one fully contains the other")
                    
if __name__ == "__main__":
    solve()