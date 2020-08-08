import yaml

def read_yaml(fname):
    obj  = open(fname, "r")
    parsed = yaml.safe_load_all(obj)
    return parsed

def write_yaml(fname, fobj):
    yaml.dump()

def parse_file(fobj):
    print(next(fobj))


obj = read_yaml("sample.yaml")
parse_file(obj)

