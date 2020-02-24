stmt = input("Enter your statement: ") # Gets statement as input
varList = getVariables(stmt)

# Transforms raw, valid input into readable input
# Takes raw input as statement, returns String containing readable input
def transformInput(stmt):

#### TODO 

# Builds ArrayList of variables from statement
# Takes a readable statement as input, returns an ArrayList of variables
def getVariables(stmt):
	varList = [] # Initializes ArrayList containing variables
	for c in stmt: # Loops through each character in equation
		if (c.isalpha() and c not in varList): # Checks if character in equation is in the alphabet and is not already contained in ArrayList vars
			varList.append(c) # Adds var to ArrayList of variables
	return varList # Returns completed list of variables in equation

# Generates table and values for each possible combination
def generateTable(stmt):
	x, y = len(varList)+1, 2**(len(varList));
	table = [[0 for i in range(x)] for n in range(y)]

