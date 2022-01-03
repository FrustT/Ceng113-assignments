###########################################
#      Group-35                           #
#        290201099 - Burak ERİNÇ          #
#        290201082 - Arif Ege ÖNDER       #
#                                         #
###########################################

import csv
from os import remove
removed = 0

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
        key_length = int(lengths[1]) - int(lengths[0])

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

def filter_frags(frag_dict, threshold=0.7):
    dissimilar_frag_dict = {}
    removed = []

    def get_similarity(s1, s2):
        similar = 0

        # get similarity with checking every character's
        # position and value. if same, increment similar
        for i in range(len(s1)):
            if s1[i] == s2[i]: similar += 1

        # lastly, divide similar to length of a sequence
        # to find the percent with format 0.x
        return similar / len(s1)
    
    # check for every key with every present
    # in the dictionary with time complexity of O(n^2)
    for key in frag_dict:
        s1 = frag_dict[key]

        for looped_key in frag_dict:
            s2 = frag_dict[looped_key]

            if key != looped_key and get_similarity(s1, s2) >= threshold:
                # to avoid duplication, only remove the second one
                if looped_key not in removed: removed.append(looped_key)

        if key not in removed: dissimilar_frag_dict[key] = frag_dict[key]

    return dissimilar_frag_dict

def get_sentences(dissimilar_frag_dict):
    sentences_dict = {}

    def generate_kmers(seq, k):
        kmers = ""
        
        # this code takes a string and splits it into k length strings and 
        # add them in order to another string
        for i in range(0, len(seq) - k + 1):
            kmers += " " + seq[i:i+k]
        return kmers
        
    # this block takes all keys and values and
    # assings kmers to its key value in another dict
    for key in dissimilar_frag_dict:
        sentences_dict[key] = generate_kmers(dissimilar_frag_dict[key], 4).lstrip()

    return sentences_dict

def clean_dict(sentences_dict):
    # keep track of removed words
    # with this global variable
    global removed

    cleaned_dict = {}

    def clean_sentence(sentence):
        cleaned_sentence_list = []

        # for each word in sentence
        for word in sentence.split():
            # check if word exists on the sentence
            if word not in cleaned_sentence_list:
                cleaned_sentence_list.append(word)

        return " ".join(cleaned_sentence_list)

    # for every key clean the sentence
    for key in sentences_dict:
        cleaned = clean_sentence(sentences_dict[key])
        cleaned_dict[key] = cleaned

        # keep track of removed words and add to global variable
        removed += len(sentences_dict[key].split(" ")) - len(cleaned.split(" "))

    return cleaned_dict

def write_genes(file_path, clean_sentences_dict):
    headers = ["fragment_id", "sentence", "sentence_length", "number_of_words"]

    # open the csv file, if doesn't exist create
    with open(file_path, "w") as f:
        writer = csv.writer(f)

        # write headers
        writer.writerow(headers)

        # written_data = 
        # [
        #   {
        #       "fragment_id": "chrX|123123-123123",
        #       "sentece": "AGAG GAGT AGTC GTCA",
        #       "sentence_length": 19,
        #       "number_of_words": 4
        #   },
        #   {
        #       "fragment_id": "chrX|123123-123123",
        #       "sentece": "AGAG GAGT AGTC GTCA",
        #       "sentence_length": 19,
        #       "number_of_words": 4
        #   }
        # ]

        # shape of written data will be like above
        written_data = []

        # create a dictionary for every element
        for element in clean_sentences_dict:
            data = {}

            data["fragment_id"] = element
            data["sentence"] = clean_sentences_dict[element]
            data["sentence_length"] = len(data["sentence"])
            data["number_of_words"] = len(clean_sentences_dict[element].split(" "))
            
            # append it to written_data
            written_data.append(data)

        # finally, write all datas to the csv file
        for data in written_data:
            writer.writerow([data["fragment_id"], data["sentence"], data["sentence_length"], data["number_of_words"]])

        f.close()
        

def main():
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
    sentences_dict = get_sentences(dissimilar_frag_dict)
    #    print the number of words in a sentence -> Expected output: 47
    print("Number of words in a sentence:", len(list(sentences_dict.values())[0].split(" ")))

    # 5) remove duplicate words in sentences
    cleaned_dict = clean_dict(sentences_dict)
    #    print the total number of words removed -> Expected output: 8521
    print(f"Number of words removed: {removed}")
        
    # 6) write sentences into output.csv
    write_genes("output.csv", cleaned_dict)

main()
