import numpy as np
from pathlib import Path

def main():
    days = int(input())
    file = Path(__file__).with_name('input.txt')
    with open(file) as f:
        data = f.read().strip().split(",")
        state = [0] * 9
        for i in data:
            state[int(i)] += 1

        for i in range(1, days + 1):
            day_zero = state.pop(0)
            state.append(day_zero) 
            state[6] += day_zero
            print(f"Day {i}:\t", state, sum(state))
if __name__ == '__main__':
    main()