import pandas as pd
import random


def load_fortunes(name):
    path = r'C:\Users\User 8\Desktop'
    fortunes = pd.read_csv(path + '/' + name + '.txt', header=None)[0]
    return fortunes
# Here I am installing loading in the fortune function.


def main():
    name = input("Enter file name : ")
    fortunes_list = load_fortunes(name)
    display_fortunes(fortunes_list)

# This is a display function that would open the function

def display_fortunes(fortunes_list):
    a = 'yes'
    while (a[:3].upper() == 'YES'):
        a = input("Want another fortune : ")
        if a[:2].upper() == 'NO':
            break
        elif a[:3].upper() != 'YES':
            print('Wrong entry. Type yes or no.')
            a = 'yes'
            continue
        i = random.randint(0, len(fortunes_list) - 1)
        print(fortunes_list[i])
    print('Exit...')

# This is where there will be a display name from the load fortunes function


if __name__ == "__main__":
    main()

