"""
input it 39
output is 3+9=12
usually the input takes it in the for of string only
xyz =input("enter a number")
r=0
print(type(xyz))
for i in range(0,len(xyz)):
    r+=int(xyz[i])
print(r)
PEMDASLR
PARANTHESIS EXPONENTS MULTIPLICATON DIVISION ADD SUB

round function it takes two parameters, first is the value and second is the decimal places

F strings
let say you want to print more than two data types in a print function
score=40
height=50.36
boll=True
print(f"your score is {score} and your height is {50.46}")

if elif and else
x=int(input("enter a number"))
y=int(input("enter a number"))
z=int(input("enter a number"))
if x>y:
    if x>z:
        print("x is greater",str(x))
    else:
        print("z is greater",str(z))
elif y>z:
    print("y is greater",str(y))
else:
    print("z is greater",str(z)) 

size=input("enter the size of pizza")
ap=input("want pp")
ec=input("che?")
bill=0
if size=="s" or "S":
     bill=10
elif size=="M" or "m":
    bill=15
elif size=="l" or "L":
    bill=20
else:
    print("enter valid size")
if ap == "Y":
    if size=="s" or "S":
        bill+=3
    else:
        bill+=10

if ec=="Y":
    bill+=10
print(f"{size}: {bill}")  

writing multiple lines in python
print('''
skjkvnsnvsv
sfvnsognsongvgs
gsfgdsg
sdfds
fds
fds
fdsgdsgsfg 

''')
x=input("enet").lower()
print(x)

FIZZBUZZ GAME FAQ IN INTERVIEWS
num=int(input("enter the number range to pplay"))
for i in range(0,num+1):
    if(i%3==0 and i%5==0):
        print("fizzbuzz\n")
    elif i%5==0:
        print("buzz\n")
    if(i%3==0):
        print("fizz\n")
    else:
        print(i)            

PASSWORD GENERATOR
EASY 
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nrc= int(input("How many letters would you like in your password?\n")) 
nrs = int(input(f"How many symbols would you like?\n"))
nrn = int(input(f"How many numbers would you like?\n"))

password=""
for i in range(1,nrc+1):
    password+=random.choice(letters)
for i in range(1,nrs+1):
    password+=random.choice(symbols)
    
for i in range(1,nrn+1):
    password+=random.choice(numbers)

print(password)

HARD
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nrc= int(input("How many letters would you like in your password?\n")) 
nrs = int(input(f"How many symbols would you like?\n"))
nrn = int(input(f"How many numbers would you like?\n"))

password=""
passli=[]
for i in range(1,nrc+1):
    #passli.append(random.choice(letters))
    passli+=random.choice(letters)

for i in range(1,nrs+1):
    #passli.append(random.choice(symbols))
    passli+=random.choice(symbols)
    
for i in range(1,nrn+1):
    #passli.append(random.choice(numbers))
    passli+=random.choice(numbers)

print(passli)
random.shuffle(passli)

password=""
for i in passli:
    password+=i
print(password)    


to identify a function any method with parenthesis is actually a function
print() len() sum() int()
 REEBORG's while loop hurdle
 def turnright():
    turn_left()
    turn_left()
    turn_left()
wall_in_front()
def jump():
    
    turn_left()
    move()
    turnright()
    move()
    turnright()
    move()
    turn_left()
while not at_goal():
    if(wall_in_front()):
        jump()
    elif front_is_clear():
       move()

HARDEEST ONE
def turnright():
    turn_left()
    turn_left()
    turn_left()
wall_in_front()
def up():    
    while not right_is_clear():
        move()
    turnright()
    move()
def down():
    while front_is_clear():
        move()           
while not at_goal():
    if(wall_in_front()):
        turn_left()
        up()
        turnright()
        down()
        turn_left()
    elif front_is_clear():
       move()

WORD GUESSING GAME
import random
lists=["basketball","football","cricket","baseball","badmiton"]
word=random.choice(lists)
print(word)
wordtbg=[]
l=len(word)
for i in range(l):
    wordtbg.append("_")
print(wordtbg)    
while "_" in wordtbg:

    guess=input("enter a letter")
    for pos in range(l):
        letter=word[pos]
        if letter == guess:
            wordtbg[pos]=letter
    print(wordtbg)   

Note
there are two ways which are important for importing the files which arenpresent in the same directory.
let's say for both the methods , the file is in the same directory, and the file to be imported is called "satish.py" and it has 
a list of marks called marks
1)import <filename>
print(filename.listname)

import satish
print(satish.marks)

2) from filename import listname
print(listname)

from satish import marks
print(makrs)
=> what if i want to import another list from same file say course

from satish import marks,course
print(marks)
print(source)

*> from replit import clear
clear() is a fucntion which will prevent you from scrolling like if the output is kept displaying we can just use clear() function 
to just clear the previous output

FUNCTIONS
arguments are the actual value you sending to the function whereas the parameter 
is defined to the fucntion and we can say that it is used inside the function to be defined

def greet(name,location):
    print(f"hello {name}")
    print(f"you are in {location}")
greet(location="india",name="satish")

we can actually change the position of the arguments by providing similar to key value pair

check prime number
def primeno(n):
    no = True
    for i in range(2,n):
        if n%i==0:
            no = False
            break
    if(no):
        print("prime")
    else:
        print(" not prime")        
primeno(11)  

CEASER CIPHER PROJECT


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd',
     'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
basically what this direction is doing is encrpytion and decryption
in encryption part the letters are moved left by the number of shift numbers
in decryption the alphabets are moved right by the number of shift numbers
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
#choice = input("enter encode or decode")


            


def encrypt(etext,eshift):
    cipher=""
    for l in etext:
        if " " in etext:
            pass
        pos=alphabet.index(l)
        newpos= pos+eshift
        newl=alphabet[newpos]
        cipher+=newl
    return cipher
    #decrypt(cipher,eshift)
    
def decrypt(etext,eshift):
    decr=""
    for l in etext:
        if " " in etext:
            pass
        pos=alphabet.index(l)
        newpos= pos-eshift
        newl=alphabet[newpos]
        decr+=newl
    return decr   
ct=encrypt(text,shift)
#print(f"the encrypted word is {ct}")
dt = decrypt(ct,shift)   
#print(f"the decrypted word is {dt}")

combining the two above functions in one
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
choice = input("enter encode or decode")
shift=shift%26
def ceaser(text,shift,ch):
    end = ""
    if ch == "d":
            shift*=-1
    for l in text:
        pos=alphabet.index(l)
        
        newpos=pos+shift
        end += alphabet[newpos]
    print(end)       

ceaser(text,shift,choice)  

ideal one is below
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
choice = input("enter encode or decode")
shift=shift%26


def ceaser(text,shift,ch):
    end = ""
    if ch == "d":
            shift*=-1
    for l in text:
        if l in alphabet:

            pos=alphabet.index(l)
            
            newpos=pos+shift
            end += alphabet[newpos]
        else:
            end+=l    
    print(end)       

ceaser(text,shift,choice)            

DICTIONARIES
student_scores={"x":81,"y":78,"z":99,"a":74,"b":62}
sd={}
for i in student_scores:
    score=student_scores[i]
    if score>91:
        sd[i]="excellent"
    elif score>80 and score< 91:
        sd[i]="good"
    elif score>70 and score<81:
        sd[i]="average"
    else:
        sd[i]="can do better"

print(sd) 

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    print(bids)
    bidding_finished = True
    find_highest_bidder(bids)

functions with output
using return keyword

capitilaizing the first letter of the word using title keyword
def namefl(f,l):
   fname=f.title()
   lname=l.title()
   print(f"{fname} {lname}")
namefl("satish","kumar")

def namefl(f,l):
   fname=f.title()
   lname=l.title()
   return f"{fname} {lname}"

x=namefl("satish","kumar")
print(x)

if you are using return keyword then make sure you assign the fucntion call to a variable and then print it , technically good practice
return also specifies the end of the fucntion
if we try to print or execute something after return statement , it won't execute anything after return statement

def add(z,y):
    c=z+y
    return c
   
    print("this statement will no be printed")


def namefl(f,l):
   fname=f.title()
   lname=l.title()
   return f"{fname} {lname}"

x=namefl(input("wat is your name"),input("whta is your last name"))
print(x)

def namefl(f,l): returns none if the f and l are empty

    if f=="" or l=="":
        return 
    fname=f.title()
    lname=l.title()
    return f"{fname} {lname}"

x=namefl(input("wat is your name"),input("whta is your last name"))
print(x)

to check whether a year is a leap year or not
def leap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print("leap")
            else:
                print("not a leap")
        else:
            print("leap")
    else:
        print("not a leap")        

DOCSTRINGS: they are used for giving documentation for a user defined function, for example to tells users what this 
user defined function do , this is done by docstrings
once the fucntion is created then immediately the next line the documnetation is supposed to be given

def add(x,y):
[""" # this fuction is used to add two numbers ,"as soon as this fucntion is called as once it is hovered it 
#displays the content which we wrote on between couple of triple quotes"



