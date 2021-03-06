import pprint
from comb import find_tokens

def expand(source, show_result):
    source_exp = find_tokens(source)
    if show_result:
        print "--C--C--C--C- JSON COMBO -C--C--C--C--"
        pprint.pprint(source_exp)
        print "--C--C--C--C--C--C--C--C--C--C--C--C--"
    return source_exp


if __name__ == '__main__':
    import sys,json

    if len(sys.argv) < 2:
        raise Exception("Need to declare a source file to work with!")

    source_file = sys.argv[1]

    if len(sys.argv) >= 3:
        dest_file = sys.argv[2]
    else:
        #default name has a _c appended
        dest_file = source_file.split(".json")[0] + "_c.json"

    show = False
    if len(sys.argv) >= 4:
        show_raw = sys.argv[3]
        if "showres" == show_raw:
            show = True

    with open(source_file) as data_file:
        source = json.load(data_file)

    source_exp = expand(source, show)

    with open(dest_file, 'w') as outfile:
        json.dump(source_exp, outfile)