print "Welcome to the English to Pig Latin translator!"
original = raw_input('Enter an English word now.')
if len(original) >= 1 and original.isalpha():
    print original
else:
    print "Empty or Remove numbers"
