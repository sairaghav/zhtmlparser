def vanakkam():
    print '''
##################################################
# Tool    : zhtmlparser                          #
# Version : 2.1                                  #
# Coded with Python 2.7                          #
# Profile : https://github.com/pr2h/             #
# ######          #####   #                      #
# #    #  # ###  #     #  #                      #
# ######  ##         #    ######                 #
# #       #        #      #    #                 #
# #       #      #######  #    #                 #
##################################################
    '''
vanakkam()


def zhp(html,find_tag='',find_text_within_tag=''):
    tag_out = ''
    close_tag = ''
    text_within_tag = ''
    while True:
        from_position=html.find('<')
        html_text = ''
        while True:
            to_position=html.find('>',from_position)

            # Confirming '<' is part of code to be parsed
            to_position_single_angular=html.find('<',from_position+1)

            if to_position_single_angular!=-1 and to_position_single_angular<to_position:
                from_position=to_position_single_angular
            else:
                break
            
        html_text=html[from_position:to_position+1]

        if find_tag != '' and find_tag in html_text and '</' not in html_text:
            tag_out+=html_text+'\n'

        if find_text_within_tag != '' and find_text_within_tag in html_text and '</' not in html_text:
            if ' ' in html_text:
                to_position_close_tag=html_text.find(' ',0)
                close_tag = '</'+html_text[1:to_position_close_tag]+'>'
            else:
                close_tag = html_text[:1]+'/'+html_text[1:]

            to_position_close_tag = html.find(close_tag)
            text_within_tag+=html[from_position:to_position_close_tag].replace(html_text,'')+'\n'
            
        html=html.replace(html_text,'',1)
        
        if html_text=='':
            break

    return html,tag_out.strip('\n'),text_within_tag.strip('\n')

html_to_parse = '<a href="somewebsite1233">22<span>22</span></a><span>hi<a href="hi">hiii</a><a href>333</a>das</span>'
parsed_html,tag_out,text_within_tag=zhp(html_to_parse,'a href','a href')
print '\nHTML TO PARSE: \n',html_to_parse
print '\nPARSED HTML: \n',parsed_html
print '\nTAG_OUT: \n',tag_out
print '\nTEXT WITHIN TAG: \n',text_within_tag
