def hujambo():
    print '''
##################################################
# Tool    : zhtmlparser                          #
# Version : 3.3                                  #
# Coded with Python 2.7                          #
# Profile : https://github.com/pr2h/             #
# ######          #####   #                      #
# #    #  # ###  #     #  #                      #
# ######  ##         #    ######                 #
# #       #        #      #    #                 #
# #       #      #######  #    #                 #
##################################################
    '''

def zhp(html):    
    while True:
        # Initializing variables
        html_text = ''

        # Finding the from_position
        from_position=html.find('<')

        # Finding the to_position
        while True:
            to_position=html.find('>',from_position)

            # Checking if there is an extra '<' after from_position
            to_position_temp=html.find('<',from_position+1)

            if to_position_temp != -1 and to_position_temp < to_position:
                from_position=to_position_temp
            else:
                break

        # Extracting the tag from the html
        html_text=html[from_position:to_position+1]
        html=html.replace(html_text,'',1)

        # Checking if extraction is complete
        if html_text=='':
            break

    # Returning the parsed html
    return html


def ztag(html,find_tag='',no_of_tags=0):
    # Initializing the variables
    tags = []
    attributes = []
    iteration = 0
    flag = 1
    flag2 = 1

    # Checking if any input is passed to the function
    # no_of_tags = 0 by default, which means all tags will be extracted
    if no_of_tags == 0:
        # Increasing no_of_tags value to enter the loop
        no_of_tags = 2
        flag = 0

    # Checking if user has mentioned attributes    
    if ',' in find_tag:
        find_tag = find_tag.replace(', ',',') # Clearing off unrequired spaces
        attributes = find_tag.split(',') # Creating a list of attributes

    else:
        attributes.append(find_tag) # Creating a list attributes with a single element
    
    # Performing extraction
    while iteration <= no_of_tags:
        flag2=1
        iteration+=1

        if flag == 0:
            no_of_tags+=1

        # Finding the from_position
        from_position = html.find('<')

        # Finding the to_position
        while True:
            to_position_temp = html.find('<',from_position+1)
            to_position = html.find('>',from_position+1)

            if to_position_temp != -1 and to_position_temp < to_position:
                from_position = to_position_temp

            else:
                break

        # Extracting the tag from the html
        html_text = html[from_position:to_position+1]
        html = html.replace(html_text,'',1)

        # Checking if extraction is complete
        if html_text == '':
            break

        # Ignoring closing tags
        elif '</' in html_text:
            continue

        # Collecting the required extracted tags in a list
        for attribute in attributes:
            if attribute in html_text:
                pass
            else:
                # Signifies attribute is not in html_text
                flag2 = 0

        # Append the tag only if all attributes are in the tag
        if flag2 == 1:
            tags.append(html_text)

    # Returning the tags list
    return tags

def ztagtext(html,find_tag='',no_of_tags=0):
    # Initializing the variables
    text_within_tag = []
    attributes = []
    iteration = 0
    flag = 1
    flag2 = 1

    # Checking if any input is passed to the function
    # no_of_tags = 0 by default, which means all tags will be extracted
    if no_of_tags == 0:
        # Increasing no_of_tags value to enter the loop
        no_of_tags = 2
        flag = 0

    # Checking if user has mentioned attributes    
    if ',' in find_tag:
        find_tag = find_tag.replace(', ',',') # Clearing off unrequired spaces
        attributes = find_tag.split(',') # Creating a list of attributes

    else:
        attributes.append(find_tag) # Creating a list attributes with a single element
    
    # Performing extraction
    while iteration <= no_of_tags:
        flag2=1
        iteration+=1

        if flag == 0:
            no_of_tags+=1

        # Finding the from_position
        from_position = html.find('<')

        # Finding the to_position
        while True:
            to_position_temp = html.find('<',from_position+1)
            to_position = html.find('>',from_position+1)

            if to_position_temp != -1 and to_position_temp < to_position:
                from_position = to_position_temp

            else:
                break

        # Extracting the tag from the html
        html_text = html[from_position:to_position+1]
        html = html.replace(html_text,'',1)

        # Checking if extraction is complete
        if html_text == '':
            break

        # Ignoring closing tags
        elif '</' in html_text:
            continue

        # Checking if all required attributes are present in tag
        for attribute in attributes:
            if attribute in html_text:
                pass
            else:
                # Signifies attribute is not in html_text
                flag2 = 0

        if flag2 == 1:
            # Inferring the closing tag for the supplied tag
            if ' ' in html_text:
                to_position_close_tag=html_text.find(' ',0)
                close_tag = '</'+html_text[1:to_position_close_tag]+'>'
            else:
                close_tag = html_text[:1]+'/'+html_text[1:]

            to_position_close_tag = html.find(close_tag)

            # Collecting the required text within tags in a list and parsing the html tags from the text
            text_within_tag.append(zhp(html[from_position:to_position_close_tag].replace(html_text,'')))

    return text_within_tag

def urls(html,no_of_tags=0):
    # Initializing variables
    extracted_urls = []
    
    # no_of_tags=0 refers to fetch all URLs
    urls_list = ztag(html,'a href',no_of_tags)

    # Seperating URLs from the tag
    for url in urls_list:
        from_position = url.find('"')
        to_position = url.find('"',from_position+1)

        extracted_urls.append(url[from_position+1:to_position])

    # Returning extracted URLs
    return extracted_urls

if __name__=='__main__':
    hujambo()

    ########################################## EXAMPLE INPUTS ##########################################

    print '\n\n########## INPUT EXAMPLE - 1 ##########'
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

    print '\n\n########## INPUT EXAMPLE - 2  (attributes example) ##########'
    # html_to_parse is the html input. Alternatively, any input can be provided by reading from a file as well
    html_to_parse = '<span class = "helloworld">1</span><span>2</span><span = 1 class=2>3</span><span = 3 class=2>4</span>'
    # zhp takes one input, the html to be parsed
    parsed_html = zhp(html_to_parse)
    # ztag takes <=3 inputs, the html input, the tag to be extracted and the number of tags to extract (attributes given)
    tag = ztag(html_to_parse,'span,class',0)
    # ztagtext takes <=3 inputs, the html input, the tag (within which lies the text to be extracted) and the number of such texts to extract (attributes given)
    tagtext = ztagtext(html_to_parse,'span,class',0)
    # urls takes <=2 inputs, the html input and number of tags to be extracted
    links = urls(html_to_parse,0)
        
    # Printing Output
    print '\n\nHTML Input  : ',html_to_parse
    print '\n\nParsed HTML : ',parsed_html
    print 'Tags : ',tag
    print 'Text withing Tag : ',tagtext
    print 'Extracted URLs : ',links
