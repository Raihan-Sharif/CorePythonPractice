list1 = [1,2,3]
list2 = ['One','Two']

print('list1:',list1)
print('list2: ',list2)
print('\n')

list12 = list1 + list2
print('list1 + list2 :',list12)

list2x3 = list2 * 3
print('list2 * 3 ; ',list2x3)

hasThree = 'Three' in list2
print('"Three" in list2? : ',hasThree)

years = [1990,1991,1992,1993,1993,1993,1994]
print('Years : ',years)
print('\n -Reverse the list')

# Reverse the list
years.reverse()

print('Years (After Reverse): ',years)

aTuple = (2001,2002,2003)
print('\n - Extend:',aTuple)
years.extend(aTuple)
print('Years (After Extend) : ',years)

print('\n -Append 3000')
years.append(3000)
print('Years (After append) : ',years)

print('\n - Remove 1993')
years.remove(1993)
print('Years (After Remove): ',years)

print('\n -Years.pop()')
# Remove last element of list
lastElement = years.pop()
print('last element : ',lastElement)
print('\n')

# Count
print("Years.count(1993): ",years.count(1993))

# sort
b = [6,3,8,2,7,3,9]
b.sort()
print(b)

# List of Integers
b = [6,3,8,2,7,3,9]
b.sort(reverse=True)
print(b)

# list of String
d = ['aaa','bb','c']
d.sort(key=len)
print(d)
d.sort(key=len,reverse=True)
print(d)
f = ['A','a','B','b','C','c']
f.sort(key=str.lower,reverse=False)
print(f)