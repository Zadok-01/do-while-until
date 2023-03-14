# Python equivalents of do-while and do-until constructs
# using eval


def do_until(cond):
	while True:
		yield
		if eval(cond):
			break


def do_while(cond):
	return do_until(f'not({cond})')
	###yield from do_until(f'not({cond})')


x = 0
for _ in do_while('x < 6'):
	print(x)
	x += 1

print('------')

for _ in do_until('x == 2'):
	print(x)
	x -= 1

