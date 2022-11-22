def popular_words(text: str, words: list) -> dict:
    d = {}
    for x in words:
        d[x]=0
    newText=text.split("\n")
    newText.sort()
    for x in newText:
        if x=="":
            pass
        else:
            for i in x.split(" "):
                for z in words:
                    if str(z).lower()==i.lower() and z in d:
                        d[i.lower()]+=1
                    else:
                        pass

    return d


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
