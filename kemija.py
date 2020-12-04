sentence = list(input())
vowel = 'aiueo'
decode = list()
i = 0
while i < len(sentence):
    if sentence[i] in vowel:
        decode.append(sentence[i])
        i += 3
    else:
        decode.append(sentence[i])
        i += 1

print(''.join(decode))