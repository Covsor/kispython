import re


def main(input_string):
    pattern = r"option\s*'([\w_]+)'\s*:=\s*q\(([\w_]+)\);"
    matches = re.findall(pattern, input_string)
    result = {key: value for key, value in matches}
    return result