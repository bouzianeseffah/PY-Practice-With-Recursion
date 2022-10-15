# Write code for algorithm 2 below
def nutural_number(n, i = 1):
    if i  > n:
        return "done"
    else:
        print(i)  
        nutural_number(n, i + 1)  

nutural_number(3)