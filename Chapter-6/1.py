a=int(input("Enter your age:"))

if(a>=18):
    print("you are a major")
    print("you are eligible to vote")

elif(a<0):
    print("you are entering invalid age")

elif(a==0):
    print("you are just born")

else:
    print("you are a minor")
    print("you are not eligible to vote")

print("End")