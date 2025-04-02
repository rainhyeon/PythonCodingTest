def solution(wallpaper):
    answer = [] * 4
    x = len(wallpaper)
    y = len(wallpaper[0])
    print(f'x: {x}, y: {y}')
    min_list = []
    for i in range(x):
        for j in range(y):
            #print(wallpaper[i][j])
            if wallpaper[i][j] == '#':
                min_list.append((i, j))
        
    print(min_list)
    # #이 나타내는 배열의 위치를 list에 저장하고 
    # [(1, 5), (2, 6), (2, 7), (3, 3), (3, 4), (4, 4)]
    # x의 최솟값: 1
    # x의 최대값: 4 + 1
    # y의 최솟값: 3
    # y의 최댓값: 7 + 1
    # [1,3,5,8]
    list_x = [i for i,j in min_list]
    list_y = [j for i,j in min_list]
    
    min_x = min(list_x)
    min_y = min(list_y)
    max_x = max(list_x) + 1
    max_y = max(list_y) + 1
    
    answer = [min_x, min_y, max_x, max_y]
    return answer