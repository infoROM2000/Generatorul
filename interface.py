import tkinter as tk

from constants import c_default_screen_height, c_default_screen_width, c_default_file_name


class InterfaceBuilder:
    def __init__(self):
        self.__file_name = c_default_file_name
        self.__height = c_default_screen_height
        self.__width = c_default_screen_width
        self.entries = dict()
        self.__root = tk.Tk()

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

    def add_entry(self, entry_name: str, bd: int, row: int, column: int) -> 'InterfaceBuilder':
        self.entries[entry_name] = tk.Entry(self.__root, bd=bd)
        return self.__set_grid(self.entries[entry_name], row=row, column=column)

    def add_spin_box(self, spin_box_value: int, from_: int, to: int, row: int, column:int, wrap: bool = True):
        var = tk.StringVar(value=spin_box_value)
        element = tk.Spinbox(self.__root, from_=from_, to=to, textvariable=var, wrap=wrap)
        return self.__set_grid(element, row=row, column=column)

    def add_button(self, text: str, command: callable, row: int, column: int):
        element = tk.Button(self.__root, text=text, command=command)
        return self.__set_grid(element, row=row, column=column)

    def persist(self):
        self.__root.mainloop()


def create_interface():
    interface = InterfaceBuilder()
    interface.\
        set_width(c_default_screen_width).\
        set_height(c_default_screen_height).\
        build().\
        add_label(text=c_default_file_name, row=0, column=0).\
        add_entry(entry_name="file_name", bd=5, row=0, column=1).\
        add_label(text="Suma de luna precedentă", row=0, column=2).\
        add_entry(entry_name="previous_sum", bd=5, row=0, column=3).\
        add_label(text="Luna: ", row=0, column=4).\
        add_spin_box(spin_box_value=1, from_=1, to=12, row=0, column=5).\
        add_label(text="An: ", row=0, column=6).\
        add_spin_box(spin_box_value=2021, from_=2000, to=2100, row=0, column=7).\
        add_button(text="+", command="COLLABLE1", row=0, column=8).\
        add_button(text="Generează XLSX", command="CALLABLE2", row=0, column=9).\
        add_label(text="TIP", row=1, column=0).\
        add_label(text="ZIUA", row=1, column=1).\
        add_label(text="EXPLICAȚIE", row=1, column=1).\
        add_label(text="VALOARE", row=1, column=3).\
        persist()
