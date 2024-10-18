#input
text = "Hi! This    is your developer."
#text = input("enter text:")

#1. count words
last_symbol = ''
words = 0
for symbol in text :
    if symbol == ' ' and last_symbol != ' ' :
        words += 1

    last_symbol = symbol

if words > 0 :
    words += 1

# count sentences
last_symbol_is_separator = False
sentences = 0
for symbol in text:
    if (last_symbol_is_separator == False and 
            ( symbol == '.' or symbol == '!' or symbol == '?')):
        sentences +=  1
        
    last_symbol_is_separator = True \
        if     symbol == '.' \
            or symbol == '!' \
            or symbol == '?' \
        else False

#output
print(" The text\n", f"\'{text}\'", "\n containts", words, "words,", \
                         sentences, "sentences"   )


# using regular expressions

import re

words = re.split(r'\W+', text)
words = len([s.strip() for s in words if s.strip()])

sentence_endings = r'[.!?]'
sentences = re.split(sentence_endings, text)
sentences = len([s.strip() for s in sentences if s.strip()])

#output
print("\n using regular expressions\n", "containts", words, "words,", \
                         sentences, "sentences"   )