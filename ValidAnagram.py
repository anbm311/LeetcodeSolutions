# Valid Anagram - Problem # 242

def validAnagram(strA, strB):
    
    if len(strA) != len(strB):
        return False

    return "".join(sorted(strA)) == "".join(sorted(strB))

print(validAnagram("abc", "cab"))
print(validAnagram("abc", "cabd"))
print(validAnagram("", "cab"))
print(validAnagram("abc", ""))
