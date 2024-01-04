class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs) #sorting words in list alphabetically.
        prefix = "" # below we are going to add common letters to prefix if they are exist 
        first = strs[0] #since we're sorted our list, if first letter of first word equals first letter of last word it means that all words in the middle also has the same common letter.
        last = strs[-1] #last letter

        for i in range(min(len(first),len(last))): #in this range we pick smallest length number(True if all words have comman letters)
            if first[i] != last[i]: #if first letters not equal 
                return prefix #return empty quates
            else:
                prefix += first[i] #otherwise if first letter of first word and first letter of last word eqals, add letter to variable prefix
        return prefix #after checking all common letters return prefix
