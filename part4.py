dic = {
    'user_id': int,
    'feedback_details': {
        'rating': int,
        'comments': str
    }
}

def rating(list):
    new_dict_list = []
    for i in range(len(list)):
        rating = list[i].get('feedback_details').get('rating') >=4
        if rating:
            new_dict = {
                'user_id': list[i].get('user_id'),
                'rating': list[i].get('feedback_details').get('rating')
            }
            
            new_dict_list.append(new_dict)

def sort(list):
    pass




