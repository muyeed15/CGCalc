# modules
from start import start
from grade import grade
from mark import mark
from gcal import gcal
from mcal import mcal
from result import result

# start
c, m, u = start()

# method
if m == "Grade":
    data, ccgpa, ccreds = grade(int(c), u)
    cgpa, creds, data = gcal(u, data)

elif m == "Mark":
    data, ccgpa, ccreds = mark(int(c), u)
    cgpa, creds, data = mcal(u, data)

# result
result(data, cgpa, creds, ccgpa, ccreds)

