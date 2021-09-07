from pathlib import Path

if __name__ == "__main__":
    from .parser import parse

    in_file = Path("output/samples/sample.xlsx")
    parse(in_file)