# Intermediate Functions II
# 1 Update values in the given dictonary and a list
x = [[5, 2, 3], [10, 8, 9]]
x[1][0] = 15
print(f"x was orginally [ [5,2,3], [10,8,9] ]  and is now {x}")
x2 = [[7, 8, 99, 10], [0, 2, -6, 10, 10]] # (f()) without f the output of {x2} will be x2
for val in x2:
    for i in range(len(val)):
        if 10 == val[i]:
            savedIndex = i
            val[savedIndex] = 15
print(f"x2 was orginally [ [7,8,99,10],[0,2,-6,10,10] ] and is now {x2}")

#2 
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print(
    "student 1's orginal information was {'first_name':  'Michael', 'last_name' : 'Jordan'}")
print("student 1's new information is {student[0]}")

#3
sports_directory2 = {
    'american_football': ['Peyton', 'Eli'],
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
for i in range(len(sports_directory2['soccer'])):
    if 'Messi' in sports_directory2['soccer']:
        sports_directory2['soccer'][i] = 'Andres'
print(
    "my new sports_directory2 changed from 'soccer' : ['Messi', 'Ronaldo', 'Rooney']  to")
for i in range(len(sports_directory2['soccer'])):
    print(f"{sports_directory2['soccer'][i]} and ")
#4
z = [{'x': 10, 'y': 20}]  # this is a list with on dictonary inside
# hard coding it
z[0]['y'] = 30
print("z used to look like [{'x': 10, 'y': 20}] now {z}")


#2 ist dictionary iteration
students2 = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

def newiterateDictionary(anyList):
    stringReturn = ''
    for val in anyList:
        stringReturn += f"first_name - {val['first_name']}, last_name - {val['last_name']}\n"
    return stringReturn


print(newiterateDictionary(students2))


#3 list of dictionaries value retrieval
def iterateDictionary2(key_name, some_list):
    stringReturn = ''
    for val in some_list:
        stringReturn += f"{val[key_name]} \n"
    return stringReturn


print(iterateDictionary2('last_name', students2))


#4 list values for dictionary iteration
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printDictonaryInfo(my_dictonary):
    for key in my_dictonary:
        print(f"{len(my_dictonary[key])} {key.upper()}")
        for val in my_dictonary[key]:
            print(val)
        print("")

printDictonaryInfo(dojo)