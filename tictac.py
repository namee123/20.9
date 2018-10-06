a=[1,2,3,4,5,6,7,8,9]
def printboard():
	print(a[0],'|',a[1],'|',a[2])
	print('-----------')
	print(a[3],'|',a[4],'|',a[5])
	print('------------')
	print(a[6],'|',a[7],'|',a[8])

player1turn=True
while True:
	printboard()
	p=int(input('choose yor place >>'))
	if(p in a):
		if player1turn:
		#p=(input('choose your place,player1>>'))
			print('player1 choice')
			a[int(p)-1]='X'
			player1turn=not player1turn
		else:
		#p=(input('choose your place,player2>>'))
			print('player2 choice')
			a[int(p)-1]='O'
			player1turn=not player1turn
		#checck for winning
		for i in range(0,3,6):
			if(a[i]==a[i+1] and a[i]==a[i+2]):
				print('player 1 wins')
				exist()
			else:
				print('player2 wins ')
				exist()
		for i in range(3):
			if(a[i]==a[i+3]and a[i]=a[i+6]):
				if a[i]='X'
				print('player 1 wins')
				exist()
				
					

	else:
		continue		




