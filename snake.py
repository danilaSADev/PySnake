import math as math
import random

class Vector2:
	x = 0
	y = 0
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, vec):
		return Vector2(self.x + vec.x, self.y + vec.y)

	def __sub__(self, vec):
		return Vector2(self.x - vec.x, self.y - vec.y)


	def __repr__(self):
		result = "( x: {}; y: {} )".format(self.x, self.y)
		return result

	def __eq__(self, vec):
		return self.x == vec.x and self.y == vec.y

	def IsIn(self, vec):
		if (0 < vec.x < self.x and 0 < vec.y < self.y):
			return vec
		if vec.x >= self.x:
			vec.x = 0
		elif vec.x < 0:
			vec.x = self.x - 1
		if vec.y >= self.y:
			vec.y = 0
		elif vec.y < 0:
			vec.y = self.y - 1
		return vec	

	def random(x, y):
		return Vector2(random.randint(0, x), random.randint(0, y))

class Snake:
	length = 2
	sections = []
	direction = Vector2(0, 0)
	def __init__(self, center):
		super(Snake, self).__init__()
		self.sections.append(center) 
		self.sections.append(center)
		self.direction = Vector2(-1, 0)
	
	def GetSize(self):
		return self.length

	def PickupBonus(self):
		self.sections.append(self.sections[len(self.sections) - 1])
		self.length = self.length + 1

	def IsInBoard(self, board_size):
		sections = self.sections
		for i in range(len(sections)):
			sections[i] = board_size.IsIn(sections[i])
				
	def MoveForward(self, board_size):
		for i in range(len(self.sections) - 1, 0, -1):
			self.sections[i] = self.sections[i - 1]
		self.sections[0] = self.sections[0] + self.direction
		self.IsInBoard(board_size)
		for i in range(1, len(self.sections)):
			if (self.Head() == self.sections[i]):
				return True
		return False

	def ChangeDirection(self, newDirection):
		self.direction = newDirection

	def Head(self):
		return self.sections[0]

class GameBoard:
	board_size = Vector2(0, 0)
	isGameOver = False
	bonus = NotImplemented
	canvas = NotImplemented
	snake = NotImplemented
	def __init__(self, tk, board_size, cell_size):
		self.canvas = tk.Canvas(width=500, height=500)
		self.canvas.pack()
		self.board_size = board_size
		self.snake = Snake(Vector2(int(board_size.x/2), int(board_size.y/2)))
		self.GenerateBonus()
		self.cell_size = cell_size 

	def Frame(self):
		self.isGameOver = self.snake.MoveForward(self.board_size)
		if not self.bonus:
			self.GenerateBonus()
		if (self.snake.Head() == self.bonus):
			self.snake.PickupBonus()
			self.GenerateBonus()

	def GenerateBonus(self):
		notGenerated = True
		tempVec = Vector2.random(self.board_size.x, self.board_size.y)
		while notGenerated:
			notGenerated = False
			tempVec = Vector2.random(self.board_size.x - 1, self.board_size.y - 1)
			for i in range(len(self.snake.sections)):
				if (self.snake.sections[i] == tempVec):
					notGenerated = True
		self.bonus = tempVec

	def DrawField(self):
		self.canvas.delete("all")
		for x in range(self.board_size.x):
			for y in range(self.board_size.y):
				tempVec = Vector2(x, y)
				isSnakeHere = False
				snake = self.snake
				for i in range(len(self.snake.sections)):
					if (snake.sections[i] == tempVec):
						isSnakeHere = True

				if isSnakeHere:
					self.canvas.create_rectangle(self.cell_size * x, self.cell_size * y, self.cell_size * (x + 1), self.cell_size * (y + 1), fill='red')
				elif tempVec == self.bonus:
					self.canvas.create_rectangle(self.cell_size * x, self.cell_size * y, self.cell_size * (x + 1), self.cell_size * (y + 1), fill='lightgreen')
				else: 
					self.canvas.create_rectangle(self.cell_size * x, self.cell_size * y, self.cell_size * (x + 1), self.cell_size * (y + 1), fill='gray')

	def Clear(self):
		self.canvas.delete("all")
				