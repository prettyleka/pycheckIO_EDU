def changing_direction(elements: list[int]) -> int:
    el=[]
    count=0
    for i in range(0, len(elements)):
        if len(elements)==1:
            return 0
        if i==0:
            if elements[i+1] != elements[i]:
                el.append(elements[i])
        elif i==len(elements)-1:
            if elements[i-1] != elements[i]:
                el.append(elements[i])
        elif elements[i-1] != elements[i]:
            el.append(elements[i])
    for i in range(1, len(el) - 1):
         if el[i - 1] <= elements[i] > elements[i + 1] or el[i - 1] > el[i] < el[i + 1]:
             count += 1
    print(count)
    return count


print("Example:")
#Example print(changing_direction([1, 2, 2, 1, 2, 2]))

#assert changing_direction([1, 2, 3, 4, 5]) == 0
#assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([5, 4, 9, 10, 10, 10, 10, 3, 8, 5, 1, 9, 9, 4, 1])==6

print("The mission is done! Click 'Check Solution' to earn rewards!")
