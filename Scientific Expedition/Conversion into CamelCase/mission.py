def to_camel_case(name: str) -> str:
    newL=name.split("_")
    q=[]
    for z in newL:
        q.append(z.capitalize())
    w="".join(q)
    return w


print("Example:")
print(to_camel_case("my_function_name"))

assert to_camel_case("my_function_name") == "MyFunctionName"
assert to_camel_case("i_phone") == "IPhone"

print("The mission is done! Click 'Check Solution' to earn rewards!")
