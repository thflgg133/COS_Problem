def solution(arr, K):
    list2 = []
    list3 = []
    arr.sort()
    if len(arr) >= 5 and len(arr) <= 1000 and min(arr) >= 1 and max(arr) < 10000 and K>= 4 and K <= 50:
        for i in range(len(arr)):
            list2.append(arr[i:K+i])
            if K+i == len(arr):
                break

        for i in range(len(list2)):
            list3.append(list2[i][-1] - list2[i][0])
        list3.sort()
    return list3[0]




# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [9, 11, 9, 6, 4, 19]
K = 4
ret = solution(arr, K)
print("solution 함수의 반환 값은", ret, "입니다.")