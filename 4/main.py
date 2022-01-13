import numpy as np
from pathlib import Path

def main():
    file = Path(__file__).with_name('input.txt')
    with open(file) as f:
        data = f.read().strip().splitlines()
        numbers = data.pop(0).split(",")
        numbers = list(map(int, numbers))

        rows = np.array([list(map(int,i.split())) for i in data if i != ''])
        cards = [rows[i:i+5] for i in range(0, len(rows),5)] 
        cards_won = [False for i in range(len(cards))]
        number_marked = [[False for i in range(5)] for j in range(len(cards))]

        for number in numbers:
            for card_ind, card in enumerate(cards):
                card[card == number] = -1
                if [-1] * 5 in card.tolist() and cards_won[card_ind] != True:
                    cards_won[card_ind] = True
                    card[card == -1] = 0
                    if all(cards_won):
                        # print(cards_won)
                        print(card)
                        print(number * sum(sum(card)))
     

if __name__ == '__main__':
    main()