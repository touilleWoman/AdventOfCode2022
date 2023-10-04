def elf_generator(lines):
    elf =[]
    for line in lines:
        if line != '\n':
            elf.append(int(line))
        else:
            yield sum(elf)
            elf = []


def solve():
    lines_gen = (line for line in open('adventofcode.com_2022_day_1_input.txt', 'r'))
    elf_gen = elf_generator(lines_gen)

    max = 0
    for compared in elf_generator(lines_gen):
        if compared > max:
            max = compared
    print(f"Biggest elf calories is {max}")
    

class TopThree:
    """data structure stores the 3 biggest elfs when iterating lines
    """
    def __init__(self) -> None:
        self.data =[0, 0, 0]
    
    def insert(self, compared):
        self.data.append(compared)
        self.data.sort(reverse=True)
        self.data.pop()
    
    def sum(self):
        return sum(self.data)
    


def solve_part_two():
    lines_gen = (line for line in open('adventofcode.com_2022_day_1_input.txt', 'r'))
    elf_gen = elf_generator(lines_gen)

    top_three = TopThree()
    
    for compared in elf_generator(lines_gen):
        top_three.insert(compared)
    print(f"Total of three biggest elves calories is {top_three.sum()}")    
       
        

if __name__ == '__main__':
    solve()
    solve_part_two()
    