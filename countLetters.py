string = input("please put your life motto here")
characterCount = 0
wordCount = 0
for i in string:
    characterCount = characterCount + 1
    if(i == " "):
        wordCount = wordCount+1
print(wordCount)
print(characterCount)