def add(a,b):
    x = a+b
    print(x)
def sub(a,b):
    x = a-b
    print(x)
def mul(a,b):
    x = a*b
    print(x)
def div(a,b):
    x = a/b
    print(x)
    
while(1):
    c=input("Enter a choice \n1.Add\n2.Sub\n3.Mul\n4.Div\n5.Exit\nchoice=")
    if c == "5":
        break
    a = float(input("Enter the 1st no."))
    b = float(input("Enter the 2nd no."))        
    match c:
        case "1":
            add(a,b)
        case "2":
             sub(a,b)
        case "3":
            mul(a,b)
        case "4":
            div(a,b)
       
    
    