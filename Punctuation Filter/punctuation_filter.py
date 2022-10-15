import argparse
symbols = ''',;:?!'."-[]{}()–—―~'''


# Create the parser
parser = argparse.ArgumentParser(
    description='path to the source and target file')

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

source_file = open(
    source_path, encoding='utf-8')
target_file = open(
    target_path, encoding='utf-8')


final_source = open('./source.bn', 'w', encoding='utf-8')
final_target = open('./target.bn', 'w', encoding='utf-8')


counter = 0

for index, line in enumerate(zip(source_file.readlines(), target_file.readlines())):

    src = line[0].strip()
    trg = line[1].strip()

    if src[-1] == '"' and trg[-1] == '"':
        # check if -2 pos has !?| or not
        if src[-2] == '?' or src[-2] == "!" or src[-2] == "।":
            if trg[-2] == '?' or trg[-2] == "!" or trg[-2] == "।":

                src_to_write = ''
                trg_to_write = ''

                if (src.count('"') % 2 == 0 and src.count('"') >= 2) and (trg.count('"') % 2 == 0 and trg.count('"') >= 2):
                    src_to_write = src
                    trg_to_write = trg

                if (src.count('"') == 1) and (trg.count('"') == 1):
                    src_to_write = src[:-1]
                    trg_to_write = trg[:-1]

                # write without the last quotation
                if src_to_write != '' and trg_to_write != '':
                    final_source.write(src_to_write+'\n')
                    final_target.write(trg_to_write+'\n')

    elif src[-1] == '\'' and trg[-1] == '\'':
        # check if -2 pos has !?| or not
        if src[-2] == '?' or src[-2] == "!" or src[-2] == "।":
            if trg[-2] == '?' or trg[-2] == "!" or trg[-2] == "।":

                src_to_write = ''
                trg_to_write = ''

                if (src.count('\'') % 2 == 0 and src.count('\'') >= 2) and (trg.count('\'') % 2 == 0 and trg.count('\'') >= 2):
                    src_to_write = src
                    trg_to_write = trg

                if (src.count('\'') == 1) and (trg.count('\'') == 1):
                    src_to_write = src[:-1]
                    trg_to_write = trg[:-1]

                # write without the last quotation
                if src_to_write != '' and trg_to_write != '':
                    final_source.write(src_to_write+'\n')
                    final_target.write(trg_to_write+'\n')

    elif src[-1] == '"' and (trg[-1] == '।' or trg[-1] == '?' or trg[-1] == '!') and src.count('"') == 1 and trg.count('"') == 0:

        # check if -2 pos has !?| or not
        if src[-2] == '?' or src[-2] == "!" or src[-2] == "।":

            final_source.write(src[:-1]+'\n')
            final_target.write(trg+'\n')

    elif src[-1] == '\'' and (trg[-1] == '।' or trg[-1] == '?' or trg[-1] == '!') and src.count('\'') == 1 and trg.count('\'') == 0:

        if src[-2] == '?' or src[-2] == "!" or src[-2] == "।":

            final_source.write(src[:-1]+'\n')
            final_target.write(trg+'\n')

    elif trg[-1] == '"' and (src[-1] == '।' or src[-1] == '?' or src[-1] == '!') and trg.count('"') == 1 and src.count('"') == 0:

        # check if -2 pos has !?| or not
        if trg[-2] == '?' or trg[-2] == "!" or trg[-2] == "।":

            final_source.write(src+'\n')
            final_target.write(trg[:-1]+'\n')

    elif trg[-1] == '\'' and (src[-1] == '।' or src[-1] == '?' or src[-1] == '!') and trg.count('\'') == 1 and src.count('\'') == 0:

        # check if -2 pos has !?| or not
        if trg[-2] == '?' or trg[-2] == "!" or trg[-2] == "।":

            final_source.write(src+'\n')
            final_target.write(trg[:-1]+'\n')

    elif (src[-1] == "।" or src[-1] == "!" or src[-1] == "?") and (trg[-1] == "।" or trg[-1] == "!" or trg[-1] == "?"):
        final_source.write(src+'\n')
        final_target.write(trg+'\n')
