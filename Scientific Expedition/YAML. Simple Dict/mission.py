import re


def yaml(a):
    d=a.split("\n")
    q={}
    for x in d:
        if x=="":
            continue
        else:
            k=x.split(": ")[0]
            v=x.split(": ")[1]
            num = re.fullmatch("\d+", v)
            if num==None:
                q[k]=v
            else:
                n=num[0]
                q[k]=int(n)
    return dict(sorted(q.items()))


if __name__ == '__main__':
#   print("Example:")
 #   print(yaml("""name: Alex
#age: 12"""))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml("""name: Alex Fox
age: 12

class: 12b""") == {'age': 12,
 'class': '12b',
 'name': 'Alex Fox'}
    print("Coding complete? Click 'Check' to earn cool rewards!")
