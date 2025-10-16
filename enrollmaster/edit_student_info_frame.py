from tkinter import *
import ttkbootstrap as ttk
from datetime import datetime
import psycopg2
import re
from dotenv import load_dotenv
import os


class EditStudentInfoFrame(ttk.Frame):

    def __init__(self, master=None, amend_menu_content_func=None, **kw):
        super().__init__(master, **kw)
        self.amend_menu_content_func = amend_menu_content_func
        self.columnconfigure((0, 2, 3, 4, 5), weight=1, minsize=300)
        self.columnconfigure(1, weight=1, minsize=50)
        self.rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28),
            weight=1, minsize=30)

        self.student_id_var = StringVar()
        self.first_name_var = StringVar()
        self.last_name_var = StringVar()
        self.street_var = StringVar()
        self.building_no_var = StringVar()
        self.local_no_var = StringVar()
        self.city_var = StringVar()
        self.postal_code_var = StringVar()
        self.country_var = StringVar()
        self.email_var = StringVar()
        self.phone_var = StringVar()
        self.personal_id_var = StringVar()
        self.document_no_var = StringVar()
        self.document_var = StringVar()
        self.language_var = StringVar()
        self.level_var = StringVar()
        self.mode_var = StringVar()
        self.enrollment_status_var = StringVar()
        self.course_var = StringVar()
        self.start_date_var = StringVar()
        self.end_date_var = StringVar()

        # name of the frame

        student_label = ttk.Label(self, text='EDYTUJ UCZNIA', font=('Open Sans', 14, 'bold'),
                                  bootstyle='default')
        student_label.grid(row=0, column=3, sticky='w')

        # student_id used for search purposes

        id_label = ttk.Label(self, text='ID Ucznia', font=('Open Sans', 12), bootstyle='default')
        id_label.grid(row=2, column=2, sticky='w')

        self.id_entry = ttk.Entry(self, bootstyle='light', width=20)
        self.id_entry.grid(row=3, column=2, sticky='w')

        # first_name

        first_name_label = ttk.Label(self, text="Imię", font=('Open Sans', 12), bootstyle='default')
        first_name_label.grid(row=2, column=3, sticky='w')

        self.first_name_entry = ttk.Entry(self, width=20, bootstyle='light')
        self.first_name_entry.grid(row=3, column=3, sticky='w')

        # last_name

        last_name_label = ttk.Label(self, text="Nazwisko", font=('Open Sans', 12), bootstyle='default')
        last_name_label.grid(row=2, column=4, sticky='w')

        self.last_name_entry = ttk.Entry(self, width=20, bootstyle='light')
        self.last_name_entry.grid(row=3, column=4, sticky='w')

        # submit button

        submit_button_style = ttk.Style()
        submit_button_style.configure('success.TButton', font=('Open Sans', 14))

        submit_button = ttk.Button(self, bootstyle='success', text='SZUKAJ', width=16,
                                   style='success.TButton', command=self.search_function)
        submit_button.grid(row=5, column=3, sticky='w')

        # student_id

        student_id_label = ttk.Label(self, text='ID Ucznia', font=('Open Sans', 12), bootstyle='default')
        student_id_label.grid(row=8, column=0, sticky='w')

        self.student_id = ttk.Entry(self, bootstyle='default', width=15, textvariable=self.student_id_var)
        self.student_id.configure(state='readonly')
        self.student_id.grid(row=9, column=0, sticky='w')

        # output_first_name

        output_first_name_label = ttk.Label(self, text='Imię', font=('Open Sans', 12),
                                            bootstyle='default')
        output_first_name_label.grid(row=8, column=2, sticky='w')

        self.first_name = ttk.Entry(self, bootstyle='default', width=20, textvariable=self.first_name_var)
        self.first_name.configure(state='readonly')
        self.first_name.grid(row=9, column=2, sticky='w')

        # output_last_name

        output_last_name_label = ttk.Label(self, text='Nazwisko', font=('Open Sans', 12),
                                           bootstyle='default')
        output_last_name_label.grid(row=8, column=3, sticky='w')

        self.last_name = ttk.Entry(self, bootstyle='default', width=20, textvariable=self.last_name_var)
        self.last_name.configure(state='readonly')
        self.last_name.grid(row=9, column=3, sticky='w')

        # output_street

        output_street_label = ttk.Label(self, text='Ulica', font=('Open Sans', 12), bootstyle='default')
        output_street_label.grid(row=8, column=4, sticky='w')

        self.street= ttk.Entry(self, bootstyle='default', width=30, textvariable=self.street_var)
        self.street.configure(state='readonly')
        self.street.grid(row=9, column=4, sticky='w')

        # output_building_no

        output_building_no_label = ttk.Label(self, text='Nr domu', font=('Open Sans', 12),
                                             bootstyle='default')
        output_building_no_label.grid(row=11, column=0, sticky='w')

        self.building_no = ttk.Entry(self, bootstyle='default', width=15, textvariable=self.building_no_var)
        self.building_no.configure(state='readonly')
        self.building_no.grid(row=12, column=0, sticky='w')

        # local_no_output

        local_no_output_label = ttk.Label(self, text='Nr lokalu', font=('Open Sans', 12),
                                          bootstyle='default')
        local_no_output_label.grid(row=11, column=2, sticky='w')

        self.local_no = ttk.Entry(self, bootstyle='default', width=15, textvariable=self.local_no_var)
        self.local_no.configure(state='readonly')
        self.local_no.grid(row=12, column=2, sticky='w')

        # city_output

        city_output_label = ttk.Label(self, text='Miasto', font=('Open Sans', 12), bootstyle='default')
        city_output_label.grid(row=11, column=3, sticky='w')

        self.city = ttk.Entry(self, bootstyle='default', width=20, textvariable=self.city_var)
        self.city.configure(state='readonly')
        self.city.grid(row=12, column=3, sticky='w')

        # postal_code_output

        postal_code_output_label = ttk.Label(self, text='Kod pocztowy', font=('Open Sans', 12),
                                             bootstyle='default')
        postal_code_output_label.grid(row=11, column=4, sticky='w')

        self.postal_code = ttk.Entry(self, bootstyle='default', width=15, textvariable=self.postal_code_var)
        self.postal_code.configure(state='readonly')
        self.postal_code.grid(row=12, column=4, sticky='w')

        # country_output

        country_output_label = ttk.Label(self, text='Państwo', font=('Open Sans', 12),
                                         bootstyle='default')
        country_output_label.grid(row=11, column=5, sticky='w')

        self.country = ttk.Entry(self, bootstyle='default', width=25, textvariable=self.country_var)
        self.country.configure(state='readonly')
        self.country.grid(row=12, column=5, sticky='w')

        # email_output

        email_output_label = ttk.Label(self, text='Adres e-mail', font=('Open Sans', 12), bootstyle='default')
        email_output_label.grid(row=14, column=0, sticky='w')

        self.email = ttk.Entry(self, bootstyle='default', width=25, textvariable=self.email_var)
        self.email.configure(state='readonly')
        self.email.grid(row=15, column=0, sticky='w')

        # phone_number_output

        phone_number_output_label = ttk.Label(self, text='Nr telefonu', font=('Open Sans', 12),
                                              bootstyle='default')
        phone_number_output_label.grid(row=14, column=2, sticky='w')

        self.phone_number = ttk.Entry(self, bootstyle='default', textvariable=self.phone_var, width=25)
        self.phone_number.configure(state='readonly')
        self.phone_number.grid(row=15, column=2, sticky='w')

        # personal_id_output

        personal_id_output_label = ttk.Label(self, text='PESEL', font=('Open Sans', 12),
                                             bootstyle='default')
        personal_id_output_label.grid(row=14, column=3, sticky='w')

        self.personal_id = ttk.Entry(self, bootstyle='default', width=25, textvariable=self.personal_id_var)
        self.personal_id.configure(state='readonly')
        self.personal_id.grid(row=15, column=3, sticky='w')

        # document_no_output

        document_no_output_label = ttk.Label(self, text='Nr dokumentu', font=('Open Sans', 12),
                                             bootstyle='default')
        document_no_output_label.grid(row=14, column=4, sticky='w')

        self.document_no = ttk.Entry(self, bootstyle='default', width=25, textvariable=self.document_no_var)
        self.document_no.configure(state='readonly')
        self.document_no.grid(row=15, column=4, sticky='w')

        # document_type_output

        document_type_output_label = ttk.Label(self, text='Rodzaj dokumentu', font=('Open Sans', 12),
                                               bootstyle='default')
        document_type_output_label.grid(row=14, column=5, sticky='w')

        self.document_type = ttk.Menubutton(self, bootstyle='dark')
        self.document_type.configure(state='disabled')
        self.document_type.grid(row=15, column=5, sticky='w')

        document_type_content = ttk.Menu(self.document_type)

        for document in ['Dowód osobisty', 'Paszport', 'Karta pobytu']:
            document_type_content.add_radiobutton(label=document, variable=self.document_var, value=document,
                                                  command=self.on_document_type_select)

        self.document_type['menu'] = document_type_content

        # course_language_output

        language_label = ttk.Label(self, text='Język kursu', font=('Open Sans', 12), bootstyle='default')
        language_label.grid(row=17, column=0, sticky='w')

        self.language_dropdown = ttk.Menubutton(self, bootstyle='dark')
        self.language_dropdown.configure(state='disabled')
        self.language_dropdown.grid(row=18, column=0, sticky='w')

        language_dropdown_content = ttk.Menu(self.language_dropdown)

        for language in ['Angielski', 'Niemiecki', 'Francuski', 'Włoski', 'Hiszpański']:
            language_dropdown_content.add_radiobutton(label=language, variable=self.language_var, value=language,
                                                      command=self.on_language_select)

        self.language_dropdown['menu'] = language_dropdown_content

        # level_output

        level_output_label = ttk.Label(self, text='Poziom', font=('Open Sans', 12), bootstyle='default')
        level_output_label.grid(row=17, column=2, sticky='w')

        self.level_dropdown = ttk.Menubutton(self, bootstyle='dark')
        self.level_dropdown.configure(state='disabled')
        self.level_dropdown.grid(row=18, column=2, sticky='w')

        level_dropdown_content = ttk.Menu(self.level_dropdown)

        for level in ['Początkujący', 'Zaawansowany']:
            level_dropdown_content.add_radiobutton(label=level, variable=self.level_var, value=level,
                                                   command=self.on_level_select)

        self.level_dropdown['menu'] = level_dropdown_content

        # mode

        mode_output_label = ttk.Label(self, text='Tryb', font=('Open Sans', 12), bootstyle='default')
        mode_output_label.grid(row=17, column=3, sticky='w')

        self.mode_dropdown = ttk.Menubutton(self, bootstyle='dark')
        self.mode_dropdown.configure(state='disabled')
        self.mode_dropdown.grid(row=18, column=3, sticky='w')

        mode_output_content = ttk.Menu(self.mode_dropdown)

        for mode in ['Normalny', 'Przyspieszony']:
            mode_output_content.add_radiobutton(label=mode, variable=self.mode_var, value=mode,
                                                command=self.on_mode_select)

        self.mode_dropdown['menu'] = mode_output_content

        # course_name_output

        course_name_output_label = ttk.Label(self, text='Nazwa kursu', font=('Open Sans', 12),
                                             bootstyle='default')
        course_name_output_label.grid(row=17, column=4, sticky='w')

        self.course_dropdown = ttk.Menubutton(self, bootstyle='dark')
        self.course_dropdown.configure(state='disabled')
        self.course_dropdown.grid(row=18, column=4, sticky='w')

        self.course_dropdown_content = ttk.Menu(self.course_dropdown)

        self.courses = []
        self.course_ids = {}

        self.retrieved_course_id = StringVar()

        self.course_dropdown['menu'] = self.course_dropdown_content

        # status_output

        status_output_label = ttk.Label(self, text='Status', font=('Open Sans', 12), bootstyle='default')
        status_output_label.grid(row=17, column=5, sticky='w')

        self.enrollment_status_output = ttk.Entry(self, bootstyle='default', state='readonly', width=25,
                                                  textvariable=self.enrollment_status_var)
        self.enrollment_status_output.configure(state='readonly')
        self.enrollment_status_output.grid(row=18, column=5, sticky='w')

        # start_date_output

        start_date_output_label = ttk.Label(self, text='Data rozpoczęcia', font=('Open Sans', 12), bootstyle='default')
        start_date_output_label.grid(row=20, column=2, sticky='w')

        self.start_date_var.set("")
        self.start_date_entry = ttk.DateEntry(self, bootstyle='primary')
        self.start_date_entry.configure(state='readonly')
        self.start_date_entry.entry.configure(textvariable=self.start_date_var)
        self.start_date_entry.grid(row=21, column=2, sticky='w')

        # end_date_output

        end_date_output_label = ttk.Label(self, text='Data zakończenia', font=('Open Sans', 12), bootstyle='default')
        end_date_output_label.grid(row=20, column=4, sticky='w')

        self.end_date_var.set("")

        self.end_date_entry = ttk.DateEntry(self, bootstyle='primary')
        self.end_date_entry.entry.configure(textvariable=self.end_date_var)
        self.end_date_entry.configure(state='readonly')
        self.end_date_entry.grid(row=21, column=4, sticky='w')

        # edit button
        """
        When clicked, the entries change status from readonly to editable. 
        """

        edit_button_style = ttk.Style()
        edit_button_style.configure('primary.TButton', font=('Open Sans', 14))

        self.edit_button = ttk.Button(self, bootstyle='primary', text='EDYTUJ', width=15,
                                      style='primary.TButton', state='disabled', command=self.edit_function)
        self.edit_button.grid(row=24, column=2, sticky='w')

        # save_button

        self.save_button = ttk.Button(self, bootstyle='info', text='ZAPISZ', width=16,
                                      state='disabled', command=self.save_button_function)
        self.save_button.grid(row=24, column=3, sticky='w')

        # block_button

        block_button_style = ttk.Style()
        block_button_style.configure('warning.TButton', font=('Open Sans', 14))

        self.block_button = ttk.Button(self, bootstyle='warning', text='ZABLOKUJ', width=15,
                                       state='disabled', command=self.block_function)
        self.block_button.grid(row=24, column=4, sticky='w')

        # cancel_button

        cancel_button_style = ttk.Style()
        cancel_button_style.configure('danger.TButton', font=('Open Sans', 14))

        self.cancel_button = ttk.Button(self, bootstyle='danger', text='ODRZUĆ', width=16,
                                        state='disabled', command=self.cancel_button_function)
        self.cancel_button.grid(row=26, column=3, sticky='w')

        self.pack()

    def search_function(self):
        connection = self.establish_database_connection()
        student_id = self.id_entry.get()
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()

        try:
            cursor = connection.cursor()

            if not student_id and not first_name and not last_name:
                self.show_custom_information("Należy podać ID nauczyciela lub imię oraz nazwisko", "Błąd")
                return

            self.start_date_var.set("")
            self.end_date_var.set("")

            if student_id and not (first_name or last_name):
                query = """
                        SELECT
                            s.student_id,
                            s.first_name,
                            s.last_name,
                            s.street,
                            s.building_no,
                            s.local_no,
                            s.city,
                            s.postal_code,
                            s.country,
                            s.email,
                            s.phone,
                            s.personal_id,
                            s.document_no,
                            s.document_type,
                            c.language,
                            c.level,
                            c.mode,
                            c.name,
                            es.status,
                            c.start_date,
                            c.end_date,
                            c.course_id
                        FROM students s
                        JOIN enrollment_status es ON s.student_id = es.student_id
                        JOIN courses c ON es.course_id = c.course_id
                        WHERE s.student_id = %s;
                        """
                cursor.execute(query, (student_id,))
            elif first_name and last_name:
                query = """
                        SELECT
                            s.student_id,
                            s.first_name,
                            s.last_name,
                            s.street,
                            s.building_no,
                            s.local_no,
                            s.city,
                            s.postal_code,
                            s.country,
                            s.email,
                            s.phone,
                            s.personal_id,
                            s.document_no,
                            s.document_type,
                            c.language,
                            c.level,
                            c.mode,
                            c.name,
                            es.status,
                            c.start_date,
                            c.end_date,
                            c.course_id
                        FROM students s
                        JOIN enrollment_status es ON s.student_id = es.student_id
                        JOIN courses c ON es.course_id = c.course_id
                        WHERE s.first_name = %s AND s.last_name = %s;
                        """
                cursor.execute(query, (first_name,last_name))
            elif first_name or last_name:
                self.show_custom_information("Należy podać ID nauczyciela lub imię oraz nazwisko", "Błąd")
                return
            else:
                query = """
                        SELECT
                            s.student_id,
                            s.first_name,
                            s.last_name,
                            s.street,
                            s.building_no,
                            s.local_no,
                            s.city,
                            s.postal_code,
                            s.country,
                            s.email,
                            s.phone,
                            s.personal_id,
                            s.document_no,
                            s.document_type,
                            c.language,
                            c.level,
                            c.mode,
                            c.name,
                            es.status,
                            c.start_date,
                            c.end_date,
                            c.course_id
                        FROM students s
                        JOIN enrollment_status es ON s.student_id = es.student_id
                        JOIN courses c ON es.course_id = c.course_id
                        WHERE s.student_id = %s AND s.first_name = %s AND s.last_name = %s;
                        """
                cursor.execute(query, (student_id, first_name, last_name))

            results = cursor.fetchone()

            if not results:
                self.show_custom_information("Nie znaleziono ucznia. Sprawdź czy podałeś poprawne dane", "Info")
            else:
                self.edit_button['state'] = 'normal'
                self.block_button['state'] = 'normal'

                student_id, first_name, last_name, street, building_no, local_no, city, postal_code, country, email, \
                    phone, personal_id, document_no, document_type, language, level, mode, course_name, status, \
                    start_date, end_date, retrieved_course_id = results

                self.student_id_var.set(student_id)
                self.first_name_var.set(first_name)
                self.last_name_var.set(last_name)
                self.street_var.set(street)
                self.building_no_var.set(building_no)
                self.local_no_var.set(local_no)
                self.city_var.set(city)
                self.postal_code_var.set(postal_code)
                self.country_var.set(country)
                self.email_var.set(email)
                self.phone_var.set(phone)
                self.personal_id_var.set(personal_id)
                self.document_no_var.set(document_no)
                self.document_var.set(document_type)
                self.document_type.configure(text=document_type)
                self.language_var.set(language)
                self.language_dropdown.configure(text=language)
                self.level_var.set(level)
                self.level_dropdown.configure(text=level)
                self.mode_var.set(mode)
                self.mode_dropdown.configure(text=mode)
                self.enrollment_status_var.set(status)
                self.retrieved_course_id.set(retrieved_course_id)
                self.course_var.set(course_name)
                self.courses.append(self.course_var.get())
                self.course_ids[self.course_var.get()] = retrieved_course_id
                self.course_dropdown.configure(text=course_name)

                start_date_str = str(start_date).split()[0]
                start_date_db = datetime.strptime(start_date_str, "%Y-%m-%d").strftime("%d.%m.%Y")
                self.start_date_var.set(start_date_db)

                end_date_str = str(end_date).split()[0]
                end_date_db = datetime.strptime(end_date_str, "%Y-%m-%d").strftime("%d.%m.%Y")
                self.end_date_var.set(end_date_db)
        finally:
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
                student_id = self.student_id_var.get()
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
                phone = self.phone_var.get()
                personal_id = self.personal_id_var.get()
                document_no = self.document_no_var.get()
                document_type = self.on_document_type_select()
                course_name = self.course_var.get()
                course_id = self.course_ids.get(course_name)
                print(course_id)
                print(self.retrieved_course_id.get())

                """
                The number of students must be updated if a student withdraws from the course. Number of students
                the course the student withdrew from should be reduced by one and the one for which he or she signed up
                increased by one.
                """

                if self.retrieved_course_id.get() != course_id:
                    update_students_table_query = """
                                                    UPDATE students
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
                                                        document_type = %s
                                                    WHERE student_id = %s;
                                                    """
                    cursor.execute(update_students_table_query, (first_name, last_name, street,building_no,
                                                        local_no, city, postal_code, country, email, phone,
                                                        personal_id, document_no, document_type, student_id))

                    update_courses_table_query = """
                                                    UPDATE courses
                                                    SET number_of_students = number_of_students - 1
                                                    WHERE course_id = %s;
                                                    
                                                    UPDATE courses
                                                    SET number_of_students = number_of_students + 1
                                                    WHERE course_id = %s;
                                                    """
                    cursor.execute(update_courses_table_query, (self.retrieved_course_id.get(), course_id))

                    update_enrollment_status_table = """
                                                        UPDATE enrollment_status
                                                        SET course_id = %s
                                                        WHERE student_id = %s;
                                                        """
                else:
                    update_students_table_query = """
                                                    UPDATE students
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
                                                        document_type = %s
                                                    WHERE student_id = %s;
                                                    """
                    cursor.execute(update_students_table_query, (first_name, last_name, street, building_no,
                                                                 local_no, city, postal_code, country, email, phone,
                                                                 personal_id, document_no, document_type, student_id))

                connection.commit()
                self.clear_entries()
                self.block_entries()
                self.cancel_button['state'] = 'disabled'
                self.save_button['state'] = 'disabled'
                self.edit_button['state'] = 'disabled'
                self.block_button['state'] = 'disabled'
                self.show_custom_information("Dane ucznia zostały zaktualizowane", "Info")

        finally:
            connection.close()

    def block_function(self):
        self.show_custom_messagebox("Czy na pewno chcesz zablokować tego nauczyciela?",
                                    "Ostrzeżenie",
                                    self.block_student,
                                    self.dismiss_messagebox)

    def block_student(self):

        connection = self.establish_database_connection()

        try:
            cursor = connection.cursor()
            student_id = self.student_id.get()

            query = """
                    UPDATE enrollment_status
                    SET status = 'Nieaktywny'
                    WHERE student_id = %s;"""
            cursor.execute(query, (student_id,))
            connection.commit()

            self.clear_entries()
            self.block_entries()
            self.cancel_button['state'] = 'disabled'
            self.save_button['state'] = 'disabled'
            self.edit_button['state'] = 'disabled'
            self.block_button['state'] = 'disabled'
            self.show_custom_information("Uczeń został zablokowany", "Info")
        finally:
            connection.close()

    def edit_function(self):

        # unblock cancel and save buttons
        self.cancel_button['state'] = 'normal'
        self.save_button['state'] = 'normal'

        # allow the user to change the data

        self.first_name.configure(state='')
        self.last_name.configure(state='')
        self.street.configure(state='')
        self.building_no.configure(state='')
        self.local_no.configure(state='')
        self.city.configure(state='')
        self.postal_code.configure(state='')
        self.country.configure(state='')
        self.email.configure(state='')
        self.phone_number.configure(state='')
        self.personal_id.configure(state='')
        self.document_no.configure(state='')
        self.document_type.configure(state='')
        self.language_dropdown.configure(state='')
        self.level_dropdown.configure(state='')
        self.mode_dropdown.configure(state='')
        self.course_dropdown.configure(state='')

        self.first_name_var.trace_add('write', self.validate_first_name)
        self.last_name_var.trace_add('write', self.validate_last_name)
        self.street_var.trace_add('write', self.validate_street)
        self.building_no_var.trace_add('write', self.validate_building_no)
        self.local_no_var.trace_add('write', self.validate_local_no)
        self.city_var.trace_add('write', self.validate_city)
        self.postal_code_var.trace_add('write', self.validate_postal_code)
        self.country_var.trace_add('write', self.validate_country)
        self.email_var.trace_add('write', self.validate_email)
        self.phone_var.trace_add('write', self.validate_phone)
        self.personal_id_var.trace_add('write', self.validate_personal_id)
        self.document_no_var.trace_add('write', self.validate_document_no)

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
        self.student_id_var.set("")
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
        self.document_var.set("")
        self.document_type.configure(text="")
        self.language_var.set("")
        self.language_dropdown.configure(text="")
        self.level_var.set("")
        self.level_dropdown.configure(text="")
        self.mode_var.set("")
        self.mode_dropdown.configure(text="")
        self.enrollment_status_var.set("")
        self.course_var.set("")
        self.course_dropdown.configure(text="")
        self.start_date_var.set("")
        self.end_date_var.set("")

    def block_entries(self):
        self.first_name.configure(state='readonly')
        self.last_name.configure(state='readonly')
        self.street.configure(state='readonly')
        self.building_no.configure(state='readonly')
        self.local_no.configure(state='readonly')
        self.city.configure(state='readonly')
        self.postal_code.configure(state='readonly')
        self.country.configure(state='readonly')
        self.email.configure(state='readonly')
        self.phone_number.configure(state='readonly')
        self.personal_id.configure(state='readonly')
        self.document_no.configure(state='readonly')
        self.document_type.configure(state='disabled')
        self.language_dropdown.configure(state='disabled')
        self.level_dropdown.configure(state='disabled')
        self.mode_dropdown.configure(state='disabled')
        self.course_dropdown.configure(state='disabled')


    def dismiss_messagebox(self):
        # Do nothing, just dismiss the messagebox
        print("Messagebox dismissed.")

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

    def update_dates(self):
        course_name = self.course_var.get()
        course_id = self.course_ids.get(course_name)
        connection = self.establish_database_connection()

        try:
            cursor = connection.cursor()

            query = """
                    SELECT 
                        start_date, 
                        end_date,
                    FROM courses
                    WHERE course_id = %s;
                    """
            cursor.execute(query, (course_id,))

            results = cursor.fetchall()

            for row in results:
                start_date, end_date = row

            start_date_str = str(start_date).split()[0]
            start_date_db = datetime.strptime(start_date_str, "%Y-%m-%d").strftime("%d.%m.%Y")

            self.start_date_entry.entry.configure(textvariable=self.start_date_var)
            self.start_date_var.set(start_date_db)

            end_date_str = str(end_date).split()[0]
            end_date_db = datetime.strptime(end_date_str, "%Y-%m-%d").strftime("%d.%m.%Y")

            self.end_date_entry.entry.configure(textvariable=self.end_date_var)
            self.end_date_var.set(end_date_db)

        finally:
            connection.close()

    def on_course_select(self):
        selected_course = self.course_var.get()
        print("Selected course:", selected_course)
        self.amend_menu_content_func(self.course_dropdown, selected_course)
        self.update_dates()
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
        phone = self.phone_var.get()

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
        elif len(self.phone_var.get()) == 0:
            self.show_custom_information("Pole 'Nr telefonu' nie może być puste\nPopraw formularz")
        if not self.validate_personal_id():
            self.show_custom_information("Pole 'PESEL' nie może zawierać liter\nPopraw formularz", "Błąd")
            return False
        elif len(self.personal_id_var.get()) == 0:
            self.show_custom_information("Pole PESEL nie może być puste\nPopraw formularz")
            return False
        if not self.validate_input(self.document_no_var.get(), 32, "Nr dokumentu", allow_empty=False, regex=regex):
            return False

        return True

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
