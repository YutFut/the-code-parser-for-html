import pyperclip


def parser(a):
    return a.replace('&nbsp;', '') \
        .replace('<br>', '') \
        .replace('</p>', '') \
        .replace('<p>', '') \
        .replace('&lt;', '<') \
        .replace('&gt;', '>') \
        .replace('<pre>', '') \
        .replace('</pre>', '') \
        .replace('&amp;', '&')
#       .replace('&amp;', '&')

if __name__ == '__main__':
    while True:
        input()
        a = pyperclip.paste()
        b = parser(a)
        pyperclip.copy(b)
        print(b)
