def reverse_any(seq):
    if isinstance(seq, str):
        return seq[::-1]
    elif isinstance(seq, list):
        return seq[::-1]
    else:
        raise TypeError("Only strings and lists are supported")