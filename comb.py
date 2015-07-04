from copy import deepcopy
import itertools

EXPAND_INDICATOR = "!C"

def build_combinations(combos, res_template, res_list):
    combinations = cartesian_product(combos)

    for combination in combinations:
        next_res = deepcopy(res_template)
        for key,value in combination.iteritems():
            next_res[key] = value
        res_list.append(next_res)

def cartesian_product(my_dict):
    sorted_vals = get_sorted_values(my_dict)
    product = [x for x in apply(itertools.product, sorted_vals)]
    return [dict(zip(sorted(my_dict.keys()), p)) for p in product]

def get_sorted_values(my_dict):
    res = []
    for key,value in sorted(my_dict.iteritems()):
        res.append(value)
    return res

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
    return isinstance(cand, list) and len(cand) > 0 and cand[0] == EXPAND_INDICATOR
