# zhtmlparser (HTML Parser)

Tool Info : zhtmlparser; Version : 3.1; Coded with Python 2.7; Src : https://github.com/pr2h/

[ pr2h ]

Purpose    : This script is designed to parse html and obtain:
	
	1) content of a page
	
	2) tags used in the page
	
	3) content with tags
	
	4) URLs in a page

NOTE: The comments in the code are detailed and provide an in-depth understanding of the processes being performed

This code can be used as API as well as independent program to parse html, obtain tags (as href) or obtain text within tags from an html code

OUTPUT EXAMPLE:

Input:

    # html_to_parse is the html input. Alternatively, any input can be provided by reading from a file as well
    
	html_to_parse = '<a href = "https://somerandom1.com">hello</a><a href = "https://somerandom2.com">>><script>newworld</script></a><a href = "something3.com"><helloworld</script>'
    
	# zhp takes one input, the html to be parsed
    
	parsed_html = zhp(html_to_parse)
    
	# ztag takes <=3 inputs, the html input, the tag to be extracted and the number of tags to extract
    
	tag = ztag(html_to_parse,'a href',2)
    
	# ztagtext takes <=3 inputs, the html input, the tag (within which lies the text to be extracted) and the number of such texts to extract
    
	tagtext = ztagtext(html_to_parse,'a href',2)
    
	# urls takes <=2 inputs, the html input and number of tags to be extracted
    
	links = urls(html_to_parse,0)

	
Output:

	HTML Input  :  <a href = "https://somerandom1.com">hello</a><a href = "https://somerandom2.com">>><script>newworld</script></a><a href = "something3.com"><helloworld</script>


	Parsed HTML :  hello>>newworld<helloworld

	Tags :  ['<a href = "https://somerandom1.com">', '<a href = "https://somerandom2.com">']

	Text withing Tag :  ['hello', '>>newworld']

	Extracted URLs :  ['https://somerandom1.com', 'https://somerandom2.com', 'something3.com']



This project is licensed under the terms of the MIT license.