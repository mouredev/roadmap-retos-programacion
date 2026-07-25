# pylint: disable=missing-module-docstring,missing-function-docstring

import os
from zipfile import ZipFile


# ---------------------------------------------------------------------------- #
#                                   FUNCTIONS                                  #
# ---------------------------------------------------------------------------- #


def create_zip(*, file_paths: list[str], zip_file_path: str) -> None:
    with ZipFile(file=zip_file_path, mode="w") as zip_file:
        for _file_path in file_paths:
            zip_file.write(filename=_file_path, arcname=os.path.basename(p=_file_path))


# ---------------------------------------------------------------------------- #
#                                     MAIN                                     #
# ---------------------------------------------------------------------------- #


FILE_PATHS: list[str] = ["./hozlucas28.py", "./hozlucas28.txt"]
ZIP_FILE_PATH: str = "./hozlucas28.zip"

for file_path in [*FILE_PATHS[1:], ZIP_FILE_PATH]:
    if os.path.exists(path=file_path):
        os.remove(path=file_path)

FILE_CONTENT: list[str] = ["Lucas Nahuel Hoz", "22", "Argentina"]
with open(file=FILE_PATHS[1], mode="w", encoding="utf8") as file:
    file.write("|".join(FILE_CONTENT))

create_zip(file_paths=FILE_PATHS, zip_file_path=ZIP_FILE_PATH)

# Uncomment to remove files on program finish
# for file_path in [*FILE_PATHS[1:], ZIP_FILE_PATH]:
#     os.remove(path=file_path)
