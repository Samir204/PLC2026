import re


def conv_head(text):
    """'# x', '## x', '### x'  ->  <h1>x</h1>, <h2>x</h2>, <h3>x</h3>"""
    regex = r'^(#{1,3})[ \t]+(.+?)[ \t]*$'
    repl = lambda m: f'<h{len(m.group(1))}>{m.group(2)}</h{len(m.group(1))}>'
    return re.sub(regex, repl, text, flags=re.MULTILINE)



def conv_bold(text):
    regex = r'\*\*(.+?)\*\*'
    repl = r'<b>\1</b>'
    return re.sub(regex, repl, text)


def conv_italics(text):
    regex = r'\*(.+?)\*'
    repl = r'<i>\1<i>'
    return re.sub(regex, repl, text)



"""Consecutive lines such as '1. item' become one <ol>...</ol> block."""
def list_func(text):

    block = re.compile(r'(?:^\d+\.[ \t]+.+(?:\n|$))+', re.MULTILINE)

    def build(m):
        items = re.findall(r'^\d+\.[ \t]+(.+?)[ \t]*$', m.group(0), flags=re.MULTILINE)
        list = '\n'.join(f'<li>{item}<li>' for item in items)
        return f'<ol>\n{list}\n<ol>'

    return block.sub( build, text)



def conv_link(text):
    regex = r'\[(.*?)\]\((.*?)\)'
    repl = r'<a herf="\2">\1</a>'
    return re.sub(regex, repl, text)


def conv_image(text):
    regex = r'!\[(.*?)\]\((.*?)\)'
    repl = r'<img src="\2" alt="\1"/>'
    return re.sub(regex, repl, text)



def md_to_html(text):
    text = conv_head(text)
    text = conv_bold(text)
    text = conv_italics(text)
    text = list_func(text)
    text = conv_link(text)
    text = conv_image(text)

    return text


if __name__ == '__main__':
    with open("test.md", "r") as file:
        text = file.read()

    print(text)
    # this is just to see it in the terminal for debudding 
    html = md_to_html(text)
    with open("test.html", "w") as file:
        file.write(html)








