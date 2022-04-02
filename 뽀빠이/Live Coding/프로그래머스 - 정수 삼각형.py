def solution(triangle):

    for i, v1 in enumerate(triangle):
        if i >= 1:
            for j, v2 in enumerate(v1):
                if j == 0:
                    triangle[i][j] = v2 + triangle[i-1][0]
                elif j == (len(v1)-1):
                    triangle[i][j] = v2 + triangle[i-1][-1]
                else:
                    if v2 + triangle[i-1][j-1] >= v2 + triangle[i-1][j]:
                        triangle[i][j] = v2 + triangle[i-1][j-1]
                    else:
                        triangle[i][j] = v2 + triangle[i-1][j]
    print(triangle)
    answer = max(triangle[-1])
    return answer
