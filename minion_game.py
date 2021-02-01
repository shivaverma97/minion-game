# WORKS FOR ALL

vowels = ['A','E','I','O','U']

def minion_game(string):
    strt_scr = 0
    kvn_scr = 0

    for i in range(len(string)):
        if string[i] in vowels:
            kvn_scr += len(string)-i
        else:
            strt_scr += len(string)-i

    if strt_scr>kvn_scr:
        print(f'Stuart {strt_scr}')
    elif strt_scr==kvn_scr:
        print(f'Draw')
    else:
        print(f'Kevin {kvn_scr}')

if __name__ == '__main__':
    s = input()
    minion_game(s)

# WORKS ONLY FOR SHORT INPUT STRINGS BECAUSE OF THE USE OF LISTS, MAY CAUSE RUNTIME ERROR BECAUSE OF HIGHER MEMORY USAGE.



# vowels = ['A','E','I','O','U']
# consonants = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
# Stuart = []
# Kevin = []


# def minion_game(string):
#     list_str = []
#     list_str.append(string[0])
#     length = len(string)
#     for i in range(2,length+1):
#         for j in range(0,length+1):
#             s = string[j:i]
#             if j<i:
#                 list_str.append(s)
#     for vowel in list_str:
#         if vowel[0] in vowels:
#             Kevin.append(vowel)
    
#     for consonant in list_str:
#         if consonant[0] in consonants:
#             Stuart.append(consonant)

#     score_kevin = len(Kevin)
#     score_stuart = len(Stuart)

#     if score_kevin>score_stuart:
#         print(f'Kevin {score_kevin}')
#     elif score_stuart==score_kevin:
#         print('Draw')
#     else:
#         print(f'Stuart {score_stuart}')

# if __name__ == '__main__':
#     s = input()
#     minion_game(s)


