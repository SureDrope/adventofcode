from pathlib import Path

def main():
    file = Path(__file__).with_name('input.txt')
    with open(file) as f:
        coordinates = [0, 0]
        for line in f:
            command, number = line.rstrip().split()
            if command == 'forward':
                coordinates[0] += int(number)
            elif command == 'up':
                coordinates[1] -= int(number)
            elif command == 'down':
                coordinates[1] += int(number)
        print(coordinates[0] * coordinates[1])
if __name__ == '__main__':
    main()