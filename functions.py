import math
# add function 
def add(n):
    i = 0
    sum = 0
    while(i<n):
        
        sum+=int(input(f"Enter the {i+1} no number : "))
        i+=1
    return sum   


# substruction function 
def substraction(a,b):
    return a-b


#find multiplication 
def multiplication(n):
    i = 0
    multi = 1
    while(i<n):
        int(input(f"Enter the {i+1} no number : "))
        multi*=multi
        i+=1
    return multi 


#find division
def division(a,b):
    return a/b



#find modulus
def modulus(a,b):
    return a%b



#check the no is even or odd
def check(n):
    if(n%2==0):
        print(f"{n} is even number .")
    else:
        print("{n} is odd number : ")    


# check the no is positive or negetive 
def check_positive(n):
    if(n<0):
        print(f"{n} is negetive number .")
    else:
        print(f"{n} is positive number : ")    


# find factorial 
def find_factorial(n):
    if(n==0):
        return 1
    return n*find_factorial(n-1)




# find fibonachi sequence upto n number

def fibonacci_sequence(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    seq = fibonacci_sequence(n - 1)   
    seq.append(seq[-1] + seq[-2])   
    return seq



# find nth fibonachi number 

def fibonacci_at_nth(n):
    if n <= 1:
        return n
    return fibonacci_at_nth(n-1) + fibonacci_at_nth(n-2)


#find sine
def sin_angle(angle):
    return math.sin(math.radians(angle))


#find cos
def cos_angle(angle):
    return math.cos(math.radians(angle))

#find tan
def tan_angle(angle):
    return math.tan(math.radians(angle))


#find log
def compute_log(value):
    return math.log(value) 

#radian to degree
def rad_to_deg(radian):
    return math.degrees(radian)
#degree to radian 
def deg_to_rad(degree):
    return math.radians(degree)
