# BOJ 13460 "구슬 탈출 2" (일명 구슬치기2) 풀이
# - BFS로 10번 이내의 최소 이동 횟수를 탐색
# - 상태 = (빨간 구슬 위치 ry, rx, 파란 구슬 위치 by, bx, 이동 횟수 count)
# - 한 방향으로 기울일 때 두 구슬을 각각 '벽(#)이나 구멍(O) 전까지' 미끄러뜨림
# - 같은 칸에 겹치면 더 멀리 이동한 쪽을 한 칸 되돌림
# - 정답 조건: 빨강만 O에 빠지고 파랑은 빠지지 않았을 때의 count (<= 10), 아니면 -1

import sys
from collections import deque

DY = (-1, 1, 0, 0)
DX = (0, 0, -1, 1)

def dfs(board, n, m, ry, rx, by, bx):
    """
    board: 보드(문자 2차원 리스트)
    n,m: 보드 크기
    (ry, rx): 빨간 구슬 시작 위치
    (by, bx): 파란 구슬 시작 위치
    반환값: 10번 이내로 빨간 구슬만 구멍에 빠뜨릴 수 있다면 최소 이동횟수, 아니면 -1
    """

    # visited[ry][rx][by][bx] = True면 해당 네 좌표 조합을 이미 방문
    # 최대 10x10 보드이므로 4차원 배열을 써도 메모리 충분
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

    q = deque()
    q.append((ry, rx, by, bx, 0)) # 0: 현재까지의 이동 횟수
    visited[ry][rx][by][bx] = True

    while q:
        cry, crx, cby, cbx, cnt = q.popleft()

        # BFS 특성상 cnt가 증가하는 순으로 나오므로.
        # 10을 초과하면 더 볼 필요가 없이 종료
        if cnt > 10:
            break

        # 성공조건: 빨강은 구멍, 파랑은 구멍이 없을 때
        if board[cry][crx] == 'O' and board[cby][cbx] != 'O':
            return cnt
        
        # 4가지 방향으로 탐색
        for d in range(4):
            nry, nrx = cry, crx
            nby, nbx = cby, cbx

            # 1) 빨간 구슬 굴리기:
            # 벽(#)이나 구멍(O)를  만나기 전까지 전진
            # 만약 벽에서 멈출경우, 벽 위가 아니라 '벽 직전 칸'에 서도록 한 칸 되돌림
            while True:
                if board[nry][nrx] != "#" and board[nry][nrx] != "O":
                    nry += DY[d]
                    nrx += DX[d]
                else:
                    if board[nry][nrx] == "#":
                        nry -= DY[d]
                        nrx -= DX[d]
                    break
            # 2) 파란 구슬 굴리기: 위와 동일 로직
            while True:
                if board[nby][nbx] != "#" and board[nby][nbx] != "O":
                    nby += DY[d]
                    nbx += DX[d]
                else:
                    if board[nby][nbx] == "#":
                        nby -= DY[d]
                        nbx -= DX[d]
                    break

            # 3) 두 구슬이 같은 칸에 멈췄다면(구멍 제외)
            # 더 멀리 이동한 구슬을 한칸 뒤로 (먼저 도착한/앞에 있던 구슬이 앞자리를 차지하게 함)
            if nry == nby and nrx == nbx:
                if board[nry][nrx] != "O":
                    red_dist = abs(nry - cry) + abs(nrx - crx)
                    blue_dist = abs(nby - cby) + abs(nbx - cbx)
                    if red_dist > blue_dist:
                        nry -= DY[d]
                        nrx -= DX[d]
                    else:
                        nby -= DY[d]
                        nbx -= DX[d]

            if not visited[nry][nrx][nby][nbx]:
                visited[nry][nrx][nby][nbx] = True
                q.append((nry, nrx, nby, nbx, cnt+1))

    return -1


def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    board = [list(input().strip()) for _ in range(n)]

    # 시작 좌표
    ry = rx = by = bx = -1
    for y in range(n):
        for x in range(m):
            if board[y][x] == "R":
                ry, rx = y, x
            elif board[y][x] == "B":
                by, bx = y, x

    # 참고: board 상의 "R", "B"를 "." 으로 바꿔도 되지만,
    # 위 이동 로직은 "#","O"만 특별 취급하므로 굳이 바꾸지 않아도 동작함
    # (R/B는 그냥 빈칸처럼 취급함)

    ans = dfs(board, n, m, ry, rx, by, bx)
    print(ans)

if __name__ == "__main__":
    main()