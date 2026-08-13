#using temp 
a=int(input())
b=int(input())
temp=a
a=b
b=temp
print(f"value of a is:{a}")
print(f"value of b is:{b}")

#without temp
a=int(input())
b=int(input())
b=b+a #30
a=b-a #20
b=b-a #10
print(f"value of a is:{a}")
print(f"value of b is:{b}")

#another method
a=int(input())
b=int(input())
a,b=b,a
print(f"value of a is:{a}")
print(f"value of b is:{b}")
