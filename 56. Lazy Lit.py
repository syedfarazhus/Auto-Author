from typing import List, Dict, TextIO
from random import choice

def flatten_once(X:List) -> List:
    """Returns a ‘flat’ list comprising the elements of
    X maintaining order.
    >>> flatten_once([])
    []
    >>> flatten_once([[3, 4, 5], [1, [6,7]]])
    [3, 4, 5, 1, [6, 7]]
    """
    flat1 = []
    for subX in X:
        for item in subX:
            flat1.append(item)
    return flat1

def make_dictionary(f: TextIO) -> Dict[str, List[str]]:
    list2 = []
    with open(f) as lit:
        lit_lines = lit.readlines()
        for line in lit_lines:
            line_v2 = line.rstrip().lstrip().strip('\n').split(' ')
            list2.append(line_v2)
    flat1 = flatten_once(list2)
    i = 0
    word2word = {}
    for i in range(len(flat1)):
        if flat1[i] == flat1[-1]:
            break
        elif flat1[i] not in word2word:
            word2word[flat1[i]] = [flat1[i + 1]]
            i += 1
        else:
            word2word[flat1[i]].append(flat1[i + 1])
            i += 1
    return word2word

def mimic_text(word2word: Dict[str, List[str]], num_words: int) -> str:
    story = ''
    nextword = list(word2word.keys())[0]
    for i in range(num_words):
        possible_words = word2word[nextword]
        nextword = choice(possible_words)
        story += nextword + ' '
    return story
        
        
