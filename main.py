# number=int(input("Enter the pallendron digits: "))
# ognumber=number
# rvnumber=0
# while number >0:
#     digit=number%10
#     rvnumber=rvnumber*10+digit
#     number//=10

# if ognumber==rvnumber:
#     print("This number is pallendron digit",ognumber)

# else:
#     print("This number is'nt a pallendron digit. Please enter a different number",ognumber)

#act-2

# numberlargest=int(input("Enter the largest digits: "))
# numbersmallest=int(input("Enter the smallest digits: "))
# while numbersmallest:
#     numberstore=numbersmallest
#     numbersmallest=numberlargest%numbersmallest
#     numberlargest=numberstore

# print("HCF is",numberlargest)

def simpint(p,r,t):
    print("principal",p,"time",t,"rate of int",r)
    si=(p*r*t)/100
    print(si)
    return si
simpint(10000,7,2)
