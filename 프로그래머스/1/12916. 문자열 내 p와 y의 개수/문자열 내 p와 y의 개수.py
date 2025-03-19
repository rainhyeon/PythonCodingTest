def solution(s):
    answer = True
    p_count = 0
    y_count = 0
    
    # sort를 해야함
    s = s.lower()
    
    for i in s:
        if i == 'p':
            p_count += 1
        elif i == 'y':
            y_count += 1
    print(f'p: {p_count}개, y: {y_count}개')
    
    
    if p_count == y_count:
        return True
    else:
        return False
