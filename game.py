#__________________________________operation on names____________________________

NAME=input("Enter your name: ")
OP_NAME=input("Enter other person name: ")

NAME=NAME.replace(" ","")
OP_NAME.replace(" ","")

name=NAME.upper()
p_name=OP_NAME.upper()

old=name+p_name
c_old=len(old)

#__________________________________________________________________________________
#__________________________________________________________________________________
#________________________________common letters ___________________________________


for i in name:
    for j in p_name:
        if i == j:
            name=name.replace(i,"")
            p_name=p_name.replace(i,"")
            #print(f"Name: {name} Partner's name{p_name}")

total=name+p_name
length=len(total)

how_much=c_old-length
percentage=(how_much*100)//c_old
#print("Percentage:",percentage)









if length%3 == 1:
    for i in range(100000000):
        if i%10000000==0:
            print("*",end="") 
    print("\n")
    print(f"Friendship...{percentage} percent ")
    if 50<=percentage<=65:
        print("Not Bad...")
    elif 65<percentage<=80:
        print("Good friends...")
    elif 80<percentage<=100:
        print("Best friends...")       




elif length%3 == 2:
    for i in range(100000000):
        if i%10000000==0:
            print("*",end="")
    print("\n")
    print(f"Love...{percentage} percent ")
    if 50<=percentage<=65:
        print("Not Bad...")
    elif 65<percentage<=80:
        print("Good partners...")
    elif 80<percentage<=100:
        print("Made for each other...😘")
      

    
elif length%3 == 0:
    for i in range(100000000):
        if i%10000000==0:
            print("😡",end="")
    print("\n")
    print(f"Hate...{percentage} percent ")
    
    if 50<=percentage<=65:
        print("It's ohk...")
    elif 65<percentage<=80:
        print("Nikal lo...")
    elif 80<percentage<=100:
        print("Want to kill each other...")      



















#___________________________________________________________________________
#_______________________________xxx_________________________________________

"""
print("Common letters {0}".format(letter))
print("Total letters {}".format(total))





percantage=(letter*100)/total

print("Percantage: {0}".format(percantage))

"""
