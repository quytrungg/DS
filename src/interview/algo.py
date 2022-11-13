import turtle

t = turtle.Turtle()
t.speed(0)
size = 2

def initialize(c, s, x, y):
  t.pensize(s)
  t.penup()
  t.goto(x, y)
  t.pendown()
  t.color(c)

def draw_circle(c, r, s, x, y):
  initialize(c, s, x, y)
  t.begin_fill()
  t.circle(r)
  t.end_fill()
  
def draw_star(c, s, x, y):
  initialize(c, s, x, y)
  t.begin_fill()
  for _ in range(5):
    t.forward(20)
    t.right(144)
  t.end_fill()
  
draw_circle('red', 50, size, -50, 0)
dist = 30
for _ in range(4):
  draw_star('red', size, dist, 50)
  dist += 40
  
dist = -150
for _ in range(2):
  draw_star('red', size, dist, 50)
  dist -= 40
  
dist = 130
for _ in range(2):
  draw_star('red', size, -60, dist)
  dist -= 160

# first bar
initialize('blue', size, -130, -80)
t.begin_fill()
t.left(60)
t.forward(80)
t.right(90)
t.forward(10)
t.right(80)
t.forward(70)
t.right(75)
t.forward(25)
t.end_fill()

# second bar
initialize('blue', size, 10, -80)
t.begin_fill()
t.right(55)
t.forward(70)
t.right(85)
t.forward(10)
t.right(90)
t.forward(80)
t.right(120)
t.forward(20)
t.end_fill()

# third bar
initialize('blue', size, 100, -80)
t.begin_fill()
t.right(45)
t.forward(120)
t.right(100)
t.forward(15)
t.right(80)
t.forward(140)
t.right(140)
t.forward(25)
t.end_fill()
# 4th bar
initialize('blue', size, 180, -80)
t.begin_fill()
t.right(35)
t.forward(170)
t.right(100)
t.forward(15)
t.right(70)
t.forward(150)
t.right(75)
t.forward(45)
t.end_fill()

# 5th bar


# 6th bar


# 7th bar


# 8th bar


# 9th bar


# 10th bar


# 11th bar


# 12th bar

