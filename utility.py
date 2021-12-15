

def replace_string(data_list,target,replaced):
    result = []
    for i in data_list:
        buffer = i.replace(target,replaced)
        result.append(buffer)
    return result

def remove_string(data_list,target):
    result=[]
    for i in data_list:
        if not target in i:
            result.append(i)
    return result

def keep_string(data_list,target):
    result=[]
    for i in data_list:
        if target in i:
            result.append(i)
    return result