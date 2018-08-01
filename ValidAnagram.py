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

def ValidAnagram_3(strA, strB):

    if len(strA) != len(strB):
        return False
    
    strA_list = [0] * 256
    strB_list = [0] * 256

    for char in strA:
        strA_list[ord(char)] += 1

    for char in strB:
        strB_list[ord(char)] += 1

    for i in range(len(strA_list)):
        if strA_list[i] != strB_list[i]:
            return False

    return True


def ValidAnagram_4(strA, strB):
    if len(strA) != len(strB):
        return False

    HashMap1={}
    HashMap2={}

    for char in strA:
        HashMap1[char] = HashMap1.get(char, 0) + 1

    for char in strB:
        HashMap2[char] = HashMap2.get(char, 0) + 1

    return HashMap1 == HashMap2

def ValidAnagram_5(strA, strB):
    if len(strA) != len(strB):
        return False

    HashMap={}
    
    for char in strA:
        HashMap[char] = HashMap.get(char, 0) + 1

    for char in strB:
        if char in HashMap:
            HashMap[char] = HashMap.get(char, 0) - 1
            if HashMap[char] < 0:
                return False
        else:
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

print(ValidAnagram_3("abc", "cab"))
print(ValidAnagram_3("abc", "cabd"))
print(ValidAnagram_3("", "cab"))
print(ValidAnagram_3("abc", ""))

print(ValidAnagram_4("abc", "cab"))
print(ValidAnagram_4("abc", "cabd"))
print(ValidAnagram_4("", "cab"))
print(ValidAnagram_4("abc", ""))
