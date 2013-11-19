pyg = 'ay' #add ay to end off word

original = raw_input('Enter a word:') #ask for input

if len(original) > 0 and original.isalpha():#getlength and make sure it is alpha
    word = original.lower() #string word
    first = word[0] #string to find if first letter is vowel
    new_word = word + pyg #string to print if it is vowel
    
    
    if first in ['a' or 'e' or 'i' or 'o' or 'u']:#if word begins with vowel
        print new_word
    else: #if word doesn't begin with vowel define string new_word again'n print
        new_word = word[1:] + first + pyg
        print new_word 
else:
    print 'Empty word or Remove the Numbers' # if  it gets to this

