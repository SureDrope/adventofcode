from pathlib import Path

def main():
    file = Path(__file__).with_name("input.txt")

    with open(file) as f:
        data = f.read().split("\n")

        co2 = main_test(0)(data)
        oxygen = main_test(1)(data)
        print(co2 * oxygen)

def main_test(key):
    def test(data, position=0):
        if len(data) == 1:
            return int(*data, 2)

        zeros = list(filter(lambda x: x[position:].startswith("0"),
        data)) 
        ones = list(filter(lambda x: x[position:].startswith("1"),
        data)) 
        print(zeros, "|", ones)
        if key == 0:
            result = zeros if len(zeros) <= len(ones) else ones
        else:
            result = ones if len(ones) >= len(zeros) else zeros

        return test(result, position+1) 
    
    return test

if __name__ == '__main__':
    main()