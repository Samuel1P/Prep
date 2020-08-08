import yaml
to_write = {'template': {'metadata': {'name': 'my-app-dep', 'labels': {'env': 'stage', 'tier': 'backend'}}, 'spec': {'containers': [{'name': 'tiny-http', 'image': 'hjacobs/tiny-docker-http-test'}]}}}


def read_yaml(fname):
    obj  = open(fname, "r")
    parsed_gen = yaml.safe_load_all(obj) # Creates a generator of all Yaml Items in a file
    return parsed_gen

def write_yaml(i, fname):
    with open(fname, "w") as fobj:
        yaml.dump(i, fobj)

def print_file(fobj):
    for yam in fobj:
        print (yam)

obj = read_yaml("sample.yaml")
print_file(obj)
write_yaml(to_write,"write.yaml")
