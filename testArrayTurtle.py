import turtle

window = turtle.Screen()
window.bgcolor('black')
window.tracer(0, 0)
# window.setup(500, 650)

pen = turtle.Turtle()
pen.color('green')
pen.pensize(30)
pen.speed(10)
pen.ht()


def draw_asset(color, x, y):
    pen.up()
    pen.goto(x, y)
    pen.color(color)
    pen.dot()


def draw_map(x_player, y_player):
    pen.clear()
    y_count = 0
    x_count = 0
    for y in range(400, -50, -50):
        y_count += 1
        for x in range(-400, 50, 50):
            x_count += 1
            if x_count == 5 and y_count == 5:
                draw_asset('red', x, y)
            else:
                map_char = map_array[y_player - (-4 + y_count)][x_player - (-4 + x_count)]
                if map_char == '#':
                    draw_asset('green', x, y)
                elif map_char == '1':
                    draw_asset('yellow', x, y)
                elif map_char == '2':
                    draw_asset('purple', x, y)
                else:
                    draw_asset('black', x, y)
        x_count = 0
    window.update()


map_array = []

with open('mapTest.txt') as file:
    for line in file:
        map_array.append(line.strip('\n'))


class points:
    x_p = 14
    y_p = 9

    def w(self):
        points.y_p += 1

    def s(self):
        points.y_p -= 1

    def a(self):
        points.x_p += 1

    def d(self):
        points.x_p -= 1


p = points

window.listen()
window.onkey(p.a, "w")
window.onkey(p.s, "s")
window.onkey(p.a, "a")
window.onkey(p.d, "d")
window.mainloop()



# while True:
#     inp = input()
#     if inp == 'w':
#         y_p += 1
#     elif inp == 's':
#         y_p -= 1
#     elif inp == 'a':
#         x_p += 1
#     elif inp == 'd':
#         x_p -= 1
#     draw_map(x_p, y_p)
