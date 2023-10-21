from pathlib import Path

ROCK = 1
PAPER = 2
SCISSORS = 3
WON = 6
DRAW = 3
LOST = 0

def round_result(opponent, you):
    if opponent == you:
        return DRAW
    elif you - opponent == 1 or you - opponent == -2:
        return WON
    elif you - opponent == -1 or you - opponent == 2:
        return LOST
    else:
        raise Exception("Wrong input")

def calculate(line):
    input1, input2 = line.strip().split(' ')
    opponent_strategy = {'A': ROCK, 'B':PAPER, 'C':SCISSORS}
    you_strategy = {'X': ROCK, 'Y':PAPER, 'Z':SCISSORS}
    opponent = opponent_strategy[input1]
    you = you_strategy[input2]
    result = round_result(opponent, you)
    return result + you

def solve():
    with open(Path(__file__).with_name('adventofcode.com_2022_day_2_input.txt'), 'r') as fd:
        line_gen = (line for line in fd)
        total = 0
        for line in line_gen:
            total += calculate(line)
        
    print(total)

if __name__ == "__main__":
    solve()