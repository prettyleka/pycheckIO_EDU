from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    newList=[]
    if len(elements)<=1:
        return True
    else:
        for x in elements:
            if x in newList:
                pass
            else:
                newList.append(x)
    if len(newList)>1:
        return False
    else:
        return True


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
