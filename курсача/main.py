from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter
import matplotlib.pyplot as plt


while True:
	try:
		text = input("calc > ")
		# list values
		list_x, list_y = [], []
		# quantity_point
		n = int(input('Quantity point = '))
		for i in range(n):
			value_x = input('x = ')
			lexer = Lexer(text, value_x, list_x)
			list_x = lexer.Valuex()
			tokens = lexer.generate_tokens()
			parser = Parser(tokens)
			tree = parser.parse()
			if not tree: continue
			interpreter = Interpreter()
			value = interpreter.visit(tree)
			list_y.append(value)
			print('y = ', value)
		print(list_x)
		print(list_y)

		plt.plot(list_x, list_y)
		plt.show()

	except Exception as e:
		print(e)


