import functools



if __name__ == '__main__':
    with open('names.txt', 'r') as f: names = f.read().splitlines()
    # מדפיסה למסך את השם הארוך ביותר בקובץ.
    print(max(names, key=len))
    #מדפיסה למסך את סכום האורכים של השמות בקובץ.
    print(functools.reduce(lambda x, y: x + len(y), names, 0))
    # מדפיסה למסך את השמות הכי קצרים בקובץ
    print('\n'.join(filter(lambda name: len(name) == len(min(names, key=len)), names)))
    # תוכנית שיוצרת קובץ חדש בשם name_length.txt המכיל את האורך של כל שם בקובץ names.txt
    with open('name_length.txt', 'w') as file:
        file.write('\n'.join(str(len(name)) for name in names))
    # קולטת מהמשתמש מספר המייצג אורך של שם ומדפיסה את כל השמות בקובץ names.txt שהם באורך הזה.
    num_of_letters = int(input("enter the num of letters: "))
    print(list(filter(lambda x: len(x) == num_of_letters, names)))





