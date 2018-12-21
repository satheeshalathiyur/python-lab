'''
Program to accept an  array and  shift by a particular number of positions
array: input array 
no_postions: shift by a particular number
'''
array = raw_input('enter values seperated by commas')
no_positions = int(raw_input('number of position'))
array = map(int,array.split(','))
head = array[0:no_positions]
array.extend(head)
del(array[0:no_positions])
print (array)