"""]

calci program through dictionary
def add(a,b):
    return a+b
def sub(a,b):
    return a-b

oper={
    "+":add,
    "-":sub
}

sym=input("symbol")
calcfun=oper[sym]

ans=calcfun(5,6)
print(ans)


ways to create a numbe of lists based on user input
num = int(input('How Many?: '))
all = {'list'+str(i+1):[] for i in range(num)}
print(all)
print(all['list1']

num_lists = int(input('How many lists?'))
lists = [[] for i in range(num_lists)]
print(lists)

my try
import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
deal=[]
num = int(input('How Many?: '))
all = {'player'+str(i+1):[] for i in range(num)}
print(all)

for i in all:
    all[i].append(random.sample(cards,2))

for i in all:
    print(f"{i}=>{all[i]}")

wanttoenter=input("want any player to add one more card")
if wanttoenter == "yes":
        
    while wanttoenter == "yes" :
        choice=input("enter the player number if you eant to add one more card")
        for i in all:
            if i=="choice":
                all[choice].append(random.choice(cards))
            else:
                break
        wanttoenter = False        

for i in all:
    print(f"{i}=>{all[i],}")   

blackjack actual code


import math
import random
def dealcardS():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
def playgame():

            
    user_cards=[]
    pccard=[]
    gameover=False
    for i in range(2):
        user_cards.append(dealcardS())
        pccard.append(dealcardS())
        
        
    def score(cards):
        return sum(cards)
    def compare(user_score,pc_score):
        if user_score == pc_score:
            return "draw"
        elif pc_score>21 and user_score>21:
            return "draw"    
        elif pc_score>21:
            return "you won"
        elif pc_score==0:
            return "you lose"
        elif user_score == 0:
            return "you won"
        elif user_score>21:
            return "you lose"
        elif pc_score >user_score:
            return "you lost"   
        else:
            return "you won"            


    print(f"{user_cards}")

    print(f"{pccard[0]} is the first card")
    while not gameover:

        user_score=score(user_cards)
        pc_score=score(pccard)

        if user_score == 0 or pc_score==0 or user_score>21:
            gameover=True
        else:
            user_should_deal=input("yes or no")
            if user_should_deal == "yes":
                user_cards.append(dealcardS())
            else:
                gameover=True
        print(f"{user_cards}")
        
        print(f"{pccard[0]} is the first card")
    user_score=score(user_cards)
    pc_score=score(pccard)


    while pc_score !=0 and pc_score<17:
        pccard.append(dealcardS())
        pc_score=score(pccard)


        
    print(compare(user_score,pc_score))
    print(f"{user_cards}")
    print(f"{pccard}")    
    user_cards=[]
    pccard=[]
    gameover=False
    for i in range(2):
        user_cards.append(dealcardS())
        pccard.append(dealcardS())
            
            
        def score(cards):
            return sum(cards)
        def compare(user_score,pc_score):
            if user_score == pc_score:
                return "draw"
            elif pc_score>21 and user_score>21:
                return "draw"    
            elif pc_score>21:
                return "you won"
            elif pc_score==0:
                return "you lose"
            elif user_score == 0:
                return "you won"
            elif user_score>21:
                return "you lose"
            elif pc_score >user_score:
                return "you lost"   
            else:
                return "you won"            


        print(f"{user_cards}")

        print(f"{pccard[0]} is the first card")
    while not gameover:

        user_score=score(user_cards)
        pc_score=score(pccard)

        if user_score == 0 or pc_score==0 or user_score>21:
            gameover=True
        else:

            user_should_deal=input("yes or no")
            if user_should_deal == "yes":
                user_cards.append(dealcardS())
            else:
                gameover=True
        print(f"{user_cards}")
            
        print(f"{pccard[0]} is the first card")
    user_score=score(user_cards)
    pc_score=score(pccard)


    while pc_score !=0 and pc_score<17:
        pccard.append(dealcardS())
        pc_score=score(pccard)


            
    print(compare(user_score,pc_score))
    print(f"{user_cards}")

while input("wanna play one more [yes/no]")=="yes":
    playgame()
"""


