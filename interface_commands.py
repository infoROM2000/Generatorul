import xlsxwriter

from constants import c_file_name, StrConstants, c_previous_sum, c_day, c_type, c_explanation, c_value
from interface import client_interface, add_errorbox_message, add_infobox_message
from repository import data_holder as d


def add_new_entry():
    # client_interface.increase_self_row()

    choices = ['BF', 'CHT', 'ATM', 'PLT', 'ODP']
    element = client_interface.append_and_get_string_var(set_value=choices[0])
    element_ident = d.get_new_generated_data_ident_for_data_type(data_type=c_type)
    client_interface.append_option_menu(string_var=element, choices=choices, row=client_interface.get_self_row(),
                                        column=0, string_var_name=element_ident)

    if d.get_data_len_for_data_type(data_type=c_day) == 0:
        day_value = 1
    else:
        day_value = d.get_data_on_index(data_type=c_day, index=d.get_data_len_for_data_type(data_type=c_day) - 1)
    day_name = d.get_new_generated_data_ident_for_data_type(data_type=c_day)
    client_interface.add_spin_box(spin_box_value=day_value, from_=1, to=31, row=client_interface.get_self_row(),
                                  column=1, spin_box_name=day_name)

    explanation_ident = d.get_new_generated_data_ident_for_data_type(data_type=c_explanation)
    client_interface.add_entry(entry_name=explanation_ident, bd=5, width=50,
                               row=client_interface.get_self_row(), column=2)

    value_ident = d.get_new_generated_data_ident_for_data_type(data_type=c_value)
    client_interface.add_entry(entry_name=value_ident, bd=4, row=client_interface.get_self_row(), column=3)
    client_interface.increase_self_row()


def generate_xlsx():
    c = StrConstants()
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

        row_index = 0
        current_day = d.get_data_on_index(data_type=c_day, index=d.get_data_len_for_data_type(data_type=c_day) - 1)
        sold = float(previous_sum.get())

        i = 0
        while i < d.get_data_len_for_data_type(data_type=c_type): # TODO: check again if <= or <
            caching_on_day = 0
            payments_on_day = 0
            day_index = 2
            worksheet.write(row_index, 0, c.short_number(), table_header)
            worksheet.write(row_index, 1, c.type(), table_header)
            worksheet.write(row_index, 2, c.short_number(), table_header)
            worksheet.write(row_index, 3, c.explanations(), table_header)
            worksheet.write(row_index, 4, c.caching(), table_header)
            worksheet.write(row_index, 5, c.payments(), table_header)
            worksheet.write(row_index + 1, 1, c.date(), table_header)
            worksheet.write(row_index + 1, 2, current_day, table_header)
            worksheet.write(row_index + 1, 3, c.previous_day_balance_report(), table_header)
            worksheet.write(row_index + 1, 4, sold, bold)

            while current_day == int(d.get_data_on_index(data_type=c_day, index=i)):
                worksheet.write(row_index + day_index, 0, day_index - 1)
                worksheet.write(row_index + day_index, 1, d.get_data_on_index(data_type=c_type, index=i))
                worksheet.write(row_index + day_index, 3, d.get_data_on_index(data_type=c_explanation, index=i))
                if len(d.get_data_on_index(data_type=c_value, index=i)) > 0:
                    number = float(d.get_data_on_index(data_type=c_value, index=i))
                    val = "{:.2f}".format(number)
                    if number > 0:
                        worksheet.write(row_index + day_index, 4, val)
                        caching_on_day += number
                    else:
                        worksheet.write(row_index + day_index, 5, val[1:])
                        payments_on_day -= number
                i += 1
                day_index += 1
                if i >= d.get_data_len_for_data_type(data_type=c_type): # TODO: debug to see if > or >=
                    break

            sold = float(sold) + float(caching_on_day) - float(payments_on_day)
            caching_on_day = "{:.2f}".format(caching_on_day)
            payments_on_day = "{:.2f}".format(payments_on_day)
            sold = "{:.2f}".format(sold)

            worksheet.write(row_index + day_index, 3, "Total")
            worksheet.write(row_index + day_index, 4, caching_on_day, bold)
            worksheet.write(row_index + day_index, 5, payments_on_day, bold)
            worksheet.write(row_index + day_index + 1, 3, "Sold", table_header)
            worksheet.write(row_index + day_index + 1, 4, sold, bold)

            if i >= d.get_data_len_for_data_type(data_type=c_type): # TODO: debug to see if > or >=
                break

            current_day = int(d.get_data_on_index(data_type=c_day, index=i))
            row_index += day_index + 4

        workbook.close()
        return True

    if generate():
        add_infobox_message(c.file_generated_successfully())
