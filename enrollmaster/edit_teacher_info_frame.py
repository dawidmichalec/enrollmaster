from tkinter import *
import ttkbootstrap as ttk
import psycopg2
import re
import decimal
from datetime import datetime
from dotenv import load_dotenv
import os


class EditTeacherInfoFrame(ttk.Frame):

    def __init__(self, master=None, amend_menu_content_func=None, **kw):
        super().__init__(master, **kw)
        self.amend_menu_content_func = amend_menu_content_func
        self.columnconfigure((0, 2, 3, 4, 5), weight=1, minsize=300)
        self.columnconfigure(1, weight=1, minsize=50)
        self.rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28),
            weight=1, minsize=30)

        self.teacher_id_var = StringVar()
        self.first_name_var = StringVar()
        self.last_name_var = StringVar()
        self.street_var = StringVar()
        self.building_no_var = StringVar()
        self.local_no_var = StringVar()
        self.city_var = StringVar()
        self.postal_code_var = StringVar()
        self.country_var = StringVar()
        self.email_var = StringVar()
        self.phone_number_var = StringVar()
        self.personal_id_var = StringVar()
        self.document_no_var = StringVar()
        self.document_var = StringVar()
        self.type_of_contract_var = StringVar()
        self.type_of_employment_var = StringVar()
        self.salary_var = StringVar()
        self.native_language_var = StringVar()
        self.language_to_teach_var = StringVar()
        self.employment_status_var = StringVar()
        self.date_var = StringVar()

        ## name of the frame/page

        teacher_label = ttk.Label(self, text='EDYTUJ NAUCZYCIELA', font=('Open Sans', 14, 'bold'),
                                  bootstyle='default')
        teacher_label.grid(row=0, column=3, sticky='w')

        ## teacher_id used for search purposes

        id_label = ttk.Label(self, text='ID Nauczyciela', font=('Open Sans', 12), bootstyle='default')
        id_label.grid(row=2, column=2, sticky='w')

        self.id_entry = ttk.Entry(self, bootstyle='light', width=20)
        self.id_entry.grid(row=3, column=2, sticky='w')

        ## first_name

        first_name_label = ttk.Label(self, text="Imię", font=('Open Sans', 12), bootstyle='default')
        first_name_label.grid(row=2, column=3, sticky='w')

        self.first_name = ttk.Entry(self, width=20, bootstyle='light')
        self.first_name.grid(row=3, column=3, sticky='w')

        ## last_name

        last_name_label = ttk.Label(self, text="Nazwisko", font=('Open Sans', 12), bootstyle='default')
        last_name_label.grid(row=2, column=4, sticky='w')

        self.last_name = ttk.Entry(self, width=20, bootstyle='light')
        self.last_name.grid(row=3, column=4, sticky='w')

        ## submit button

        submit_button_style = ttk.Style()
        submit_button_style.configure('success.TButton', font=('Open Sans', 14))

        submit_button = ttk.Button(self, bootstyle='success', text='SZUKAJ', width=15,
                                   style='success.TButton', command=self.search_function)
        submit_button.grid(row=5, column=3, sticky='w')

        # teacher_id

        teacher_id_label = ttk.Label(self, text='ID Nauczyciela', font=('Open Sans', 12),
                                     bootstyle='default')
        teacher_id_label.grid(row=8, column=0, sticky='w')

        self.teacher_id = ttk.Entry(self, bootstyle='default', width=15, textvariable=self.teacher_id_var)
        self.teacher_id.configure(state='readonly')
        self.teacher_id.grid(row=9, column=0, sticky='w')

        # output_first_name

        output_first_name_label = ttk.Label(self, text='Imię', font=('Open Sans', 12),
                                            bootstyle='default')
        output_first_name_label.grid(row=8, column=2, sticky='w')

        self.output_first_name = ttk.Entry(self, bootstyle='default', width=20, textvariable=self.first_name_var)
        self.output_first_name.configure(state='readonly')
        self.output_first_name.grid(row=9, column=2, sticky='w')

        # output_last_name

        output_last_name_label = ttk.Label(self, text='Nazwisko', font=('Open Sans', 12),
                                           bootstyle='default')
        output_last_name_label.grid(row=8, column=3, sticky='w')

        self.output_last_name = ttk.Entry(self, bootstyle='default', width=20, textvariable=self.last_name_var)
        self.output_last_name.configure(state='readonly')
        self.output_last_name.grid(row=9, column=3, sticky='w')

        # output_street

        output_street_label = ttk.Label(self, text='Ulica', font=('Open Sans', 12), bootstyle='default')
        output_street_label.grid(row=8, column=4, sticky='w')

        self.output_street = ttk.Entry(self, bootstyle='default', width=30, textvariable=self.street_var)
        self.output_street.configure(state='readonly')
        self.output_street.grid(row=9, column=4, sticky='w')

        # output_building_no

        output_building_no_label = ttk.Label(self, text='Nr domu', font=('Open Sans', 12),
                                             bootstyle='default')
        output_building_no_label.grid(row=11, column=0, sticky='w')

        self.output_building_no = ttk.Entry(self, bootstyle='default', width=15, textvariable=self.building_no_var)
        self.output_building_no.configure(state='readonly')
        self.output_building_no.grid(row=12, column=0, sticky='w')

        # local_no_output

        local_no_output_label = ttk.Label(self, text='Nr lokalu', font=('Open Sans', 12),
                                          bootstyle='default')
        local_no_output_label.grid(row=11, column=2, sticky='w')

        self.local_no_output = ttk.Entry(self, bootstyle='default', width=15, textvariable=self.local_no_var)
        self.local_no_output.configure(state='readonly')
        self.local_no_output.grid(row=12, column=2, sticky='w')

        # city_output

        city_output_label = ttk.Label(self, text='Miasto', font=('Open Sans', 12), bootstyle='default')
        city_output_label.grid(row=11, column=3, sticky='w')

        self.city_output = ttk.Entry(self, bootstyle='default', width=20, textvariable=self.city_var)
        self.city_output.configure(state='readonly')
        self.city_output.grid(row=12, column=3, sticky='w')

        # postal_code_output

        postal_code_output_label = ttk.Label(self, text='Kod pocztowy', font=('Open Sans', 12),
                                             bootstyle='default')
        postal_code_output_label.grid(row=11, column=4, sticky='w')

        self.postal_code_output = ttk.Entry(self, bootstyle='default', width=15, textvariable=self.postal_code_var)
        self.postal_code_output.configure(state='readonly')
        self.postal_code_output.grid(row=12, column=4, sticky='w')

        # country_output

        country_output_label = ttk.Label(self, text='Państwo', font=('Open Sans', 12),
                                         bootstyle='default')
        country_output_label.grid(row=11, column=5, sticky='w')

        self.country_output = ttk.Entry(self, bootstyle='default', width=25, textvariable=self.country_var)
        self.country_output.configure(state='readonly')
        self.country_output.grid(row=12, column=5, sticky='w')

        # email_output

        email_output_label = ttk.Label(self, text='Adres e-mail', font=('Open Sans', 12),
                                       bootstyle='default')
        email_output_label.grid(row=14, column=0, sticky='w')

        self.email_output = ttk.Entry(self, bootstyle='default', width=25, textvariable=self.email_var)
        self.email_output.configure(state='readonly')
        self.email_output.grid(row=15, column=0, sticky='w')

        # phone_number_output

        phone_number_output_label = ttk.Label(self, text='Nr telefonu', font=('Open Sans', 12),
                                              bootstyle='default')
        phone_number_output_label.grid(row=14, column=2, sticky='w')

        self.phone_number_output = ttk.Entry(self, bootstyle='default', width=25, textvariable=self.phone_number_var)
        self.phone_number_output.configure(state='readonly')
        self.phone_number_output.grid(row=15, column=2, sticky='w')

        # personal_id_output

        personal_id_output_label = ttk.Label(self, text='PESEL', font=('Open Sans', 12),
                                             bootstyle='default')
        personal_id_output_label.grid(row=14, column=3, sticky='w')

        self.personal_id_output = ttk.Entry(self, bootstyle='default', width=25, textvariable=self.personal_id_var)
        self.personal_id_output.configure(state='readonly')
        self.personal_id_output.grid(row=15, column=3, sticky='w')

        # document_no_output

        document_no_output_label = ttk.Label(self, text='Nr dokumentu', font=('Open Sans', 12),
                                             bootstyle='default')
        document_no_output_label.grid(row=14, column=4, sticky='w')

        self.document_no_output = ttk.Entry(self, bootstyle='default', width=25, textvariable=self.document_no_var)
        self.document_no_output.configure(state='readonly')
        self.document_no_output.grid(row=15, column=4, sticky='w')

        # document_type_output

        document_type_output_label = ttk.Label(self, text='Rodzaj dokumentu', font=('Open Sans', 12),
                                               bootstyle='default')
        document_type_output_label.grid(row=14, column=5, sticky='w')

        self.document_type_output = ttk.Menubutton(self, bootstyle='dark')
        self.document_type_output.configure(state='disabled')
        self.document_type_output.grid(row=15, column=5, sticky='w')

        document_type_content = ttk.Menu(self.document_type_output)

        self.document_var.set("")
        for document in ['Dowód osobisty', 'Paszport', 'Karta pobytu']:
            document_type_content.add_radiobutton(label=document, variable=self.document_var, value=document,
                                                  command=self.on_document_type_select)

        self.document_type_output['menu'] = document_type_content

        # type_of_contract_output

        type_of_contract_label = ttk.Label(self, text='Rodzaj umowy', font=('Open Sans', 12),
                                                  bootstyle='default')
        type_of_contract_label.grid(row=17, column=0, sticky='w')

        self.type_of_contract = ttk.Menubutton(self, bootstyle='dark')
        self.type_of_contract.configure(state='disabled')
        self.type_of_contract.grid(row=18, column=0, sticky='w')

        type_of_contract_output_content = ttk.Menu(self.type_of_contract)

        self.type_of_contract_var.set("")

        for contract in ['Umowa o pracę', 'Umowa zlecenie']:
            type_of_contract_output_content.add_radiobutton(label=contract, variable=self.type_of_contract_var,
                                                            value=contract, command=self.on_contract_type_select)

        self.type_of_contract['menu'] = type_of_contract_output_content

        # type_of_employment_output

        type_of_employment_output_label = ttk.Label(self, text='Rodzaj zatrudnienia',
                                                    font=('Open Sans', 12),
                                                    bootstyle='default')
        type_of_employment_output_label.grid(row=17, column=2, sticky='w')

        self.type_of_employment_output = ttk.Menubutton(self, bootstyle='dark')
        self.type_of_employment_output.configure(state='disabled')
        self.type_of_employment_output.grid(row=18, column=2, sticky='w')

        type_of_employment_output_content = ttk.Menu(self.type_of_employment_output)

        self.type_of_employment_var.set("")

        for employment in ['Pełny etat', 'Pół etatu']:
            type_of_employment_output_content.add_radiobutton(label=employment, variable=self.type_of_employment_var,
                                                              value=employment, command=self.on_employment_type_select)

        self.type_of_employment_output['menu'] = type_of_employment_output_content

        # salary_output

        salary_output_label = ttk.Label(self, text='Wynagrodzenie', font=('Open Sans', 12),
                                        bootstyle='default')
        salary_output_label.grid(row=17, column=3, sticky='w')

        self.salary_output = ttk.Entry(self, bootstyle='default', width=25, textvariable=self.salary_var)
        self.salary_output.configure(state='readonly')
        self.salary_output.grid(row=18, column=3, sticky='w')

        ## native_language_output

        native_language_output_label = ttk.Label(self, text='Język ojczysty', font=('Open Sans', 12),
                                                 bootstyle='default')
        native_language_output_label.grid(row=17, column=4, sticky='w')

        self.native_language_output = ttk.Entry(self, bootstyle='default', width=25, textvariable=self.native_language_var)
        self.native_language_output.configure(state='readonly')
        self.native_language_output.grid(row=18, column=4, sticky='w')

        ## language_to_teach_output

        language_to_teach_output_label = ttk.Label(self, text='Język nauczania', font=('Open Sans', 12),
                                                   bootstyle='default')
        language_to_teach_output_label.grid(row=17, column=5, sticky='w')

        self.language_to_teach = ttk.Menubutton(self, bootstyle='dark')
        self.language_to_teach.configure(state='disabled')
        self.language_to_teach.grid(row=18, column=5, sticky='w')

        language_to_teach_content = ttk.Menu(self.language_to_teach)

        self.language_to_teach_var.set("")

        for language in ['Angielski', 'Niemiecki', 'Francuski', 'Włoski', 'Hiszpański']:
            language_to_teach_content.add_radiobutton(label=language, variable=self.language_to_teach_var, value=language,
                                                      command=self.on_language_to_teach_select)

        self.language_to_teach['menu'] = language_to_teach_content

        ## start_date_output

        start_date_output_label = ttk.Label(self, text='Data rozpoczęcia pracy', font=('Open Sans', 12),
                                            bootstyle='default')
        start_date_output_label.grid(row=20, column=0, sticky='w')

        self.start_date_output = ttk.DateEntry(self, bootstyle='primary')
        self.start_date_output.configure(state='readonly')
        self.date_var.set("")
        self.start_date_output.entry.configure(textvariable=self.date_var)
        self.start_date_output.grid(row=21, column=0, sticky='w')

        ## status_of_employment

        status_of_employment_label = ttk.Label(self, text='Status zatrudnienia', font=('Open Sans', 12),
                                               bootstyle='default')
        status_of_employment_label.grid(row=20, column=2, sticky='w')

        self.status_of_employment = ttk.Entry(self, bootstyle='default', width=25, textvariable=self.employment_status_var)
        self.status_of_employment.configure(state='readonly')
        self.status_of_employment.grid(row=21, column=2, sticky='w')

        ## edit button
        """
        When clicked, the entries change status from readonly to editable. 
        """

        edit_button_style = ttk.Style()
        edit_button_style.configure('primary.TButton', font=('Open Sans', 14))

        self.edit_button = ttk.Button(self, bootstyle='primary', text='EDYTUJ', width=16,
                                 style='primary.TButton', command=self.edit_function)
        self.edit_button.grid(row=24, column=2, sticky='w')
        self.edit_button['state'] = 'disabled'

        ## save_button

        self.save_button = ttk.Button(self, bootstyle='info', text='ZAPISZ', width=16, command=self.save_button_function)
        self.save_button.grid(row=24, column=3, sticky='w')
        self.save_button['state'] = 'disabled'

        ## block_button

        block_button_style = ttk.Style()
        block_button_style.configure('warning.TButton', font=('Open Sans', 14))

        self.block_button = ttk.Button(self, bootstyle='warning', text='ZABLOKUJ', width=16, command=self.block_function)
        self.block_button.grid(row=24, column=4, sticky='w')
        self.block_button['state'] = 'disabled'

        ## cancel_button - sets entries back to the readonly state and buttons do disabled state, including itself

        cancel_button_style = ttk.Style()
        cancel_button_style.configure('danger.TButton', font=('Open Sans', 14))

        self.cancel_button = ttk.Button(self, bootstyle='danger', text='ODRZUĆ', width=16, command=self.cancel_button_function)
        self.cancel_button.grid(row=26, column=3, sticky='w')
        self.cancel_button['state'] = 'disabled'

        self.pack()

    def establish_database_connection(self):
        # Connect to the PostgreSQL database
        load_dotenv()

        connection = psycopg2.connect(
            database=os.getenv('DB_NAME'),
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            port=os.getenv('DB_PORT')
        )
        return connection

    def search_function(self):
        # Connect to the PostgreSQL database
        connection = self.establish_database_connection()

        teacher_id = self.id_entry.get()
        first_name = self.first_name.get()
        last_name = self.last_name.get()

        try:
            cursor = connection.cursor()
            if not teacher_id and not first_name and not last_name:
                self.show_custom_information("Należy podać ID nauczyciela lub imię oraz nazwisko", "Błąd")
                return

            # Check if only ID is provided
            if teacher_id and not (first_name or last_name):
                query = """SELECT  
                                    teacher_id, 
                                    first_name, 
                                    last_name, 
                                    street, 
                                    building_no, 
                                    local_no,
                                    city, 
                                    postal_code, 
                                    country, 
                                    email, 
                                    phone,
                                    personal_id,
                                    document_no,
                                    document_type, 
                                    type_of_contract, 
                                    type_of_employment,
                                    salary,
                                    native_language, 
                                    language_to_teach, 
                                    employment_start,
                                    status_of_employment FROM teachers  
                                    WHERE teacher_id = %s;"""
                cursor.execute(query, (teacher_id,))
                # Check if both first name and last name are provided
            elif first_name and last_name:
                query = """SELECT
                                    teacher_id, 
                                    first_name, 
                                    last_name, 
                                    street, 
                                    building_no, 
                                    local_no,
                                    city, 
                                    postal_code, 
                                    country, 
                                    email, 
                                    phone,
                                    personal_id,
                                    document_no,
                                    document_type, 
                                    type_of_contract, 
                                    type_of_employment,
                                    salary,
                                    native_language, 
                                    language_to_teach, 
                                    employment_start,
                                    status_of_employment FROM teachers  WHERE first_name = %s AND last_name = %s;"""
                cursor.execute(query, (first_name, last_name))
                # Check if only first name or only last name is provided
            elif first_name or last_name:
                self.show_custom_information("Należy podać ID nauczyciela lub imię oraz nazwisko", "Błąd")
                return
            # If all three values are provided
            else:
                query = """SELECT
                            teacher_id, 
                            first_name, 
                            last_name, 
                            street, 
                            building_no, 
                            local_no,
                            city, 
                            postal_code, 
                            country, 
                            email, 
                            phone,
                            personal_id,
                            document_no,
                            document_type, 
                            type_of_contract, 
                            type_of_employment,
                            salary,
                            native_language, 
                            language_to_teach, 
                            employment_start,
                            status_of_employment FROM teachers 
                            WHERE teacher_id = %s AND first_name = %s AND last_name = %s;"""
                cursor.execute(query, (teacher_id, first_name, last_name))

            # Fetch and return the results
            results = cursor.fetchone()

            if not results:
                self.show_custom_information("Nie znaleziono nauczyciela. Sprawdź czy podałeś poprawne dane", "Info")
            else:
                # If the search is successful, unblock edit and block buttons:
                self.edit_button['state'] = 'normal'
                self.block_button['state'] = 'normal'

                teacher_id, first_name, last_name, street, building_no, local_no, city, postal_code, country, email,\
                    phone,personal_id, document_no, document_type, type_of_contract, type_of_employment, salary,\
                    native_language, language_to_teach, employment_start, status_of_employment = results

                self.teacher_id_var.set(teacher_id)
                self.first_name_var.set(first_name)
                self.last_name_var.set(last_name)
                self.street_var.set(street)
                self.building_no_var.set(building_no)
                self.local_no_var.set(local_no)
                self.city_var.set(city)
                self.postal_code_var.set(postal_code)
                self.country_var.set(country)
                self.email_var.set(email)
                self.phone_number_var.set(phone)
                self.personal_id_var.set(personal_id)
                self.document_no_var.set(document_no)
                self.document_type_output.configure(text=document_type)
                self.document_var.set(document_type)
                self.type_of_contract.configure(text=type_of_contract)
                self.type_of_contract_var.set(type_of_contract)
                self.type_of_employment_output.configure(text=type_of_employment)
                self.type_of_employment_var.set(type_of_employment)
                self.salary_var.set(salary)
                self.native_language_var.set(native_language)
                self.language_to_teach.configure(text=language_to_teach)
                self.language_to_teach_var.set(language_to_teach)
                self.employment_status_var.set(status_of_employment)

                # Extract the date portion from the timestamp string
                date_str = str(employment_start).split()[0]

                # Parse the date string into a datetime object
                db_date = datetime.strptime(date_str, "%Y-%m-%d").strftime("%d-%m-%Y")
                new_date = db_date.replace("-", ".")
                self.start_date_output.entry.configure(textvariable=self.date_var)
                self.date_var.set(new_date)

        finally:
            # Close the database connection
            connection.close()

    def save_button_function(self):
        self.show_custom_messagebox("Czy na pewno chcesz zapisać wprowadzone zmiany?",
                                    "Ostrzeżenie",
                                    self.save_function,
                                    self.dismiss_messagebox)

    def save_function(self):
        connection = self.establish_database_connection()
        validation = self.validation_on_submission()

        try:
            if validation is True:
                cursor = connection.cursor()
                teacher_id = self.teacher_id_var.get()
                first_name = self.first_name_var.get()
                last_name = self.last_name_var.get()
                street = self.street_var.get()
                building_no = self.building_no_var.get()
                local_no = self.local_no_var.get()
                if local_no == "None":
                    local_no = None
                city = self.city_var.get()
                postal_code = self.postal_code_var.get()
                country = self.country_var.get()
                email = self.email_var.get()
                if email == "None":
                    email = None
                phone = self.phone_number_var.get()
                personal_id = self.personal_id_var.get()
                document_no = self.document_no_var.get()
                document_type = self.on_document_type_select()
                type_of_contract = self.on_contract_type_select()
                type_of_employment = self.on_employment_type_select()
                salary = self.salary_var.get()
                native_language = self.native_language_var.get()
                language_to_teach = self.on_language_to_teach_select()
                employment_start = self.start_date_output.entry.get()

                query = """
                        UPDATE teachers
                        SET 
                            first_name = %s,
                            last_name = %s,
                            street = %s,
                            building_no = %s,
                            local_no = %s,
                            city = %s,
                            postal_code = %s,
                            country = %s,
                            email = %s,
                            phone = %s,
                            personal_id = %s,
                            document_no = %s,
                            document_type = %s,
                            type_of_contract = %s,
                            type_of_employment = %s,
                            salary = %s,
                            native_language = %s,
                            language_to_teach = %s,
                            employment_start = %s
                        WHERE teacher_id = %s;
                        """

                cursor.execute(query, (first_name, last_name, street, building_no, local_no, city,
                                       postal_code, country, email, phone, personal_id, document_no, document_type,
                                       type_of_contract, type_of_employment, salary, native_language, language_to_teach,
                                       employment_start, teacher_id))
                connection.commit()
                self.clear_entries()
                self.block_entries()
                self.cancel_button['state'] = 'disabled'
                self.save_button['state'] = 'disabled'
                self.edit_button['state'] = 'disabled'
                self.block_button['state'] = 'disabled'
                self.show_custom_information("Dane nauczyciela zostały zaktualizowane", "Info")

        finally:
            connection.close()

    def block_function(self):
        self.show_custom_messagebox("Czy na pewno chcesz zablokować tego nauczyciela?",
                                    "Ostrzeżenie",
                                    self.block_teacher,
                                    self.dismiss_messagebox)

    def block_teacher(self):

        connection = self.establish_database_connection()

        try:
            cursor = connection.cursor()
            teacher_id = self.teacher_id_var.get()

            query = """
                    UPDATE teachers
                    SET status_of_employment = 'Nieaktywny'
                    WHERE teacher_id = %s;"""
            cursor.execute(query, (teacher_id,))
            connection.commit()

            self.clear_entries()
            self.block_entries()
            self.cancel_button['state'] = 'disabled'
            self.save_button['state'] = 'disabled'
            self.edit_button['state'] = 'disabled'
            self.block_button['state'] = 'disabled'
            self.show_custom_information("Nauczyciel został zablokowany", "Info")
        finally:
            connection.close()

    def edit_function(self):

        # unblock cancel and save buttons
        self.cancel_button['state'] = 'normal'
        self.save_button['state'] = 'normal'

        # allow the user to change the data

        self.output_first_name.configure(state='')
        self.output_last_name.configure(state='')
        self.output_street.configure(state='')
        self.output_building_no.configure(state='')
        self.local_no_output.configure(state='')
        self.city_output.configure(state='')
        self.postal_code_output.configure(state='')
        self.country_output.configure(state='')
        self.email_output.configure(state='')
        self.phone_number_output.configure(state='')
        self.personal_id_output.configure(state='')
        self.document_no_output.configure(state='')
        self.document_type_output.configure(state='')
        self.type_of_contract.configure(state='')
        self.type_of_employment_output.configure(state='')
        self.salary_output.configure(state='')
        self.native_language_output.configure(state='')
        self.language_to_teach.configure(state='')
        self.start_date_output.configure(state='normal')

        self.first_name_var.trace_add('write', self.validate_first_name)
        self.last_name_var.trace_add('write', self.validate_last_name)
        self.street_var.trace_add('write', self.validate_street)
        self.building_no_var.trace_add('write', self.validate_building_no)
        self.local_no_var.trace_add('write', self.validate_local_no)
        self.city_var.trace_add('write', self.validate_city)
        self.postal_code_var.trace_add('write', self.validate_postal_code)
        self.country_var.trace_add('write', self.validate_country)
        self.email_var.trace_add('write', self.validate_email)
        self.phone_number_var.trace_add('write', self.validate_phone)
        self.personal_id_var.trace_add('write', self.validate_personal_id)
        self.document_no_var.trace_add('write', self.validate_document_no)
        self.salary_var.trace_add('write', self.validate_salary)
        self.native_language_var.trace_add('write', self.validate_native_language)

    def cancel_button_function(self):
        self.show_custom_messagebox("Czy na pewno chcesz odrzucić zmiany?",
                                    "Ostrzeżenie",
                                    self.cancel_function,
                                    self.dismiss_messagebox)

    def cancel_function(self):
        self.clear_entries()
        self.block_entries()
        self.cancel_button['state'] = 'disabled'
        self.save_button['state'] = 'disabled'
        self.edit_button['state'] = 'disabled'
        self.block_button['state'] = 'disabled'

    def clear_entries(self):

        self.teacher_id_var.set("")
        self.first_name_var.set("")
        self.last_name_var.set("")
        self.street_var.set("")
        self.building_no_var.set("")
        self.local_no_var.set("")
        self.city_var.set("")
        self.postal_code_var.set("")
        self.country_var.set("")
        self.email_var.set("")
        self.phone_number_var.set("")
        self.personal_id_var.set("")
        self.document_no_var.set("")
        self.document_var.set("")
        self.document_type_output.configure(text='')
        self.type_of_contract_var.set("")
        self.type_of_contract.configure(text='')
        self.type_of_employment_var.set("")
        self.type_of_employment_output.configure(text='')
        self.salary_var.set("")
        self.native_language_var.set("")
        self.language_to_teach_var.set("")
        self.language_to_teach.configure(text='')
        self.employment_status_var.set("")
        self.date_var.set("")

    def block_entries(self):
        self.output_first_name.configure(state='readonly')
        self.output_last_name.configure(state='readonly')
        self.output_street.configure(state='readonly')
        self.output_building_no.configure(state='readonly')
        self.local_no_output.configure(state='readonly')
        self.city_output.configure(state='readonly')
        self.postal_code_output.configure(state='readonly')
        self.country_output.configure(state='readonly')
        self.email_output.configure(state='readonly')
        self.phone_number_output.configure(state='readonly')
        self.personal_id_output.configure(state='readonly')
        self.document_no_output.configure(state='readonly')
        self.document_type_output.configure(state='disabled')
        self.type_of_contract.configure(state='disabled')
        self.type_of_employment_output.configure(state='disabled')
        self.salary_output.configure(state='readonly')
        self.native_language_output.configure(state='readonly')
        self.language_to_teach.configure(state='disabled')
        self.start_date_output.configure(state='readonly')

    def dismiss_messagebox(self):
        # Do nothing, just dismiss the messagebox
        print("Messagebox dismissed.")

    """
    Functions for dropdown selection.
    """

    def on_document_type_select(self):
        selected_document_type = self.document_var.get()
        print("Selected document type:", selected_document_type)
        self.amend_menu_content_func(self.document_type_output, selected_document_type)
        return selected_document_type

    def on_language_to_teach_select(self):
        selected_language = self.language_to_teach_var.get()
        print("Selected language:", selected_language)
        self.amend_menu_content_func(self.language_to_teach, selected_language)
        return selected_language

    def on_contract_type_select(self):
        selected_contract_type = self.type_of_contract_var.get()
        print("Selected type of contract:", selected_contract_type)
        self.amend_menu_content_func(self.type_of_contract, selected_contract_type)
        return selected_contract_type

    def on_employment_type_select(self):
        selected_employment_type = self.type_of_employment_var.get()
        print("Selected type of employment:", selected_employment_type)
        self.amend_menu_content_func(self.type_of_employment_output, selected_employment_type)
        return selected_employment_type

    # Custom messagebox

    def show_custom_messagebox(self, message, title, action_yes, action_no):
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

        # Add "Yes" button
        Button(custom_mb, text="Yes", command=lambda: self.yesno_response(custom_mb, True, action_yes),
               width=10, height=1, font=('Open Sans', 12)).pack(side='left', padx=10)

        # Add "No" button
        Button(custom_mb, text="No", command=lambda: self.yesno_response(custom_mb, False, action_no),
               width=10, height=1, font=('Open Sans', 12)).pack(side='right', padx=10)

    def show_custom_information(self, message, title):
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

    def yesno_response(self, custom_mb, response, action):
        # Do something with the response (True for "Yes", False for "No")
        print("User response:", response)
        # Call the associated action
        action()
        # Close the messagebox
        custom_mb.destroy()

    """
    Validation functions
    """

    def validate_first_name(self, *args):
        first_name = self.first_name_var.get()
        print(len(first_name))

        if len(first_name) > 64:
            self.show_custom_information("Długość imienia nie może przekraczać 64 znaków", "Błąd")

        if any(chr.isdigit() for chr in first_name):
            self.show_custom_information("Pole 'Imię' nie może zawierać liczb", "Błąd")

        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

        if (regex.search(first_name) == None):
            pass
        else:
            self.show_custom_information("Pole 'Imię' nie może zawierać znaków specjalnych", "Błąd")

    def validate_last_name(self, *args):
        last_name = self.last_name_var.get()
        print(len(last_name))

        if len(last_name) > 64:
            self.show_custom_information("Długość nazwiska nie może przekraczać 64 znaków", "Błąd")

        if any(chr.isdigit() for chr in last_name):
            self.show_custom_information("Pole 'Nazwisko' nie może zawierać liczb", "Błąd")

        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

        if (regex.search(last_name) == None):
            pass
        else:
            self.show_custom_information("Pole 'Nazwisko' nie może zawierać znaków specjalnych", "Błąd")

    def validate_street(self, *args):
        street = self.street_var.get()
        print(len(street))

        if len(street) > 128:
            self.show_custom_information("Długość nazwy ulicy nie może przekraczać 128 znaków", "Błąd")

        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

        if (regex.search(street) == None):
            pass
        else:
            self.show_custom_information("Pole 'Ulica' nie może zawierać znaków specjalnych", "Błąd")

    def validate_building_no(self, *args):
        building_no = self.building_no_var.get()

        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

        if (regex.search(building_no) == None):
            pass
        else:
            self.show_custom_information("Pole 'Nr domu' nie może zawierać znaków specjalnych", "Błąd")

    def validate_local_no(self, *args):
        local_no = self.local_no_var.get()

        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

        if (regex.search(local_no) == None):
            pass
        else:
            self.show_custom_information("Pole 'Nr lokalu' nie może zawierać znaków specjalnych", "Błąd")

    def validate_city(self, *args):
        city = self.city_var.get()
        print(len(city))

        if len(city) > 64:
            self.show_custom_information("Długość nazwy miasta nie może przekraczać 64 znaków", "Błąd")

        if any(chr.isdigit() for chr in city):
            self.show_custom_information("Pole 'Miasto' nie może zawierać liczb", "Błąd")

        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

        if (regex.search(city) == None):
            pass
        else:
            self.show_custom_information("Pole 'Miasto' nie może zawierać znaków specjalnych", "Błąd")

    def validate_postal_code(self, *args):
        postal_code = self.postal_code_var.get()
        print(len(postal_code))

        if len(postal_code) > 8:
            self.show_custom_information("Długość kodu pocztowego nie może przekraczać 8 znaków", "Błąd")

        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

        if (regex.search(postal_code) == None):
            pass
        else:
            self.show_custom_information("Pole 'Kod pocztowy' nie może zawierać znaków specjalnych", "Błąd")

    def validate_country(self, *args):
        country = self.country_var.get()
        print(len(country))

        if len(country) > 64:
            self.show_custom_information("Długość nazwy kraju nie może przekraczać 64 znaków", "Błąd")

        if any(chr.isdigit() for chr in country):
            self.show_custom_information("Pole 'Państwo' nie może zawierać liczb", "Błąd")

        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

        if (regex.search(country) == None):
            pass
        else:
            self.show_custom_information("Pole 'Państwo' nie może zawierać znaków specjalnych", "Błąd")

    def validate_email(self, *args):
        email = self.email_var.get()
        print(len(email))

        if len(email) > 64:
            self.show_custom_information("Długość adresu email nie może przekraczać 64 znaków", "Błąd")

    def validate_phone(self, *args):
        phone = self.phone_number_var.get()

        for i in phone:
            if i.isdigit() is False:
                self.show_custom_information("Pole 'Nr telefonu nie może zawierać liter ani znaków specjalnych", "Błąd")
                return False
            else:
                return True

    def validate_personal_id(self, *args):
        pid = self.personal_id_var.get()

        for i in pid:
            if i.isdigit() is False:
                self.show_custom_information("Pole 'PESEL' nie może zawierać liter", "Błąd")
                return False
            else:
                return True

    def validate_document_no(self, *args):
        doc_no = self.document_no_var.get()

        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

        if (regex.search(doc_no) == None):
            pass
        else:
            self.show_custom_information("Pole 'Nr dokumentu' nie może zawierać znaków specjalnych", "Błąd")

        if len(doc_no) > 32:
            self.show_custom_information("Długość numeru dokumentu nie może przekraczać 32 znaków", "Błąd")

    def validate_salary(self, *args):
        salary = self.salary_var.get()

        for i in salary:
            if i == " ":
                self.show_custom_information("Pole 'Wypłata' nie może zawierać spacji", "Błąd")
                return False
            elif i.isdigit() is False and i != '.':
                self.show_custom_information("Pole 'Wypłata' nie może zawierać liter ani znaków specjalnych", "Błąd")
                return False
            elif salary[0] == '.':
                self.show_custom_information("Wartość pola 'Wypłata' nie może zaczynać się od kropki", "Błąd")
                return False
            else:
                d = decimal.Decimal(salary)
                if d.as_tuple().exponent == -1 or d.as_tuple().exponent <= -3:
                    self.show_custom_information("Pole 'Wypłata' musi zawierać dwa miejsca po przecinku",
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
            self.show_custom_information("Pole 'Język ojczysty' nie może zawierać znaków specjalnych", "Błąd")

        if any(chr.isdigit() for chr in native_language):
            self.show_custom_information("Pole 'Język ojczysty' nie może zawierać liczb", "Błąd")

    def validate_input(self, input_value, max_length, error_message, allow_empty=False, regex=None):
        if not allow_empty and not input_value.strip():
            self.show_custom_information(f"Pole '{error_message}' nie może być puste\nPopraw formularz", "Błąd")
            return False
        if len(input_value) > max_length:
            self.show_custom_information(error_message, "Błąd")
            return False
        if regex and regex.search(input_value):
            self.show_custom_information(error_message, "Błąd")
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
            self.show_custom_information("Format adresu email jest niepoprawny\nPopraw formularz", "Błąd")
            return False
        if not self.validate_phone():
            self.show_custom_information(
                "Pole 'Nr telefonu' nie może zawierać liter ani znaków specjalnych\nPopraw formularz", "Błąd")
            return False
        elif len(self.phone_number_var.get()) == 0:
            self.show_custom_information("Pole 'Nr telefonu' nie może być puste\nPopraw formularz")
        if not self.validate_input(self.native_language_var.get(), 16, "Język ojczysty", allow_empty=False,
                                   regex=regex):
            return False
        if not self.validate_personal_id():
            self.show_custom_information("Pole 'PESEL' nie może zawierać liter\nPopraw formularz", "Błąd")
            return False
        elif len(self.personal_id_var.get()) == 0:
            self.show_custom_information("Pole PESEL nie może być puste\nPopraw formularz")
            return False
        if not self.validate_input(self.document_no_var.get(), 32, "Nr dokumentu", allow_empty=False, regex=regex):
            return False
        if not self.validate_salary() or self.salary_var == '':
            self.show_custom_information("Pole 'Wypłata' zawiera błędy\nPopraw formularz", "Błąd")
            return False
        elif len(self.salary_var.get()) == 0:
            self.show_custom_information("Pole 'Wypłata' nie może być puste\nPopraw formularz", "Błąd")

        return True
