import pathlib

import fire

from bpdf import Client


def get_font_path():
    return pathlib.Path(__file__).parent / "font" / "Lora-Regular.ttf"


def proc(text: str):
    font_path = get_font_path()
    c = Client(font_path)
    c.run(text)


def main():
    fire.Fire(proc)


if __name__ == "__main__":
    main()
