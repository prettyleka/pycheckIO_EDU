def between_markers(text: str, begin: str, end: str) -> str:
    if begin not in text:
        newS=text.split(end)[0]
        return newS
    if end not in text:
        newS=text.split(begin)[1]
        return newS
    if len(text.split(begin)[0].split()) > len(text.split(end)[0].split()):
        return ""
    else:
        newS=text.split(begin)[1].split(end)[0]
        return newS


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')
