###########################################
#      Group-35                                                                    #
#        290201099 - Burak ERİNÇ                                        #
#        290201082 - Arif Ege ÖNDER                                  #
#                                                                                         #
###########################################

def read_genes(file_path):
    # store all headers and sequences to
    # add them later to the dictionary
    headers = []
    sequences = []
    gene_dict = {}

    # open the file in 'read' mode
    with open(file_path, "r") as f:
        for line in f.readlines():
            # if line starts with '>', therefore is a header;
            if line.startswith(">"): headers.append(line.strip("\n").strip(">"))
            # else it is a sequence
            else: sequences.append(line.strip("\n"))

    # add all sequences with their keys to the dictionary
    for i in range(len(headers)):
        gene_dict[headers[i]] = sequences[i]

    return gene_dict

def get_fragments(gene_dict, frag_len=50):
    new_dict = {}

    for key in gene_dict:
        # split the header from '|' to create ["chrX", "123123-123123"]
        # then select the second element and split it from '-' 
        # to create ["123123", "123123"]
        lengths = key.split("|")[1].split("-")

        # find the length with substracting both key values
        key_length = int(lengths[1]) - int(lengths[0]) + 1

        # only execute if frag_len is bigger than the length
        # to filter the shorter ones
        if key_length >= frag_len:
            sequence = gene_dict[key]

            # split into pieces by frag_len
            fragment = [(sequence[i: i + frag_len]) for i in range(0, len(sequence), frag_len)]
            
            # integer divide to find out how many times it will be splitted
            number_of_times = key_length // frag_len

            key_prefix = key.split("|")[0]
            key_first = int(lengths[0])
            key_last = key_first + frag_len

            for i in range(number_of_times):
                # create the fragments and push it to the new dictionary
                new_dict[f"{key_prefix}|{key_first}-{key_last}"] = fragment[i]

                # update the next fragment
                key_first, key_last = key_last, key_last + frag_len

    return new_dict

def get_similarity(s1, s2):
    similar = 0

    # get similarity with checking every character's
    # position and value. if same, increment similar
    for i in range(len(s1)):
        if s1[i] == s2[i]: similar += 1

    # lastly, divide similar to length of a sequence
    # to find the percent with format 0.x
    return similar / len(s1)

def filter_frags(frag_dict, threshold=0.7):
    dissimilar_frag_dict = {}
    added = []
    # check for every key with every present
    # in the dictionary with time complexity of O(n^2)
    for key in frag_dict:
        dissimilar = True
        s1 = frag_dict[key]

        for looped_key in frag_dict:
            s2 = frag_dict[looped_key]

            if key != looped_key and get_similarity(s1, s2) >= threshold:
                # to avoid duplication, check if key already exists in the list
                if looped_key not in added: added.append(key)
                dissimilar = False

        # finally if similarity not found, add to dissimilar dictionary
        if dissimilar: dissimilar_frag_dict[key] = frag_dict[key]

    # avoid duplication and add the values added before
    for key in added:
        dissimilar_frag_dict[key] = frag_dict[key]

    return dissimilar_frag_dict

def get_sentences(dissimilar_frag_dict):
    sentences_dict = {}

    def generate_kmers(seq, k):
        kmers= ""afewfaw

        # this code takes a string and splits it into k length strings and 
        # add them in order to another string
        for i in range(0,len(seq)- k + 1):
            kmers += " " + seq[i:i+k]
        return kmers
        
    # this block takes all keys and values and
    # assings kmers to its key value in another dict
    for key in dissimilar_frag_dict:
        sentences_dict[key] = generate_kmers(dissimilar_frag_dict[key],4).lstrip()
    return sentences_dict

def clean_dict(sentences_dict):
    cleaned_dict = {}

    def clean_sentence(sentence):
        cleaned_sentence_list = []
        for word in sentence.split():
            if word not in cleaned_sentence_list:
                cleaned_sentence_list.append(word)
        return " ".join(cleaned_sentence_list)
    for key in sentences_dict:
        cleaned_dict[key] = clean_sentence(sentences_dict[key])
    return cleaned_dict

def get_wordNumber(dict):
    wordNumber = 0

    # this block gets total word number in  a dict
    for key in dict:
        # +1 is for first word that has no blank spaces before it
        wordNumber +=(len(dict[key])+1)/ 5
    return wordNumber

def write_genes(file_path, clean_sentences_dict):
    # STEP 6
    pass

def main():
    # STEP 7: Runs required steps and prints data statistics

        # 1) read genes from input.txt
        gene_dict = read_genes("input.txt")
        #    print the number of genes -> Expected output: 115
        print(f"Number of genes: {len(gene_dict)}")
        # 2) get fragments for genes read
        new_dict = get_fragments(gene_dict)
        #    print the number of fragments -> Expected output: 1293
        print(f"Number of fragments: {len(new_dict)}")
        # 3) filter out similar fragments
        dissimilar_frag_dict = filter_frags(new_dict)
        #    print the number of dissimilar fragments -> Expected output: 1286
        print(f"Number of dissimilar fragments: {len(dissimilar_frag_dict)}")
        # 4) get sentences for dissimilar fragments
        #    print the number of words in a sentence -> Expected output: 46
        sentences_dict = get_sentences(dissimilar_frag_dict)
        # 5) remove duplicate words in sentences
        cleaned_dict = clean_dict(sentences_dict)
        #    print the total number of words removed -> Expected output: 8194
        get_wordNumber(sentences_dict) - get_wordNumber(cleaned_dict)
        # 6) write sentences into output.csv

    # DO NOT SCAN OR PRINT EXTRA INFORMATION. JUST THE STATS LISTED ABOVE.

main()


