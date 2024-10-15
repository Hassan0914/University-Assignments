d1 = {
    'name':'kakamanna', 
    'age':22, 
    'address':'Johar Town', 
    'marks':[60, 75, 80]
}
l1 = d1.items()
print(l1)

dict1 = {'rauf': 81, 
         'arif':90, 
        'maaz':76, 
        'hadeed':73,
         'mujahid':93, 
        }

def func1(item):
    return item[1]


mylist = sorted(dict1.items(), key = func1, reverse=True)

print(mylist)

students = [
         {"name": "Hashim", "age": 18, "grade": "B"},
         {"name": "Salman", "age": 11, "grade": "A"},
         {"name": "Mazhar", "age": 12, "grade": "C"},
         {"name": "Farhan", "age": 22, "grade": "D"},
         {"name": "Bilal", "age": 19, "grade": "A"},
         {"name": "Zalaid", "age": 17, "grade": "B"}
        ]
def func2(item):
     return item.get('age') #return item['age']

sorted_students = sorted(students, key = func2)


import copy
dict1 = {'rauf': 81, 
         'arif':90, 
        'maaz':76, 
        'hadeed':73,
         'mujahid':93, 
        }

#dict2 = copy.copy(dict1)
dict2 = dict1.copy()


# Both variables point to different memory objects, so have the different ID
print('ID of dict1:', id(dict1))
print('ID of dict2:', id(dict2))




