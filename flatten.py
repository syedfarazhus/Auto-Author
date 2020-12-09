from typing import List

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
        
        
