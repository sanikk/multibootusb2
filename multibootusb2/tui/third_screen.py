def third_screen(stdscr, height, width, selected):
    stdscr.clear()
    stdscr.addstr(height // 2, (width - 20) // 2, f"You selected: {selected}")
    stdscr.refresh()
    stdscr.getch()  # Wait for final key press
