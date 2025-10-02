import sys
input = sys.stdin.readline

def rotate(grid):
    return [list(row) for row in zip(*grid[::-1])]

def can_place(board, sticker, sx, sy):
    r, c = len(sticker), len(sticker[0])
    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1 and board[sx+i][sy+j] == 1:
                return False
    return True

def place(board, sticker, sx, sy):
    r, c = len(sticker), len(sticker[0])
    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1:
                board[sx+i][sy+j] = 1


N, M, K = map(int, input().split())
stickers = []
for _ in range(K):
    r, c = map(int, input().split())
    st = [list(map(int, input().split())) for _ in range(r)]
    stickers.append(st)

board = [[0]*M for _ in range(N)]

for st in stickers:
    placed = False
    for _ in range(4):
        r, c = len(st), len(st[0])
        for x in range(N - r + 1):
            if placed: break
            for y in range(M - c + 1):
                if can_place(board, st, x, y):
                    place(board, st, x, y)
                    placed = True
                    break
        if placed:
            break
        st = rotate(st)

print(sum(map(sum, board)))
