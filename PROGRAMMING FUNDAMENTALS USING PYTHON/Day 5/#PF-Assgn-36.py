#PF-Assgn-36

def create_largest_number(number_list):
    number_list.sort(reverse=True)
    print(number_list)

    s=[str(i) for i in number_list]
    result=int("".join(s))
    return result

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)