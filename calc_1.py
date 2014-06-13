s = raw_input()
op_arr = ['/', '*', '+', '-']

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

def divide(data):
	div_pos = data.index('/')
	div_res = float(data[div_pos-1]) / float(data[div_pos+1])
	data[div_pos] = str(div_res)
	data.pop(div_pos-1)
	data.pop(div_pos)
	return data

def multiply(data):
	mul_pos = data.index('*')
	mul_res = float(data[mul_pos-1]) * float(data[mul_pos+1])
	data[mul_pos] = str(mul_res)
	data.pop(mul_pos-1)
	data.pop(mul_pos)
	return data

def add(data):
	add_pos = data.index('+')
	add_res = float(data[add_pos-1]) + float(data[add_pos+1])
	data[add_pos] = str(add_res)
	data.pop(add_pos-1)
	data.pop(add_pos)
	return data

def subtract(data):
	sub_pos = data.index('-')
	sub_res = float(data[sub_pos-1]) - float(data[sub_pos+1])
	data[sub_pos] = str(sub_res)
	data.pop(sub_pos-1)
	data.pop(sub_pos)
	return data


data = format_input(s, op_arr)
while '/' in data:
	data = divide(data)
while '*' in data:
	data = multiply(data)
while '+' in data:
	data = add(data)
while '-' in data:
	data = subtract(data)
print data[0]
