def even_numbers():
    x = range(10)
    for i in x:
        if i%2==0:
            print(i)

def odd_numbers():
    x = range(20) 
    for i in x:  
        if i%2!=0:
            print(i) 
def divisible_by_5():
    x = range(50)
    for i in x:
        if i%5==0:
            print(f"{i} is divisible by 5")            
    else:
        print(f"{i} is not divisible by 5")  

def multiple_comparison():
    x = range(50)
    for i in x:
        if i%5==0:
            print(f"{i} is divisible by 5") 
        elif i%7==0:
            print(f"{i} is divisible by 7") 
        elif i%9==0:
            print(f"{i} is divisible by 9")   
        else:
            print(f"{i}is not divisible by 5,7or9") 

def odd_even():
    x = range(20)
    for i in x:
        if i%2==0 and i%3==0:
            print(f"{i} is divisible by both 2 and 3")
        elif i%2==0 or i%3==0:
            print(f"{i} is divisible by either 2 or 3")        
        else:
            print(f"{i} is not divisible by either 2 or 3") 

def while_loop():
    x=1
    while x<10:
        print("Hello")  
        x+=1  

def break_statement():
    x=1
    while x<10:
        print("Hello") 
        x+=1
        if x==5:
            break  

def continue_statement():
    x=1
    while x<=20:
        x+=1
        if x %3==0:
            continue
        print(x) 

    #   Assignment     
#Write a function that uses while, if and continue statements to print all the even numbers between 0 and 50.
def  even_num():
    x=0
    while x<=50:
        x+=1
        if x%2!=0:
            continue
        print(x)

#Write a function that takes an integer argument and prints "Prime" if the number 
# is prime, and "Not prime" if the number is not prime. 
def prime_num(b):
    if b<=1:
        print("is a prime number")
    elif b>1:
        for i in range (2,b):
            if b%i==0:
                print("not prime")
                break 
            else:
                print("prime")    

   

# Write a function that takes a list of integers as input and prints the sum of all 
# the even numbers in the list.    
        
def sum_odd():
    sum=0
    for i in range(15):
        if i%2==0:
            sum=sum+i
            print("sum=",sum)


#Write a function that takes any two integers as input, and prints the sum of all 
# the numbers between the two integers (inclusive) that are divisible by 3. 

def int_nums():
    n,m=3,10
    for i in range(1,m+1):
        sum1=0
        sum2=0
    if i %n==0:
        sum1+=i
    else:
        sum2+=i
        print(f"{sum1} {sum2}")        





