from tui.first_screen import first_screen
from tui.second_screen import second_screen
import curses


def start_tui(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    first_screen(stdscr, height, width)
    # Second screen: selection menu
    second_screen(stdscr, height, width)
