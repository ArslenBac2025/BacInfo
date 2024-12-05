def anagram(ch1, ch2):
    if(ch1 == ''):
        return True
    elif (ch2.find(ch1[0]) == - 1):
        return False
    else:
        p = ch2.find(ch1[0])
        ch1 = ch1[1: len(ch1) - 1]
        ch2 = ch2[0 : p] + ch2[p + 1: len(ch2)]
        return anagram(ch1, ch2)

print(anagram("adem", "meda"))