import tk


def calc_prime(N):
    """素数計算"""
    result = [True] * (N + 1)
    primes = set()
    primes.add(2)
    for i in range(3, N + 1, 2):
        if not result[i]:
            continue
        primes.add(i)
        idx = 3
        while idx * i <= N:
            result[idx * i] = False
            idx += 2
    return primes


def make_data(HW, primes):
    """画面描画用データ作成"""
    result = [[None for _ in range(HW + 2)] for _ in range(HW + 2)]
    # 周囲をFalseで囲む
    for idx in range(HW + 2):
        result[0][idx] = False
        result[HW + 1][idx] = False
        result[idx][0] = False
        result[idx][HW + 1] = False
    tmp = HW * HW
    x = 1
    y = HW
    dx = 0
    dy = -1
    # 外周から値を埋めていく
    while tmp > 0:
        result[y][x] = tmp in primes
        if result[y + dy][x + dx] is not None:
            if dy == -1:
                dy = 0
                dx = 1
            elif dy == 1:
                dy = 0
                dx = -1
            elif dx == -1:
                dy = -1
                dx = 0
            elif dx == 1:
                dy = 1
                dx = 0
        x += dx
        y += dy
        tmp -= 1
    return result


N = 100
HW = N * 2 + 1
m = 4
primes = calc_prime(HW * HW)
data = make_data(HW, primes)
win = tk.make_window(HW+2, m)
tk.draw(win, data, HW, m)
win.mainloop()
