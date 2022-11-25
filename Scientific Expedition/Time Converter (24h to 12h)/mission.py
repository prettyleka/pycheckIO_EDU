from datetime import datetime

def time_converter(time: str) -> str:
    d = datetime.strptime(time, "%H:%M")
    result=d.strftime("%I:%M %p")
    if "AM" in result:
        if result[0]=="0":
            return result.replace("AM", "a.m.")[1:]
        else:
            return result.replace("AM", "a.m.")
    elif "PM" in result:
        if result[0]=="0":
            return result.replace("PM", "p.m.")[1:]
        else:
            return result.replace("PM", "p.m.")


print("Example:")
print(time_converter("12:30"))

assert time_converter("12:30") == "12:30 p.m."
assert time_converter("09:00") == "9:00 a.m."

print("The mission is done! Click 'Check Solution' to earn rewards!")
