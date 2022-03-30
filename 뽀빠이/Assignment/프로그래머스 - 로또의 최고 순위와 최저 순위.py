def solution(lottos, win_nums):
    del_list = []
    j = 0
    for i in range(len(lottos)):
        k = i - j
        if lottos[k] in win_nums:
            win_nums.remove(lottos[k])
            del lottos[k]
            j = j + 1

    if len(win_nums) <= 4:        
        min_num = len(win_nums) + 1
    else:
        min_num = 6
    print(min_num)
    print(lottos.count(0))
    if lottos.count(0) == 6:
        max_num = min_num - lottos.count(0) + 1
    else:
        max_num = min_num - lottos.count(0)
    
    answer = [max_num, min_num]
            
    return answer
