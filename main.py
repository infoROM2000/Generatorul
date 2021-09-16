# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import tkinter as tk
import xlsxwriter
from tkcalendar import DateEntry
from tkinter import messagebox

from interface import create_interface

r = 2
tipuri = []
date = []
explicatii = []
valori = []


def start():
    global tipuri, date, explicatii, valori

    def generator():
        for x in date:
            print(x.get())
        eroare = 0
        if len(nume_fisier.get()) == 0:
            messagebox.showerror("Eroare", "Fisierul trebuie sa aiba un nume!")
            eroare = 1
        if len(suma_precedenta.get()) == 0:
            messagebox.showerror("Eroare", "Introduceti suma de luna precedenta (chiar si 0)!")
            eroare = 1
        if eroare:
            return
        workbook = xlsxwriter.Workbook(nume_fisier.get() + '.xlsx')
        cap_tabel = workbook.add_format()
        cap_tabel.set_bold()
        cap_tabel.set_align('center')
        bold = workbook.add_format()
        bold.set_bold()
        worksheet = workbook.add_worksheet()
        worksheet.set_column(3, 3, 30)
        i = 0
        zi_curenta = int(date[i].get())
        index_rand = 0
        sold = float(suma_precedenta.get())
        while i <= len(tipuri):
            incasari_zi = 0
            plati_zi = 0
            index_zi = 2
            worksheet.write(index_rand, 0, "Nr.", cap_tabel)
            worksheet.write(index_rand, 1, "Tip", cap_tabel)
            worksheet.write(index_rand, 2, "Nr.", cap_tabel)
            worksheet.write(index_rand, 3, "Explicatii", cap_tabel)
            worksheet.write(index_rand, 4, "Incasari", cap_tabel)
            worksheet.write(index_rand, 5, "Plati", cap_tabel)
            worksheet.write(index_rand + 1, 1, "Data", cap_tabel)
            worksheet.write(index_rand + 1, 2, zi_curenta, cap_tabel)
            worksheet.write(index_rand + 1, 3, "Raport/sold ziua precendenta", cap_tabel)
            worksheet.write(index_rand + 1, 4, sold, bold)

            while zi_curenta == int(date[i].get()):
                worksheet.write(index_rand + index_zi, 0, index_zi - 1)
                worksheet.write(index_rand + index_zi, 1, tipuri[i].get())
                worksheet.write(index_rand + index_zi, 3, explicatii[i].get())
                if len(valori[i].get()) > 0:
                    val = "{:.2f}".format(float(valori[i].get()))
                    nr = float(valori[i].get())
                    if nr > 0:
                        worksheet.write(index_rand + index_zi, 4, val)
                        incasari_zi += nr
                    else:
                        worksheet.write(index_rand + index_zi, 5, val[1:])
                        plati_zi -= nr
                i += 1
                index_zi += 1
                if i >= len(date):
                    break

            sold = sold + incasari_zi - plati_zi
            incasari_zi = "{:.2f}".format(incasari_zi)
            plati_zi = "{:.2f}".format(plati_zi)
            sold = "{:.2f}".format(sold)
            worksheet.write(index_rand + index_zi, 3, "Total")
            worksheet.write(index_rand + index_zi, 4, incasari_zi, bold)
            worksheet.write(index_rand + index_zi, 5, plati_zi, bold)
            worksheet.write(index_rand + index_zi + 1, 3, "Sold", cap_tabel)
            worksheet.write(index_rand + index_zi + 1, 4, sold, bold)
            if i >= len(date):
                break
            zi_curenta = int(date[i].get())
            index_rand += index_zi + 4
        workbook.close()
        messagebox.showinfo("Info", "Fisier generat cu succes!")

    def inregistrare_noua():
        global r

        choices = ['BF', 'CHT', 'ATM', 'PLT', 'ODP']
        variable = tk.StringVar(root)
        variable.set('BF')
        selectie_tip = tk.OptionMenu(root, variable, *choices)
        selectie_tip.grid(row=r, column=0)
        tipuri.append(variable)
        if len(date) == 0:
            zi = tk.StringVar(value=1)
        else:
            zi = tk.StringVar(value=date[-1].get())
        selectie_zi = tk.Spinbox(
            root,
            from_=1,
            to=31,
            textvariable=zi,
            wrap=True)
        selectie_zi.grid(row=r, column=1)
        date.append(zi)
        explicatie = tk.Entry(root, bd=5, width=50)
        explicatie.grid(row=r, column=2)
        explicatii.append(explicatie)
        valoare = tk.Entry(root, bd=5)
        valoare.grid(row=r, column=3)
        valori.append(valoare)
        r += 1

    root = tk.Tk()
    root.geometry("1280x720")
    a = tk.Label(root, text="Numele fisierului: ").grid(row=0, column=0)
    nume_fisier = tk.Entry(root, bd=5)
    nume_fisier.grid(row=0, column=1)

    b = tk.Label(root, text="Suma de luna precedenta: ").grid(row=0, column=2)
    suma_precedenta = tk.Entry(root, bd=5)
    suma_precedenta.grid(row=0, column=3)

    c = tk.Label(root, text="Luna: ").grid(row=0, column=4)
    luna = tk.StringVar(value=1)
    selectie_luna = tk.Spinbox(
        root,
        from_=1,
        to=12,
        textvariable=luna,
        wrap=True)
    selectie_luna.grid(row=0, column=5)

    d = tk.Label(root, text="An: ").grid(row=0, column=6)
    an = tk.StringVar(value=2021)
    selectie_an = tk.Spinbox(
        root,
        from_=2000,
        to=2100,
        textvariable=an,
        wrap=True)
    selectie_an.grid(row=0, column=7)

    buton_nou = tk.Button(root, text="+", command=inregistrare_noua).grid(row=0, column=8)
    genereaza = tk.Button(root, text="Genereaza XLSX", command=generator).grid(row=0, column=9)
    e1 = tk.Label(root, text="TIP").grid(row=1, column=0)
    e2 = tk.Label(root, text="ZIUA").grid(row=1, column=1)
    e3 = tk.Label(root, text="EXPLICATIE").grid(row=1, column=2)
    e4 = tk.Label(root, text="VALOARE").grid(row=1, column=3)
    root.mainloop()


if __name__ == '__main__':
    start()
    create_interface()
