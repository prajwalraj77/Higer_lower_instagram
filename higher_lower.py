import random
from replit import clear
import art 
print(art.logo)
from game_data import data
count=0
def random_data():
    flag=False 
    global count
    while not flag:
        details1=random.choice(data)
        details_of_1= [details1["name"],details1['description'],details1['country']]
        print(details_of_1)
        
        print(art.vs)

        details2=random.choice(data)
        details_of_2= [details2["name"],details2['description'],details2['country']]
        print(details_of_2)

        user_input=input(" A or B : ")
        if user_input=='A':
            
            if details1['follower_count']>details2['follower_count']:
                print("yes")
                clear()
                count+=1
            else:
                print("no ur answer is wrong")
                flag=True
                
        elif user_input=='B':
            
            if details1['follower_count']<details2['follower_count']:
                print("yes")
                count+=1
                clear()
            else:
                print("no ur answer is wrong")
                flag=True
                
        else :
            print("Type only A or B")
    return count 

random_data()

print(f" ur score is {count}")



