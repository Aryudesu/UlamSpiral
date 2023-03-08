import tkinter as tk


def make_window(hw, cell_size=2):
    result = tk.Tk()
    result.title(u"Ulam Spiral")
    result.geometry(f"{hw*cell_size}x{hw*cell_size}")
    return result


def draw(win, data, hw, cell_size=2):
    cv = tk.Canvas(win, bg="white")
    cv.pack(fill=tk.BOTH, expand=True)
    for i_y in range(hw + 2):
        for i_x in range(hw + 2):
            if data[i_y][i_x]:
                cv.create_rectangle(
                    i_x * cell_size, i_y * cell_size, (i_x + 1) * cell_size, (i_y + 1) * cell_size, fill="#000000")
