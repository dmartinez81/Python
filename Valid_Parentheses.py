# class Solution(object):
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    if len(s) == 1: return False
    middle = len(s)//2
    for i in range(0, middle):
                                                    # s = "([])"
        if s[i] == '(' and s[len(s)-1-i] == ')' or s[i] == '{' and s[len(s)-1-i] == '}' or s[i] == '[' and s[len(s)-1-i] == ']':
            if i == middle - 1:
                return True
            else:  
                continue
                                                    # s = "()[]"

    for (i = 0; i < len(s); i++):
        if s[i] == '(' and s[i+1] == ')' or s[i] == '{' and s[i+1] == '}' or s[i] == '[' and s[i+1] == ']':
            
 
    #         for i in range(1, len(s)-1):
    #             if s[i+1] == '(' and s[len[-2]] == ')' or s[i+1] == '{' and s[len[s-2]] == '}' or s[i+1] == '[' and s[len[s-2]] == ']':
    #                 return True
    # else:
    #     return False






    
# s = "(}"
# s = "()[]{}"
s = "[([])]"
print(isValid(s))
