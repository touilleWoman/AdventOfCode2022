import itertools

def main():
    with open('adventofcode.com_2022_day_1_input.txt', 'r') as f:
        lines = f.readlines()
    new = []
    sum = 0
    for line in lines:
        
        if line != '\n':
            sum += int(line)
        else:
            new.append(sum)
            sum = 0
        
    print(f"The answer is {max(new)}")

if __name__ == '__main__':
    main()
    