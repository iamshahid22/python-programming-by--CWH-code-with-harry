m1=int(input("Enter m1:"))
m2=int(input("Enter m2:"))
m3=int(input("Enter m3:"))
m4=int(input("Enter m4:"))
m5=int(input("Enter m5:"))
m6=int(input("Enter m6:"))
m7=int(input("Enter m7:"))
m8=int(input("Enter m8:"))

tp=(100*(m1+m2+m3+m4+m5+m6+m7+m8))/800

if(tp>=40 and m1>=40 and m2>=40 and m3>=40 and m4>=40 and m5>=40 and m6>=40 and m7>=40 and m8>=40):
    print("you are passed!:", tp)

else:
    print("you are fail!:", tp)