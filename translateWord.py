#!/usr/bin/env
#coding:utf-8
#英、法语互译

E2F = {'bread':'pain', 'wine':'vin', 'with':'avec', 'I':'Je',
       'eat':'mange', 'drink':'bois', 'John':'Jean',
       'friends':'amis', 'and':'et', 'of':'du', 'red':'rouge'}
F2E = {'pain':'bread', 'vin':'wine', 'avec':'with', 'Je':'I',
       'mange':'eat', 'bois':'drink', 'Jean':'John',
       'amis':'friends', 'et':'and', 'du':'of', 'rouge':'red'}
dicts = {'English to French':E2F, 'French to English':F2E}

def translateWord(word, dictionary):
    if word in dictionary.keys():
        return dictionary[word]
    elif word != '':
        return '"' + word + '"'
    return word

def translate(phrase, dicts, direction):
    UCLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LCLetters = UCLetters.lower()
    letters = UCLetters + LCLetters
    dictionary = dicts[direction]
    translation = ''
    word = ''
    for c in phrase:
        if c in letters:
            word = word + c
        else:
            translation = translation + translateWord(word, dictionary) + c
            word = ''
    return translation + ' ' + translateWord(word, dictionary)

print translate('I drink good red wine, and eat bread.',
                dicts, 'English to French')
print translate('Je bois du vin rouge.',
                dicts, 'French to English')
