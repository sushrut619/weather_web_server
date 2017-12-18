import yaml

def build_config(config_path):
    with open(config_path, 'r') as f:
        config = yaml.load(f)

    return config
