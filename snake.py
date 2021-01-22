from config import Config
from food import Food
import random

class Snake():
    UP='up'
    DOWN='down'
    LEFT='left'
    RIGHT='right'
    HEAD=0
    def __init__(self):
        self.snakePosition()
    def snakePosition(self):
        self.x= random.randint(5,Config.CELLWIDTH-6)
        self.y= random.randint(5,Config.CELLHEIGHT-6)
        self.direction=self.RIGHT
        self.snakeCoods=[
            {'x':self.x,'y':self.y},{
            'x': self.x-1, 'y': self.y}
            ,{'x':self.x-2, 'y': self.y}
        ]

    def update(self,apple):
        if self.snakeCoods[self.HEAD]['x']==apple.x and self.snakeCoods[self.HEAD]['y']==apple.y:
            apple.setNewLocation()
        else:
            del self.snakeCoods[-1]
        if self.direction==self.UP:
            newHead={'x':self.snakeCoods[self.HEAD]['x'],'y':self.snakeCoods[self.HEAD]['y']-1}

        elif self.direction == self.DOWN:
            newHead = {'x': self.snakeCoods[self.HEAD]['x'], 'y': self.snakeCoods[self.HEAD]['y'] + 1}

        elif self.direction == self.LEFT:
            newHead = {'x': self.snakeCoods[self.HEAD]['x']-1, 'y': self.snakeCoods[self.HEAD]['y'] }

        elif self.direction == self.RIGHT:
            newHead = {'x': self.snakeCoods[self.HEAD]['x']+1, 'y': self.snakeCoods[self.HEAD]['y'] }

        self.snakeCoods.insert(0,newHead)