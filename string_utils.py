

def explore_string(a_string):
    return list(a_string)

def _explode_list_of_strings(list_of_strings):

    result = []
    for each_string in list_of_strings:
        result.append(explore_string(each_string))
    return result