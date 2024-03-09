import turtle

t = turtle.Turtle()
t.speed(10)  # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest


def squaire(a):
    for i in range(4):
        t.forward(a)
        t.left(90)


def treugolnik(a):
    for i in range(3):
        t.forward(a)
        t.left(120)


squaire(100)
t.left(90)
t.forward(35)
t.right(90)
t.up()
t.forward(35)
t.down()
squaire(30)
squaire(15)
t.up()
t.forward(15)
t.left(90)
t.down()
t.forward(15)
t.right(90)
squaire(15)
t.up()
t.goto(100, 100)
t.down()
for i in range(2):
    t.left(120)
    t.forward(100)

turtle.done()
