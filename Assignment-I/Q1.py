Physics_Marks=int(input("Enter Physics Marks"))
Chemistry_Marks=int(input("Enter Chemistry Marks"))
Math_Marks=int(input("Enter Math Marks"))
Bio_Marks=int(input("Enter Bio Marks"))
English_Marks=int(input("Enter English Marks"))

#Calculate Percentage

Student_Percentage= float((Physics_Marks+Chemistry_Marks+Math_Marks+Bio_Marks+English_Marks)/500) * 100

print("The Percentage of student is: ",Student_Percentage)
