# Write code for algorithm 1 below
def positive(num):
    if num == 0:
        return "done"
    else:
        return positive( num - 1)    

print(positive(4))