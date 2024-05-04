from tkinter import *
import ttkbootstrap as ttk
from datetime import datetime, timedelta
import psycopg2
import re
import decimal

class NewStudentFrame(ttk.Frame):

    def __init__(self, master=None, amend_menu_content_func=None, **kw):
        super().__init__(master, **kw)
        self.amend_menu_content_func = amend_menu_content_func
        self.columnconfigure((0, 2, 3, 4, 5), weight=1, minsize=300)
        self.columnconfigure(1, weight=1, minsize=50)
        self.rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28),
            weight=1, minsize=30)

        new_student_label = ttk.Label(self, text="NOWY UCZEŃ", font=('Open Sans', 14, 'bold'),
                                      bootstyle='default')
        new_student_label.grid(column=3, row=0, sticky='w')

        ## first_name

        first_name_label = ttk.Label(self, text="Imię*", font=('Open Sans', 12), bootstyle='default')
        first_name_label.grid(row=2, column=0, sticky='w')

        self.first_name_var = StringVar()

        self.first_name = ttk.Entry(self, width=30, bootstyle='light', textvariable=self.first_name_var)
        self.first_name.grid(row=3, column=0, sticky='w')

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
        personal_id_label.grid(row=14, column=0, sticky='w')

        self.personal_id_var = StringVar()

        self.personal_id = ttk.Entry(self, width=20, bootstyle='light', textvariable=self.personal_id_var)
        self.personal_id.grid(row=15, column=0, sticky='w')

        self.personal_id_var.trace_add('write', self.validate_personal_id)

        ## document_no

        document_no_label = ttk.Label(self, text="Nr dokumentu*", font=('Open Sans', 12),
                                      bootstyle='default')
        document_no_label.grid(row=14, column=2, sticky='w')

        self.document_no_var = StringVar()

        self.document_no = ttk.Entry(self, width=20, bootstyle='light', textvariable=self.document_no_var)
        self.document_no.grid(row=15, column=2, sticky='w')

        self.document_no_var.trace_add('write', self.validate_document_no)

        ## document_type

        document_type_label = ttk.Label(self, text="Rodzaj dokumentu*", font=('Open Sans', 12),
                                        bootstyle='default')
        document_type_label.grid(row=14, column=3, sticky='w')

        self.document_type = ttk.Menubutton(self, bootstyle='dark', text="Wybierz dokument")
        self.document_type.grid(row=15, column=3, sticky='w')

        document_type_content = ttk.Menu(self.document_type)

        self.document_var = ttk.StringVar()
        self.document_var.set("")

        for document in ['Dowód osobisty', 'Paszport', 'Karta pobytu']:
            document_type_content.add_radiobutton(label=document, variable=self.document_var, value=document,
                                                  command=self.on_document_type_select)

        self.document_type['menu'] = document_type_content

        ## language

        language_label = ttk.Label(self, text="Język kursu*", font=('Open Sans', 12), bootstyle='default')
        language_label.grid(row=17, column=0, sticky='w')

        self.language_dropdown = ttk.Menubutton(self, bootstyle='dark', text="Wybierz język")
        self.language_dropdown.grid(row=18, column=0, sticky='w')

        language_dropdown_content = ttk.Menu(self.language_dropdown)

        self.language_var = ttk.StringVar()
        self.language_var.set("Angielski")

        for language in ['Angielski', 'Niemiecki', 'Francuski', 'Włoski', 'Hiszpański']:
            language_dropdown_content.add_radiobutton(label=language, variable=self.language_var, value=language,
                                                      command=self.on_language_select)

        self.language_dropdown['menu'] = language_dropdown_content

        ## level

        level_label = ttk.Label(self, text="Poziom*", font=('Open Sans', 12), bootstyle='default')
        level_label.grid(row=17, column=2, sticky='w')

        self.level_dropdown = ttk.Menubutton(self, bootstyle='dark', text="Wybierz poziom")
        self.level_dropdown.grid(row=18, column=2, sticky='w')

        level_dropdown_content = ttk.Menu(self.level_dropdown)

        self.level_var = StringVar()
        self.level_var.set("Początkujący")

        for level in ['Początkujący', 'Zaawansowany']:
            level_dropdown_content.add_radiobutton(label=level, variable=self.level_var, value=level,
                                                   command=self.on_level_select)

        self.level_dropdown['menu'] = level_dropdown_content

        ## mode

        mode_label = ttk.Label(self, text="Tryb*", font=('Open Sans', 12), bootstyle='default')
        mode_label.grid(row=17, column=3, sticky='w')

        self.mode_dropdown = ttk.Menubutton(self, bootstyle='dark', text="Wybierz tryb")
        self.mode_dropdown.grid(row=18, column=3, sticky='w')

        mode_dropdown_content = ttk.Menu(self.mode_dropdown)

        self.mode_var = StringVar()
        self.mode_var.set("Normalny")

        for mode in ['Normalny', 'Przyspieszony']:
            mode_dropdown_content.add_radiobutton(label=mode, variable=self.mode_var, value=mode,
                                                  command=self.on_mode_select)

        self.mode_dropdown['menu'] = mode_dropdown_content

        ## course

        course_label = ttk.Label(self, text="Wybierz dostępny kurs*", font=('Open Sans', 12),
                                 bootstyle='default')
        course_label.grid(row=17, column=4, sticky='w')

        self.course_dropdown = ttk.Menubutton(self, bootstyle='dark', text="Wybierz kurs")
        self.course_dropdown.grid(row=18, column=4, sticky='w')

        self.course_dropdown_content = ttk.Menu(self.course_dropdown)

        self.course_var = StringVar()
        self.course_var.set("")

        self.courses = []
        self.course_ids = {}

        self.course_dropdown['menu'] = self.course_dropdown_content

        ## start_date

        start_date_label = ttk.Label(self, text="Data rozpoczęcia*", font=('Open Sans', 12),
                                     bootstyle='default')
        start_date_label.grid(row=20, column=0, sticky='w')

        self.start_date_var = StringVar()
        self.start_date_var.set("")

        self.start_date_entry = ttk.DateEntry(self, bootstyle='primary')
        self.start_date_entry.configure(state='readonly')
        self.start_date_entry.entry.configure(textvariable=self.start_date_var)
        self.start_date_entry.grid(row=21, column=0, sticky='w')

        ## end_date

        end_date_label = ttk.Label(self, text="Data zakończenia", font=('Open Sans', 12),
                                   bootstyle='default')
        end_date_label.grid(row=20, column=2, sticky='w')

        self.end_date_var = StringVar()
        self.end_date_var.set("")

        self.end_date_entry = ttk.DateEntry(self, bootstyle='primary')
        self.end_date_entry.configure(state='readonly')
        self.end_date_entry.entry.configure(textvariable=self.end_date_var)
        self.end_date_entry.grid(row=21, column=2, sticky='w')

        ## payment

        payment_label = ttk.Label(self, text="Płatność*", font=('Open Sans', 12), bootstyle='default')
        payment_label.grid(row=20, column=3, sticky='w')

        self.payment_dropdown = ttk.Menubutton(self, bootstyle='dark', text="Wybierz sposób płatności")
        self.payment_dropdown.grid(row=21, column=3, sticky='w')

        payment_dropdown_content = ttk.Menu(self.payment_dropdown)

        self.payment_var = ttk.StringVar()
        self.payment_var.set("")

        for payment_method in ['W placówce', 'Przelew']:
            payment_dropdown_content.add_radiobutton(label=payment_method, variable=self.payment_var, value=payment_method,
                                                     command=self.on_payment_select)

        self.payment_dropdown['menu'] = payment_dropdown_content

        ## prize

        prize_label = ttk.Label(self, text="Cena", font=('Open Sans', 12), bootstyle='default')
        prize_label.grid(row=20, column=4, sticky='w')

        self.price_var = StringVar()

        self.price_entry = ttk.Entry(self, bootstyle='default', width=15, textvariable=self.price_var)
        self.price_entry.configure(state='readonly')
        self.price_entry.grid(row=21, column=4, sticky='w')

        ## submit

        submit_button_style = ttk.Style()
        submit_button_style.configure('success.TButton', font=('Open Sans', 14))

        submit_button = ttk.Button(self, bootstyle='success', text='ZAPISZ', width=20,
                                   style='success.TButton', command=self.submit_data)
        submit_button.grid(row=24, column=3, sticky='w')

        self.pack()

    def submit_data(self):

        validation =self.validation_on_submission()

        try:
            connection = self.establish_database_connection()
            cursor = connection.cursor()
            first_name = self.first_name.get()
            last_name = self.last_name.get()
            street = self.street.get()
            building_no = self.building_no.get()
            local_no = self.local_no.get()
            city = self.city.get()
            postal_code = self.postal_code.get()
            country = self.country.get()
            email = self.email.get()
            phone = self.phone_number.get()
            personal_id = self.personal_id.get()
            document_no = self.document_no.get()
            document_type = self.on_document_type_select()
            course_name = self.course_var.get()
            course_id = self.course_ids.get(course_name)

            enrollment_status = "Aktywny"

            if validation is True:
                query = """
                        -- Insert into students
                        INSERT INTO students (
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
                        document_type)
                        VALUES (
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                        
                        -- Get the generated student_id
                        SET @student_id := LAST_INSERT_ID();
                        
                        -- Insert into enrollment_status using the generated student_id
                        INSERT INTO enrollment_status (student_id, course_id, status)
                        VALUES (@student_id, %s, %s);
                        
                        -- Insert into payments using generated student_id
                        INSERT INTO payments (student_id, course_id, amount, payment_type, date_due, status)
                        VALUES (@student_id, %s, %s, %s, %s, %s);
                        """

                self.show_custom_messagebox("Uczeń został dodany", "Info")
        finally:
            connection.close()


    def establish_database_connection(self):
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(
            database='enroll_proto',
            host='localhost',
            user='postgres',
            password='kulek',
            port='5432'
        )
        return connection

    def look_for_course(self):
        connection = self.establish_database_connection()
        language = self.language_var.get()
        level = self.level_var.get()
        mode = self.mode_var.get()
        availability = 'Dostępny'

        try:
            cursor = connection.cursor()
            self.course_dropdown_content.delete(0, 'end')
            self.courses.clear()
            self.course_ids.clear()

            query = """
                    SELECT
                        course_id,
                        name
                    FROM courses
                    WHERE language = %s AND level = %s AND mode = %s and availability = %s;
                    """

            cursor.execute(query, (language, level, mode, availability))

            results = cursor.fetchall()

            for row in results:
                course_id, name = row
                self.courses.append(name)
                self.course_ids[name] = course_id

            for course in self.courses:
                self.course_dropdown_content.add_radiobutton(label=course, variable=self.course_var, value=course,
                                                             command=self.on_course_select)
        finally:
            connection.close()

    def update_dates_and_price(self):
        course_name = self.course_var.get()
        course_id = self.course_ids.get(course_name)
        connection = self.establish_database_connection()

        try:
            cursor = connection.cursor()

            query = """
                    SELECT 
                        start_date, 
                        end_date,
                        price
                    FROM courses
                    WHERE course_id = %s;
                    """
            cursor.execute(query, (course_id, ))

            results = cursor.fetchall()

            for row in results:
                start_date, end_date, price = row

            start_date_str = str(start_date).split()[0]
            start_date_db = datetime.strptime(start_date_str, "%Y-%m-%d").strftime("%d.%m.%Y")

            self.start_date_entry.entry.configure(textvariable=self.start_date_var)
            self.start_date_var.set(start_date_db)

            end_date_str = str(end_date).split()[0]
            end_date_db = datetime.strptime(end_date_str, "%Y-%m-%d").strftime("%d.%m.%Y")

            self.end_date_entry.entry.configure(textvariable=self.end_date_var)
            self.end_date_var.set(end_date_db)

            self.price_entry.configure(textvariable=self.price_var)
            self.price_var.set(price)

        finally:
            connection.close()


    def on_course_select(self):
        selected_course = self.course_var.get()
        print("Selected course:", selected_course)
        self.amend_menu_content_func(self.course_dropdown, selected_course)
        self.update_dates_and_price()
        return selected_course

    def on_document_type_select(self):
        selected_document_type = self.document_var.get()
        print("Selected document type:", selected_document_type)
        self.amend_menu_content_func(self.document_type, selected_document_type)
        return selected_document_type

    def on_language_select(self):
        selected_language = self.language_var.get()
        print("Selected language:", selected_language)
        self.amend_menu_content_func(self.language_dropdown, selected_language)
        self.look_for_course()
        return selected_language

    def on_level_select(self):
        selected_level = self.level_var.get()
        print("Selected level:", selected_level)
        self.amend_menu_content_func(self.level_dropdown, selected_level)
        self.look_for_course()
        return selected_level

    def on_mode_select(self):
        selected_mode = self.mode_var.get()
        print("Selected mode:", selected_mode)
        self.amend_menu_content_func(self.mode_dropdown, selected_mode)
        self.look_for_course()
        return selected_mode

    def on_payment_select(self):
        selected_payment_method = self.payment_var.get()
        print("Selected payment method:", selected_payment_method)
        self.amend_menu_content_func(self.payment_dropdown, selected_payment_method)
        return selected_payment_method

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
        if not self.validate_personal_id():
            self.show_custom_messagebox("Pole 'PESEL' nie może zawierać liter\nPopraw formularz", "Błąd")
            return False
        elif len(self.personal_id_var.get()) == 0:
            self.show_custom_messagebox("Pole PESEL nie może być puste\nPopraw formularz")
            return False
        if not self.validate_input(self.document_no_var.get(), 32, "Nr dokumentu", allow_empty=False, regex=regex):
            return False

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

