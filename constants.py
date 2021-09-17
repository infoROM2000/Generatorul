from language import client_language

c_default_screen_height = 720
c_default_screen_width = 1280
c_default_client_language = "ro"
c_file_name = "file_name"
c_previous_sum = "previous_sum"
c_day = "day"


class StrConstants:
    def __init__(self):
        """
        A translation service is intended to be used for a larger scale.
        """
        self.language = client_language if client_language is not None else c_default_client_language

    def default_file_name(self):
        if self.language == "en":
            return "File name: "
        return "Numele fisierului: "

    def last_month_sum(self):
        if self.language == "en":
            return "Last month's sum"
        return "Suma de luna precedentă"

    def month(self):
        if self.language == "en":
            return "Month: "
        return "Luna: "

    def year(self):
        if self.language == "en":
            return "Year: "
        return "An: "

    def generate_xlsx(self):
        if self.language == "en":
            return "Generate XLSX"
        return "Generează XLSX"

    def type(self):
        if self.language == "en":
            return "TYPE"
        return "TIP"

    def day(self):
        if self.language == "en":
            return "DAY"
        return "ZIUA"

    def explanation(self):
        if self.language == "en":
            return "EXPLANATION"
        return "EXPLICAȚIE"

    def value(self):
        if self.language == "en":
            return "VALUE"
        return "VALOARE"

    def error(self):
        if self.language == "en":
            return "Error"
        return "Eroare"

    def file_must_have_name(self):
        if self.language == "en":
            return "File must have a name!"
        return "Fișierul trebuie să aibă un nume!"

    def enter_last_month_sum(self):
        if self.language == "en":
            return "Please enter last month's sum (even 0)!"
        return "Introduceți suma de luna precedentă (chiar și 0)!"

    def no_days(self):
        if self.language == "en":
            return "No days"
        return "Nicio zi"
