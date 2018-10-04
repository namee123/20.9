import random
print('welcome to the game stone paper scissors')
g={1:'r',2:'p',3:'s'}

a=0
b=0
while a<3 and b<3:
	c=g[random.randint(1,3)]
	m=input('your choice stone/paper/scissor or q to quit')
	if m=='q':
		print('bye')
		exit()
	if(c==m):
		print("it's tie")
	elif(c=='r'):
		if(m=='p'):
			print('computer wins')
			b=b+1
		else:
			print('you win')
			a=a+1
	elif(c=='p'):
		if(m=='s'):
			print("you win")
			a=a+1
		else:
			print('computer wins')
			b=b+1
	elif(c=='s'):
		if(m=='r'):
			print('you win')
			a=a+1
		else:
			print('computer wins')
			b=b+1
	if a==3:
		print('you win')
	elif b==3:
		print('computer wins')
		