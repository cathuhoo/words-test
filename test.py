import os
import sys
import json
import re
from datetime import datetime
import logging

def test():
    print('Hello World inside test()')

# This function sorts the words in the list
def sort_words():
    word_list = [  
        ['household', '家庭'],  
        ['possess', '拥有，持有'],  
        ['remark', '言论，评述'],  
        ['counsel', '忠告，建议']
    ]
    word_list.sort()
    print(word_list)
# This function is the main function that runs the game
if __name__ == '__main__':
    print('Hello World')
    sort_words()

