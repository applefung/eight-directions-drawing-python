import turtle

number_of_divisions = 8 # The number of subdivisions around the centre
turtle_width = 5         # The width of the turtles
# Don't show the animation
turtle.tracer(False)

turtle.color("gray")
for i in range(number_of_divisions):
    turtle.forward(500)
    turtle.backward(500)
    turtle.left(360 / number_of_divisions)
turtle.color("black")

# Create the required turtles
allTurtles = [] # The turtles are put in this list

# The default turtle is the first one in the list
turtle.shape("circle")
turtle.shapesize(2,2)
turtle.width(turtle_width)
##### Add your code here #####
allTurtles.append(turtle)
# Add the rest of the turtles in the list
for c in range(1,number_of_divisions):
    newTurtle=turtle.Turtle()
    allTurtles.append(newTurtle)
    newTurtle.width(turtle_width)
    newTurtle.hideturtle()
    

def draw(x,y):
    print(x,y)
    turtle.ondrag(None)
    turtle.goto(x,y)
    xt=[1,1,-1,-1,1,1,-1,-1]
    yt=[1,1,-1,-1,1,1,-1,-1]
    for a in range(1,number_of_divisions):
        new_x = x
        new_y = y
        if a < 4:
            new_x = x*xt[a]
            new_y = y*yt[a]
        else:
            new_x = y*yt[a]
            new_y = x*xt[a]
        allTurtles[a].goto(new_x,new_y)
    turtle.update()
    turtle.ondrag(draw)

def click(x,y):
    for d in range(len(colours)):
        if x <= (-130+50*d):
            for cc in range(8):
                allTurtles[cc].color(colours[d])
            turtle.update()
            break
        turtle.update()
        
# Draw the background lines



print(len(allTurtles))    
turtle.ondrag(draw)
##### Add your code here #####

# Set up the ondrag event

##### Add your code here #####

# Make the colour selection turtles
# Here is the list of colours
colours = ["black", "tomato", "spring green", "slate blue", "turquoise", "orchid", "gold"]

##### Add your code here #####
for  b in range(len(colours)):
    newTurtle = turtle.Turtle()
    newTurtle.shape("square")
    newTurtle.shapesize(2,2)
    newTurtle.color(colours[b])
    x=-150+50*b
    newTurtle.up()
    newTurtle.goto(x,-250)
    newTurtle.onclick(click)
# Set up the onclick events
##### Add your code here #####


turtle.update()

turtle.done()
