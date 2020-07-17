#PF-Assgn-47

def encrypt_sentence(sentence):
    splitted_sentence=sentence.split()
    new=""
    print(splitted_sentence)
    
    for word in splitted_sentence:
        index=splitted_sentence.index(word)
        if(index%2==0 ):
            splitted_sentence[index]=word[::-1]
        else:
            list_of_vowels=""
            consonents=""
            word1=""
            for letter in word :
                if (letter in "aeiou" or letter in "AEIOU"):
                    list_of_vowels+=letter
                else:
                    consonents+=letter
            word1+=consonents+list_of_vowels
            splitted_sentence[index]=word1

    new=str(" ".join(splitted_sentence))
    return new
            
sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)