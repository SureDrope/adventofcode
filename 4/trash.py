import numpy as np
from pathlib import Path

def main():
    file = Path(__file__).with_name("input.txt")
    with open(file) as f:
        rows = f.read().split("\n")
        numbers = rows.pop(0).split(",")
        numbers = list(map(int, numbers))
        rows = np.array([list(map(int,i.split())) for i in rows if i != ''])
        columns = []
        for i in range(0, len(rows), 5):
            for j in range(0, 5):
                columns.append(rows[i:i+5, j])
        lines = np.concatenate((rows, columns))

        part_one(lines, numbers)
        part_two(lines, numbers)

def part_one(lines, numbers):
    while True:
        number = numbers.pop(0)
        lines[lines == number] = -1 
        if [-1] * 5 in lines.tolist():
            break
    start = start_of_card(lines)
    lines[lines == -1] = 0 
    print(number)
    print(number * sum(sum(lines[start:start + 5])))

def part_two(lines, numbers):
    while len(numbers):
        number = numbers.pop(0)
        lines[lines == number] = -1 
        # if [-1] * 5 in lines.tolist():
        while [-1] * 5 in lines.tolist():
            start = start_of_card(lines)
            winning_card = lines[start:start + 5]
            last_number = number
        #    print(winning_card)
        #    print("#" * 10)
            print(last_number)
            lines = np.delete(lines, np.s_[start:start + 5], axis = 0)

    print(last_number)
    winning_card[winning_card == -1] = 0 
    print(winning_card)
    print(last_number * sum(sum(winning_card)))

def start_of_card(lines):
    index_of_bingo = lines.tolist().index([-1] * 5)
    start_of_card = index_of_bingo - (index_of_bingo % 5)
    # print(lines[start_of_card:start_of_card + 5])
    return start_of_card

if __name__ == '__main__':
    main()