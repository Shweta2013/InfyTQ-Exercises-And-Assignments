#DSA-Assgn-17

def find_matches(country_name):
    list_of_matches=[]
    for match in match_list:
        detail=match.split(":")
        if detail[0] == country_name:
            list_of_matches.append(match)      
    return list_of_matches
    

def max_wins():
    dictionary={}
    for match in match_list:
        detail = match.split(":")
        if detail[1] not in dictionary.keys():
            dictionary[detail[1]]=None
        if dictionary[detail[1]]==None:
            dictionary[detail[1]]=int(detail[3])
        elif dictionary[detail[1]]>=0:
            if dictionary[detail[1]]<int(detail[3]):
                dictionary[detail[1]]=int(detail[3])
    temp=dictionary.copy()
    for key, values in dictionary.items():
        dictionary[key]=[]
    for match in match_list:
        detail = match.split(":")
        if int(detail[3])==temp[detail[1]]:
            dictionary[detail[1]].append(detail[0])
    return dictionary

def find_winner(country1,country2):
    count1,count2=0,0
    for match in match_list:
        detail = match.split(":")
        if detail[0] == country1:
            count1+=int(detail[3])
        if detail[0] == country2:
            count2+=int(detail[3])
    if count1==count2:
        return "Tie"
    elif count1>count2:
        return country1
    else:
        return country2

#Consider match_list to be a global variable
match_list=["AUS:CHAM:5:2","AUS:WOR:2:1","ENG:WOR:2:0","IND:T20:5:3","IND:WOR:2:1","PAK:WOR:2:0","PAK:T20:5:1","SA:WOR:2:0","SA:CHAM:5:1","SA:T20:5:0"]
country=[]
champioship=[]
matches_played=[]
wins=[]
for element in match_list:
    temp=element.split(":")
    country.append(temp[0])
    champioship.append(temp[1])
    matches_played.append(temp[2])
    wins.append(temp[3])
# print(country)
# print()
# print(champioship)
# print()
# print(matches_played)
# print()
# print(wins)
# print()
#Pass different values to each function and test your program
print("The match status list details are:")
print(match_list)
result=find_matches("AUS")
print(result)
print()