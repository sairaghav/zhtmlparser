# zhtmlparser (HTML Parser)

Tool Info : zhtmlparser; Version : 2.0; Coded with Python 2.7; Src : https://github.com/pr2h/

[ pr2h ]

Purpose    : This script is designed to parse html and obtain the content of a page

USAGE EXAMPLE:

Scenario 1: Using zhtmlparser in your code

1) Place the file zhtmlparser in the same folder as your python code.

2) Import the function 'zhp' from 'zhtmlparser' in your python code.
e.g.
	from zhtmlparser import zhp

3) Use the function in your code to obtain the parsed text.
e.g.
	zhp(htmlfile)


Scenario 2: Directly parse html with zhtmlparser and obtain output

1) Open the file 'zhtmlparser.py' and change the line:
	print zhp('<class id=<abc>>>helloworld<</class>')
to
	print zhp(htmltobeparsed)

where htmltobeparsed is your input

This project is licensed under the terms of the MIT license.
