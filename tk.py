import tkinter as tk


def make_window(HW, m=2):
    result = tk.Tk()
    result.title(u"Ulam Spiral")
    result.geometry(f"{HW*m}x{HW*m}")
    return result


def draw(win, data, HW, m):
    cv = tk.Canvas(win, bg="white")
    cv.pack(fill=tk.BOTH, expand=True)
    for i_y in range(HW + 2):
        for i_x in range(HW + 2):
            if data[i_y][i_x]:
                cv.create_rectangle(
                    i_x * m, i_y * m, (i_x + 1) * m, (i_y + 1) * m, fill="#000000")
