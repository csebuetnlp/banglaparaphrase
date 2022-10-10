import argparse
from bengali_stemmer.rafikamal2014 import RafiStemmer
"""Must be kept inside the rafikamal stemmer"""


def stem_string(string):
    """
    returns a stemmed string without punctuations

    Args:
        string (str) : string to be stemmed
    Returns:
        stemmed_string (str) : stemmed version of the string
    """
    stemmer = RafiStemmer()
    punc = '''।,;:?!'."-[]{}()–—―~'''

    for ele in string:
        if ele in punc:
            string = string.replace(ele, "")
    words = string.split()
    return ' '.join([stemmer.stem_word(word) for word in words])


def calculate_ngram_repeat(text):
    stemmed = stem_string(text)

    splitted = stemmed.split()

    for i,baseword in enumerate(splitted):
        for j,cmpword in enumerate(splitted[i+1:]):
            if baseword==cmpword:
                if len(splitted) - i-j-1 > j:
                    trackflag=True
                    for k in range(1,j+1):
                        if splitted[i+k]!=splitted[i+1+j+k]:
                            trackflag=False
                            break
                    if trackflag:
                        if j+1 >= 2:
                            return ' '.join([s for s in splitted[i:i+j+1]])
        
    return ''



if __name__ == '__main__':
    # Create the parser
    parser = argparse.ArgumentParser(description='path to the source and target file')

    # Add the arguments
    parser.add_argument('--s',
                        metavar='s',
                        type=str,
                        help='the path to the source file')
    
    parser.add_argument('--t',
                        metavar='t',
                        type=str,
                        help='the path to the target file')


    args = parser.parse_args()

    source_path = args.s
    target_path = args.t


source_file = open(source_path, encoding='utf-8')
target_file = open(target_path, encoding='utf-8')

final_target = open('./punctuation_filtered_source.bn', 'w', encoding='utf-8')
final_source = open('./punctuation_filtered_target.bn', 'w', encoding='utf-8')
output_file = open('./final_output.bn', 'w', encoding='utf-8')

target_lines = target_file.readlines()
source = source_file.readlines()
counter = 0

for line_index, line in enumerate(target_lines):
    output = calculate_ngram_repeat(line)
        
    if (line_index+1) % 20000 == 0:
        print(line_index + 1)
        
    if output != '':
        output_file.write(line + output + '\n' + str(line_index+1)+'\n\n')
        counter += 1
    else:
        final_target.write(line)
        final_source.write(source[line_index])

        
    
    output_file.write('\n'+ 'Total repeating sentence: ' + str(counter))
    
        


