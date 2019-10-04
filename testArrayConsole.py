mapp = []

with open('mapTest.txt') as file:
    for line in file:
        mapp.append(line.strip('\n'))


def print_map(x_start, y_start, x_len, y_len, map_, char_char):
    for b in range(2 * x_len):
        print()
    for y in range(y_start, y_start + y_len):
        for x in range(x_start, x_start + x_len):
            if 0 <= x < map_[0].__len__() and 0 <= y < map_.__len__():
                if (x - x_start) == (x_len - 1)/2 and (y - y_start) == (y_len - 1)/2:
                    print(char_char, end='')
                else:
                    print(map_[y][x], end='')
        print()

print_map(13, 4, 9, 9, mapp, '@')

x = 13
y = 4
l = 9
while True:
    inp = input()
    if inp == 'w':
        y -= 1
    elif inp == 's':
        y += 1
    elif inp == 'a':
        x -= 1
    elif inp == 'd':
        x += 1
    print_map(x, y, l, l, mapp, '@')

