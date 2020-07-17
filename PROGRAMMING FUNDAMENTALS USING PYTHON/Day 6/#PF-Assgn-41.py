#PF-Assgn-41

def find_ten_substring(num_str):
    sub_string=[]
    for i in range(len(num_str)):
        substring=""
        add=int(num_str[i])
        for j in range(i+1,len(num_str)):
            add+=int(num_str[j])
            if(add==10):
                substring=num_str[i:j+1]
                sub_string.append(substring)
            else:
                continue
    return sub_string   
                
         

num_str="2825302"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)
