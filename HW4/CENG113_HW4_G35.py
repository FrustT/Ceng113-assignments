# CENG113 HW4 TEMPLATE
# AUTHOR: SAMET TENEKECI
# DATE: 27/12/2021

# MODIFY AND RENAME THIS FILE FOR YOUR ASSIGNMENT
# EXAMPLE FILE NAMING: CENG113_HW4_G01.py OR CENG_113_HW4_G25.py
# WRITE STUDENT IDS, NAMES & SURNAMES OF THE GROUP MEMBERS AT THE TOP
# SUBMIT ONLY THIS FILE AND ONLY ONCE FOR YOUR GROUP


def read_genes(file_path):
    # STEP 1


def get_fragments(gene_dict, frag_len = 50):
    # STEP 2


def filter_frags(frag_dict, threshold = 0.7):
    def get_similarity(s1, s2):
        # STEP 3.a
    # STEP 3.b


def get_sentences(dissimilar_frag_dict):
    def generate_kmers(seq, k):
        # STEP 4.a
    # STEP 4.b


def clean_dict(sentences_dict):
    def clean_sentence(sentence):
        # STEP 5.a
    # STEP 5.b


def write_genes(file_path, clean_sentences_dict):
    # STEP 6


def main():

    # STEP 7: Runs required steps and prints data statistics

        # 1) read genes from input.txt
        #    print the number of genes -> Expected output: 115
        # 2) get fragments for genes read
        #    print the number of fragments -> Expected output: 1293
        # 3) filter out similar fragments
        #    print the number of dissimilar fragments -> Expected output: 1286
        # 4) get sentences for dissimilar fragments
        #    print the number of words in a sentence -> Expected output: 46
        # 5) remove duplicate words in sentences
        #    print the total number of words removed -> Expected output: 8194
        # 6) write sentences into output.csv

    # DO NOT SCAN OR PRINT EXTRA INFORMATION. JUST THE STATS LISTED ABOVE.


main()
