def backward_string_by_word(text:str) -> str:
    newS=""
    if text =="":
        return ""
    else:
        for x in text.split(" "):
            if x==text.split(" ")[-1]:
                newS=newS+x[::-1]
            else:
                newS=newS+x[::-1]+" "
    return newS

if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word('world'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
