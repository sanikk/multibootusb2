from udev.udev import get_all_block_devices
import curses


def second_screen(stdscr, height, width):
    options = get_all_block_devices()
    selected = 0

    while True:
        stdscr.clear()
        for i, option in enumerate(options):
            if i == selected:
                stdscr.addstr(
                    height // 2 + i,
                    (width - len(option)) // 2,
                    option,
                    curses.A_REVERSE,
                )
            else:
                stdscr.addstr(height // 2 + i, (width - len(option)) // 2, option)

        stdscr.refresh()

        key = stdscr.getch()
        if key == curses.KEY_UP and selected > 0:
            selected -= 1
        elif key == curses.KEY_DOWN and selected < len(options) - 1:
            selected += 1
        elif key == 10:
            return options[selected]