import math
import random
def dealcardS():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
def playgame():

            
    user_cards=[]
    pccard=[]
    gameover=False
    for i in range(2):
        user_cards.append(dealcardS())
        pccard.append(dealcardS())
        
        
    def score(cards):
        return sum(cards)
    def compare(user_score,pc_score):
        if user_score == pc_score:
            return "draw"
        elif pc_score>21 and user_score>21:
            return "draw"    
        elif pc_score>21:
            return "you won"
        elif pc_score==0:
            return "you lose"
        elif user_score == 0:
            return "you won"
        elif user_score>21:
            return "you lose"
        elif pc_score >user_score:
            return "you lost"   
        else:
            return "you won"            


    print(f"{user_cards}")

    print(f"{pccard[0]} is the first card")
    while not gameover:

        user_score=score(user_cards)
        pc_score=score(pccard)

        if user_score == 0 or pc_score==0 or user_score>21:
            gameover=True
        else:
            user_should_deal=input("yes or no")
            if user_should_deal == "yes":
                user_cards.append(dealcardS())
            else:
                gameover=True
        print(f"{user_cards}")
        
        print(f"{pccard[0]} is the first card")
    user_score=score(user_cards)
    pc_score=score(pccard)


    while pc_score !=0 and pc_score<17:
        pccard.append(dealcardS())
        pc_score=score(pccard)


        
    print(compare(user_score,pc_score))
    print(f"{user_cards}")
    print(f"{pccard}")    
    user_cards=[]
    pccard=[]
    gameover=False
    for i in range(2):
        user_cards.append(dealcardS())
        pccard.append(dealcardS())
            
            
        def score(cards):
            return sum(cards)
        def compare(user_score,pc_score):
            if user_score == pc_score:
                return "draw"
            elif pc_score>21 and user_score>21:
                return "draw"    
            elif pc_score>21:
                return "you won"
            elif pc_score==0:
                return "you lose"
            elif user_score == 0:
                return "you won"
            elif user_score>21:
                return "you lose"
            elif pc_score >user_score:
                return "you lost"   
            else:
                return "you won"            


        print(f"{user_cards}")

        print(f"{pccard[0]} is the first card")
    while not gameover:

        user_score=score(user_cards)
        pc_score=score(pccard)

        if user_score == 0 or pc_score==0 or user_score>21:
            gameover=True
        else:

            user_should_deal=input("yes or no")
            if user_should_deal == "yes":
                user_cards.append(dealcardS())
            else:
                gameover=True
        print(f"{user_cards}")
            
        print(f"{pccard[0]} is the first card")
    user_score=score(user_cards)
    pc_score=score(pccard)


    while pc_score !=0 and pc_score<17:
        pccard.append(dealcardS())
        pc_score=score(pccard)


            
    print(compare(user_score,pc_score))
    print(f"{user_cards}")

while input("wanna play one more [yes/no]")=="yes":
    playgame()















                

    






