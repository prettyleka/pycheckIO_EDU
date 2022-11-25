def translate(text: str) -> str:
    newL=[]
    z=0
    i=0   #hieeelalaooo
    vowels="aeiouy"
    while z<len(text):
        if i>0:
                i=0
                z+=1
                continue
        if text[z] not in vowels:
            if text[z]==" ":
                newL.append(" ")
                z+=1
            else:
                newL.append(text[z])
                i+=1
                z+=1
        elif text[z] in vowels:
                newL.append(text[z])
                i+=2
                z+=2
        else:
                i+=1
                z+=1
    w = "".join(newL)

    return w


print("Example:")
print(translate("aaa bo cy da eee fe"))

assert translate("hieeelalaooo") == "hello"
assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translate("aaa bo cy da eee fe") == "a b c d e f"
assert translate("sooooso aaaaaaaaa") == "sos aaa"

print("The mission is done! Click 'Check Solution' to earn rewards!")
