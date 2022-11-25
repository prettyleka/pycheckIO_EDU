def goes_after(word: str, first: str, second: str) -> bool:
    count=0
    i=0
    while i<len(word)-1:
        if word[i]==first:
            count+=1
            if word[i+1]==second and count==1:
                return True
            else:
                return False
        else:
            i+=1
    return False


print("Example:")
print(goes_after('transport', 'r', 't'))

# These "asserts" are used for self-checking
assert goes_after('transport', 'r', 't') == False
assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("panorama", "a", "n") == True
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False
assert goes_after("Almaz", "a", "l") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
