"""
simonc@uber.com

str_a ="
    persist_series(
        sum_two_series(
            get_series_a(),
            get_series_b()
        ),
        get_timeout()
    )"

output = [
    "persist_series(",
    "  sum_two_series(",
    "    get_series_a(),",
    "    get_series_b()"
]
persist_series(
    sum_two_series(
        get_series_a(),
        get_series_b()
    ),
    get_timeout()
)
"""

def separate_string(input_string):
    output = []
    indent = 0
    idx = 0
    start_idx = 0
    if len(input_string) == 0:
        return []
    while idx < len(input_string):
        if input_string[idx] == '(':
            output.append(indent*" " + input_string[start_idx:idx+1])
            indent += 4
            start_idx = idx+1
        if input_string[idx] == ')':
            indent -= 4
            if input_string[idx-1] == ')':
                output.append(indent*" " + ')')
            else:
                output[-1] = output[-1] + ')'
        if input_string[idx] == ',':
            output[-1] = output[-1] + ','
            start_idx = idx+1
        idx += 1
    return output

if __name__ == "__main__":
    str_a = "persist_series(sum_two_series(get_series_a(),get_series_b()),get_timeout())"
    print separate_string(str_a) == [
        "persist_series(",
        "    sum_two_series(",
        "        get_series_a(),",
        "        get_series_b()",
        "    ),",
        "    get_timeout()",
        ")"
    ]

    print separate_string("dummy_function()") == ["dummy_function()"]
    print separate_string("hi(a(),b())") == [
        "hi(",
        "    a(),",
        "    b()",
        ")"
    ]
    print separate_string("hi(a(,b())") 
