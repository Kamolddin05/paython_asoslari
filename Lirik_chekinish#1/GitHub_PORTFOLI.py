import random
import curses

def draw_matrix(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    stdscr.nodelay(True)  # foydalanuvchi klavish bosmasdan davom etadi
    stdscr.clear()

    sh, sw = stdscr.getmaxyx()  # oynaning o‘lchami (height, width)
    chars = '01'
    columns = [random.randint(0, sh - 1) for _ in range(sw)]

    while True:
        stdscr.clear()
        for x in range(sw):
            y = columns[x]
            char = random.choice(chars)

            # XATONI OLDINI OLISH: faqatgina ekranda joy bo‘lsa yozadi
            if 0 <= y < sh and 0 <= x < sw:
                try:
                    stdscr.addstr(y, x, char, curses.color_pair(1))
                except curses.error:
                    pass  # xato yuz bersa, davom etadi

            columns[x] = (y + 1) % sh

        stdscr.refresh()
        curses.napms(100)

curses.wrapper(draw_matrix)
 
