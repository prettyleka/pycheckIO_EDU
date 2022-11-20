def date_time(time: str) -> str:
    return days(time)+month1(time)+years(time)+hours(time)+minutes(time)


def days(time: str) -> str:
    dateS=time.split(" ")[0]
    dayS=dateS.split(".")[0]
    if dayS[0] == "0":
        day = dayS[1]
        return day
    else:
        return dayS
def month1(time: str) -> str:
    dateS=time.split(" ")[0]
    monthS = dateS.split(".")[1]
    if monthS =="01":
        return " January"
    if monthS =="02":
        return " February"
    if monthS=="03":
        return " March"
    if monthS=="04":
        return " April"
    if monthS=="05":
        return " May"
    if monthS=="06":
        return " June"
    if monthS=="07":
        return " July"
    if monthS=="08":
        return " August"
    if monthS=="09":
        return " September"
    if monthS=="10":
        return " October"
    if monthS=="11":
        return " November"
    if monthS=="12":
        return " December"
def years(time: str) -> str:
    dateS=time.split(" ")[0]
    years = dateS.split(".")[2]
    return "".join(" "+years + " year")
def hours(time: str) -> str:
    timeS=time.split(" ")[1]
    hourS =timeS.split(":")[0]
    if hourS[0]=="0":
        hour = hourS[1]
    else:
        hour = hourS
    if hour=="1":
        return "".join(" "+hour + " hour")
    else:
        return "".join(" "+hour + " hours")
def minutes(time: str) -> str:
    timeS=time.split(" ")[1]
    minuteS =timeS.split(":")[1]
    if minuteS[0] == "0":
        minute = minuteS[1]
    else:
        minute = minuteS
    if minute == "1":
        return "".join(" "+minute + " minute")
    else:
        return "".join(" "+minute + " minutes")







if __name__ == "__main__":
    print("Example:")
    print(date_time("20.11.1990 03:55"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert (
        date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
    ), "Millenium"
    assert (
        date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes"
    ), "Victory"
    assert (
        date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes"
    ), "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
