#multiple if stmts code
age=int(input("Enter age:"))

if(age==0):
    print("you are a Baby")

elif(age>=18):
    print("you are a major")
 
elif(age<18):
    print("you are a minor")

elif(age<0):
    print("invalid age")

else:
    print("end")

if(age>=60):
    print("you are an oldman or old-women")  

elif(age<60):
    print("you are not oldman or old-women")
  
else:
    print("end")