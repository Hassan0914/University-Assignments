from datetime import datetime, timedelta
import random

# Creating 30 transaction tuples with variable names
transaction1 = (1, 1001, 150.25, datetime.now() - timedelta(days=1, hours=3))
transaction2 = (2, 1002, 245.80, datetime.now() - timedelta(days=2, hours=5))
transaction3 = (3, 1003, 89.99, datetime.now() - timedelta(days=3, hours=2))
transaction4 = (4, 1004, 300.55, datetime.now() - timedelta(days=4, hours=1))
transaction5 = (5, 1005, 210.75, datetime.now() - timedelta(days=5, hours=4))
transaction6 = (6, 1006, 47.60, datetime.now() - timedelta(days=6, hours=6))
transaction7 = (7, 1007, 157.30, datetime.now() - timedelta(days=7, hours=2))
transaction8 = (8, 1008, 450.45, datetime.now() - timedelta(days=8, hours=3))
transaction9 = (9, 1009, 325.00, datetime.now() - timedelta(days=9, hours=1))
transaction10 = (10, 1010, 75.25, datetime.now() - timedelta(days=10, hours=4))

transaction11 = (11, 1001, 123.45, datetime.now() - timedelta(days=11, hours=3))
transaction12 = (12, 1002, 298.99, datetime.now() - timedelta(days=12, hours=5))
transaction13 = (13, 1003, 50.00, datetime.now() - timedelta(days=13, hours=2))
transaction14 = (14, 1004, 320.25, datetime.now() - timedelta(days=14, hours=1))
transaction15 = (15, 1005, 215.75, datetime.now() - timedelta(days=15, hours=6))
transaction16 = (16, 1006, 79.99, datetime.now() - timedelta(days=16, hours=4))
transaction17 = (17, 1007, 410.15, datetime.now() - timedelta(days=17, hours=2))
transaction18 = (18, 1008, 99.50, datetime.now() - timedelta(days=18, hours=3))
transaction19 = (19, 1009, 389.70, datetime.now() - timedelta(days=19, hours=1))
transaction20 = (20, 1010, 56.10, datetime.now() - timedelta(days=20, hours=4))

transaction21 = (21, 1001, 245.00, datetime.now() - timedelta(days=21, hours=5))
transaction22 = (22, 1002, 398.80, datetime.now() - timedelta(days=22, hours=1))
transaction23 = (23, 1003, 115.20, datetime.now() - timedelta(days=23, hours=3))
transaction24 = (24, 1004, 275.50, datetime.now() - timedelta(days=24, hours=2))
transaction25 = (25, 1005, 88.45, datetime.now() - timedelta(days=25, hours=6))
transaction26 = (26, 1006, 349.99, datetime.now() - timedelta(days=26, hours=5))
transaction27 = (27, 1011, 125.30, datetime.now() - timedelta(days=27, hours=3))
transaction28 = (28, 1008, 278.90, datetime.now() - timedelta(days=28, hours=4))
transaction29 = (29, 1009, 940.50, datetime.now() - timedelta(days=29, hours=2))
transaction30 = (30, 1010, 425.25, datetime.now() - timedelta(days=30, hours=1))

# Appending transactions to the list
transaction_list = [
    transaction1, transaction2, transaction3, transaction4, transaction5, 
    transaction6, transaction7, transaction8, transaction9, transaction10,
    transaction11, transaction12, transaction13, transaction14, transaction15,
    transaction16, transaction17, transaction18, transaction19, transaction20,
    transaction21, transaction22, transaction23, transaction24, transaction25,
    transaction26, transaction27, transaction28, transaction29, transaction30
]

# Printing the transaction list


def unique_users(ttransaction_list):

    users = set()
    for t in ttransaction_list:
        user_id = t[1]
        users.add(user_id)
        
        
    return len(users)

print(unique_users(transaction_list))

def highest_amount(list):
    tr_amount = []
    for i in range(len(list)):
        tr_amount.append(list[i][2])

    return max(tr_amount)
print(highest_amount(transaction_list))

def two_lists(list):
    tr_ids = []
    user_ids = []
    for i in range(len(list)):
        tr_ids.append(list[i][0])
        user_ids.append(list[i][1])
    return tr_ids, user_ids

print(two_lists(transaction_list))


