projects = {
    "libft": {
        "malloc": "stdlib.h",
        "free": "stdlib.h",
        "write": "unistd.h",
    },
    "get_next_line": {
        "malloc": "stdlib.h",
        "free": "stdlib.h",
        "read": "unistd.h",
    },
    "ft_printf": {
        "malloc": "stdlib.h",
        "free": "stdlib.h",
        "write": "unistd.h",
        "va_start": "stdarg.h",
        "va_arg": "stdarg.h",
        "va_copy": "stdarg.h",
        "va_end": "stdarg.h",
    },
    "minishell": {
        "readline": "readline.h",
        "rl_clear_history": "readline.h",
        "rl_on_new_line": "readline.h",
        "rl_replace_line": "readline.h",
        "rl_redisplay": "readline.h",
        "add_history": "readline.h",

        "printf": "stdio.h",
        "malloc": "stdlib.h",
        "free": "stdlib.h",

        "write": "unistd.h",
        "access": "unistd.h",
        "open": "fcntl.h",
        "read": "unistd.h",
        "close": "unistd.h",

        "fork": "unistd.h",
        "wait": "sys/wait.h",
        "waitpid": "sys/wait.h",
        "wait3": "sys/wait.h",
        "wait4": "sys/wait.h",

        "signal": "signal.h",
        "sigaction": "signal.h",
        "sigemptyset": "signal.h",
        "sigaddset": "signal.h",
        "kill": "signal.h",

        "exit": "stdlib.h",

        "getcwd": "unistd.h",
        "chdir": "unistd.h",

        "stat": "sys/stat.h",
        "lstat": "sys/stat.h",
        "fstat": "sys/stat.h",
        "unlink": "unistd.h",

        "execve": "unistd.h",
        "dup": "unistd.h",
        "dup2": "unistd.h",
        "pipe": "unistd.h",

        "opendir": "dirent.h",
        "readdir": "dirent.h",
        "closedir": "dirent.h",

        "strerror": "string.h",
        "perror": "stdio.h",

        "isatty": "unistd.h",
        "ttyname": "unistd.h",
        "ttyslot": "unistd.h",
        "ioctl": "sys/ioctl.h",

        "getenv": "stdlib.h",

        "tcsetattr": "termios.h",
        "tcgetattr": "termios.h",
        "tgetent": "curses.h term.h",
        "tgetflag": "curses.h term.h",
        "tgetnum": "curses.h term.h",
        "tgetstr": "curses.h term.h",
        "tgoto": "curses.h term.h",
        "tputs": "curses.h term.h",
    },
}
