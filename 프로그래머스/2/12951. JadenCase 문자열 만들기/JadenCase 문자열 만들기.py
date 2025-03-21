def solution(s):
    answer = ''
    
    list_ans = s.split(" ")
    new_list = []
    
    for i in list_ans:
        if i.isalnum():
            anwer = i[0].upper() + i[1:].lower()
            new_list.append(anwer)
        else:
            anwer = i
            new_list.append(anwer)
        
    return " ".join(new_list)