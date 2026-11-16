import random

from block import Block



class ComputerBlock(Block):
    def __init__(self, difficulty):
        super().__init__()
        self.goto(450, 0)
        if difficulty == "easy":
            self.COMPUTER_BLOCK_SPEED= 1.5
        elif difficulty == "medium":
            self.COMPUTER_BLOCK_SPEED = 2
        else:
            self.COMPUTER_BLOCK_SPEED = 2.5

    def up(self):
        self.forward(self.COMPUTER_BLOCK_SPEED)

    def down(self):
        self.backward(self.COMPUTER_BLOCK_SPEED)

    def follow_ball(self, ball_ycor):
        if self.ycor() < ball_ycor:
            self.up()
        elif self.ycor() > ball_ycor:
            self.down()
        else:
            return
