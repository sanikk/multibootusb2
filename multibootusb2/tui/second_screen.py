from udev.udev import get_all_block_devices
from tui.third_screen import third_screen
from tui.common_elements import enter_prompt, quit_text, draw_box
import curses


def second_screen(stdscr, height, width):
    options = get_all_block_devices()
    selected = 0
    box_height = max(len(options) + 6, 8)
    box_width = width - 10
    box_y = height // 2 - box_height // 2
    box_x = width // 2 - box_width // 2

    while True:
        stdscr.clear()
        stdscr.box()
        draw_box(stdscr, box_y, box_x, box_height, box_width)

        if not options:
            stdscr.addstr(box_y + 2, box_x + 2, "No devices found.")
            stdscr.addstr(box_y + 4, box_x + 2, enter_prompt)
        else:
            for i, option in enumerate(options):
                device_str = " ".join(option)
                attr = curses.A_REVERSE if i == selected else curses.A_NORMAL
                stdscr.addstr(box_y + 2 + i, box_x + 2, device_str, attr)

        stdscr.addstr(box_y + box_height - 2, box_x + 2, quit_text, curses.A_BOLD)

        stdscr.refresh()
        key = stdscr.getch()

        if key == ord("q") or key == 27:  # 27 is escape
            quit()
        elif not options and key == 10:
            return
        elif options:
            if key == curses.KEY_UP and selected > 0:
                selected -= 1
            elif key == curses.KEY_DOWN and selected < len(options) - 1:
                selected += 1
            elif key == 10:
                third_screen(stdscr, height, width, options[selected])
