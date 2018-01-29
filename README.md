# zhtmlparser (HTML Parser)

Tool Info : zhtmlparser; Version : 3.3; Coded with Python 2.7; Src : https://github.com/pr2h/

[ pr2h ]

Purpose    : This script is designed to parse html and obtain:
	
1) content of a page

2) tags used in the page

3) content with tags
	
4) URLs in a page


NOTE: The comments in the code are detailed and provide an in-depth understanding of the processes being performed

This code can be used as API as well as independent program to parse html, obtain tags (as href), obtain text within tags or obtain URLs from a html code

In addition to specifying the tags, the user can also specify the attributes, seperated by a ',' as given in INPUT EXAMPLE - 2 below.

<b>OUTPUT EXAMPLE:</b>

<b>Input:</b>

    ########## INPUT EXAMPLE - 1 ##########
    
	# html_to_parse is the html input. Alternatively, any input can be provided by reading from a file as well
    
	html_to_parse = '<a href = "https://somerandom1.com">hello</a><a href = "https://somerandom2.com">>><script>newworld</script></a><a href = "something3.com">what!</a><helloworld</script><a "https://">new</a>'
    
	# zhp takes one input, the html to be parsed
    
	parsed_html = zhp(html_to_parse)
    
	# ztag takes <=3 inputs, the html input, the tag to be extracted and the number of tags to extract
    
	tag = ztag(html_to_parse,'a href',0)
    
	# ztagtext takes <=3 inputs, the html input, the tag (within which lies the text to be extracted) and the number of such texts to extract
    
	tagtext = ztagtext(html_to_parse,'a href',0)
    
	# urls takes <=2 inputs, the html input and number of tags to be extracted
    
	links = urls(html_to_parse,0)
        
    
	# Printing Output
    
	print '\n\nHTML Input  : ',html_to_parse
    
	print '\n\nParsed HTML : ',parsed_html
    
	print 'Tags : ',tag
    
	print 'Text withing Tag : ',tagtext
    
	print 'Extracted URLs : ',links

	
    ########## INPUT EXAMPLE - 2 (attributes example) ##########
    
	# html_to_parse is the html input. Alternatively, any input can be provided by reading from a file as well
	
	html_to_parse = '<span class = "helloworld">1</span><span>2</span><span = 1 class=2>3</span><span = 3 class=2>4</span>'
    
	# zhp takes one input, the html to be parsed
    
	parsed_html = zhp(html_to_parse)
    
	# ztag takes <=3 inputs, the html input, the tag to be extracted and the number of tags to extract

    tag = ztag(html_to_parse,'span,class',0)

    # ztagtext takes <=3 inputs, the html input, the tag (within which lies the text to be extracted) and the number of such texts to extract

    tagtext = ztagtext(html_to_parse,'span,class',0)

    # urls takes <=2 inputs, the html input and number of tags to be extracted

    links = urls(html_to_parse,0)

	
    # Printing Output

    print '\n\nHTML Input  : ',html_to_parse

    print '\n\nParsed HTML : ',parsed_html

    print 'Tags : ',tag

    print 'Text withing Tag : ',tagtext

    print 'Extracted URLs : ',links


	
<b>Output:</b>

	########## OUTPUT EXAMPLE - 1 ##########


	HTML Input  :  <a href = "https://somerandom1.com">hello</a><a href = "https://somerandom2.com">>><script>newworld</script></a><a href = "something3.com">what!</a><helloworld</script><a "https://">new</a>


	Parsed HTML :  hello>>newworldwhat!<helloworldnew
	
	Tags :  ['<a href = "https://somerandom1.com">', '<a href = "https://somerandom2.com">', '<a href = "something3.com">']
	
	Text withing Tag :  ['hello', '>>newworld', 'what!']
	
	Extracted URLs :  ['https://somerandom1.com', 'https://somerandom2.com', 'something3.com']


	
	########## OUTPUT EXAMPLE - 2 (attributes example) ##########


	HTML Input  :  <span class = "helloworld">1</span><span>2</span><span = 1 class=2>3</span><span = 3 class=2>4</span>


	Parsed HTML :  1234
	
	Tags :  ['<span class = "helloworld">', '<span = 1 class=2>', '<span = 3 class=2>']
	
	Text withing Tag :  ['1', '3', '4']
	
	Extracted URLs :  []



This project is licensed under the terms of the MIT license.
