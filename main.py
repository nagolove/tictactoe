exm3 = "XOOOXOXXO"

def fill(exm):
	pole=[]
	for i in range(0,3):
		pole.append([])
	counter1=0
	counter2=0	
	for char in exm:
		if counter1%3==0:
			counter2+=1
			counter1=0
			
		pole[counter2-1].append(char)
		#print(counter2)
		counter1+=1
		
	return pole

def test():
        print("exm3", exm3)
        pole = fill(exm3)
        print(pole)

test()
