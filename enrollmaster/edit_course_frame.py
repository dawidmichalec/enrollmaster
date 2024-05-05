from tkinter import *
import ttkbootstrap as ttk
import psycopg2
from datetime import datetime, timedelta
import decimal


class EditCourseFrame(ttk.Frame):

    def __init__(self, master=None, amend_menu_content_func=None, **kw):
        super().__init__(master, **kw)
        self.amend_menu_content_func = amend_menu_content_func
        self.columnconfigure((0, 1, 2, 3, 4), weight=1, minsize=310)
        self.rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28),
            weight=1, minsize=30)

        # Variables

        self.course_id_var = StringVar()
        self.course_name_var = StringVar()
        self.course_language_var = StringVar()
        self.course_level_var = StringVar()
        self.course_mode_var = StringVar()
        self.course_teacher_name = StringVar()


        # edit_course_label

        edit_course_label = ttk.Label(self, text='EDYTUJ KURS', font=('Open Sans', 14, 'bold'),
                                      bootstyle='default')
        edit_course_label.grid(row=0, column=2, sticky='w')

        # course_id search

        course_id_search_label = ttk.Label(self, text='ID kursu', font=('Open Sans', 12),
                                           bootstyle='default')
        course_id_search_label.grid(row=2, column=2, sticky='w')

        self.course_id_search_entry = ttk.Entry(self, bootstyle='light', width=26)
        self.course_id_search_entry.grid(row=3, column=2, sticky='w')

        submit_button_style = ttk.Style()
        submit_button_style.configure('success.TButton', font=('Open Sans', 14))

        submit_button = ttk.Button(self, bootstyle='success', text='SZUKAJ', width=15,
                                   style='success.TButton', command=self.search_function)
        submit_button.grid(row=5, column=2, sticky='w')

        # course_id

        course_id_label = ttk.Label(self, text='ID Kursu', font=('Open Sans', 12), bootstyle='default')
        course_id_label.grid(row=8, column=0, sticky='w')

        self.course_id_entry = ttk.Entry(self, bootstyle='default', width=20, textvariable=self.course_id_var)
        self.course_id_entry.configure(state='readonly')
        self.course_id_entry.grid(row=9, column=0, sticky='w')

        # course_name

        course_name_label = ttk.Label(self, text='Nazwa kursu', font=('Open Sans', 12),
                                      bootstyle='default')
        course_name_label.grid(row=8, column=1, sticky='w')

        self.course_name_entry = ttk.Entry(self, bootstyle='default', width=20, textvariable=self.course_name_var)
        self.course_name_entry.configure(state='readonly')
        self.course_name_entry.grid(row=9, column=1, sticky='w')

        # course_language

        language_label = ttk.Label(self, text="Język kursu", font=('Open Sans', 12),
                                          bootstyle='default')
        language_label.grid(row=8, column=2, sticky='w')

        self.language_dropdown = ttk.Menubutton(self, bootstyle='dark')
        self.language_dropdown.configure(state='disabled')
        self.language_dropdown.grid(row=9, column=2, sticky='w')

        course_language_dropdown_content = ttk.Menu(self.language_dropdown)

        self.language_var = StringVar()
        self.language_var.set("")
        for language in ['Angielski', 'Niemiecki', 'Francuski', 'Włoski', 'Hiszpański']:
            course_language_dropdown_content.add_radiobutton(label=language, variable=self.language_var, value=language,
                                                             command=self.on_language_select)

        self.language_dropdown['menu'] = course_language_dropdown_content

        # course_level

        course_level_label = ttk.Label(self, text='Poziom', font=('Open Sans', 12), bootstyle='default')
        course_level_label.grid(row=8, column=3, sticky='w')

        self.level_dropdown = ttk.Menubutton(self, bootstyle='dark')
        self.level_dropdown.configure(state='disabled')
        self.level_dropdown.grid(row=9, column=3, sticky='w')

        course_level_dropdown_content = ttk.Menu(self.level_dropdown)

        self.level_var = StringVar()
        self.level_var.set("")

        for level in ['Początkujący', 'Zaawansowany']:
            course_level_dropdown_content.add_radiobutton(label=level, variable=self.level_var, value=level,
                                                          command=self.on_level_select)

        self.level_dropdown['menu'] = course_level_dropdown_content

        # course_mode

        mode_label = ttk.Label(self, text=f"Tryb", font=('Open Sans', 12), bootstyle='default')
        mode_label.grid(row=8, column=4, sticky='w')

        self.mode_dropdown = ttk.Menubutton(self, bootstyle='dark')
        self.mode_dropdown.configure(state='disabled')
        self.mode_dropdown.grid(row=9, column=4, sticky='w')

        mode_dropdown_content = ttk.Menu(self.mode_dropdown)

        self.mode_var = StringVar()
        self.mode_var.set("")

        for mode in ['Normalny', 'Przyspieszony']:
            mode_dropdown_content.add_radiobutton(label=mode, variable=self.mode_var, value=mode,
                                                  command=self.on_mode_select)

        self.mode_dropdown['menu'] = mode_dropdown_content

        # start_date

        start_date_label = ttk.Label(self, text='Data rozpoczęcia', font=('Open Sans', 12),
                                     bootstyle='default')
        start_date_label.grid(row=11, column=0, sticky='w')

        self.start_date_entry_var = StringVar()
        self.start_date_entry_var.set("")

        self.start_date_entry = ttk.DateEntry(self, bootstyle='primary')
        self.start_date_entry.configure(state='readonly')
        self.start_date_entry.entry.configure(textvariable=self.start_date_entry_var)
        self.start_date_entry.grid(row=12, column=0, sticky='w')

        # end date

        end_date_label = ttk.Label(self, text='Data zakończenia', font=('Open Sans', 12),
                                   bootstyle='default')
        end_date_label.grid(row=11, column=1, sticky='w')

        self.end_date_var = StringVar()
        self.end_date_var.set("")

        self.end_date_entry = ttk.DateEntry(self, bootstyle='primary')
        self.end_date_entry.configure(state='readonly')
        self.end_date_entry.entry.configure(textvariable=self.end_date_var)
        self.end_date_entry.grid(row=12, column=1, sticky='w')

        # teacher_selection

        teacher_selection_label = ttk.Label(self, text='Nauczyciel', font=('Open Sans', 12),
                                            bootstyle='default')
        teacher_selection_label.grid(row=11, column=2, sticky='w')

        self.teacher_name = StringVar()
        self.teacher_name.set("")

        self.teacher_selection_dropdown = ttk.Menubutton(self, bootstyle='dark')
        self.teacher_selection_dropdown.configure(state='disabled')
        self.teacher_selection_dropdown.grid(row=12, column=2, sticky='w')
        self.teacher_selection_dropdown_content = ttk.Menu(self.teacher_selection_dropdown)

        self.teachers = []
        self.teacher_ids = {}

        self.teacher_selection_dropdown['menu'] = self.teacher_selection_dropdown_content

        # price

        price_label = ttk.Label(self, text="Cena", font=('Open Sans', 12), bootstyle='default')
        price_label.grid(row=11, column=3, sticky='w')

        self.price_var = StringVar()
        self.price_var.set("")

        self.price_entry = ttk.Entry(self, bootstyle='default', width=15, textvariable=self.price_var)
        self.price_entry.configure(state='readonly')
        self.price_entry.grid(row=12, column=3, sticky='w')

        # edit button
        """
        When clicked, the entries change status from readonly to editable. 
        """

        edit_button_style = ttk.Style()
        edit_button_style.configure('primary.TButton', font=('Open Sans', 14))

        self.edit_button = ttk.Button(self, bootstyle='primary', text='EDYTUJ', width=15,
                                 style='primary.TButton',
                                 state='disabled', command=self.edit_function)
        self.edit_button.grid(row=16, column=1, sticky='w')

        # save_button

        self.save_button = ttk.Button(self, bootstyle='info', text='ZAPISZ', width=16,
                                 state='disabled', command=self.save_button_function)
        self.save_button.grid(row=16, column=2, sticky='w')

        # cancel_button - sets entries back to the readonly state and buttons do disabled state, including itself

        cancel_button_style = ttk.Style()
        cancel_button_style.configure('danger.TButton', font=('Open Sans', 14))

        self.cancel_button = ttk.Button(self, bootstyle='danger', text='ODRZUĆ', width=15,
                                   state='disabled', command=self.cancel_button_function)
        self.cancel_button.grid(row=16, column=3, sticky='w')

        self.pack()

    def save_button_function(self):
        self.show_custom_messagebox("Czy na pewno chcesz zapisać wprowadzone zmiany?",
                                    "Ostrzeżenie",
                                    self.save_function,
                                    self.dismiss_messagebox)

    def save_function(self):
        connection = self.establish_database_connection()
        validation = self.validate_price()

        try:
            cursor = connection.cursor()
            course_id = self.course_id_var.get()
            name = self.course_name_var.get()
            language = self.language_var.get()
            level = self.level_var.get()
            mode = self.mode_var.get()
            teacher_name = self.teacher_name.get()
            teacher_id = self.teacher_ids.get(teacher_name)
            start_date = self.start_date_entry.entry.get()
            end_date = self.end_date_entry.entry.get()
            price = self.price_entry.get()


            if validation is True:
                query = """
                        UPDATE courses
                        SET 
                            name = %s, 
                            language = %s, 
                            level = %s, 
                            mode = %s, 
                            teacher_id = %s, 
                            start_date = %s,
                            end_date = %s,
                            price = %s
                        WHERE course_id = %s;
                        """
                cursor.execute(query, (name, language, level, mode, teacher_id, start_date, end_date, price,
                                       course_id))

                connection.commit()
                self.clear_entries()
                self.block_entries()
                self.cancel_button['state'] = 'disabled'
                self.save_button['state'] = 'disabled'
                self.edit_button['state'] = 'disabled'
                self.show_custom_information("Dane kursu zostały zaktualizowane", "Info")
        finally:
            connection.close()



    def search_function(self):
        connection = self.establish_database_connection()

        course_id = self.course_id_search_entry.get()

        try:
            cursor = connection.cursor()

            if not course_id:
                self.show_custom_information("Należy podać ID kursu", "Błąd")
                return

            if course_id:
                query = """
                        SELECT
                            c.course_id,
                            c.name,
                            c.language,
                            c.level,
                            c.mode,
                            c.start_date,
                            c.end_date,
                            CONCAT(t.first_name, ' ', t.last_name) as teacher_name,
                            c.price
                        FROM courses c
                        JOIN teachers t ON c.teacher_id = t.teacher_id
                        WHERE c.course_id = %s
                        """
                cursor.execute(query, (course_id,))
                results = cursor.fetchone()

                if not results:
                    self.show_custom_information("Nie znaleziono nauczyciela. Sprawdź czy podałeś poprawne ID kursu",
                                                 "Info")
                else:
                    # If the search is successful, unblock edit and cancel buttons
                    self.edit_button['state'] = 'normal'

                    course_id, name, language, level, mode, start_date, end_date, teacher_name, price = results

                    self.course_id_var.set(course_id)
                    self.course_name_var.set(name)
                    self.language_var.set(language)
                    self.language_dropdown.configure(text=language)
                    self.level_var.set(level)
                    self.level_dropdown.configure(text=level)
                    self.mode_var.set(mode)
                    self.mode_dropdown.configure(text=mode)
                    start_date_str = str(start_date).split()[0]
                    start_date_db = datetime.strptime(start_date_str, "%Y-%m-%d").strftime("%d.%m.%Y")
                    self.start_date_entry_var.set(start_date_db)

                    end_date_str = str(end_date).split()[0]
                    end_date_db = datetime.strptime(end_date_str, "%Y-%m-%d").strftime("%d.%m.%Y")
                    self.end_date_var.set(end_date_db)
                    self.teacher_name.set(teacher_name)
                    self.teacher_selection_dropdown.configure(text=teacher_name)
                    self.price_var.set(price)
        finally:
            connection.close()

    def edit_function(self):
        self.save_button['state'] = 'normal'
        self.cancel_button['state'] = 'normal'

        self.language_dropdown.configure(state='')
        self.level_dropdown.configure(state='')
        self.mode_dropdown.configure(state='')
        self.start_date_entry.entry.configure(state='')
        self.teacher_selection_dropdown.configure(state='')
        self.price_entry.configure(state='')

        self.price_var.trace_add('write', self.validate_price)

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

    def clear_entries(self):
        self.course_id_var.set("")
        self.course_name_var.set("")
        self.language_var.set("")
        self.language_dropdown.configure(text="")
        self.level_var.set("")
        self.level_dropdown.configure(text="")
        self.mode_var.set("")
        self.mode_dropdown.configure(text="")
        self.start_date_entry_var.set("")
        self.end_date_var.set("")
        self.teacher_name.set("")
        self.teacher_selection_dropdown.configure(text="")
        self.price_var.set("")

    def block_entries(self):
        self.language_dropdown.configure(state='disabled')
        self.level_dropdown.configure(state='disabled')
        self.mode_dropdown.configure(state='disabled')
        self.start_date_entry.entry.configure(state='readonly')
        self.teacher_selection_dropdown.configure(state='disabled')
        self.price_entry.configure(state='readonly')

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

    def look_for_teachers(self):
        connection = self.establish_database_connection()
        language = self.language_var.get()

        try:
            cursor = connection.cursor()
            self.teacher_selection_dropdown_content.delete(0, 'end')
            self.teachers.clear()
            self.teacher_ids.clear()

            query = """
                    SELECT
                        teacher_id, CONCAT(first_name, ' ', last_name)
                    FROM teachers
                    WHERE language_to_teach = %s;
                    """
            cursor.execute(query, (language,))

            results = cursor.fetchall()

            for row in results:
                teacher_id, teacher_name = row
                self.teachers.append(teacher_name)
                self.teacher_ids[teacher_name] = teacher_id

            print(self.teachers)

            for teacher in self.teachers:
                self.teacher_selection_dropdown_content.add_radiobutton(label=teacher, variable=self.teacher_name,
                                                                   value=teacher,
                                                                   command=self.on_teacher_select)
        finally:
            connection.close()

    def update_end_date(self, *args):
        selected_mode = self.mode_var.get()
        if selected_mode == 'Przyspieszony':
            start_date_str = self.start_date_entry.entry.get()
            start_date = datetime.strptime(start_date_str, "%d.%m.%Y")
            end_date = self.calculate_end_date(start_date, 6)  # Calculate end date 6 months from start date
        elif selected_mode == 'Normalny':
            start_date_str = self.start_date_entry.entry.get()
            start_date = datetime.strptime(start_date_str, "%d.%m.%Y")
            end_date = self.calculate_end_date(start_date, 12)  # Calculate end date 1 year from today
        else:
            end_date = ""
        self.end_date_var.set(end_date)
        return end_date

    def calculate_end_date(self, start_date, months):
        end_date = start_date
        print(end_date)
        business_days_count = 0
        while business_days_count < months * 22:  # Assuming 22 business days per month
            end_date += timedelta(days=1)
            if end_date.weekday() < 5:  # Weekday is from 0 to 4 (Monday to Friday)
                business_days_count += 1

        return end_date.strftime("%d.%m.%Y")

    def update_the_name_of_the_course(self):
        language = self.language_var.get()
        level = self.level_var.get()
        mode = self.mode_var.get()
        start_date = self.start_date_entry.entry.get()
        end_date = self.update_end_date()

        three_letters_language = language[:3].upper()

        self.course_name_var.set(f"{three_letters_language}/{start_date}/{end_date}/{level}/{mode}")

    def validate_price(self, *args):
        price = self.price_var.get()

        for i in price:
            if i == " ":
                self.show_custom_information("Pole 'Cena' nie może zawierać spacji", "Błąd")
                return False
            elif i.isdigit() is False and i != '.':
                self.show_custom_information("Pole 'Cena' nie może zawierać liter ani znaków specjalnych", "Błąd")
                return False
            elif price[0] == '.':
                self.show_custom_information("Wartość pola 'Cena' nie może zaczynać się od kropki", "Błąd")
                return False
            else:
                d = decimal.Decimal(price)
                if d.as_tuple().exponent == -1 or d.as_tuple().exponent <= -3:
                    self.show_custom_information("Pole 'Cena' musi zawierać dwa miejsca po przecinku",
                                                "Błąd")
                    return False

            return True

    """
        Functions for dropdowns
    """

    def on_teacher_select(self):
        selected_teacher = self.teacher_name.get()
        print("Selected teacher:", selected_teacher)
        self.amend_menu_content_func(self.teacher_selection_dropdown, selected_teacher)
        self.update_the_name_of_the_course()
        return selected_teacher

    def on_language_select(self):
        selected_language = self.language_var.get()
        print("Selected language:", selected_language)
        self.amend_menu_content_func(self.language_dropdown, selected_language)
        self.update_the_name_of_the_course()
        self.look_for_teachers()
        return selected_language

    def on_level_select(self):
        selected_level = self.level_var.get()
        print("Selected level:", selected_level)
        self.amend_menu_content_func(self.level_dropdown, selected_level)
        self.update_the_name_of_the_course()
        self.look_for_teachers()
        return selected_level

    def on_mode_select(self):
        selected_mode = self.mode_var.get()
        print("Selected mode:", selected_mode)
        self.amend_menu_content_func(self.mode_dropdown, selected_mode)
        self.update_the_name_of_the_course()
        self.look_for_teachers()
        return selected_mode

    """
    Custom messageboxes functions
    """

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

    def dismiss_messagebox(self):
        # Do nothing, just dismiss the messagebox
        print("Messagebox dismissed.")
