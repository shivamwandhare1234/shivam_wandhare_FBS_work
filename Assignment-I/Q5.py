Principle=int(input("Enter Principle: "))
Rate=float(input("Enter Rate: "))
Time=int(input("Enter Time: "))

Amount_After_Time= Principle*(1+Rate/100)**Time

#Calculate Compound Intrest

Compound_Intrest= Amount_After_Time-Principle

print("The Compound Intrest is: ",Compound_Intrest)

