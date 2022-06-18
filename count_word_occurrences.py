sentence = "Testing a word ting word sometimes a happy word"

def count_words(v_word, v_string):
    counter = {}
    for wrd in v_string.split(" "):
        if wrd in counter:
            counter[wrd] += 1
        else:
            counter[wrd] = 1
    if v_word in counter:
        return(counter[v_word])
    else:
        return("0")

print(count_words("asd",sentence))