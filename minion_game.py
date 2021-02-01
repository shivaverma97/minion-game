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




