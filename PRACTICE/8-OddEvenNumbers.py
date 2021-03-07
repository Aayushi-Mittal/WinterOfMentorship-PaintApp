start=int(input("Enter the starting point: "))
end=int(input("Enter the ending point: "))
for i in range(start, end+1):
    if(i%2==0):
        print(f"{i} is even")
    else:
        print(f"{i} is odd")