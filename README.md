# zhtmlparser (HTML Parser)

Tool Info : zhtmlparser; Version : 2.1; Coded with Python 2.7; Src : https://github.com/pr2h/

[ pr2h ]

Purpose    : This script is designed to parse html and obtain:
	
	1) content of a page
	
	2) tags used in the page
	
	3) content with tags

NOTE: The comments in the code are detailed and provide an in-depth understanding of the processes being performed

This code can be used as API as well as independent program to parse html, obtain tags (as href) or obtain text within tags from an html code

The speciality of this code is that each 'function' can function seperately without dependencies from other functions or global variables.
	
OUTPUT EXAMPLE:

Output:

	HTML Input  :  <a href = "https://somerandom1.com">hello</a><a href = https://somerandom2.com">>><script>newworld</script></a><a href = "something"><helloworld</script>


	Parsed HTML :  hello>>newworld<helloworld

	Tags :  ['<a href = "https://somerandom1.com">', '<a href = https://somerandom2.com">']

	Text withing Tag :  ['hello', '>>newworld']

This project is licensed under the terms of the MIT license.