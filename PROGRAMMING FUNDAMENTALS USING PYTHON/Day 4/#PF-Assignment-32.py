#PF-Assgn-32

def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    list1={}
    p,e,o=0,0,0
    for i in range(1,len(patient_medical_speciality_list),2):
        if (patient_medical_speciality_list[i]=="P"):
            p+=1
        elif(patient_medical_speciality_list[i]=="O"):
            o+=1
        elif(patient_medical_speciality_list[i]=="E"):   
            e+=1
    list1["P"]=p
    list1["O"]=o
    list1["E"]=e
    m=max(list1.values())
    for key in list1:
        if list1[key]==m:
            k1=key
    
    speciality=medical_speciality[k1]
    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)