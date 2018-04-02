print("hello python world")
message = "hello zh"
print(message)

name = "yue ruiqing"
print(name.title())
print(name.lower())
print(name.upper())


bycyles = ['a', 'f', 'b', 'c']
print(bycyles[0])
print(bycyles[-1])

bycyles.append('d')
print(bycyles)

bycyles.sort(reverse = True)
print(bycyles)

print(len(bycyles))

for b in bycyles:
	if b == 'c':
		print("c is here")
	elif b == "b":
		print("b haha")
	else:
		print(b)

alien = {'color': 'red', 'point': 1}
print(alien)

print(alien['color'])

for key, value in alien.items():
	print("key=" + key + ", value=" + str(value))


def greet_user():
	print("hello")

greet_user()

