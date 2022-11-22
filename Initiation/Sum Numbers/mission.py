import re


def sum_numbers(text: str) -> int:
    numW=re.findall("[\d+]+[a-zA-Z]", text)
    if len(numW)>0:
        return 0
    numL=re.findall("[\d+]+", text)
    if len(numL)==0:
        return 0
    elif len(numL)==1:
        return int(numL[0])
    else:
        res = [eval(i) for i in numL]
        Sum=sum(res)
        return Sum


print("Example:")
print(sum_numbers("hi"))

assert sum_numbers("hi") == 0
assert sum_numbers("who is 1st here") == 0
assert sum_numbers("my numbers is 2") == 2
assert sum_numbers("This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year") == 3755

assert sum_numbers("5 plus 6 is") == 11
assert sum_numbers("") == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")
