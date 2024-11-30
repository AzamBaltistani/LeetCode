def reversePrefix(word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        
        word  = str(word)
        ind = word.index(ch)
        sub_word = word[0:ind+1]
        rem_word = word[ind+1:]
        return sub_word[::-1] + rem_word
        

print(reversePrefix("abcdefd", "k"))

# dcbaefd