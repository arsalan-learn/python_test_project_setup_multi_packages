import yaml

def define_schema():
    yaml.safe_load("a: 1")  # uses PyYAML
    print("Schema defined")
