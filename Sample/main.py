#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# kuri_pome
"""main"""
import logging

from tk_main import TkMain
from ini_parser import Config
from json_parser import Storage
from logger import create_logger

logger: logging.Logger = create_logger(__name__, level="debug")


def main() -> None:
    """Main"""
    _: Config = Config(r"config.ini")
    _: Storage = Storage(r"storage.json")
    tk_main: TkMain = TkMain()
    tk_main.main()


if __name__ == "__main__":
    main()
