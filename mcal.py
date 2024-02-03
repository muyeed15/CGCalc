# modules
from database import grade_list
from database import number_list
from gcal import gcal

# mark to grade
def converter(u, m):
    g_list = grade_list(u)
    g_list.remove("Select")

    n_list = number_list(u)

    index = 0
    for num in n_list:
        if m >= num:
            return g_list[index]
        
        index += 1
    
    return g_list[-1]


# mark to grade calculation
def mcal(u, data):
    f_data = []

    for m in data[2]:
        f_data.append(converter(u, float(m)))

    data[2] = f_data

    return gcal(u, data)

