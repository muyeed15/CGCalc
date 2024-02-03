# modules
from database import grade_list
from database import point_list

# grade calculation
def gcal(u, data):
    g_list = grade_list(u)
    g_list.remove("Select")

    p_list = point_list(u)

    total_p = 0
    tindex = 0
    for grade in data[2]:
        index = g_list.index(grade)
        total_p += p_list[index]*float(data[1][tindex])
        tindex += 1

    total_c = 0
    for credits in data[1]:
        total_c += float(credits)

    cgpa = float("{:.2f}".format(total_p/total_c))

    return cgpa, total_c, data

