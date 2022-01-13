from pathlib import Path

def main():
    file = Path(__file__).with_name('input.txt')
    with open(file) as f:
        coordinates = [0, 0]
        aim = 0
        for line in f:
            command, number = line.rstrip().split()
            if command == 'forward':
                coordinates[0] += int(number)
                coordinates[1] += int(number) * aim
            elif command == 'up':
                aim -= int(number)
            elif command == 'down':
               aim += int(number)
        print(coordinates[0] * coordinates[1])

if __name__ == '__main__':
    main()