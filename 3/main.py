from pathlib import Path

def main():
    file = Path(__file__).with_name("input.txt")

    with open(file) as f:
        data = f.read().split("\n")
        digits = [0 for _ in range(len(data[0]))]
        for i in data:
            line = list(enumerate(list(str(i))))
            for j in line:
                position = int(j[0])
                digit = int(j[1])
                if digit == 1:
                    digits[position] += 1
                else:
                    digits[position] -= 1
        # print(digits)
        gamma = ""
        epsilon = ""
        for i in digits:
            if i > 0:
                gamma += "1"
                epsilon += "0"
            else:
                gamma += "0"
                epsilon += "1"
        print(int(gamma, 2) * int(epsilon, 2))
        
if __name__ == '__main__':
    main()