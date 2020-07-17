#PF-Assgn-26

def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0

    #Start writing your code here
    #Populate the variables: chicken_count and rabbit_count
    if legs%2!=0 or heads>legs:
        print(error_msg)
    else:
        rabbit_count=(legs-(heads*2))/2
        chicken_count=heads-rabbit_count
        print(int(chicken_count),int(rabbit_count))

#Provide different values for heads and legs and test your program
solve(35,94)