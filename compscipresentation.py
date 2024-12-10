import turtle

Sheldon = turtle.Turtle()
Chris = turtle.Turtle()


screen=turtle.Screen()
screen.setup(500, 500)
screen.bgcolor('SpringGreen')

#intro page
Sheldon.penup()
Sheldon.goto(0,20)
Sheldon.pendown()
Sheldon.fillcolor('YellowGreen')
Sheldon.begin_fill()
Sheldon.circle(20)
Sheldon.end_fill()
Chris.penup()
turtle.addshape("turtle.gif")
Chris.shape("turtle.gif")
Chris.goto(-160,160)
Chris.stamp()
Chris.penup()
turtle.addshape("turtle3.gif")
Chris.shape("turtle3.gif")
Chris.goto(160,-160)
Chris.stamp()
Sheldon.fillcolor('black')
Sheldon.penup()
Sheldon.goto(0,75)
Sheldon.pendown()
Sheldon.write("-Who I Am-", font=("Playfair Display", 24, "bold"),align="center")
Sheldon.penup()
Sheldon.hideturtle()
Sheldon.goto(-67.5, -10)
Sheldon.write("Welcome to my turtle presentation!", font=("Bebas Neue", 10, "bold"),align="center")
Sheldon.goto(-67.5, -20)
Sheldon.write("To move from one page to the next,",font=("Bebas Neue", 10, "bold"),align="center")
Sheldon.goto(-67.5, -30)
Sheldon.write("press the Enter button on your keyboard.",font=("Bebas Neue", 10, "bold"),align="center")
Sheldon.goto(-80,-35)
Sheldon.pendown()
Sheldon.fillcolor('black')
Sheldon.begin_fill()
Sheldon.forward(25)
Sheldon.right(90)
Sheldon.forward(35)
Sheldon.left(90)
Sheldon.forward(10)
Sheldon.goto(-67.5,-90)
Sheldon.goto(-90,-70)
Sheldon.forward(10)
Sheldon.left(90)
Sheldon.forward(35)
Sheldon.end_fill()
enter = input("Press Enter to continue: ")
Chris.clear()
Chris.hideturtle()
Sheldon.clear()

#food page
screen.bgcolor('tomato')
Sheldon.penup()
Sheldon.goto(0,200)
Sheldon.pendown()
Sheldon.fillcolor('DarkRed')
Sheldon.begin_fill()
Sheldon.write("Favorite Foods", font=("Cherry Cream Soda", 24, "bold"),align="center")
Sheldon.end_fill()
Sheldon.penup()
Sheldon.goto(0,150)
Sheldon.pendown()
Sheldon.write("These are some of my favorite foods.",font=("Bebas Neue", 10, "bold"),align="center")
Chris.penup()
turtle.addshape("pizza.gif")
Chris.shape("pizza.gif")
Chris.goto(-150,100)
Chris.stamp()
Sheldon.penup()
Sheldon.goto(-150, 10)
Sheldon.pendown()
Sheldon.write("I love pizza because there is so\nmuch variety, and it tastes \nreally good.",font=("Bebas Neue", 8, "bold"),align="center")
Chris.penup()
turtle.addshape("raspberry.gif")
Chris.shape("raspberry.gif")
Chris.goto(150,100)
Chris.stamp()
Sheldon.penup()
Sheldon.goto(150,10)
Sheldon.pendown()
Sheldon.write("Raspberries are my favorite\nbecause they're tart and sweet.",font=("Bebas Neue", 9, "bold"),align="center")
Chris.penup()
turtle.addshape("breadstick.gif")
Chris.shape("breadstick.gif")
Chris.goto(0,-60)
Chris.stamp()
Sheldon.penup()
Sheldon.goto(0,-150)
Sheldon.pendown()
Sheldon.write("I love Olive Garden because \ntheir breadsticks are delicious.",font=("Bebas Neue", 10, "bold"),align="center")
Sheldon.penup()
Sheldon.goto(0,60)
Sheldon.pendown()
Sheldon.pencolor('firebrick')
Sheldon.fillcolor('indianred')
Sheldon.begin_fill()
Sheldon.goto(40,30)
Sheldon.goto(-40,30)
Sheldon.goto(0,60)
Sheldon.end_fill()
enter = input("Press Enter to continue: ")
Sheldon.clear()
Chris.clear()
Chris.hideturtle()


