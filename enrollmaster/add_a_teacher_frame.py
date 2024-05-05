from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox
import psycopg2
import re
import decimal


class AddATeacherFrame(ttk.Frame):

    def __init__(self, master=None, amend_menu_content_func=None, **kw):
        super().__init__(master, **kw)
        self.amend_menu_content_func = amend_menu_content_func
        self.columnconfigure((0, 2, 3, 4, 5), weight=1, minsize=300)
        self.columnconfigure(1, weight=1, minsize=50)
        self.rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28),
            weight=1, minsize=30)

        add_a_teacher_label = ttk.Label(self, text='DODAJ NAUCZYCIELA', font=('Open Sans', 14, 'bold'),
                                        bootstyle='default')
        add_a_teacher_label.grid(row=0, column=3, sticky='w')

        ## first_name

        first_name_label = ttk.Label(self, text="Imię*", font=('Open Sans', 12), bootstyle='default')
        first_name_label.grid(row=2, column=0, sticky='w')

        self.first_name_var = StringVar()

        self.first_name = ttk.Entry(self, width=30, bootstyle='light', textvariable=self.first_name_var)
        self.first_name.grid(row=3, column=0, sticky ='w')

        self.first_name_var.trace_add('write', self.validate_first_name)

        ## last_name

        last_name_label = ttk.Label(self, text="Nazwisko*", font=('Open Sans', 12), bootstyle='default')
        last_name_label.grid(row=2, column=2, sticky='w')

        self.last_name_var = StringVar()

        self.last_name = ttk.Entry(self, width=30, bootstyle='light', textvariable=self.last_name_var)
        self.last_name.grid(row=3, column=2, sticky='w')

        self.last_name_var.trace_add('write', self.validate_last_name)

        ## street

        street_label = ttk.Label(self, text='Ulica*', font=('Open Sans', 12), bootstyle='default')
        street_label.grid(row=5, column=0, sticky='w')

        self.street_var = StringVar()

        self.street = ttk.Entry(self, width=30, bootstyle='light', textvariable=self.street_var)
        self.street.grid(row=6, column=0, sticky='w')

        self.street_var.trace_add('write', self.validate_street)

        ## building_no

        building_no_label = ttk.Label(self, text='Nr domu*', font=('Open Sans', 12), bootstyle='default')
        building_no_label.grid(row=5, column=2, sticky='w')

        self.building_no_var = StringVar()

        self.building_no = ttk.Entry(self, width=10, bootstyle='light', textvariable=self.building_no_var)
        self.building_no.grid(row=6, column=2, sticky='w')

        self.building_no_var.trace_add('write', self.validate_building_no)

        ## local_no

        local_no_label = ttk.Label(self, text='Nr lokalu', font=('Open Sans', 12), bootstyle='default')
        local_no_label.grid(row=5, column=3, sticky='w')

        self.local_no_var = StringVar()

        self.local_no = ttk.Entry(self, width=10, bootstyle='light', textvariable=self.local_no_var)
        self.local_no.grid(row=6, column=3, sticky='w')

        self.local_no_var.trace_add('write', self.validate_local_no)

        ## city

        city_label = ttk.Label(self, text="Miasto*", font=('Open Sans', 12), bootstyle='default')
        city_label.grid(row=8, column=0, sticky='w')

        self.city_var = StringVar()

        self.city = ttk.Entry(self, width=30, bootstyle='light', textvariable=self.city_var)
        self.city.grid(row=9, column=0, sticky='w')

        self.city_var.trace_add('write', self.validate_city)

        ## postal_code

        postal_code_label = ttk.Label(self, text="Kod pocztowy*", font=('Open Sans', 12),
                                      bootstyle='default')
        postal_code_label.grid(row=8, column=2, sticky='w')

        self.postal_code_var = StringVar()

        self.postal_code = ttk.Entry(self, width=15, bootstyle='light', textvariable=self.postal_code_var)
        self.postal_code.grid(row=9, column=2, sticky='w')

        self.postal_code_var.trace_add('write', self.validate_postal_code)

        ## country

        country_label = ttk.Label(self, text="Państwo*", font=('Open Sans', 12), bootstyle='default')
        country_label.grid(row=8, column=3, sticky='w')

        self.country_var = StringVar()

        self.country = ttk.Entry(self, width=30, bootstyle='light', textvariable=self.country_var)
        self.country.grid(row=9, column=3, sticky='w')

        self.country_var.trace_add('write', self.validate_country)

        ## email

        email_label = ttk.Label(self, text="Adres e-mail", font=('Open Sans', 12), bootstyle='default')
        email_label.grid(row=11, column=0, sticky='w')

        self.email_var = StringVar()

        self.email = ttk.Entry(self, width=30, bootstyle='light', textvariable=self.email_var)
        self.email.grid(row=12, column=0, sticky='w')

        self.email_var.trace_add('write', self.validate_email)

        ## phone number

        phone_number_label = ttk.Label(self, text="Nr telefonu*", font=('Open Sans', 12),
                                       bootstyle='default')
        phone_number_label.grid(row=11, column=2, sticky='w')

        self.phone_var = StringVar()

        self.phone_number = ttk.Entry(self, width=20, bootstyle='light', textvariable=self.phone_var)
        self.phone_number.grid(row=12, column=2, sticky='w')

        self.phone_var.trace_add('write', self.validate_phone)

        ## personal id

        personal_id_label = ttk.Label(self, text="PESEL*", font=('Open Sans', 12), bootstyle='default')
        personal_id_label.grid(row=11, column=3, sticky='w')

        self.personal_id_var = StringVar()

        self.personal_id = ttk.Entry(self, width=20, bootstyle='light', textvariable=self.personal_id_var)
        self.personal_id.grid(row=12, column=3, sticky='w')

        self.personal_id_var.trace_add('write', self.validate_personal_id)

        ## document_no

        document_no_label = ttk.Label(self, text="Nr dokumentu*", font=('Open Sans', 12),
                                      bootstyle='default')
        document_no_label.grid(row=14, column=0, sticky='w')

        self.document_no_var = StringVar()

        self.document_no = ttk.Entry(self, width=20, bootstyle='light', textvariable=self.document_no_var)
        self.document_no.grid(row=15, column=0, sticky='w')

        self.document_no_var.trace_add('write', self.validate_document_no)

        ## document_type

        document_type_label = ttk.Label(self, text="Rodzaj dokumentu*", font=('Open Sans', 12),
                                        bootstyle='default')
        document_type_label.grid(row=14, column=2, sticky='w')

        self.document_type = ttk.Menubutton(self, bootstyle='dark', text='Wybierz dokument')
        self.document_type.grid(row=15, column=2, sticky='w')

        document_type_content = ttk.Menu(self.document_type)

        self.document_var = StringVar()
        self.document_var.set("Dowód osobisty")
        for document in ['Dowód osobisty', 'Paszport', 'Karta pobytu']:
            document_type_content.add_radiobutton(label=document, variable=self.document_var, value=document,
                                                  command=self.on_document_type_select)

        self.document_type['menu'] = document_type_content

        ## type_of_contract

        type_of_contract_label = ttk.Label(self, text="Rodzaj umowy*", font=('Open Sans', 12),
                                           bootstyle='default')
        type_of_contract_label.grid(row=14, column=3, sticky='w')

        self.type_of_contract = ttk.Menubutton(self, bootstyle='dark', text='Wybierz umowę')
        self.type_of_contract.grid(row=15, column=3, sticky='w')

        type_of_contract_content = ttk.Menu(self.type_of_contract)

        self.type_var = StringVar()
        self.type_var.set("Umowa o pracę")

        for contract in ['Umowa o pracę', 'Umowa zlecenie']:
            type_of_contract_content.add_radiobutton(label=contract, variable=self.type_var, value=contract,
                                                     command=self.on_contract_type_select)

        self.type_of_contract['menu'] = type_of_contract_content

        ## type_of_employment

        type_of_employment_label = ttk.Label(self, text='Rodzaj zatrudnienia*', font=('Open Sans', 12),
                                             bootstyle='default')
        type_of_employment_label.grid(row=14, column=4, sticky='w')

        self.type_of_employment = ttk.Menubutton(self, bootstyle='dark', text='Wybierz')
        self.type_of_employment.grid(row=15, column=4, sticky='w')

        type_of_employment_content = ttk.Menu(self.type_of_employment)

        self.employment_var = StringVar()
        self.employment_var.set("Pełny etat")

        for employment in ['Pełny etat', 'Pół etatu']:
            type_of_employment_content.add_radiobutton(label=employment, variable=self.employment_var, value=employment,
                                                       command=self.on_employment_type_select)

        self.type_of_employment['menu'] = type_of_employment_content

        ## salary

        salary_label = ttk.Label(self, text="Wynagrodzenie*", font=('Open Sans', 12), bootstyle='default')
        salary_label.grid(row=17, column=0, sticky='w')

        self.salary_var = StringVar()

        self.salary = ttk.Entry(self, width=20, bootstyle='light', textvariable=self.salary_var)
        self.salary.grid(row=18, column=0, sticky='w')

        self.salary_var.trace_add('write', self.validate_salary)

        ## employment_start

        employment_start_label = ttk.Label(self, text='Data rozpoczęcia pracy*', font=('Open Sans', 12),
                                           bootstyle='default')
        employment_start_label.grid(row=17, column=2, sticky='w')

        self.employment_start_entry = ttk.DateEntry(self, bootstyle='primary')
        self.employment_start_entry.grid(row=18, column=2, sticky='w')

        # native_language

        native_language_label = ttk.Label(self, text='Język ojczysty*', font=('Open Sans', 12),
                                          bootstyle='default')
        native_language_label.grid(row=17, column=3, sticky='w')

        self.native_language_var = StringVar()

        self.native_language_entry = ttk.Entry(self, width=20, bootstyle='light', textvariable=self.native_language_var)
        self.native_language_entry.grid(row=18, column=3, sticky='w')

        self.native_language_var.trace_add('write', self.validate_native_language)

        # language_to_teach

        language_to_teach_label = ttk.Label(self, text='Język nauczania*', font=('Open Sans', 12),
                                            bootstyle='default')
        language_to_teach_label.grid(row=17, column=4, sticky='w')

        self.language_to_teach = ttk.Menubutton(self, bootstyle='dark', text='Wybierz')
        self.language_to_teach.grid(row=18, column=4, sticky='w')

        language_to_teach_content = ttk.Menu(self.language_to_teach)

        self.lang_var = StringVar()
        self.lang_var.set("Angielski")
        for language in ['Angielski', 'Niemiecki', 'Francuski', 'Włoski', 'Hiszpański']:
            language_to_teach_content.add_radiobutton(label=language, variable=self.lang_var, value=language,
                                                      command=self.on_language_to_teach_select)

        self.language_to_teach['menu'] = language_to_teach_content

        submit_button_style = ttk.Style()
        submit_button_style.configure('success.TButton', font=('Open Sans', 14))

        submit_button = ttk.Button(self, bootstyle='success', text='ZAPISZ', width=20,
                                   style='success.TButton', command=self.submit_data)

        submit_button.grid(row=21, column=3, sticky='w')

        self.pack()

    def submit_data(self):

        validation = self.validation_on_submission()

        if validation is True:

            # Connect to the database
            conn = psycopg2.connect(
                database='enroll_proto',
                host='localhost',
                user='postgres',
                password='kulek',
                port='5432'
            )

            cur = conn.cursor()

            local_no_value = self.local_no.get() or None
            email_value = self.email.get() or None

            cur.execute(
                """
                INSERT INTO teachers (
                    first_name, last_name, street, building_no, local_no, city, postal_code, country, email, phone, personal_id,
                    document_no, document_type, type_of_contract, type_of_employment, salary, native_language, 
                    language_to_teach, status_of_employment, employment_start
                )
                VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                )
                """,
                (
                    self.first_name.get(), self.last_name.get(), self.street.get(), self.building_no.get(),
                    local_no_value, self.city.get(), self.postal_code.get(), self.country.get(),
                    email_value, self.phone_number.get(), self.personal_id.get(), self.document_no.get(),
                    self.on_document_type_select(), self.on_contract_type_select(), self.on_employment_type_select(),
                    self.salary.get(), self.native_language_entry.get(), self.on_language_to_teach_select(),
                    'Aktywny', self.employment_start_entry.entry.get()
                )
            )

            self.show_custom_messagebox("Nauczyciel został dodany", "Info")

            self.first_name_var.set("")
            self.last_name_var.set("")
            self.street_var.set("")
            self.building_no_var.set("")
            self.local_no_var.set("")
            self.city_var.set("")
            self.postal_code_var.set("")
            self.country_var.set("")
            self.email_var.set("")
            self.phone_var.set("")
            self.personal_id_var.set("")
            self.document_no_var.set("")
            self.document_type.configure(text="Wybierz dokument")
            self.document_var.set("")
            self.type_of_contract.configure(text="Wybierz umowę")
            self.type_var.set("Umowa o pracę")
            self.type_of_employment.configure(text="Wybierz")
            self.employment_var.set("Pełny etat")
            self.salary_var.set("")
            self.native_language_var.set("")
            self.language_to_teach.configure(text="Wybierz")
            self.lang_var.set("Angielski")

            conn.commit()
            cur.close()
            conn.close()



    """
    Functions for dropdown selection.
    """

    def on_document_type_select(self):
        selected_document_type = self.document_var.get()
        print("Selected document type:", selected_document_type)
        self.amend_menu_content_func(self.document_type, selected_document_type)
        return selected_document_type

    def on_contract_type_select(self):
        selected_contract_type = self.type_var.get()
        print("Selected type of contract:", selected_contract_type)
        self.amend_menu_content_func(self.type_of_contract, selected_contract_type)
        return selected_contract_type

    def on_language_to_teach_select(self):
        selected_language = self.lang_var.get()
        print("Selected language:", selected_language)
        self.amend_menu_content_func(self.language_to_teach, selected_language)
        return selected_language

    def on_employment_type_select(self):
        selected_employment_type = self.employment_var.get()
        print("Selected type of employment:", selected_employment_type)
        self.amend_menu_content_func(self.type_of_employment, selected_employment_type)
        return selected_employment_type

    """
    Validation functions
    """

    def validate_first_name(self, *args):
        first_name = self.first_name_var.get()
        print(len(first_name))

        if len(first_name) > 64:
            self.show_custom_messagebox("Długość imienia nie może przekraczać 64 znaków", "Błąd")

        if any(chr.isdigit() for chr in first_name):
            self.show_custom_messagebox("Pole 'Imię' nie może zawierać liczb", "Błąd")

        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

        if (regex.search(first_name) == None):
            pass
        else:
            self.show_custom_messagebox("Pole 'Imię' nie może zawierać znaków specjalnych", "Błąd")

    def validate_last_name(self, *args):
        last_name = self.last_name_var.get()
        print(len(last_name))

        if len(last_name) > 64:
            self.show_custom_messagebox("Długość nazwiska nie może przekraczać 64 znaków", "Błąd")

        if any(chr.isdigit() for chr in last_name):
            self.show_custom_messagebox("Pole 'Nazwisko' nie może zawierać liczb", "Błąd")

        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

        if (regex.search(last_name) == None):
            pass
        else:
            self.show_custom_messagebox("Pole 'Nazwisko' nie może zawierać znaków specjalnych", "Błąd")

    def validate_street(self, *args):
        street = self.street_var.get()
        print(len(street))

        if len(street) > 128:
            self.show_custom_messagebox("Długość nazwy ulicy nie może przekraczać 128 znaków", "Błąd")

        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

        if (regex.search(street) == None):
            pass
        else:
            self.show_custom_messagebox("Pole 'Ulica' nie może zawierać znaków specjalnych", "Błąd")


    def validate_building_no(self, *args):
        building_no = self.building_no_var.get()

        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

        if (regex.search(building_no) == None):
            pass
        else:
            self.show_custom_messagebox("Pole 'Nr domu' nie może zawierać znaków specjalnych", "Błąd")

    def validate_local_no(self, *args):
        local_no = self.local_no_var.get()

        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

        if (regex.search(local_no) == None):
            pass
        else:
            self.show_custom_messagebox("Pole 'Nr lokalu' nie może zawierać znaków specjalnych", "Błąd")

    def validate_city(self, *args):
        city = self.city_var.get()
        print(len(city))

        if len(city) > 64:
            self.show_custom_messagebox("Długość nazwy miasta nie może przekraczać 64 znaków", "Błąd")

        if any(chr.isdigit() for chr in city):
            self.show_custom_messagebox("Pole 'Miasto' nie może zawierać liczb", "Błąd")

        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

        if (regex.search(city) == None):
            pass
        else:
            self.show_custom_messagebox("Pole 'Miasto' nie może zawierać znaków specjalnych", "Błąd")

    def validate_postal_code(self, *args):
        postal_code = self.postal_code_var.get()
        print(len(postal_code))

        if len(postal_code) > 8:
            self.show_custom_messagebox("Długość kodu pocztowego nie może przekraczać 8 znaków", "Błąd")

        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

        if (regex.search(postal_code) == None):
            pass
        else:
            self.show_custom_messagebox("Pole 'Kod pocztowy' nie może zawierać znaków specjalnych", "Błąd")

    def validate_country(self, *args):
        country = self.country_var.get()
        print(len(country))

        if len(country) > 64:
            self.show_custom_messagebox("Długość nazwy kraju nie może przekraczać 64 znaków", "Błąd")

        if any(chr.isdigit() for chr in country):
            self.show_custom_messagebox("Pole 'Państwo' nie może zawierać liczb", "Błąd")

        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

        if (regex.search(country) == None):
            pass
        else:
            self.show_custom_messagebox("Pole 'Państwo' nie może zawierać znaków specjalnych", "Błąd")


    def validate_email(self, *args):
        email = self.email_var.get()
        print(len(email))

        if len(email) > 64:
            self.show_custom_messagebox("Długość adresu email nie może przekraczać 64 znaków", "Błąd")

    def validate_phone(self, *args):
        phone = self.phone_var.get()

        for i in phone:
            if i.isdigit() is False:
                self.show_custom_messagebox("Pole 'Nr telefonu nie może zawierać liter ani znaków specjalnych", "Błąd")
                return False
            else:
                return True

    def validate_personal_id(self, *args):
        pid = self.personal_id_var.get()

        for i in pid:
            if i.isdigit() is False:
                self.show_custom_messagebox("Pole 'PESEL' nie może zawierać liter", "Błąd")
                return False
            else:
                return True

    def validate_document_no(self, *args):
        doc_no = self.document_no_var.get()

        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

        if (regex.search(doc_no) == None):
            pass
        else:
            self.show_custom_messagebox("Pole 'Nr dokumentu' nie może zawierać znaków specjalnych", "Błąd")

        if len(doc_no) > 32:
            self.show_custom_messagebox("Długość numeru dokumentu nie może przekraczać 32 znaków", "Błąd")

    def validate_salary(self, *args):
        salary = self.salary_var.get()

        for i in salary:
            if i == " ":
                self.show_custom_messagebox("Pole 'Wypłata' nie może zawierać spacji", "Błąd")
                return False
            elif i.isdigit() is False and i != '.':
                self.show_custom_messagebox("Pole 'Wypłata' nie może zawierać liter ani znaków specjalnych", "Błąd")
                return False
            elif salary[0] == '.':
                self.show_custom_messagebox("Wartość pola 'Wypłata' nie może zaczynać się od kropki", "Błąd")
                return False
            else:
                d = decimal.Decimal(salary)
                if d.as_tuple().exponent == -1 or d.as_tuple().exponent <= -3:
                    self.show_custom_messagebox("Pole 'Wypłata' musi zawierać dwa miejsca po przecinku",
                                                "Błąd")
                    return False

            return True

    def validate_native_language(self, *args):
        native_language = self.native_language_var.get()

        if len(native_language) > 16:
            self.show_custom_messagebox("Wartość pola 'Język ojczysty' nie może przekraczać 16 znaków", "Błąd")

        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

        if (regex.search(native_language) == None):
            pass
        else:
            self.show_custom_messagebox("Pole 'Język ojczysty' nie może zawierać znaków specjalnych", "Błąd")

        if any(chr.isdigit() for chr in native_language):
            self.show_custom_messagebox("Pole 'Język ojczysty' nie może zawierać liczb", "Błąd")

    def validate_input(self,input_value, max_length, error_message, allow_empty=False, regex=None):
        if not allow_empty and not input_value.strip():
            self.show_custom_messagebox(f"Pole '{error_message}' nie może być puste\nPopraw formularz", "Błąd")
            return False
        if len(input_value) > max_length:
            self.show_custom_messagebox(error_message, "Błąd")
            return False
        if regex and regex.search(input_value):
            self.show_custom_messagebox(error_message, "Błąd")
            return False
        return True
    def validation_on_submission(self):

        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not self.validate_input(self.first_name_var.get(), 64, "Imię", allow_empty=False):
            return False
        if not self.validate_input(self.last_name_var.get(), 64, "Nazwisko", allow_empty=False):
            return False
        if not self.validate_input(self.street_var.get(), 128, "Ulica", allow_empty=False, regex=regex):
            return False
        if not self.validate_input(self.building_no_var.get(), float('inf'), "Nr domu", allow_empty=False, regex=regex):
            return False
        if not self.validate_input(self.local_no_var.get(), float('inf'), "Nr lokalu", allow_empty=True, regex=regex):
            return False
        if not self.validate_input(self.city_var.get(), 64, "Miasto", allow_empty=False, regex=regex):
            return False
        if not self.validate_input(self.postal_code_var.get(), 8, "Kod pocztowy", allow_empty=False, regex=regex):
            return False
        if not self.validate_input(self.country_var.get(), 64, "Państwo", allow_empty=False):
            return False
        if not self.validate_input(self.email_var.get(), 64, "Adres email", allow_empty=False):
            return False
        elif re.match(pattern, self.email_var.get()) is None:
            self.show_custom_messagebox("Format adresu email jest niepoprawny\nPopraw formularz", "Błąd")
            return False
        if not self.validate_phone():
            self.show_custom_messagebox(
                "Pole 'Nr telefonu' nie może zawierać liter ani znaków specjalnych\nPopraw formularz", "Błąd")
            return False
        elif len(self.phone_var.get()) == 0:
            self.show_custom_messagebox("Pole 'Nr telefonu' nie może być puste\nPopraw formularz")
        if not self.validate_input(self.native_language_var.get(), 16, "Język ojczysty", allow_empty=False, regex=regex):
            return False
        if not self.validate_personal_id():
            self.show_custom_messagebox("Pole 'PESEL' nie może zawierać liter\nPopraw formularz", "Błąd")
            return False
        elif len(self.personal_id_var.get()) == 0:
            self.show_custom_messagebox("Pole PESEL nie może być puste\nPopraw formularz")
            return False
        if not self.validate_input(self.document_no_var.get(), 32, "Nr dokumentu", allow_empty=False, regex=regex):
            return False
        if not self.validate_salary() or self.salary_var == '':
            self.show_custom_messagebox("Pole 'Wypłata' zawiera błędy\nPopraw formularz", "Błąd")
            return False
        elif len(self.salary_var.get()) == 0:
            self.show_custom_messagebox("Pole 'Wypłata' nie może być puste\nPopraw formularz", "Błąd")

        return True

    """
    Function that allows to generate a custom messagebox and control its position. 
    """

    def show_custom_messagebox(self, message, title):
        custom_mb = Toplevel(self.master)
        custom_mb.title(title)

        width = 700
        height = 130

        custom_mb.geometry(f"{width}x{height}")

        x_offset = 40
        y_offset = -70
        self.master.update_idletasks()  # Ensures the window is fully updated before getting its size
        x_pos = self.master.winfo_x() + (self.master.winfo_width() // 2) - (width // 2) + x_offset
        y_pos = self.master.winfo_y() + (self.master.winfo_height() // 2) - (height // 2) + y_offset
        custom_mb.geometry(f"+{x_pos}+{y_pos}")

        Label(custom_mb, text=message, font=('Open Sans', 12), pady=20).pack()
        Button(custom_mb, text="OK", command=custom_mb.destroy, width=20, height=1, font=('Open Sans', 12)).pack()
