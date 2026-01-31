from turtle import Turtle , Screen 
import time
from snake_class  import Snake
from food import Food
from score import ScoreBored
screen = Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title("My snake game")

screen.tracer(0)
    
snake = Snake()
food = Food()
scoreBored = ScoreBored()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_is_on = True   


while game_is_on:
    screen.update() 
    time.sleep(0.1)   
    snake.move()


    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreBored.score_update()
    
    # detect collison to the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreBored.game_over()

    # detect the collison with snake body
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreBored.game_over




screen.exitonclick()



