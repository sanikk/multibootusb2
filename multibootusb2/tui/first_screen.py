import curses


def first_screen(stdscr, height, width):
    title = "MultiBootUSB"
    prompt = "Press Enter to continue"

    stdscr.addstr(height // 2 - 1, (width - len(title)) // 2, title, curses.A_BOLD)
    stdscr.addstr(height // 2 + 1, (width - len(prompt)) // 2, prompt)
    stdscr.refresh()

    while True:
        key = stdscr.getch()
        if key == 10:
            return
