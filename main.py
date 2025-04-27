import turtle

window = turtle.Screen()
window.title("Drawing_shapes")

t = turtle.Turtle()
t.shape("turtle")

while True:
    try:
        choose_shape = int(input("Choose shape to draw (1 - square, 2 - triangle, 3 - spiral, 4 - circle): "))
        if choose_shape not in [1, 2, 3, 4]:
            print("Invalid choice! Please select a number from 1 to 4.")
            continue
    except ValueError:
        print("Please enter a valid number!")
        continue

    if choose_shape == 1:
        for _ in range(4):
            t.forward(100)
            t.right(90)
    elif choose_shape == 2:
        for _ in range(3):
            t.forward(100)
            t.left(120)
    elif choose_shape == 3:
        for i in range(36):
            t.forward(i * 5)
            t.right(90)
    elif choose_shape == 4:
        t.circle(50)
        t.right(90)
    
    draw_again = input("Repeat drawing? (yes/no)").lower()

    if draw_again == "no":
        print("End of the program.")
        break
    elif draw_again == "yes":
        t.reset()
        continue