#hobby page
screen.bgcolor('skyblue')
Sheldon.penup()
Sheldon.goto(0,200)
Sheldon.pendown()
Sheldon.pencolor('DodgerBlue')
Sheldon.fillcolor('DodgerBlue')
Sheldon.begin_fill()
Sheldon.write("Hobbies", font=("Fuzzy Bubbles", 24, "bold"),align="center")
Sheldon.penup()
Sheldon.goto(0,170)
Sheldon.pendown()
Sheldon.write("These are some of my favorite activities.", font=("Fuzzy Bubbles", 10, "bold"),align="center")
Sheldon.end_fill()
Chris.penup()
turtle.addshape("theatre.gif")
Chris.shape("theatre.gif")
Chris.goto(-150,80)
Chris.stamp()
Chris.penup()
turtle.addshape("sing.gif")
Chris.shape("sing.gif")
Chris.goto(150,100)
Chris.stamp()
Chris.penup()
turtle.addshape("art.gif")
Chris.shape("art.gif")
Chris.goto(150,-100)
Chris.stamp()
Chris.penup()
turtle.addshape("beanieboo.gif")
Chris.shape("beanieboo.gif")
Chris.goto(-150,-120)
Chris.stamp()
Chris.penup()
Chris.goto(-150, 60)
Chris.pendown()
Chris.write("I love to perform.", font=("Fuzzy Bubbles", 10, "bold"),align="center")
Chris.penup()
Chris.goto(150,40)
Chris.pendown()
Chris.write("I love to sing.", font=("Fuzzy Bubbles", 10, "bold"),align="center")
Chris.penup()
Chris.goto(150, -150)
Chris.pendown()
Chris.write("I love art.", font=("Fuzzy Bubbles", 10, "bold"),align="center")
Chris.penup()
Chris.goto(-150, -160)
Chris.pendown()
Chris.write("I love to collect Beanie Boos \n(collector's items).", font=("Fuzzy Bubbles", 10, "bold"),align="center")
Sheldon.penup()
Sheldon.goto(0,-30)
Sheldon.pendown()
Sheldon.pencolor('CornflowerBlue')
Sheldon.fillcolor('LightCyan')
Sheldon.begin_fill()
Sheldon.right(90)
Sheldon.forward(20)
Sheldon.left(90)
Sheldon.forward(40)
Sheldon.left(90)
Sheldon.forward(40)
Sheldon.left(90)
Sheldon.forward(40)
Sheldon.left(90)
Sheldon.forward(20)
Sheldon.end_fill()
enter = input("Press Enter to continue: ")
Sheldon.clear()
Chris.clear()
Chris.hideturtle()

#movie page
screen.bgcolor('black')
Sheldon.penup()
Sheldon.goto(0,200)
Sheldon.pendown()
Sheldon.pencolor('Red')
#Sheldon.begin_fill()
Sheldon.write("M  v e", font=("Fuzzy Bubbles", 24, "bold"),align="center")
#Sheldon.end_fill()
Sheldon.pencolor('White')
#Sheldon.begin_fill()
Sheldon.write("     o  i  s", font=("Fuzzy Bubbles", 24, "bold"),align="center")
#Sheldon.end_fill()
Sheldon.penup()
Sheldon.goto(0,150)
Sheldon.pendown()
Sheldon.write("  These are my three favorite movies.", font=("Fuzzy Bubbles", 10, "bold"),align="center")
Chris.penup()
turtle.addshape("movie.gif")
Chris.shape("movie.gif")
Chris.goto(-100,0)
Chris.stamp()
Sheldon.pencolor('white')
Sheldon.penup()
Sheldon.goto(-120, -60)
Sheldon.pendown()
Sheldon.write("Annabelle: Creation", font=("Fuzzy Bubbles", 10, "bold"),align="center")
Chris.penup()
turtle.addshape("movie2.gif")
Chris.shape("movie2.gif")
Chris.goto(145,0)
Chris.stamp()
Sheldon.penup()
Sheldon.goto(145, -70)
Sheldon.pendown()
Sheldon.write("The Tigger Movie", font=("Fuzzy Bubbles", 10, "bold"),align="center")
Chris.penup()
turtle.addshape("movie3.gif")
Chris.shape("movie3.gif")
Chris.goto(15,-100)
Chris.stamp()
Sheldon.penup()
Sheldon.goto(0, -170)
Sheldon.pendown()
Sheldon.write("The Greatest Showman", font=("Fuzzy Bubbles", 10, "bold"),align="center")
Sheldon.penup()
Sheldon.goto(0,15)
Sheldon.pendown()
Sheldon.pencolor('white')
Sheldon.fillcolor('white')
Sheldon.begin_fill()
Sheldon.forward(10)
Sheldon.left(90)
Sheldon.forward(60)
Sheldon.left(90)
Sheldon.forward(20)
Sheldon.left(90)
Sheldon.forward(60)
Sheldon.left(90)
Sheldon.forward(10)
Sheldon.end_fill()
enter = input("Press Enter to continue: ")
Sheldon.clear()
Chris.clear()
Chris.hideturtle()

