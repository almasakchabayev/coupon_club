# -*- coding: utf-8 -*-
import re

    # mb put this in utils both support functions
def clean_extract(selector, path_of_info, elements_order=0):
    try:
        clean_value = selector.css(path_of_info).extract()[elements_order]
        clean_value = clean_value.strip()
    except:
        clean_value = ''
    # self.log('clean_value="" for \nxpath: %s\n count: %d\n item: %s' % (xpath_of_info, count, self.items[count]))
    return clean_value

def get_numbers_from_string(string):
    numbers_list = re.findall('\d+', string.replace(' ', ''))
    if numbers_list:
        return numbers_list[0]
    else:
        return 0