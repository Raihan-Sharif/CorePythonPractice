
'''
a = -10

if a == 0:
    print('Zero')
elif a > 0:
    print('Positive Number')
else:
    print('Negative Number')


age = 6

if ((age >= 8) and (age <= 12)):
    print('Welcome Your are In.')
elif((age >= 8) or (age <= 5)):
    print('Welcome to new Era')
else:
    print('Sorry you not eligible.')


my_list = ['Raihan','Raju','Hasin','Jabbar']

for x in my_list:
    print((x),': ' +  len(x).__str__())

for i in range(10,1,-1):
    if(i % 2):
        print('Value : {0} is ',i)

for i in range(18):
    if (i == 5):
        continue
    else: print(i)
'''

'''
my_Var = 10
my_Var > 10 ? print('geater than 10') : print('less than 10')
'''

'''
politicleParties = ['AAP','Elephent','Hand','Rest']
electionYear = ['2014','2009','2005','2001']
countryStatus = ['worst','developing','developed']
corruptionStatus = ['Max','Normal','Min']
for party in politicleParties:
     year = input("Enter Election Year : ")
     if year in electionYear:
         if year == '2014':
             print('AAp Wins !')
             print('Country Status: '+ countryStatus[2])
             print('Corruption Status: '+ corruptionStatus[2])
             continue
         elif year == '2009':
             print("'Hand Won :(")
             print('Country Status: ' + countryStatus[0])
             print('Corruption Status: ' + corruptionStatus[0])
             continue
         elif year == '2005':
             print("'Hand Won :(")
             print('Country Status: ' + countryStatus[0])
             print('Corruption Status: ' + corruptionStatus[0])
             continue
         elif year == '2001':
            print('Rest Won!')
            continue
     else:
        print('Wrong Year of election!')
        continue
else:
    print('The above loop was just was demonestration purpose')

'''

'''
while True:
    s = input("Enter your Query: ")
    if s == 'quit':
        break
    print('Length of string is : ', len(s))
print('Done.')
'''

'''
x = 50
while x > 0:
    print(x)
    x -= 1
else:
    print('Last number : ',x)

'''

'''
politicleParties = ['AAP','Elephent','Hand','Rest']
electionYear = ['2014','2009','2005','2001']
countryStatus = ['worst','developing','developed']
corruptionStatus = ['Max','Normal','Min']
polticalPartiesCount = len(politicleParties)
attemptCount = 0
isContinue = True
while isContinue:
     attemptCount += 1
     print('You take attempt : ',attemptCount)
     polticalPartiesCount -= 1
     inputText = input("Enter Year,type 'no' for exit : ")
     if(inputText.upper() == 'NO'):
            isContinue = False
            print('Good bye!')
     else:
         year = inputText
         if year in electionYear:
             if year == '2014':
                 print('AAp Wins !')
                 print('Country Status: '+ countryStatus[2])
                 print('Corruption Status: '+ corruptionStatus[2])
                 continue
             elif year == '2009':
                 print("'Hand Won :(")
                 print('Country Status: ' + countryStatus[0])
                 print('Corruption Status: ' + corruptionStatus[0])
                 continue
             elif year == '2005':
                 print("'Hand Won :(")
                 print('Country Status: ' + countryStatus[0])
                 print('Corruption Status: ' + corruptionStatus[0])
                 continue
             elif year == '2001':
                print('Rest Won!')
                continue
         else:
            print('Wrong Year of election!')
            continue
else:
    print('The above loop was just was demonestration purpose')
'''


fruitList = ['apple','apricot','banana','coconut','lemon','plum','mango']
print(fruitList)

# Element Count
print('Element Count: ', len(fruitList))
'''
for i in fruitList:
    print('Element at ',i,'= ',i)
'''

#for i in range(0,len(fruitList)):
#    print('Element at ',i,'= ',fruitList[i])
#    print('fruitList index at : ',i,' value : ',fruitList[i -1:])

subList1 = fruitList[-4:]

print('\n')
print('Sub LIst FruitList[-4]:')
print(subList1)

subList2 = fruitList[2:-2]
print('\n')
print('Sub List fruitList[2:-2]')
print(subList2)

subList3 = fruitList[-4:-2]
print('\n')
print('Sub List fruitList[-4:-2]')
print(subList3)

years = [1991,2000,2005,2010,2015,2020]
years[3:len(years)] = [2222,3333,4444]
print(years)
if years.__contains__(2000):
    indexOfYear = years.index(2000)
    print('indexOfYear : ',indexOfYear)
    years[indexOfYear] = 1111
print(years)

customList = []
customList.append(input('Please enter a value : '))
print(customList)

