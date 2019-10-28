l = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    block[(i // 3) * 3 + j // 3].remove(val)
                else:
                    empty.append((i, j))

        def backtrack(iter=0):
            if iter == len(empty):  # 处理完empty代表找到了答案
                return True
            i, j = empty[iter]
            b = (i // 3) * 3 + j // 3
            for val in row[i] & col[j] & block[b]:  # row、col、block中均有val可用
                row[i].remove(val)
                col[j].remove(val)
                block[b].remove(val)
                board[i][j] = str(val)
                if backtrack(iter + 1):
                    return True
                row[i].add(val)  # 回溯
                col[j].add(val)
                block[b].add(val)
            return False

        backtrack()