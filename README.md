# zhtmlparser (HTML Parser)

Tool Info : zhtmlparser; Version : 2.1; Coded with Python 2.7; Src : https://github.com/pr2h/

[ pr2h ]

Purpose    : This script is designed to parse html and obtain:
	1) content of a page
	2) tags used in the page
	3) content with tags

OUTPUT EXAMPLE:

Commands used:
	html_to_parse = '<script sometag>22<span>22</span></script><span>hi<script>hiii</script><script>333</script>das</span>'
	parsed_html,tag_out,text_within_tag=zhp(html_to_parse,'script','script')

Output:

HTML TO PARSE: 
<script sometag>22<span>22</span></script><span>hi<script>hiii</script><script>333</script>das</span>

PARSED HTML: 
2222hihiii333das

TAG_OUT: 
<script sometag>
<script>
<script>

TEXT WITHIN TAG: 
22<span>22</span>
hiii
333
	
USAGE AS API EXAMPLE:

Scenario 1: Using zhtmlparser in your code

1) Place the file zhtmlparser in the same folder as your python code.

2) Import the function 'zhp' from 'zhtmlparser' in your python code.
e.g.
	from zhtmlparser import zhp

3) Use the function in your code to obtain the parsed text.
e.g.
	parsed_html,tag_out,text_within_tag=zhp(htmlfile)
	
or

	print zhp(htmlfile) #will print a tuple consisting of 3 entries parsed_html, tag_out and text_within_tag

Scenario 2: Directly parse html with zhtmlparser and obtain output

1) Open the file 'zhtmlparser.py' and change the line:
	html_to_parse = '<a href="somewebsite1233">22<span>22</span></a><span>hi<a href="hi">hiii</a><a href>333</a>das</span>'
to
	html_to_parse = '<yourinput>'

where <yourinput> is your input

This project is licensed under the terms of the MIT license.