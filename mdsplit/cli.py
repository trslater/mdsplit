from argparse import ArgumentParser


def main():
    parser = ArgumentParser(prog="python -m mdsplit",
                            description=("A CLI tool for splitting "
                                         "markdown files"))
    parser.add_argument("FILE", help="path of markdown file to split")
    parser.add_argument("DEPTH", help="heading depth to split down to")
    parser.add_argument("--dir-leaves",
                        help=("turn leaves of parse tree into directories "
                              "containing a single index.md, instead of "
                              "into files"),
                        action="store_true")
    args = parser.parse_args()
