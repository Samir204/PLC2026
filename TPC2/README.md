# TPC2: Markdown to HTML Converter

## Author

- **Name:** Samir Mansour
- **Student ID:** A105856
![image alt](https://github.com/Samir204/PLC2026/blob/b3e55188b2e1ea4fe75a52dcd04147db13e16fbc/image/IMG_4084.png)

## Summary

- For this TPC I wrote a small Markdown to HTML converter in Python. It handles headings (`#`, `##`, `###`), bold, italic, numbered lists, links and images. All of it is done with regular expressions, mostly with `re.sub()`.

- I split the work into one small function per element (`convert_headers`, `convert_lists`, `convert_bold`, `convert_italic`, `convert_images`, `convert_links`), and `md_to_html()` just calls them one after the other. That way each regex can be tested on its own, which made it much easier to see which one was wrong when something didn't match.

- The order the functions run in matters. Headings and lists go first, so that bold, italic and links still work inside them. Bold has to go before italic: `**` starts with `*`, so if italic runs first it takes one star from each `**` and breaks the bold. Images go before links, because an image is just a link with a `!` in front, and if links run first that `!` gets left behind.

- For headings I used `^(#{1,3})[ \t]+(.+?)[ \t]*$` with `re.MULTILINE`, so that `^` and `$` work on every line and not just at the start and end of the whole text. The number of `#` gives the heading level. Since the tag name depends on that number, I passed a function to `re.sub()` instead of a plain replacement string.

- Numbered lists were the trickiest part, because all the items have to end up inside a single `<ol>`. First, one regex finds a whole block of consecutive lines like `1. text`. Then a function takes that block, pulls out the item texts with `re.findall()` and builds the `<li>` lines. The original numbers are thrown away, since HTML numbers the items on its own.

- For bold, italic, links and images I used the non-greedy `.+?` and `.*?`. With the greedy version, two bold pieces on the same line get merged into one big match. Links and images reuse the captured groups in the replacement, and for images they come out in a different order from the input: `<img src="\2" alt="\1"/>`.

- It works on all the examples from the assignment, but it is not a full Markdown parser. There are no paragraphs, no unordered lists, no code, and `<`, `>` and `&` are not escaped. A lone `*` in something like `2 * 3 * 4` also gets turned into italic. Headings stop at level 3, as the assignment asks.

- To run it: `python3 md2html.py test.md > test.html`. It reads the file you give it, or standard input if you don't give one, and prints the HTML to the terminal.

## List of results

- [md2html.py](md2html.py): the converter, my solution
- [test.md](test.md): an example input that uses every element
- [test.html](test.html): the HTML generated from `test.md`
