from pathlib import Path

ROCK = 1
PAPER = 2
SCISSORS = 3
WON = 6
DRAW = 3
LOST = 0

def round_result(opponent, you):
    if opponent not in [ROCK, PAPER, SCISSORS] or you not in [ROCK, PAPER, SCISSORS]:
        raise Exception("Wrong input")
    if opponent == you:
        return DRAW
    if you - opponent == 1 or you - opponent == -2:
        return WON
    if you - opponent == -1 or you - opponent == 2:
        return LOST

def calculate(line):
    input1, input2 = line.strip().split(' ')
    opponent_strategy = {'A': ROCK, 'B':PAPER, 'C':SCISSORS}
    you_strategy = {'X': ROCK, 'Y':PAPER, 'Z':SCISSORS}
    opponent = opponent_strategy[input1]
    you = you_strategy[input2]
    result = round_result(opponent, you)
    return result + you

def your_choice(opponent, outcome):
    if opponent not in [ROCK, PAPER, SCISSORS] or outcome not in [WON, LOST, DRAW]:
        raise Exception("Wrong input")
    if outcome == DRAW:
        return opponent
    if outcome == WON:
        if opponent == SCISSORS:
            return ROCK
        else :
            return opponent + 1
    if outcome == LOST:
        if opponent == ROCK:
            return SCISSORS
        else:
            return opponent - 1

def calculate_part_two(line):
    input1, input2 = line.strip().split(' ')
    opponent_strategy = {'A': ROCK, 'B':PAPER, 'C':SCISSORS}
    opponent = opponent_strategy[input1]
    outcome_strategy = {'X': LOST, 'Y':DRAW, 'Z':WON}
    outcome = outcome_strategy[input2]
    return your_choice(opponent, outcome) + outcome
    

def solve(part_two=False):
    with open(Path(__file__).with_name('adventofcode.com_2022_day_2_input.txt'), 'r') as fd:
        line_gen = (line for line in fd)
        total = 0
        for line in line_gen:
            if part_two == False:
                total += calculate(line)
            if part_two == True:
                total += calculate_part_two(line)
    print(total)

if __name__ == "__main__":
    solve()
    solve(part_two=True)