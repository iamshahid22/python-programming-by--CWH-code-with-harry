a = int(input("Enter a number :"))
b = int(input("Enter b number :"))
c = int(input("Enter c number :"))
d = int(input("Enter d number :"))

def greatest(a,b,c,d):
    if(a>b and a>c and a>d):
        return a
    elif(b>a and b>c and b>d):
        return b
    elif(c>a and c>b and c>d):
        return c
    elif(d>a and d>b and d>c):
        return d
    
print("Greatest Number is a : ", greatest(a,b,c,d))
print("Greatest Number is b : ", greatest(a,b,c,d))
print("Greatest Number is c : ", greatest(a,b,c,d))
print("Greatest Number is d : ", greatest(a,b,c,d))
