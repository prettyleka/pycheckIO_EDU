from datetime import datetime

from datetime import date

def days_diff(a, b):
    a1 = str(a).replace("(","").replace(")", "")
    b1=str(b).replace("(","").replace(")", "")
    if len(a1.split(",")[0])<4 and len(b1.split(",")[0])<4:
        d1 = datetime.strptime(a1, "%Y, %m, %d")
        d2 = datetime.strptime(b1, "%Y, %m, %d")
        return abs(d2 - d1).days
    else:
        if b1>a1:
            d0 = date(int(a1.split(",")[0]), int(a1.split(", ")[1]), int(a1.split(", ")[2]))
            d1 = date(int(b1.split(",")[0]), int(b1.split(", ")[1]), int(b1.split(", ")[2]))
            delta = d1 - d0
            return abs(delta.days)
        else:
            d0 = date(int(a1.split(",")[0]), int(a1.split(", ")[1]), int(a1.split(", ")[2]))
            d1 = date(int(b1.split(",")[0]), int(b1.split(", ")[1]), int(b1.split(", ")[2]))
            delta = d0 - d1
            return abs(delta.days)


if __name__ == "__main__":
    print("Example:")
    print(days_diff((1982, 4, 19), (1982, 4, 22)))

    # These "asserts" are used for self-checking and not for an auto-testing
    #assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    #assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((1, 1, 1), (9999, 12, 31)) == 3652058
    print("Coding complete? Click 'Check' to earn cool rewards!")
