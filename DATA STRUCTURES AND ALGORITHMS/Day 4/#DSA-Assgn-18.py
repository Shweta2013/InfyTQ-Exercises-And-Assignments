#DSA-Assgn-18

def find_unknown_words(text,vocabulary):
    unknown=[]
    split_text=text.split()
    for word in split_text:
        if word.lower() not in vocabulary:
            unknown.append(word)
        else:
            continue
    if len(unknown)==0:
        return -1
    return set(unknown)
            

#Pass different values of text and vocabulary to the function and test your program
text="The sun rises in the east"
vocabulary = ["sun","in","rises","the","east"]
unknown_words=find_unknown_words(text,vocabulary)
print("The unknown words in the file are:",unknown_words)