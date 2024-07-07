# def substrings(word):
#     stuart = []  
#     stu_score = 0
#     kevin = []
#     kev_score = 0

#     n = len(word)
#     for i, letter in enumerate(word):
#         for j in range(i, n+1):
#             substr = word[i:j]
#             if len(substr) > 0:
#                 if substr[0] in ['a', 'e', 'i', 'o', 'u']:
#                     if substr not in kevin:
#                         kevin.append(substr)
#                     kev_score+=1
#                 else:
#                     if substr not in stuart:
#                         stuart.append(substr) 
#                     stu_score+=1
#     if kev_score>stu_score:
#         return f"Kevin {kev_score}"
#     else:
#         return f"Stuart {stu_score}"    
# print(substrings("banana"))
def minion_game(string):
    word = string.lower()
    stuart = []  
    stu_score = 0
    kevin = []
    kev_score = 0

    n = len(word)
    for i, letter in enumerate(word):
        for j in range(i, n+1):
            substr = word[i:j]
            if len(substr) > 0:
                if substr[0] in ['a', 'e', 'i', 'o', 'u']:
                    if substr not in kevin:
                        kevin.append(substr)
                    kev_score+=1
                else:
                    if substr not in stuart:
                        stuart.append(substr) 
                    stu_score+=1
    if kev_score>stu_score:
        return f"Kevin {kev_score}"
    else:
        return f"Stuart {stu_score}"  
if __name__ == '__main__':
    # s = input()
    s = "Ugabuga"
    minion_game(s)