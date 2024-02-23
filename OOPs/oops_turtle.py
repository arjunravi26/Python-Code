# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red")
# timmy.fillcolor('#ffffff')
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
x=PrettyTable()
x.add_column("States",['Kerala','Tamil Nadu','Karnataka','Goa','Delhi'])
x.add_column("Capitals",['Thiruvananthapuram','Chennai','Bengaluru','Panaji','Delhi'])
x.add_row(['Andra Pradesh','Amravati'])
x.align='l'
print(x.align)
print(x)