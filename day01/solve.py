import itertools

def main():
    # with open('adventofcode.com_2022_day_1_input.txt', 'r') as f:
    #     lines = f.readlines()
    # new = []
    # sum = 0
    # for line in lines:
    #     if line != '\n':
    #         sum += int(line)
    #     else:
    #         new.append(sum)
    #         sum = 0
    # print(f"The answer is {max(new)}")
    
    with open('adventofcode.com_2022_day_1_input.txt', 'r') as f:
        max = 0
        compared = 0
        first_elf_summed = False

        for index, line in enumerate(f):
            if first_elf_summed is False:
                if line !='\n':
                    max += int(line)
                else:
                    first_elf_summed = True
            else:
                if line != '\n':
                    compared += int(line)
                else:
                    if compared > max:
                        max = compared
                    compared = 0
        
    print(f"The answer is {max}")
        

if __name__ == '__main__':
    main()
    