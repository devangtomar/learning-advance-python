import re

Sentence = "he is a good programmer, he won 865 competitions, but sometimes he dont. What do you think? ?d All test-cases should pass. Done-done?"
#Sentence = "he is a goof"
words = re.findall('\w+', Sentence)

for word in words:
    if  re.match('^[a-zA-Z]', word,  re.IGNORECASE) and not re.match('^\?\S+', str(word)):
        print(str(word))

    # else:
    #   print(str(word)