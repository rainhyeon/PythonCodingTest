def solution(s):
    answer = []
    count = 0
    remove_count = 0
    
    while s != "1":
        first_s = s
        s = s.split("0")    
        gether_num = "".join(s)
        len_num = len(gether_num)
        remove_count += (len(first_s) - len(gether_num))
        s = str(bin(len_num))
        s = int(s[2:])
        s = str(s)
        count += 1
        
    answer.append(count)
    answer.append(remove_count)
    
    return answer