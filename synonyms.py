import math, re

def norm(vec):
    '''
    Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    ''' Calculate the similarity between two string words
        vec1: dic
        vec2: dic
        return: float'''
        
    # find the intersection of v1 & v2's keys
    int_key = list(set(vec1.keys() & vec2.keys()))
    if not int_key:  # if there is no intersection between them
        return -1

    numerator = 0
    for key in int_key:
        numerator += vec1[key] * vec2[key]

    deno = 1
    deno *= norm(vec1)*norm(vec2)

    return numerator / deno


def word_counts(file):
    ''' count the number of time a word exist in a file - list of sentences
        file: list of list
        return: dic'''
        
    counts_dict = {}
    for sentence in file:
        for word in sentence:
            if word not in counts_dict.keys():
                counts_dict[word] = 1
            else:
                counts_dict[word] += 1
    return counts_dict


def build_semantic_descriptors(sentences):
    '''transfer centences into semantic descriptors of words
        sentences: list of list
        return: dict'''
        
    d = {}
    counts_dict = word_counts(sentences)
    # print(counts_dict)

    for key in counts_dict.keys():
        # collect all sentences containing the key word
        sen_col = []

        for sen in sentences:
            if key in sen:
                sen_col.append(sen)  # ready to be sent to word_counts
        count = word_counts(sen_col)

        # remove the count of the key word itself
        del count[key]
        d[key] = count

    return d


def build_semantic_descriptors_from_files(filenames):
    '''transfer centences into semantic descriptors of words
        sentences: text file
        return: dict'''
        
    # combine all files into a single one
    comb_file = ""

    for i in range(len(filenames)):
        comb_file += open(filenames[i], encoding="latin1").read()
        comb_file += "\n"

    # all lower case and remove "\t" "\n"
    comb_file = comb_file.lower()


    for punc in ["!", "?"]:
        if punc in comb_file:
            comb_file = comb_file.replace(punc, ".")
    while "\n" in comb_file:
        comb_file = comb_file.replace("\n", " ")

    if "." in comb_file:
        comb_file = comb_file.split(".")


    s = []
    for line in comb_file:
        line = re.sub('[^a-z ]', '', line)  # remove all non-letters (including punctuations, numbers)
        line = " ".join(line.split()) 
        s.append(line.split(" "))

    return build_semantic_descriptors(s)


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    """return the element of choices with the largest semantic similarity to word
    word: str
    choices: list of strings
    semantic descriptors: dict
    """
    
    res = {}
    for candidate in choices:
        if word not in semantic_descriptors.keys() or candidate not in semantic_descriptors.keys():
            res[candidate] = -1
        else:
            res[candidate] = similarity_fn(semantic_descriptors[word], semantic_descriptors[candidate])

    max_value = max(res.values())
    list_value = list(res.values())
    if list_value.count(max_value) > 1:
        ind = list_value.index(max_value)  # this returns the smaller ind of the key with max value
        return choices[ind]

    return max(res, key=res.get)  # get the max value's key, if there is no tie


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    file = open(filename, encoding="latin1").read()
    file = file.split("\n")
    count = 0

    for line in file:
        line = line.split(" ")
        word = line[0]
        correct_ans = line[1]
        choices = line[2:]
        actual_ans = most_similar_word(word, choices, semantic_descriptors, similarity_fn)

        if correct_ans == actual_ans:
            count += 1

    return count / len(file) *100
