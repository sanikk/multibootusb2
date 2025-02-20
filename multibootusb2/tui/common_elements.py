enter_prompt = "Press Enter to continue"
quit_text = "press [Q] to Quit"


def draw_box(stdscr, y, x, height, width):
    stdscr.addstr(y, x, "+" + "-" * (width - 2) + "+")
    for i in range(1, height - 1):
        stdscr.addstr(y + i, x, "|")
        stdscr.addstr(y + i, x + width - 1, "|")
    stdscr.addstr(y + height - 1, x, "+" + "-" * (width - 2) + "+")
    pass
