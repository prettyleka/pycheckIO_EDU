def follow(instructions: str) -> tuple[int, int] | list[int]:
    f=[0, 1]
    b=[0, -1]
    l=[-1, 0]
    r=[1, 0]
    newCo=[0,0]
    for x in instructions:
        if x=="f":
            newCo[1]=newCo[1]+f[1]
        elif x=="b":
            newCo[1]=newCo[1]+b[1]
        elif x=="l":
            newCo[0]=newCo[0]+l[0]
        elif x=="r":
            newCo[0]=newCo[0]+r[0]
    return newCo






print("Example:")
print(list(follow("fflff")))

assert list(follow("fflff")) == [-1, 4]
assert list(follow("ffrff")) == [1, 4]
assert list(follow("fblr")) == [0, 0]

print("The mission is done! Click 'Check Solution' to earn rewards!")
