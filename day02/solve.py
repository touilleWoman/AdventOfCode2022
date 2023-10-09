from pathlib import Path

def calculate(line):
    shape ={'X':1, 'Y':2, 'Z':3}
    win_combination = ['AY', 'BZ', 'CX']
    draw_combination = ['AX', 'BY', 'CZ']
    lost_combination = ['AZ', 'BX', 'CY']
    opponent, me = line.strip().split(' ')
    combination = opponent + me
    if combination in win_combination:
        score = 6
    elif combination in draw_combination:
        score = 3
    elif combination in lost_combination:
        score = 0
    else:
        raise Exception("Wrong input")
        
    return score + shape[me]
    
    
    

def solve():
    with open(Path(__file__).with_name('adventofcode.com_2022_day_2_input.txt'), 'r') as fd:
        line_gen = (line for line in fd)
        total = 0
        for line in line_gen:
            total += calculate(line)
        
    print(total)

if __name__ == "__main__":
    solve()