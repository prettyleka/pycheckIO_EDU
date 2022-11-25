def caps_lock(text: str) -> str:
    newL=[]
    count=0
    i=0
    while i<len(text):
        if count==0:
            if text[i]!="a":
                newL.append(text[i])
                i+=1
            else:
                count+=1
                i+=1
        elif count == 1:
            if text[i]!="a":
                newL.append(text[i].capitalize())
                i+=1
            else:
                count=0
                i+=1
    w="".join(newL)
    return w

if __name__ == "__main__":
    print("Example:")
    print(caps_lock("Why are you asking me that?"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    assert caps_lock("Aloha from Hawaii") == "Aloh FROM HwII"
    print("Coding complete? Click 'Check' to earn cool rewards!")
