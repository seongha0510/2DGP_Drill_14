import turtle
import random
import math  # 삼각함수(cos, sin)를 사용하기 위해 math 모듈을 가져옵니다.


def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)  # 축 그리는 속도
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(0)  # 도형 그리는 속도 (0이 가장 빠름)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     ' + str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())


def draw_parametric_shape(k, scale, steps):
    a = k
    b = 1.0
    t_end = 20 * math.pi

    print(f"Drawing shape for k={k}, scale={scale}, steps={steps}")

    for i in range(0, steps + 1):
        t = (i / steps) * t_end

        x = (a - b) * math.cos(t) + b * math.cos(t * (a / b - 1))
        y = (a - b) * math.sin(t) - b * math.sin(t * (a / b - 1))

        draw_point((x * scale, y * scale))

prepare_turtle_canvas()

draw_parametric_shape(k=1.3, scale=50, steps=1000)

turtle.done()