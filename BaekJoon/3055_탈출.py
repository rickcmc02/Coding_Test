'''
사악한 암흑의 군주 이민혁은 드디어 마법 구슬을 손에 넣었고, 그 능력을 실험해보기 위해 근처의 티떱숲에 홍수를 일으키려고 한다. 이 숲에는 고슴도치가 한 마리 살고 있다. 고슴도치는 제일 친한 친구인 비버의 굴로 가능한 빨리 도망가 홍수를 피하려고 한다.

티떱숲의 지도는 R행 C열로 이루어져 있다. 비어있는 곳은 '.'로 표시되어 있고, 물이 차있는 지역은 '*', 돌은 'X'로 표시되어 있다. 비버의 굴은 'D'로, 고슴도치의 위치는 'S'로 나타내어져 있다.

매 분마다 고슴도치는 현재 있는 칸과 인접한 네 칸 중 하나로 이동할 수 있다. (위, 아래, 오른쪽, 왼쪽) 물도 매 분마다 비어있는 칸으로 확장한다. 물이 있는 칸과 인접해있는 비어있는 칸(적어도 한 변을 공유)은 물이 차게 된다. 물과 고슴도치는 돌을 통과할 수 없다. 또, 고슴도치는 물로 차있는 구역으로 이동할 수 없고, 물도 비버의 소굴로 이동할 수 없다.

티떱숲의 지도가 주어졌을 때, 고슴도치가 안전하게 비버의 굴로 이동하기 위해 필요한 최소 시간을 구하는 프로그램을 작성하시오.

고슴도치는 물이 찰 예정인 칸으로 이동할 수 없다. 즉, 다음 시간에 물이 찰 예정인 칸으로 고슴도치는 이동할 수 없다. 이동할 수 있으면 고슴도치가 물에 빠지기 때문이다. 

입력
첫째 줄에 50보다 작거나 같은 자연수 R과 C가 주어진다.

다음 R개 줄에는 티떱숲의 지도가 주어지며, 문제에서 설명한 문자만 주어진다. 'D'와 'S'는 하나씩만 주어진다.

출력
첫째 줄에 고슴도치가 비버의 굴로 이동할 수 있는 가장 빠른 시간을 출력한다. 만약, 안전하게 비버의 굴로 이동할 수 없다면, "KAKTUS"를 출력한다.
'''
# underdevelop
# bfs
from collections import deque
r, c = list(input.split(' '))
rmap = [list(input()) for _ in range(r)]
h_trace = [[0] * c for _ in range(r)]
w_trace = [[0] * c for _ in range(r)]

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]
dq_hedge = deque()
dq_water = deque()

loc_hedge = []
loc_water = []
loc_cave = []

for r_i, c_i in enumerate(rmap) :
    if 'S' in c_i :
        loc_hedge = [r_i, c_i.index('S')]
    if 'D' in c_i :
        loc_cave = [r_i, ]


def bfs(y, x):
    dq.

# bfs
for i in range(v) :
    for j in range(h) :
        if not visited[i][j] :
            bfs(i,j)


def bfs(y, x):
    dq.append([y, x])
    visited[y][x] = 1
    
    while dq :
        pos = dq.popleft()

        for i in range(4) :
            ny = pos[0] + dy[i]
            nx = pos[1] + dx[i]
            if 0 <= ny < v and 0 <= nx < h and maze[ny][nx] and not visited[ny][nx] :
                maze[ny][nx] = maze[pos[0]][pos[1]] + 1
                visited[ny][nx] = 1
                dq.append([ny, nx])

print(maze[-1][-1])