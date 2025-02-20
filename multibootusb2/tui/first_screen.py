from tui.common_elements import enter_prompt
import curses


def first_screen(stdscr, height, width):
    title = "MultiBootUSB"

    stdscr.addstr(height // 2 - 1, (width - len(title)) // 2, title, curses.A_BOLD)
    stdscr.addstr(height // 2 + 1, (width - len(enter_prompt)) // 2, enter_prompt)
    stdscr.refresh()

    while True:
        key = stdscr.getch()
        if key == 10:
            return
