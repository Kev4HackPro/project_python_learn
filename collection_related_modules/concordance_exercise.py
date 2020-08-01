from collections import Counter, OrderedDict
sentence = input('Hey there, just write a random sentence here: ')
sentence_split = sentence.split(' ')
list_sentence = Counter(sentence_split)
print('Unordered word count')
print(list_sentence)
print('Ordered word count')
alphabetic_list = OrderedDict(list_sentence)
print(alphabetic_list)

# Author's code
word_count = Counter()
input_string = input('Enter your sentence here: ')

split_sentence = input_string.split(' ')
for words in split_sentence:
    if words == '':
        pass
    elif words in word_count:
        word_count[words] += 1
    else:
        word_count[words] = 1

print('Unordered Counter')
print(word_count)

ordered_word_count = OrderedDict()
for key in sorted(word_count):
    ordered_word_count[key] = word_count[key]

print('Ordered Word Count')
print(ordered_word_count)

