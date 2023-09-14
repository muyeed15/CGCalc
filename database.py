# uni list
def uni_list():
    uni = ["Select", "IUB", "NSU", "AIUB", "SEU", "UIU", "EWU"]

    return uni


# grade list
def grade_list(u):
    iub = ["Select", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"]
    nsu = ["Select", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"]
    aiub = ["Select", "A+", "A", "B+", "B", "C+", "C", "D+", "D", "F"]
    seu = ["Select", "A+", "A", "A-", "B+", "B", "B-", "C+", "C", "D", "F"]
    uiu = ["Select", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"]
    ewu = ["Select", "A+", "A", "A-", "B+", "B", "B-", "C+", "C", "D", "F"]

    uni = {"IUB": iub, "NSU":nsu, "AIUB":aiub, "SEU":seu, "UIU":uiu, "EWU":ewu}

    return uni[u]


# point list
def point_list(u):
    iub = [4.00, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.00]
    nsu = [4.00, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.00]
    aiub = [4.00, 3.75, 3.50, 3.25, 3.00, 2.75, 2.50, 2.25, 0.00]
    seu = [4.00, 3.75, 3.50, 3.25, 3.00, 2.75, 2.50, 2.25, 2.00, 0.00]
    uiu = [4.00, 3.67, 3.33, 3.00, 2.67, 2.33, 2.00, 1.67, 1.33, 1.00, 0.00]
    ewu = [4.00, 3.75, 3.50, 3.25, 3.00, 2.75, 2.50, 2.25, 2.00, 0.00]

    uni = {"IUB": iub, "NSU":nsu, "AIUB":aiub, "SEU":seu, "UIU":uiu, "EWU":ewu}

    return uni[u]


# number list
def number_list(u):
    iub = [90, 85, 80, 75, 70, 65, 60, 55, 50, 45]
    nsu = [93, 90, 87, 83, 80, 77, 73, 70, 67, 60]
    aiub =[90, 85, 80, 75, 70, 65, 60, 50]
    seu = [80, 75, 70, 65, 55, 50, 45, 40]
    uiu = [90, 86, 82, 78, 74, 70, 66, 62, 58, 55]
    ewu = [80, 75, 70, 65, 55, 50, 45, 40]

    uni = {"IUB": iub, "NSU":nsu, "AIUB":aiub, "SEU":seu, "UIU":uiu, "EWU":ewu}

    return uni[u]

