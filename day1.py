n= 5
for i in range(1,5):
    print(f"i+1 ={1} outer loop")
    for j in range(1,i-1):
        print(f"i={i} inner loop")
    print()
