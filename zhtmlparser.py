def hujambo():
    print '''
##################################################
# Tool    : zhtmlparser                          #
# Version : 3.0                                  #
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
    iteration = 0
    flag = 1

    # Checking if any input is passed to the function
    # no_of_tags = 0 by default, which means all tags will be extracted
    if no_of_tags == 0:
        # Increasing no_of_tags value to enter the loop
        no_of_tags = 2
        flag = 0
        
    while iteration <= no_of_tags:
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
        if find_tag in html_text:
            tags.append(html_text)

    # Returning the tags list
    return tags

def ztagtext(html,tag='',no_of_tags=0):
    # Initializing the variables
    iteration = 0
    text_within_tag = []
    flag = 1

    # Checking if any input is passed to the function
    # no_of_tags = 0 by default, which means all tags will be extracted
    if no_of_tags == 0:
        # Increasing no_of_tags value to enter the loop
        no_of_tags = 2
        flag = 0
    
    while iteration <= no_of_tags:
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

        # Checking if the tag obtained is the required tag
        if tag in html_text:
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


if __name__=='__main__':
    hujambo()

    # html_to_parse is the html input. Alternatively, any input can be provided by reading from a file as well
    html_to_parse = '<a href = "https://somerandom1.com">hello</a><a href = https://somerandom2.com">>><script>newworld</script></a><a href = "something"><helloworld</script>'
    # zhp takes one input, the html to be parsed
    parsed_html = zhp(html_to_parse)
    # ztag takes <=3 inputs, the html input, the tag to be extracted and the number of tags to extract
    tag = ztag(html_to_parse,'a href',2)
    # ztagtext takes <=3 inputs, the html input, the tag (within which lies the text to be extracted) and the number of such texts to extract
    tagtext = ztagtext(html_to_parse,'a href',2)

    # Printing Output
    print '\n\nHTML Input  : ',html_to_parse
    print '\n\nParsed HTML : ',parsed_html
    print 'Tags : ',tag
    print 'Text withing Tag : ',tagtext
