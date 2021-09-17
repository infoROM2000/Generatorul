from __future__ import annotations

import tkinter as tk
from tkinter import messagebox
from typing import List

from constants import StrConstants
from utilities import CustomError


class InterfaceBuilder:
    def __init__(self):
        self.__file_name = ""
        self.__height = 0
        self.__width = 0
        self.__entries = dict()
        self.__root = tk.Tk()
        self.__self_row = 0

    def set_height(self, height: int) -> 'InterfaceBuilder':
        self.__height = height
        return self

    def set_width(self, width: int) -> 'InterfaceBuilder':
        self.__width = width
        return self

    # def set_file_name(self, file_name: str) -> 'InterfaceBuilder':
    #     self.__file_name = file_name
    #     return self

    def __set_grid(self, element, row: int, column: int) -> 'InterfaceBuilder':
        element.grid(row=row, column=column)
        return self

    def build(self) -> 'InterfaceBuilder':
        self.__root.geometry(f"{self.__width}x{self.__height}")
        return self

    def add_label(self, text: str, row: int, column: int) -> 'InterfaceBuilder':
        element = tk.Label(self.__root, text=text)
        return self.__set_grid(element, row=row, column=column)

    def add_entry(self, entry_name: str, bd: int, row: int, column: int, width: int = None) -> 'InterfaceBuilder':
        if width is None:
            self.__entries[entry_name] = tk.Entry(self.__root, bd=bd)
        else:
            self.__entries[entry_name] = tk.Entry(self.__root, bd=bd, width=width)
        return self.__set_grid(self.__entries[entry_name], row=row, column=column)

    def add_spin_box(self, spin_box_value: int, from_: int, to: int, column: int, row: int, wrap: bool = True,
                     spin_box_name: str = ""):
        var = tk.StringVar(value=spin_box_value)
        self.__entries[spin_box_name] = var
        element = tk.Spinbox(self.__root, from_=from_, to=to, textvariable=var, wrap=wrap)
        return self.__set_grid(element, row=row, column=column)

    def add_button(self, text: str, command: callable, row: int, column: int):
        element = tk.Button(self.__root, text=text, command=command)
        return self.__set_grid(element, row=row, column=column)

    def persist(self):
        self.__root.mainloop()

    def append_and_get_string_var(self, set_value: str) -> tk.StringVar:
        element = tk.StringVar(self.__root)
        element.set(set_value)
        return element

    def append_option_menu(self, string_var: tk.StringVar, choices: List[str], column: int):
        element = tk.OptionMenu(self.__root, string_var, *choices)
        self.__set_grid(element, row=self.__self_row, column=column)

    def increase_self_row(self):
        self.__self_row += 1

    def get_self_row(self):
        return self.__self_row

    def get_entry(self, entry_name: str) -> tk.Entry:
        """
        An error is raised if no entry is found with the given entry_name. Assume its an interface building error.

        :param entry_name: the name of the entry searched into the client interface
        :return: the entry with that name
        """
        if entry_name in self.__entries.keys():
            return self.__entries[entry_name]
        raise CustomError(f"'{entry_name}' not an entry in client interface")


def add_errorbox_message(message: str):
    messagebox.showerror(StrConstants().error(), message=message)
