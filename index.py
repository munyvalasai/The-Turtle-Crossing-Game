from turtle import Screen
import time
from player import Player
from manage_cars import ManageCars
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
manage_car = ManageCars()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_over = False
while not game_over:
    time.sleep(0.1)
    screen.update()
    manage_car.create_car()
    manage_car.move_cars()

    # Collision with cars
    for car in manage_car.all_cars:
        if car.distance(player) < 20:
            game_over = True
            scoreboard.game_over()

    # Player reached the other side
    if player.reached_at_other_side():
        player.go_to_start()
        manage_car.level_up()
        scoreboard.update_level()





screen.exitonclick()