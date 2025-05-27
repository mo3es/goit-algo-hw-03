import turtle

# Визначення функції побудови кривої Коха від одиночного відрізку. Функція приймає 
# відображувач t - Turtle, глибину рекурсії order

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

# Визначення функції побудови сніжинки Коха. Функція приймає глибину рекурсії order та кількість граней, 
# від яких будується сніжинка - edges та ініціалізує відображувач t - Turtle. Ітеративно, залежно від кількості граней,
# викликає функцію побудови кривої Коха, після чого здійснює поворот відображувача на кут 360 / кількість граней
# точне позіціонування відображення залежно від кількості граней потребує доопрацювання та значних математичних розрахунків - 
# в даній роботі не здійснювалось
def draw_koch_curve(order, edges, size = 300):
    window = turtle.Screen()
    window.setup(width = 1200, height=1000)
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size * (edges / 10 if edges >= 10 else 1/2), size * (edges / 10 if edges >= 10 else 1/2))
    t.pendown()
    for _ in range(edges):
        koch_curve(t, order, size)
        t.right(360/edges)

    window.mainloop()

# Запитуємо у користувача глибину рекурсії та кількість граней побудови, у разі введення нечислового значення
# встановлюємо значення за замовчуванням. З отриманими значеннями викликає функцію побудови сніжинки Коха
if __name__ == "__main__":
    order = input("Введіть глибину рекурсії (за замовчуванням - 3)\n")
    edges = input("Введіть кількість граней побудови сніжинки (за замовчуванням - 3)\n")
    order = int(order) if order.isnumeric() else 3
    edges = int(edges) if edges.isnumeric() else 3
    draw_koch_curve(order, edges)
