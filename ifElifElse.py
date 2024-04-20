age = int(input("Enter Your age"))
if(age<1):
    print("Baby")
elif(age>=1 and age<=3):
    print("Toddler")
elif(age>3 and age<=5):
    print("Pre-School")
elif(age>5 and age<=12):
    print("Grade schooler")
elif(age>12 and age<=18):
    print("Teenager");
else:
    print("Adult")