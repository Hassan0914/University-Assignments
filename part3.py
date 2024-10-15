page_a = {1,4,5,7,6,9,3}
page_b = {1,4,7,8,9,12}
page_c = set()


def find_users(pg1,pg2):
    users = pg1.intersection(pg2)
    
    return users
print(find_users(page_a,page_b))

def new_user_ids(ids,page_a):
    for i in range(len(ids)):
        page_a.add(ids[i])
    return page_a
def remove_user_ids(user_ids,page_b):
    for i in user_ids:
        page_b.discard(i)
    return page_b
print(remove_user_ids([1,4,5],page_b))


