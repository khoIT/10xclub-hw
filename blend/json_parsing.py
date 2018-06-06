# """
jsons_in = [
        {
            "k1": 1.0,
            "k2": {
                "k1": 5.0,
                "k2": 4738.0
            },
            "k3": 45.0
        },
        {
            "k1": 7.0,
            "k2": {
                "k1": 1534.5,
                "k2": 55.0,
                "k3": 77.0
            },
            "k3": 66.0,
            "k5": {
                "k1": 88.0,
                "k2": 399.0
            }
        }
    ]

"""
get_avg_json(jsons_in) =
{
    "k1": 4.0,
    "k2": {
        "k1": 769.75,
        "k2": 2396.5,
        "k3": 77.0
    },
    "k3": 55.5,
    "k5": {
    "k1": 88.0,
        "k2": 399.0
    }
}
"""


def parse_json(jsons_in):
    inter_dict = {}
    for blob in jsons_in:
        parse_json_recursive(blob, inter_dict)
    print inter_dict
    return process_intermediary_dict(inter_dict)

def process_intermediary_dict(inter_dict):
    res_dict = {}
    for k,v in inter_dict.iteritems():
        if type(v) == tuple:
            res_dict[k] = inter_dict[k][0] / inter_dict[k][1]
        else:
            res_dict[k] = process_intermediary_dict(v)
    return res_dict

def parse_json_recursive(jsons_in, json_dict):
    for k, v in jsons_in.iteritems():
        if k not in json_dict:
            if type(v) != dict:
                json_dict[k] = (jsons_in[k], 1)
            else:
                json_dict[k] = parse_json_recursive(v, {})
        else:
            if type(v) != dict:
                json_dict[k] = (json_dict[k][0]+v, json_dict[k][1]+1)
            else:
                json_dict[k] = parse_json_recursive(v, json_dict[k])
    return json_dict

if __name__ == "__main__":
    print parse_json(jsons_in)
