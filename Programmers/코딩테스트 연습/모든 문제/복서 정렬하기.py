'''
문제 설명
복서 선수들의 몸무게 weights와, 복서 선수들의 전적을 나타내는 head2head가 매개변수로 주어집니다. 
복서 선수들의 번호를 다음과 같은 순서로 정렬한 후 return 하도록 solution 함수를 완성해주세요.

전체 승률이 높은 복서의 번호가 앞쪽으로 갑니다. 아직 다른 복서랑 붙어본 적이 없는 복서의 승률은 0%로 취급합니다.
승률이 동일한 복서의 번호들 중에서는 자신보다 몸무게가 무거운 복서를 이긴 횟수가 많은 복서의 번호가 앞쪽으로 갑니다.
자신보다 무거운 복서를 이긴 횟수까지 동일한 복서의 번호들 중에서는 자기 몸무게가 무거운 복서의 번호가 앞쪽으로 갑니다.
자기 몸무게까지 동일한 복서의 번호들 중에서는 작은 번호가 앞쪽으로 갑니다.

제한사항
weights의 길이는 2 이상 1,000 이하입니다.
weights의 모든 값은 45 이상 150 이하의 정수입니다.
weights[i] 는 i+1번 복서의 몸무게(kg)를 의미합니다.
head2head의 길이는 weights의 길이와 같습니다.
head2head의 모든 문자열은 길이가 weights의 길이와 동일하며, 'N', 'W', 'L'로 이루어진 문자열입니다.
head2head[i] 는 i+1번 복서의 전적을 의미하며, head2head[i][j]는 i+1번 복서와 j+1번 복서의 매치 결과를 의미합니다.
'N' (None)은 두 복서가 아직 붙어본 적이 없음을 의미합니다.
'W' (Win)는 i+1번 복서가 j+1번 복서를 이겼음을 의미합니다.
'L' (Lose)는 i+1번 복사가 j+1번 복서에게 졌음을 의미합니다.
임의의 i에 대해서 head2head[i][i] 는 항상 'N'입니다. 자기 자신과 싸울 수는 없기 때문입니다.
임의의 i, j에 대해서 head2head[i][j] = 'W' 이면, head2head[j][i] = 'L'입니다.
임의의 i, j에 대해서 head2head[i][j] = 'L' 이면, head2head[j][i] = 'W'입니다.
임의의 i, j에 대해서 head2head[i][j] = 'N' 이면, head2head[j][i] = 'N'입니다.

입출력 예
weights	        head2head	                  result
[50,82,75,120]	["NLWL","WNLL","LWNW","WWLN"]	  [3,4,1,2]
[145,92,86]	["NLW","WNL","LWN"]	          [2,3,1]
[60,70,60]	["NNN","NNN","NNN"]           	  [2,1,3]

입출력 예 설명

입출력 예 #1
다음은 선수들의 정보를 나타낸 표입니다.
선수 번호	vs 1번	vs 2번	vs 3번	vs 4번	승률	자기보다 무거운 복서를 이긴 횟수	몸무게
1번	-	패배	승리	패배	33.33%	1회	50kg
2번	승리	-	패배	패배	33.33%	0회	82kg
3번	패배	승리	-	승리	66.66%	2회	75kg
4번	승리	승리	패배	-	66.66%	0회	120kg
본문에 서술된 우선순위를 따라 [3,4,1,2] 를 return 합니다.

입출력 예 #2
다음은 선수들의 정보를 나타낸 표입니다.
선수 번호	vs 1번	vs 2번	vs 3번	승률	자기보다 무거운 복서를 이긴 횟수	몸무게
1번	-	패배	승리	50%	0회	145kg
2번	승리	-	패배	50%	1회	92kg
3번	패배	승리	-	50%	1회	86kg
본문에 서술된 우선순위를 따라 [2,3,1] 을 return 합니다.

입출력 예 #3
다음은 선수들의 정보를 나타낸 표입니다.
선수 번호	vs 1번	vs 2번	vs 3번	승률	자기보다 무거운 복서를 이긴 횟수	몸무게
1번	-	-	-	0% (무전적)	0회	60kg
2번	-	-	-	0% (무전적)	0회	70kg
3번	-	-	-	0% (무전적)	0회	60kg
본문에 서술된 우선순위를 따라 [2,1,3] 을 return 합니다.
'''

def solution(weights, head2head):
    answer = []
    count = [0] * len(weights)
    win_count = [0] * len(weights)
    win_rate = [0] * len(weights)
    over_weight = [0] * len(weights)
    result = []
    
    for i in range(len(head2head)):
        for idx, j in enumerate(head2head[i]):
            if j != 'N':                
                count[i] += 1
                if j == 'W':
                    win_count[i] += 1
                    if weights[i] < weights[idx]:
                        over_weight[i] += 1
        if count[i] == 0:
            win_rate[i] = 0
        else:
            win_rate[i] = win_count[i] / (count[i])
        result.append((i+1, win_rate[i], over_weight[i], weights[i]))
    result = sorted(result, key=lambda x: (-x[1], -x[2], -x[3], x[0]))
    answer = [i[0] for i in result]

    return answer

