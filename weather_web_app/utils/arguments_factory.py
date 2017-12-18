import argparse

def parse_arguments():
    parser = argparse.ArgumentParser("Weather web app using ")
    parser.add_argument(
        "config_path",
        help="path to yaml config file"
    )
    args = parser.parse_args()
    return args