# Python equivalents of do-while and do-until constructs
# using lambda


def do_until(pred):
	while True:
		yield
		if pred():
			break


def do_while(pred):
	return do_until(lambda: not pred())
	###yield from do_until(lambda: not pred())


x = 0
for _ in do_while(lambda: x < 6):
	print(x)
	x += 1

print('------')

for _ in do_until(lambda: x == 2):
	print(x)
	x -= 1

