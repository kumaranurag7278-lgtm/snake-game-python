from turtle import Turtle,Screen

class ScoreBored(Turtle):
    

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("blue")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scorebored()

    def update_scorebored(self):
        self.write(f"SCORE : {self.score} ",False, align="center",font=("Aerial", 24 ,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",False,align="center",font=("arial",25,"normal"))

    def score_update(self):
        
        self.score += 1
        self.clear()
        self.update_scorebored()




