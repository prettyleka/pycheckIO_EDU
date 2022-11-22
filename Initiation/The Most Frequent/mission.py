def most_frequent(data: list) -> str:
    d = {}
    for x in data:
        if x not in d:
            d[x]=1
        else:
            d[x]+=1
    return max(d, key=lambda k: d[k])

if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print("Example:")
    print(most_frequent(["a", "b", "c", "a", "b", "a"]))

    assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"

    assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"
    print("Done")
