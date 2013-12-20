zoo_animals = ["pangolin", "cassowary", "sloth", "jaguar" ];
# One animal is missing!

if len(zoo_animals) > 3:
	print "The first animal at the zoo is the " + zoo_animals[0]
	print "The second animal at the zoo is the " + zoo_animals[1]
	print "The third animal at the zoo is the " + zoo_animals[2]
	print "The fourth animal at the zoo is the " + zoo_animals[3]

##part 2/13
numbers = [5, 6, 7, 8]

print "Adding the numbers at indices 0 and 2..."
print numbers[0] + numbers[2]
print "Adding the numbers at indices 1 and 3..."
# Your code here!
print "Adding the numbers at indices 2 and 4..."
print numbers[1] + numbers[3]


####part 3/13
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
# Last night our zoo's sloth brutally attacked 
#the poor tiger and ate it whole.

# The ferocious sloth has been replaced by a friendly hyena.
zoo_animals[2] = "hyena"

# What shall fill the void left by our dear departed tiger?
# Your code here!
zoo_animals[3] = "jaguar"

###part 4/13
suitcase = [] 
suitcase.append("sunglasses")
suitcase.append("bathing")
suitcase.append("books")
suitcase.append("liquor")
# Your code here!




list_length = len(suitcase)# Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase

###part 5/13
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

first =   my_slice1 = suitcase[0:2] # The first two items
middle =  my_slice2 = suitcase[2:4] # Third and fourth items
last =    my_slice3 = suitcase[4:6] # The last two items

####part 6/13
animals = "catdogfrog"
cat = animals[0:3]  # The first three characters of animals
dog = animals[3:6]  # The fourth through sixth characters
frog = animals[6:10]  # From the seventh character to the end`

####part 7/13
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")   # Use index() to find "duck"

# Your code here!
animals.insert(duck_index, "cobra")


print animals # Observe what prints after the insert operation


####part 8/13
my_list = [1,9,3,8,5,7]

for number in my_list:
    # Your code here
    print 2 * number

###part 9/13
start_list = [5, 3, 1, 2, 4]
square_list = []
# Your code here!
for number in start_list: 
    square_list.append(number ** 2)
    square_list.sort()
    
print square_list

####10/13
# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number

# Your code here!
print residents['Sloth'] 
print residents['Burmese Python']


#####12/13
# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
zoo_animals['Rockhopper Penguin'] = 'The Hole'



print zoo_animals








