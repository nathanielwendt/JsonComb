from copy import deepcopy
import itertools

# def expand(cand_dict):
#     with open(source_file) as data_file:
#         source = json.load(data_file)
#
#     source_exp = find_tokens(source)
#
#     import pprint
#     print "--C--C--C--C- JSON COMBO -C--C--C--C--"
#     pprint.pprint(source_exp)
#     print "--C--C--C--C--C--C--C--C--C--C--C--C--"
#     with open(output_file, 'w') as outfile:
#         json.dump(source, outfile)

def build_combinations(combos, res_template, res_list):
    combinations = cartesian_product(combos)

    for combination in combinations:
        next_res = deepcopy(res_template)
        for key,value in combination.iteritems():
            next_res[key] = value
        res_list.append(next_res)

def cartesian_product(my_dict):
    product = [x for x in apply(itertools.product, my_dict.values())]
    return [dict(zip(my_dict.keys(), p)) for p in product]

def find_tokens(source):
    res = []
    if isinstance(source, dict):
        combos = {}
        res = {}
        for key, value in source.iteritems():
            if check_exp(value):
                combos[key] = find_tokens(value[1:])
            else:
                res[key] = find_tokens(source[key])

        if len(combos) > 0:
            res_template = res
            res = []
            build_combinations(combos, res_template, res)

    elif isinstance(source, list):
        combos = []
        res = []
        for item in source:
            if check_exp(item):
                combos = item
                #res.append(find_tokens(item[1:]))
            else:
                res.append(find_tokens(item))

        if len(combos) > 0:
            res_template = res
            res = []
            for combo in combos[1:]:
                res.append(res_template + [combo])
    else:
        res = source

    return res

def check_exp(cand):
    return isinstance(cand, list) and len(cand) > 0 and cand[0] == "!"
