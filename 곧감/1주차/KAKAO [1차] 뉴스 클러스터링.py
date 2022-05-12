from collections import Counter 
def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    str1_list = []
    str2_list = []
    for i in range(0, len(str1)-1):
        if str1[i:i+2].isalpha():
            str1_list.append(str1[i:i+2])
    for j in range(0, len(str2)-1):
        if str2[j:j+2].isalpha():
            str2_list.append(str2[j:j+2])
            
    Counter1 = Counter(str1_list)
    Counter2 = Counter(str2_list)
    
    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())
    
    print(inter, union)
    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)
    
