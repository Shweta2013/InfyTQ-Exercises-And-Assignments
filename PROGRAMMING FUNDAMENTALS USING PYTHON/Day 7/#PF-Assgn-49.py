#PF-Tryout
#Start writing your code here

#ASSUME HEADS=1 AND TAILS=2
import random
no_of_heads=0
no_of_tails=0

dictionary={"HEADs":0,"TAILs":0}
for number in range(1,101):
    i=random.randrange(1,100)
    if (i<=70):
        no_of_heads+=1
        dictionary["HEADs"]=no_of_heads
    else:
        no_of_tails+=1
        dictionary["TAILs"]=no_of_tails
        
print(dictionary)