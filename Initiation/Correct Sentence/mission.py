def correct_sentence(text: str) -> str:
    n = []
    if len(text.split(" "))==1:
        if "." in text.split(" ")[0]:
            return (text.split(" ")[0]).capitalize()
        else:
            return (text.split(" ")[0]).capitalize()+"."
    for x in text.split(" "):
        if x == text.split(" ")[0]:
            n.append(x.capitalize()+" ")
        elif x== text.split(" ")[-1]:
            if "." in x:
                n.append(x)
            else:
                n.append(x+".")
        else:
            n.append(x+" ")
    return "".join(n)


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."

    print("Coding complete? Click 'Check' to earn cool rewards!")
