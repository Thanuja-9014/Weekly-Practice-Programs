def is_anagram(str1,str2):
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()
    return sorted(str1)==sorted(str2)
w1="thanu"
w2="anuryt"
if(is_anagram(w1,w2)):
    print(f"{w1} and {w2} are anagrams")
else:
    print(f"{w1} and {w2} are not anagrams")
    