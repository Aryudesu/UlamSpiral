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


def make_data(hw, primes):
    """画面描画用データ作成"""
    result = [[None for _ in range(hw + 2)] for _ in range(hw + 2)]
    # 周囲をFalseで囲む
    for idx in range(hw + 2):
        result[0][idx] = result[hw+1][idx] = False
        result[idx][0] = result[idx][hw + 1] = False
    x, y = 1, hw
    dx, dy = 0, -1
    # 外周から値を埋めていく
    for count in range(hw * hw, 0, -1):
        result[y][x] = count in primes
        if result[y + dy][x + dx] is not None:
            if abs(dy) == 1:
                dx = -dy
                dy = 0
            elif abs(dx) == 1:
                dy = dx
                dx = 0
        x += dx
        y += dy
    return result


def main(N):
    """本体"""
    hw = N * 2 + 1
    cell_size = 4
    primes = calc_prime(hw * hw)
    data = make_data(hw, primes)
    win = tk.make_window(hw+2, cell_size)
    tk.draw(win, data, hw, cell_size)
    win.mainloop()


main(100)
