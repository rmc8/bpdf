import tomllib
import pathlib

import fire

from bpdf import Client


def get_font_path():
    return pathlib.Path(__file__).parent / "font" / "Lora-Regular.ttf"


def get_config():
    p = pathlib.Path(__file__).parent / "config.toml"
    with open(p, "rb") as f:
        return tomllib.load(f)


def proc(text: str):
    font_path = get_font_path()
    config = get_config()
    c = Client(font_path, config)
    c.run(text)


def main():
    fire.Fire(proc)


if __name__ == "__main__":
    main()