#sport page
screen.bgcolor('cornsilk')
Sheldon.penup()
Sheldon.goto(0,200)
Sheldon.pendown()
Sheldon.pencolor('brown')
Sheldon.write("Sports", font=("Fuzzy Bubbles", 24, "bold"),align="center")
Sheldon.penup()
Sheldon.goto(0,150)
Sheldon.pendown()
Sheldon.write("These are my two favorite sports.", font=("Fuzzy Bubbles", 10, "bold"),align="center")
Chris.penup()
turtle.addshape("ballet.gif")
Chris.shape("ballet.gif")
Chris.goto(-100,0)
Chris.stamp()
Sheldon.penup()
Sheldon.goto(-105,-50)
Sheldon.pendown()
Sheldon.write("Ballet/Dance", font=("Fuzzy Bubbles", 10, "bold"),align="center")
Chris.penup()
turtle.addshape("badminton.gif")
Chris.shape("badminton.gif")
Chris.goto(100,0)
Chris.stamp()
Sheldon.penup()
Sheldon.goto(105,-50)
Sheldon.pendown()
Sheldon.write("Badminton", font=("Fuzzy Bubbles", 10, "bold"),align="center")
Sheldon.penup()
Sheldon.goto(0,20)
Sheldon.pendown()
Sheldon.pencolor('SandyBrown')
Sheldon.fillcolor("NavajoWhite")
Sheldon.begin_fill()
Sheldon.goto(20,40)
Sheldon.goto(0,60)
Sheldon.goto(-20,40)
Sheldon.goto(0,20)
Sheldon.end_fill()
enter = input("Press Enter to continue: ")
Sheldon.clear()
Chris.clear()
Chris.hideturtle()

Sheldon.penup()
Sheldon.goto(0,60)
Sheldon.pendown()
Sheldon.write("The End!", font=("Fuzzy Bubbles", 24, "bold"),align="center")
Chris.penup()
turtle.addshape("turtle2.gif")
Chris.shape("turtle2.gif")
Chris.goto(-160,160)
Chris.stamp()
Chris.penup()
turtle.addshape("turtle4.gif")
Chris.shape("turtle4.gif")
Chris.goto(160,160)
Chris.stamp()
Sheldon.penup()
Sheldon.goto(0,20)
Sheldon.pendown()
Sheldon.write("Thank you for watching my turtle presentation!", font=("Fuzzy Bubbles", 10, "bold"),align="center")
Sheldon.penup()
Sheldon.goto(-80,-35)
Sheldon.pendown()
Sheldon.fillcolor('black')
Sheldon.begin_fill()
Sheldon.forward(25)
Sheldon.right(90)
Sheldon.forward(35)
Sheldon.left(90)
Sheldon.forward(10)
Sheldon.goto(-67.5,-90)
Sheldon.goto(-90,-70)
Sheldon.forward(10)
Sheldon.left(90)
Sheldon.forward(35)
Sheldon.end_fill()
Chris.penup()
Chris.goto(-80, -25)
Chris.pendown()
Chris.write("Press Enter to end.", font=("Fuzzy Bubbles", 10, "bold"),align="center")
enter = input("Press Enter to end:")
Sheldon.clear()
Chris.clear()
Chris.hideturtle()

