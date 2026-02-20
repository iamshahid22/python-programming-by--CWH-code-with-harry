#spam detection code
c1="Makes a lot of money"
c2="buy now"
c3="subscribe this"
c4="click this"

msg=input("enter your cmnt:")

if((c1 in msg) or (c2 in msg) or (c3 in msg)):
    print("this cmnt is a spam")

else:
    print("this cmnt is not a spam")