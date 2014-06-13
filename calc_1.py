# Take input string to be operated. Make sure there is no space in it. If there is just remove it.
s = raw_input()
# Array of permitted operations
op_arr = ['/', '*', '+', '-']

# Formatting of input string into a list of numbers and operations between them
# For Example: For input - '23+2*2-54/27', this function will return ['23', '+', '2', '*', '2', '-', '54', '/', '27']
def format_input(s, op_arr):
	data = []
	count = 0
	for i in range(len(s)):
		if s[i] in op_arr:
			data.append(s[count:i])
			data.append(s[i])
			count = i+1
		if i == len(s)-1:
			data.append(s[count:])
	return data

# For performing one division operation
def divide(data):
	div_pos = data.index('/')
	div_res = float(data[div_pos-1]) / float(data[div_pos+1])
	data[div_pos] = str(div_res)
	data.pop(div_pos-1)
	data.pop(div_pos)
	return data

# For performing one multiplication operation
def multiply(data):
	mul_pos = data.index('*')
	mul_res = float(data[mul_pos-1]) * float(data[mul_pos+1])
	data[mul_pos] = str(mul_res)
	data.pop(mul_pos-1)
	data.pop(mul_pos)
	return data

# For performing one addition operation
def add(data):
	add_pos = data.index('+')
	add_res = float(data[add_pos-1]) + float(data[add_pos+1])
	data[add_pos] = str(add_res)
	data.pop(add_pos-1)
	data.pop(add_pos)
	return data

# For performing one subtraction operation
def subtract(data):
	sub_pos = data.index('-')
	sub_res = float(data[sub_pos-1]) - float(data[sub_pos+1])
	data[sub_pos] = str(sub_res)
	data.pop(sub_pos-1)
	data.pop(sub_pos)
	return data


data = format_input(s, op_arr)
# Perform 'divide' operation for every '/' in the input
while '/' in data:
	data = divide(data)
	
# Perform 'multiply' operation for every '*' in the input
while '*' in data:
	data = multiply(data)
	
# Perform 'add' operation for every '+' in the input
while '+' in data:
	data = add(data)
	
# Perform 'subtract' operation for every '-' in the input
while '-' in data:
	data = subtract(data)

# The final result will be a list with just one element, which will be our required output
print data[0]
