import time
'''
print log with unicode mode
'''

COLOR_END = '\033[0m'
COLOR_END_UN = '\033[4m'
COLORS = {'fg_black': '\033[30m',\
    'fg_red': '\033[31m',\
    'fg_green': '\033[32m',\
    'fg_yellow': '\033[33m',\
    'fg_blue': '\033[34m',\
    'fg_purple': '\033[35m',\
    'fg_cyan': '\033[36m',\
    'fg_white': '\033[37m',\
    'bg_black': '\033[40m',\
    'bg_red': '\033[41m',\
    'bg_green': '\033[42m',\
    'bg_yellow': '\033[43m',\
    'bg_blue': '\033[44m',\
    'bg_purple': '\033[45m',\
    'bg_cyan': '\033[46m',\
    'bg_white': '\033[47m'}

def reg_chi_code(msg):
    if (None == msg):
        return ''
    try:
        msg = str(msg).decode('utf-8')
    except UnicodeEncodeError:
        # it's already an unicode string.
        pass
    return msg

def create_time_tag():
    time_str = time.ctime()
    time_str = time_str[4: (len(time_str) - 5)]
    time_str = '[' + time_str + '] '
    return time_str

def normal(msg, time_tag=False, only_get=False):
    msg = reg_chi_code(msg)
    if (time_tag):
        msg = create_time_tag() + msg
    msg = u'\u261b ' + msg
    if (only_get):
        return msg
    print(msg)

def info(msg, time_tag=False, only_get=False):
    msg = reg_chi_code(msg)
    if (time_tag):
        msg = create_time_tag() + msg
    msg = COLORS['fg_white'] + COLORS['bg_blue'] + u'\u2618 ' + msg + COLOR_END
    if (only_get):
        return msg
    print(msg)

def warn(msg, time_tag=False, only_get=False):
    msg = reg_chi_code(msg)
    if (time_tag):
        msg = create_time_tag() + msg
    msg = COLORS['fg_black'] + COLORS['bg_yellow'] + u'\u267b ' + msg + COLOR_END
    if (only_get):
        return msg
    print(msg)

def error(msg, time_tag=False, only_get=False):
    msg = reg_chi_code(msg)
    if (time_tag):
        msg = create_time_tag() + msg
    msg = COLORS['fg_white'] + COLORS['bg_red'] + u'\u2689 ' + msg + COLOR_END
    if (only_get):
        return msg
    print(msg)

# normal('beautiful log')
# info('beautiful log')
# warn('beautiful log')
# error('beautiful log')
