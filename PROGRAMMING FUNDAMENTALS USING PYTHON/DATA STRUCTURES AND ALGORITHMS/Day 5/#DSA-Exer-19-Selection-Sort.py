#DSA-Exer-19

def swap(num_list, first_index, second_index):
    temp=num_list[first_index]
    num_list[first_index]=num_list[second_index]
    num_list[second_index]=temp
    return num_list

def find_next_min(num_list,start_index):
    minimum=num_list[start_index]
    for i in range(start_index+1,len(num_list)):
        if num_list[i]<minimum:
            minimum=num_list[i]
    return num_list.index(minimum)  

def selection_sort(num_list):
    i=0
    while(i<len(num_list)-1):
        data=find_next_min(num_list,i)
        swap(num_list,i,data)
        i+=1
        
#Pass different values to the function and test your program
num_list=[8,2,19,34,23, 67, 91]
print("Before sorting;",num_list)
selection_sort(num_list)
print("After sorting:",num_list)