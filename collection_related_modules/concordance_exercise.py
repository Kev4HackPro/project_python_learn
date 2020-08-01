from collections import *
sentence = input('Hey there, just write a random sentence here: ')
sentence_split = sentence.split(' ')
list_sentence = Counter(sentence_split)
print('Unordered word count')
print(list_sentence)
print('Ordered word count')
alphabetic_list = OrderedDict(list_sentence)
print(alphabetic_list)

