#DSA-Exer-21
def merge_sort(num_list):
    low=0
    high=len(num_list)-1
    if low==high:
        return num_list
    else:
        list1=merge_sort(num_list[:(high//2+1)])
        list2=merge_sort(num_list[(high//2+1):])
        new_list=merge(list1,list2)
        return new_list
        
def merge(left_list,right_list):
    i,j=0,0
    sorted_list=[]
    while(i<len(left_list) and j<len(right_list)):
        if left_list[i]<=right_list[j]:
            sorted_list.append(left_list[i])
            i+=1
        else:
            sorted_list.append(right_list[j])
            j+=1
    
    if len(left_list)!=0:
        for i in left_list:
            if i not in sorted_list:
                sorted_list.append(i)
    
    if len(right_list)!=0:
        for i in right_list:
            if i not in sorted_list:
                sorted_list.append(i)

    return sorted_list

num_list=[34, 67, 8, 19, 2, 23, 1, 91]
print("Before sorting:",num_list)
sorted_list = merge_sort(num_list)
print("After sorting:",sorted_list)