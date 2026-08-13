n=5
for i in range(1,n+1):
    print(" " * (n-i) + "* " * i)

#right triangle
for i in range(1,5):
    print("* " * i)

#inverted triangle
for i in range(5,0,-1):
    print("* " * i)    

#inverted pyramid
n=5 
for i in range(n,0,-1):
    print(" " * (n-i) + "* " * i)   

#same number triangle
for i in range(1,6):
    print((str(i) + " ") * i)

#number triangle
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")    
    print()    

#alphabet triangle
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end=" ")    
    print()    

#diamond
n=5
for i in range(1,n+1):
    print(" " * (n-i) + "* " * i)

#inverted diamond
n=5    
for i in range(n-1,0,-1):
    print(" " * (n-i) + "* " * i)
