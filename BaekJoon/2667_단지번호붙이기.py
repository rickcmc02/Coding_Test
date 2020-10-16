'''
<그림 1>과 같이 정사각형 모양의 지도가 있다. 
1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 
철수는 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 
대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

[입력]
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

[출력]
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.
'''

N = int(input()) # 입력 첫 줄 N 값 가져오기
house = []
for _ in range(N) : # 집 배치도를 2차원 배열로 가져오기
    house.append(list(map(int, str(input()))))
group_num = 0
house_num = 0
house_nums = []

# dfs
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

visited_lst = [[0] * N for _ in range(N)]

def dfs(y, x):
    global house_num
    house_num += 1
    visited_lst[y][x] = 1
    for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]
        if ny in range(0,N) and nx in range(0,N) and house[ny][nx] and not visited_lst[ny][nx] :
            dfs(ny, nx)

for i in range(N) :
    for j in range(N) :
        if house[i][j] and not visited_lst[i][j] :
            group_num += 1
            house_nums.append(house_num)
            house_num = 0
            dfs(i, j)

house_nums.append(house_num)
house_nums = house_nums[1:]
house_nums.sort()

print(group_num)
for num_i in house_nums :
    print(num_i)