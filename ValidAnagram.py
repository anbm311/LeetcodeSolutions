# Valid Anagram - Problem # 242

# Time complexity - O(nlogn), Space Complexity - O(1)

def validAnagram(strA, strB):
    
    if len(strA) != len(strB):
        return False

    return "".join(sorted(strA)) == "".join(sorted(strB))


# Time complexity - O(n), Space Complexity - O(1)

def ValidAnagramSolution(strA, strB):
    if len(strA) != len(strB):
        return False

    HashMap = {}

    for i in range(len(strA)):
        HashMap[strA[i]] = HashMap.get(strA[i],0)+1
        HashMap[strB[i]] = HashMap.get(strB[i],0)-1

    for key in HashMap.keys():
        if HashMap[key] != 0:
            return False

    return True

print(validAnagram("abc", "cab"))
print(validAnagram("abc", "cabd"))
print(validAnagram("", "cab"))
print(validAnagram("abc", ""))
print(ValidAnagramSolution("abc", "cab"))
print(ValidAnagramSolution("abc", "cabd"))
print(ValidAnagramSolution("", "cab"))
print(ValidAnagramSolution("abc", ""))
