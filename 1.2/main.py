from pathlib import Path

def main():
    file = Path(__file__).with_name('input.txt')
    with open(file) as f:
        numbers = []
        plus = 0
        for i in f:
            numbers.append(int(i.strip()))
        for i in range(1, len(numbers)):
            if sum(numbers[i:i+3]) > sum(numbers[i-1:i+2]):
                plus += 1
        
        print(plus)


if __name__ == '__main__':
    main()