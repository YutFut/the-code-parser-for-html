def parser():
    a = """

    """.replace('&nbsp;', '')\
        .replace('<br>', '')\
        .replace('</p>', '')\
        .replace('<p>', '')\
        .replace('&lt;', '<')\
        .replace('&gt;', '>') \
        .replace('<pre>', '')\
        .replace('</pre>', '') \
        .replace('&amp;', '&')

    print(a)


if __name__ == '__main__':
    parser()