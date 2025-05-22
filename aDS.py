# defining a function


def wellwishes():
    print("hello")
    print("how are you")

# calling functions
wellwishes()


def weathercodition():
    print("weather is pleasent in", spring)
    print("weather is same in", autimm)
    
spring="spring season"
autimm="autumn"
    
weathercodition()


def add(p,q):
    return p+q
def subtract(p,q):
    return p-q
def mul(p,q):
    return p *q
def divide(p,q):
    return p/q



print("please enter your choice")
print("a. add")
print("b. subtract")
print("c. mul")
print("d . divide")


choice = input("please enter your choice a, b , c , d")

n1 = int(input("please enter the first number"))
n2 = int(input("please enter the second number"))



if choice == "a":
    print(n1, "+", n2 ,"=" , add(n1, n2))
elif choice == "b":
    print(n1, "-", n2 ,"=" , subtract(n1, n2))
elif choice == "c":
    print(n1, "*" ,n2 ,"=" , mul(n1, n2))
elif choice == "d":
    print(n1, "/", n2 ,"=" , divide(n1, n2))
else: 
    print("invalid input")
    



    
    
    
    

    