#print("Simple calculator")
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
operation=input("Enter operation(+,-,*,/):")
if operation=="+":
    print("Result:",num1+num2)
elif operation=="-":
    print("Result:",num1-num2)
elif operation=="*":
    print("Result:",num1*num2) 
elif operation=="/":
    print("Result:",num1/num2)
else:
    print("Invalid operation")           

#add loop
while True:
    num1=float(input("Enter first number:"))
    num2=float(input("Enter second number:"))
    operation=input("Enter operation(+,-,*,/):")
    if operation=="+":
       print("Result:",num1+num2)
    choice=input("continue yes/no:")
    if choice=="no":
       break

#square root
import math
num=float(input("Enter number:"))
print(math.sqrt(num))

#percentage calculator
value=float(input("Enter value:"))
total=float(input("enter total:"))
percentage=(value/total)*100
print("percentage:",percentage)

#GUI calculator
from tkinter import*
root=Tk()
root.title("calculator")
root.geometry("300x300")
label=Label(root,text="My Calculator")
label.pack()
root.mainloop()
