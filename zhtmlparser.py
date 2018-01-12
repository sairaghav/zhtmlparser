def vanakkam():
    print '''
##################################################
# Tool    : zhtmlparser                          #
# Version : 2.0                                  #
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


def zhp(html):
    while True:
        from_position=html.find('<')
        while True:         
            to_position=html.find('>',from_position)

            # Confirming '<' is part of code to be parsed
            to_position_single_angular=html.find('<',from_position+1)

            if to_position_single_angular!=-1 and to_position_single_angular<to_position:
                from_position=to_position_single_angular
            else:
                break
            
        html_text=html[from_position:to_position+1]
        html=html.replace(html_text,'')
        
        if html_text=='':
            break
        
        # Reducing number of loops for reducing exec time
        html_text=html_text[:1]+'/'+html_text[1:]
        if html_text in html:
            html=html.replace(html_text,'')

    return html

print zhp('<class id=<abc>>>helloworld<</class>')
