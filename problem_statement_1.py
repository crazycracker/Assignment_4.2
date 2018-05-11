#below function returns the list of the lengths of the coressponding words
def map_to_lengths(seq):
    lengths = []
    for word in seq:
        lengths.append(len(word))
    return lengths
