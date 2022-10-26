#!/usr/bin/env python3

from pathlib import Path
from yaml_parser import Parser

YAML_FILE = "app_config.yaml"


def main():
    filepath = Path(YAML_FILE).resolve(strict=True)
    parser = Parser()
    data = parser.to_dict(filepath)
    print(data)


if __name__ == "__main__":
    main()
