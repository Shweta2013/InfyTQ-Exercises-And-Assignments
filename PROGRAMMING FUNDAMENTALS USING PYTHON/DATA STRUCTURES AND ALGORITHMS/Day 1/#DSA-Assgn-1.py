#DSA-Assgn-1

def merge_list(list1, list2):
    merged_data=""
    resultant_data = ""
    i, j = 0, len(list2) - 1 
    while( i < len(list1) and j >= 0 ):
        if list1[i] == None:
            merged_data = list2[j] + " "
        elif list2[j] == None:
            merged_data = list1[i] + " "
        else:
            merged_data = str(list1[i]) + str(list2[j]) + " "
        resultant_data += merged_data
        i += 1 
        j -= 1 
        
    return resultant_data

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)