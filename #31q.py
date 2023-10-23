#31q

num_rows = 5


max_digits = len(str(num_rows))


for i in range(1, num_rows + 1):
    
    for j in range(1, i + 1):
        
        print(f"{j:0{max_digits}}", end=" ")
    
    print()
