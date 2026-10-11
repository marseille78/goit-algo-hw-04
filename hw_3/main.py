from pathlib import Path
from sys import argv
from colorama import Fore

def parse_folder(folder: str, offset: int) -> str:
    root_foder = Path(folder)
    offset_total = "\t" * offset

    if offset == 1:
        print(f"{Fore.BLUE + str(root_foder)}/")
    for element in root_foder.iterdir():
        if element.is_dir():
            print(f"{offset_total}{Fore.BLUE + element.name}/")
            parse_folder(element, offset + 1)
        if element.is_file():
            print(f"{offset_total}{Fore.GREEN + element.name}")


def main():
    try:
        if len(argv) > 1:
            parse_folder(argv[1], 1)
        else:
            print("Enter path of dir")
    except FileNotFoundError:
        print("File Not Found")


if __name__ == "__main__":
    main()