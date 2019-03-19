#time complexity O(n) and space complexity O(n)

def toLowerCase_Ord(string):
    h = []
    for i in string:
        if ord(i) >= 65 and ord(i) <= 90 :
            j = chr (ord(i) + 32)
            h.append(j)
        else:
            h.append(i)
    return ''.join(h)


#time complexity O(n) and space complexity O(1)

def toLowerCase_join(string):
    return "".join(char.lower() for char in string)


print(toLowerCase_Ord('HELLO'))
print(toLowerCase_Ord('hElLO'))
print(toLowerCase_Ord('Hello'))
print(toLowerCase_Ord('helLLO'))

print(toLowerCase_join('HELLO'))
print(toLowerCase_join('hElLO'))
print(toLowerCase_join('Hello'))
print(toLowerCase_join('helLLO'))
