def from_camel_case(name: str) -> str:
    newL=[]
    for x in name:
        if x==x.capitalize() and x==name[0]:
            newL.append(x.lower())
        elif x==x.capitalize():
            newL.append("_"+x.lower())
        else:
            newL.append(x)

    w="".join(newL)
    return w


print("Example:")
print(from_camel_case("MyFunctionName"))

assert from_camel_case("MyFunctionName") == "my_function_name"
assert from_camel_case("IPhone") == "i_phone"

print("The mission is done! Click 'Check Solution' to earn rewards!")
