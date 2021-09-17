import xlsxwriter

from constants import c_file_name, StrConstants, c_previous_sum, c_day
from interface import client_interface
from interface.interface_builder import add_errorbox_message
from repository import InterfaceDataHolder


def add_new_entry():
    choices = ['BF', 'CHT', 'ATM', 'PLT', 'ODP']
    element = client_interface.append_and_get_string_var(set_value=choices[0])
    client_interface.append_option_menu(element=element, choices=choices, column=0)
    d = InterfaceDataHolder()

    if d.get_data_len_for_data_type(data_type=c_day) == 0:
        day_value = 1
    else:
        day_value = d.get_data_on_index(data_type=c_day, index=d.get_data_len_for_data_type(data_type=c_day) - 1)
    day_name = d.get_new_generated_data_ident_for_data_type(data_type=c_day)
    client_interface.add_spin_box(spin_box_value=day_value, from_=1, to=31, row=client_interface.get_self_row(),
                                  column=1, spin_box_name=day_name)

    explanation_nr = "DE adaugat numar la explicatie"
    client_interface.add_entry(entry_name=f"explanation_{explanation_nr}", bd=5, width=50,
                               row=client_interface.get_self_row(), column=2)
    # TODO: append exmplanation_nr to explanations
    value_nr = "De cautat numar la valoare"
    client_interface.add_entry(entry_name=f"value_{value_nr}", bd=4, row=client_interface.get_self_row(), column=3)
    client_interface.increase_self_row()


def generate_xlsx():
    c = StrConstants()
    d = InterfaceDataHolder()
    for x in d.get_all_data_of_type(data_type=c_day):
        print(x)

    def generate() -> bool:
        file_name = client_interface.get_entry(entry_name=c_file_name)
        if len(file_name.get()) == 0:
            add_errorbox_message(c.file_must_have_name())
            return False

        previous_sum = client_interface.get_entry(entry_name=c_previous_sum)
        if len(previous_sum.get()) == 0:
            add_errorbox_message(c.enter_last_month_sum())
            return False

        if d.get_data_len_for_data_type(data_type=c_day) == 0:
            add_errorbox_message(c.no_days())
            return False

        # TODO: maybe move xlsx construction into a separate, factory method that can be easily modified and
        #  parametrized

        workbook = xlsxwriter.Workbook(file_name.get() + '.xlsx')
        table_header = workbook.add_format()
        table_header.set_bold()
        table_header.set_align('center')
        bold = workbook.add_format()
        bold.set_bold()
        worksheet = workbook.add_worksheet()
        worksheet.set_column(3, 3, 30)
        # ...
