board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
save = []
answer = 0

for i in range(0, len(moves)):
    cnt = 0
    full_chk = False

    while board[cnt][moves[i]-1] == 0:
        if cnt + 1 == len(board[0]):
            full_chk = True
            break
        cnt += 1

    if full_chk == False:
        save.append(board[cnt][moves[i]-1])
        board[cnt][moves[i]-1] = 0

        while len(save)>1 and save[-1] == save[-2]:
            del(save[-2:])
            answer += 2
print(answer)