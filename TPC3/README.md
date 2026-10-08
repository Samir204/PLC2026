# TPC3: Lexical Analyser

## Author

- **Name:** Samir Mansour
- **Student ID:** `A105856`
![image alt](https://github.com/Samir204/PLC2026/blob/b3e55188b2e1ea4fe75a52dcd04147db13e16fbc/image/IMG_4084.png)



## Summary

- For this TPC I wrote a lexical analyser in Python for a small SPARQL-like query language, like the DBPedia example in the assignment. It reads a query and prints its tokens one per line. Whitespace and comments are skipped.

- The tokens are: `var` (`?nome`), `lan` (`@en`), `string` (`"Chuck Berry"`), `decimal or delim` (`{`, `}` and `.`), `number` (`1000`), `reserved` (only `LIMIT`) and `concept` for every other sequence of alphanumerics. Comments start with `#` and go to the end of the line, and they produce no token.

- It is done with one big regular expression made of named groups, one per token type, separated by `|`. I go through the text with `re.finditer()` and use `m.lastgroup` to know which group matched, which is the token type. The order of the groups matters because the first one that matches wins: `number` goes before the generic word rule (otherwise every number would be a concept), and a catch all `error` rule goes last.

- The example in the assignment has concepts like `dbo:MusicalArtist` and `foaf:name`, with a colon, even though the text only says alphanumerics. So a concept is some word characters, optionally followed by `:` and more word characters. `NUMBER` ends with `\b` so that something like `12ab` stays one concept instead of being split in two.

- `LIMIT` does not have its own regex. The generic word rule matches first, and then I check if the word is in a list of reserved words. This way `LIMITED` is still a normal concept, and adding more reserved words is easy. Following the assignment literally, `select` and `where` come out as concepts.

- Characters that fit no rule are printed as `error` with the line where they appear, and the lexer keeps going instead of stopping at the first problem.

- The input can come from a file (`python3 lexer.py example.query`), from a pipe (`cat example.query | python3 lexer.py`) as talk about in class, or typed directly in the terminal, finishing with Ctrl-D.


## List of results

- [tpc3.py](lexer.py): the lexical analyser, my solution
- [example.query](example.query): the query from the assignment
- [errors.query](errors.query): a query with a few deliberate mistakes, to check the error messages
