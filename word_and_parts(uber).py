def findSubstrings(words, parts):
    res = []
    for word in words:
        longest_sub = ""
        sub_position = 0
        for sub in parts:
            position = word.find(sub)
            if position > -1:
                if len(sub) > len(longest_sub):
                    longest_sub = sub
                    sub_position = position
                if len(sub) == len(longest_sub):
                    if position < sub_position:
                        longest_sub = sub
                        sub_position = position
        if longest_sub != "":
            word = word[:sub_position] + "[" + word[sub_position:sub_position+len(longest_sub)] + "]" + word[sub_position+len(longest_sub):]
        res.append(word)
    return res
if __name__=="__main__":
    words= ["Apple","Melon","Orange","Watermelon"]
    parts= ["a","mel","lon","el","An"]
    print findSubstrings(words, parts)
