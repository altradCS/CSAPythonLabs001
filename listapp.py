import random

######## Custom Shuffle #############
def custom_shuffle(lst):
    shuffled_list = lst[:]
    for i in range(len(shuffled_list)):
        rand_index = random.randint(0, len(shuffled_list) -1)
        shuffled_list[i], shuffled_list[rand_index] = shuffled_list[rand_index], shuffled_list[i]

    return shuffled_list


####### Remove Duplicated Values ############
def remove_duplicates(lst):
    # add your algorimth.....

    return unique_lst


####### sort list in ascending ############
def sort_list(lst):
    # add your code......

    return sorted_lst


