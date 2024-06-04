import functools



if __name__ == '__main__':
    with open('names.txt', 'r') as f: names = f.read().splitlines()
    print(max(names, key=len))
    print(functools.reduce(lambda x, y: x + len(y), names, 0))

    print('\n'.join(filter(lambda name: len(name) == len(min(names, key=len)), names)))
    with open('name_length.txt', 'w') as file:
        file.write('\n'.join(str(len(name)) for name in names))
    num_of_letters = int(input("enter the num of letters: "))
    print(list(filter(lambda x: len(x) == num_of_letters, names)))





