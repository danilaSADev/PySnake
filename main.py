from enum import Enum
import sys
import os 
import snake as sn
import time as time
import tkinter as tk

window = tk.Tk()
window.title("Snake Game")
cell_size = 40
board = sn.GameBoard(tk, sn.Vector2(20, 20), cell_size)
board.DrawField()

class Direction(Enum):
    Left = sn.Vector2(-1, 0)
    Up = sn.Vector2(0, -1)
    Right = sn.Vector2(1, 0)
    Down = sn.Vector2(0, 1)

print(sn.Vector2(0,0) == sn.Vector2(0, 0))

def onKeyPress(event):
    kc = event.keycode - 36
    if kc == 1 and board.snake.direction != Direction.Right.value:
        board.snake.ChangeDirection(Direction.Left.value)
    elif kc == 2 and board.snake.direction != Direction.Down.value:
        board.snake.ChangeDirection(Direction.Up.value)
    elif kc == 3 and board.snake.direction != Direction.Left.value:
        board.snake.ChangeDirection(Direction.Right.value)
    elif kc == 4 and board.snake.direction != Direction.Up.value:
        board.snake.ChangeDirection(Direction.Down.value)

window.bind('<KeyPress>', onKeyPress)

while not board.isGameOver:
    board.Frame()
    board.DrawField()
    window.update()
    window.update_idletasks()
    time.sleep(0.05)

board.Clear()
os.execv(sys.executable, sys.argv)

