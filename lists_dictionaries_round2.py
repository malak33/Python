###part 1/13
names = ["Adam","Alex","Mariah","Martine","Columbus"]   
for x in names:
    print x

####part 2/13

webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

# Add your code below!
for key in webster:
    print webster[key]

###part 3/13

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for x in a:
    if x % 2 == 0:
        print x



####part 4/13

# Write your function below!
x ="fizz", "buzz", "fizz", "tiger", "lama", "bear"

def fizz_count(x):
    count = 0
    for i in x:
        if i == "fizz":
            count +=1
    return count

 ##part 5/13

for letter in "Codecademy":
    print letter
    
# Empty lines to make the output pretty
print
print

word = "Programming is fun!"

for letter in word:
    # Only print out the letter i
    if letter == "i":
        print letter

###part 6/13

prices = {"banana" : 4,
"apple" : 2,
"orange" : 1.5,
"pear" : 3,}


####part 7/13

prices = {"banana" : 4,
"apple" : 2,
"orange" : 1.5,
"pear" : 3,}

stock = {"banana" : 6,
"apple" : 0,
"orange" : 32,
"pear" : 15,}

####part 8/13

prices = {"banana" : 4,
"apple" : 2,
"orange" : 1.5,
"pear" : 3,}

stock = {"banana" : 6,
"apple" : 0,
"orange" : 32,
"pear" : 15,}

for x in prices:
    print str(x)
    print "price: " + str(prices[x])
    print "stock: " + str(stock[x])

####part 9/13

xs = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
    
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

total=0
for x in prices and stock:
    add = prices[x] * stock[x]
    total = total + add
print total

######part 10/13



###part 11/13



####part 12/13



###part 13/13
