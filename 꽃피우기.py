import copy 
def simulate_day(garden): 
    next_garden = copy.deepcopy(garden) # 복합객체를 새롭게 생성하고 그 안의 내용까지 재귀적으로 새롭게 생성하게 됨
    dir =[[0,1],[0,-1],[1,0],[-1,0]] #방향 설정
    done = True 
    for i in range(0,len(garden)): #garden 리스트길이
        for j in range(0, len(garden[i])): #garden 내부 리스트길이
            if garden[i][j] == 0: #2차원리스트 인덱스 값이 0 일 경우
                done = False #done에 거짓 할당
    if  done: #만약 done이다 == 만약 참이다 
        return True  #참을 리턴값으로 반환

    for i in range(0,len(garden)): # 
        for j in range(0, len(garden[i])):  
            for diff in dir:
                print(diff)
                dx = diff[0] #  0 0 1 -1
                dy = diff[1] #  1 -1 0 0
                if (j + dx) < 0 or (j + dx) >= len(garden[i]): 
                    continue
                if (i + dy) < 0 or (i + dy) >= len(garden):  
                    continue
                if garden[i][j] == 1:
                    print("이때 더하기")
                    next_garden[i + dy][j + dx] = 1
                 
    for i in range(0,len(garden)):
        for j in range(0, len(garden[i])):
            garden[i][j] = next_garden[i][j]
    return False

def solution(garden):
    answer = 0
    while simulate_day(garden) == False:
        answer += 1
    return answer


garden = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(solution(garden))


