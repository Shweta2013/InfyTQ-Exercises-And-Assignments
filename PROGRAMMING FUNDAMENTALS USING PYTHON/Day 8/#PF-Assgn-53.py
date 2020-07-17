#PF-Assgn-53

#This verification is based on string match.

import re
poem='''
If I can stop one heart from breaking,
I shall not live in vain;
If I can ease one life the aching,
Or cool one pain,
Or help one fainting robin
Unto his nest again,
I shall not live in vain.
'''

#Note: Triple quotes can be used to enclose Strings which has lines of text.

print(len(re.findall(r"v",poem)))

print()
print(re.sub(r"\s+"," ",poem))

print()
poem=re.sub(r"co","Co",poem)
poem=re.sub(r"ch","Ch",poem)
print(poem)

print()
if(re.search(r"ai|hi",poem)!=None):
    result=re.sub(r"{ai}...|{hi}...","*/*",poem)
print(poem)