from tui.tui import start_tui
import curses

if __name__ == "__main__":
    curses.wrapper(start_tui)
