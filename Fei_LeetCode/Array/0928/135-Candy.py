def candy(ratings):
    n = len(ratings)
    sum = 1
    down = up = peak = 1
    for i in range(1, n):
        if ratings[i-1] < ratings[i]:
            up += 1
            down = 1
            peak = up
            sum += up
        elif ratings[i-1] == ratings[i]:
            peak = up = down = 1
            sum += 1
        else:
            up = 1
            sum += down
            if peak <= down:
                sum += 1
            down += 1
    return sum


if __name__ == '__main__':
    print(candy([4, 2, 3, 1, 0, 2, 2]))
