import numpy as np
from pathlib import Path

def main():
    file = Path(__file__).with_name('input.txt')
    with open(file) as f:
        data = f.read().split("\n")
        data = [i.split(" -> ") for i in data] 
        grid = np.zeros((1000, 1000), dtype=int) # making grid 1000x1000 based on the highest number in input

        for i in data:
            x1, y1 = list(map(int, i[0].split(",")))
            x2, y2 = list(map(int, i[1].split(",")))

            if x1 == x2: # vertical line
                if y1 > y2:
                    y1, y2 = y2, y1
                grid[y1:y2 + 1, x1] += 1 
            elif y1 == y2: # horizontal line
                if x1 > x2:
                    x1, x2 = x2, x1
                grid[y1, x1:x2 + 1] += 1 
            else: # diagonal line
                x_increase = 1
                y_increase = 1
                if x1 > x2:
                    x_increase = -1
                if y1 > y2:
                    y_increase = -1
                distance = abs(x1 - x2) + 1
                for i in range(distance):
                    grid[y1 + (i * y_increase)][x1 + (i * x_increase)] += 1
                pass
        unique, counts = np.unique(grid, return_counts=True)
        print(np.asarray((unique, counts)).T)
if __name__ == '__main__':
    main()