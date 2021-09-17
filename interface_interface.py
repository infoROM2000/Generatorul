from constants import c_default_screen_height, c_default_screen_width, StrConstants, c_file_name, c_previous_sum
from interface import client_interface
from interface_commands import add_new_entry


def create_interface():
    c = StrConstants()
    client_interface.\
        set_width(c_default_screen_width).\
        set_height(c_default_screen_height).\
        build().\
        add_label(text=c.default_file_name(), row=0, column=0).\
        add_entry(entry_name=c_file_name, bd=5, row=0, column=1).\
        add_label(text=c.last_month_sum(), row=0, column=2).\
        add_entry(entry_name=c_previous_sum, bd=5, row=0, column=3).\
        add_label(text=c.month(), row=0, column=4).\
        add_spin_box(spin_box_value=1, from_=1, to=12, row=0, column=5).\
        add_label(text=c.year(), row=0, column=6).\
        add_spin_box(spin_box_value=2021, from_=2000, to=2100, row=0, column=7).\
        add_button(text="+", command=add_new_entry, row=0, column=8).\
        add_button(text=c.generate_xlsx(), command="CALLABLE2", row=0, column=9).\
        add_label(text=c.type(), row=1, column=0).\
        add_label(text=c.day(), row=1, column=1).\
        add_label(text=c.explanation(), row=1, column=1).\
        add_label(text=c.value(), row=1, column=3).\
        persist()
