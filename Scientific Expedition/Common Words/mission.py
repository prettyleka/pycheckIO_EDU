def checkio(line1: str, line2: str) -> str:
    newL=[]
    sLine1=line2.split(",")
    sLine2=line1.split(",")
    for x in sLine1:
        for z in sLine2:
            if x==z:
                newL.append(x)

    if len(newL)==0:
        return ""
    elif len(newL)==1:
        return "".join(newL)
    else:
        a=[]
        w=sorted(newL)
        for x in w:
            if x!=w[-1]:
                a.append(x+",")
            else:
                a.append(x)
        q="".join(a)
        return q


print("Example:")
print(checkio("hello,world", "hello,earth"))

assert checkio("hello,world", "hello,earth") == "hello"
assert checkio("one,two,three", "four,five,six") == ""
assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two"

print("The mission is done! Click 'Check Solution' to earn rewards!")
