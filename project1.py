R=int(input("Type 1 for basic details: \n Type 2 for voting eligibility:"))

print(R)
if R==1:
  print("Basic Details")
  Name=str(input("Name: "))
  USN=input("USN: ")
  Dept=str(input("Dept: "))
  Year_OF_Admission=int(input("Year of Admission: "))
  Year_Of_Graduation=int(input("Year of Graduation: "))
  college =str(input("college:"))  
  print(USN)
  print(Dept)
  print(Year_OF_Admission)
  print(Year_Of_Graduation)
  print(college)

elif R==2:
 print("Voting machine ")
 age=int(input("Enter your age:"))
 if age <18:
  print("your not eligible for vote")
 elif age >18:
  print("you are eligible for vote")
else:
 print("You choosed wrong number")
 


