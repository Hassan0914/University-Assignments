

data1 = (1,"Muhammad Hassan",22,"Pakistan")
data2 = (2,"Muhammad Ahmad",22,"Pakistan")
data3 = (3,"Hassan",43,"India")
data4 = (4,"Muhammad Hassan",32,"Canada")
data5 = (5,"Raza",32,"USA")
data6 = (6,"William",45,"USA")
data7 = (7,"Ifti",28,"Canada")
data8 = (8,"Muhammad Hassan",25,"Afghanistan")
data9 = (1,"Muhammad Hassan",22,"Pakistan")
data10 = (2,"Muhammad",22,"Pakistan")
data11 = (3,"Hassan",43,"India")
data12 = (4,"Mukhtar",32,"Canada")
data13= (5,"Raza",32,"USA")
data14= (6,"William",45,"USA")
data15= (7,"Ifti",28,"Canada")
data16= (8,"Riaz",25,"Afghanistan")

list_of_tuples = [data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14,data15,data16]

def filter_users(age,country):

    new_list = []

    #print("id, user_name, age, country")
    for i in range(len(list_of_tuples)):
        if list_of_tuples[i][2] > age and list_of_tuples[i][3] == country:
            new_list.append(list_of_tuples[i][1])
            #for j in range(4):
                #print(list_of_tuples[i][j],end="  ")
            #print()
    return new_list
collection1 = filter_users(30,"USA")
print(collection1)

def sort_list(listt):
    sorted_li = []

    sorted_l = sorted(listt,key=lambda x: x[2])
    for i in range(10):
        sorted_li.append(sorted_l[i])

    return sorted_li

d1 = sort_list(list_of_tuples)
for i in d1:
    print(i)

def check_duplicates(list):
    duplicates = []
    seen = set()
    for i in range(len(list)):
        name = list[i][1]
        
        if name in seen and name not in duplicates:
            duplicates.append(name)
        else:
            seen.add(name)
        
        
    return set(duplicates)
b1 = check_duplicates(list_of_tuples)
print(b1)

