from tkinter import *
import ttkbootstrap as ttk
from datetime import datetime, timedelta, date
import psycopg2
import decimal


class CreateCourseFrame(ttk.Frame):
    
    def __init__(self, master=None, amend_menu_content_func=None, **kw):
        super().__init__(master, **kw)
        self.amend_menu_content_func = amend_menu_content_func

        self.columnconfigure((0, 2, 3, 4, 5), weight=1, minsize=300)
        self.columnconfigure(1, weight=1, minsize=50)
        self.rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28),
            weight=1, minsize=30)

        create_course_label = ttk.Label(self, text='STWÓRZ KURS', font=('Open Sans', 14, 'bold'),
                                        bootstyle='default')
        create_course_label.grid(row=0, column=3, sticky='w')

        ## course_language

        language_label = ttk.Label(self, text="Język kursu*", font=('Open Sans', 12), bootstyle='default')
        language_label.grid(row=2, column=0, sticky='w')

        self.language_dropdown = ttk.Menubutton(self, bootstyle='dark', text="Wybierz język")
        self.language_dropdown.grid(row=3, column=0, sticky='w')

        language_dropdown_content = ttk.Menu(self.language_dropdown)

        self.language_var = ttk.StringVar()
        self.language_var.set("")

        for language in ['Angielski', 'Niemiecki', 'Francuski', 'Włoski', 'Hiszpański']:
            language_dropdown_content.add_radiobutton(label=language, variable=self.language_var, value=language,
                                                      command=self.on_language_select)

        self.language_dropdown['menu'] = language_dropdown_content

        ## course_level

        level_label = ttk.Label(self, text='Poziom*', font=('Open Sans', 12), bootstyle='default')
        level_label.grid(row=2, column=2, sticky='w')

        self.level_dropdown = ttk.Menubutton(self, bootstyle='dark', text='Wybierz poziom')
        self.level_dropdown.grid(row=3, column=2, sticky='w')

        level_dropdown_content = ttk.Menu(self.level_dropdown)

        self.level_var = StringVar()
        self.level_var.set("")

        for level in ['Początkujący', 'Zaawansowany']:
            level_dropdown_content.add_radiobutton(label=level, variable=self.level_var, value=level,
                                                   command=self.on_level_select)

        self.level_dropdown['menu'] = level_dropdown_content

        ## course_mode

        mode_label = ttk.Label(self, text="Tryb*", font=('Open Sans', 12), bootstyle='default')
        mode_label.grid(row=2, column=3, sticky='w')

        self.mode_dropdown = ttk.Menubutton(self, bootstyle='dark', text="Wybierz tryb")
        self.mode_dropdown.grid(row=3, column=3, sticky='w')

        mode_dropdown_content = ttk.Menu(self.mode_dropdown)

        self.mode_var = StringVar()
        self.mode_var.set("")

        for mode in ['Normalny', 'Przyspieszony']:
            mode_dropdown_content.add_radiobutton(label=mode, variable=self.mode_var, value=mode,
                                                  command=self.on_mode_select)

        self.mode_dropdown['menu'] = mode_dropdown_content

        ## start_date

        self.start_date_label = ttk.Label(self, text='Data rozpoczęcia*', font=('Open Sans', 12),
                                     bootstyle='default')
        self.start_date_label.grid(row=2, column=4, sticky='w')


        self.start_date_entry = ttk.DateEntry(self, bootstyle='primary')
        self.start_date_entry.grid(row=3, column=4, sticky='w')
        self.start_date_entry.bind("<<DateEntrySelected>>", self.update_the_name_of_the_course)


        ## end date

        self.end_date_var = StringVar()
        self.end_date_var.set("")

        end_date_label = ttk.Label(self, text='Data zakończenia', font=('Open Sans', 12),
                                   bootstyle='default')
        end_date_label.grid(row=5, column=0, sticky='w')

        self.end_date_entry = ttk.DateEntry(self, bootstyle='primary')
        self.end_date_entry.entry.configure(textvariable=self.end_date_var)
        self.end_date_entry.configure(state="readonly")
        self.end_date_entry.grid(row=6, column=0, sticky='w')

        ## teacher_selection

        teacher_selection_label = ttk.Label(self, text='Nauczyciel*', font=('Open Sans', 12),
                                            bootstyle='default')
        teacher_selection_label.grid(row=5, column=2, sticky='w')

        self.teacher_selection_dropdown = ttk.Menubutton(self, text='Wybierz nauczyciela', bootstyle='dark')
        self.teacher_selection_dropdown.configure(state='disabled')
        self.teacher_selection_dropdown.grid(row=6, column=2, sticky='w')

        self.teacher_selection_dropdown_content = ttk.Menu(self.teacher_selection_dropdown)
        self.teacher_name = StringVar()
        self.teacher_name.set("")

        self.teachers = []
        self.teacher_ids = {}

        self.teacher_selection_dropdown['menu'] = self.teacher_selection_dropdown_content

        ## prize

        price_label = ttk.Label(self, text="Cena*", font=('Open Sans', 12), bootstyle='default')
        price_label.grid(row=5, column=3, sticky='w')

        self.price_var = StringVar()

        self.price_entry = ttk.Entry(self, bootstyle='light', width=15, textvariable=self.price_var)
        self.price_entry.grid(row=6, column=3, sticky='w')

        self.price_var.trace_add('write', self.validate_price)

        ## course_name

        course_name_label = ttk.Label(self, text='Nazwa kursu', font=('Open Sans', 12),
                                      bootstyle='default')
        course_name_label.grid(row=5, column=4, sticky='w')

        self.course_name_var = StringVar()
        self.course_name_var.set("")

        self.course_name_entry = ttk.Entry(self, bootstyle='light', width=30, textvariable=self.course_name_var)
        self.course_name_entry.configure(state='readonly')
        self.course_name_entry.grid(row=6, column=4, sticky='w')

        submit_button_style = ttk.Style()
        submit_button_style.configure('success.TButton', font=('Open Sans', 14))

        submit_button = ttk.Button(self, bootstyle='success', text='ZAPISZ', width=20,
                                   style='success.TButton', command=self.save_button_function)
        submit_button.grid(row=9, column=3, sticky='w')

        self.pack()

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

    def unblock_dropdown(self):
        self.teacher_selection_dropdown.configure(state='normal')

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

    def save_button_function(self):
        self.show_custom_messagebox("Czy na pewno chcesz zapisać wprowadzone informacje?",
                                    "Ostrzeżenie",
                                    self.save_function,
                                    self.dismiss_messagebox)

    def save_function(self):
        connection = self.establish_database_connection()
        validation = self.validate_price()
        try:
            cursor = connection.cursor()
            name = self.course_name_var.get()
            language = self.language_var.get()
            level = self.level_var.get()
            start_date = self.start_date_entry.entry.get()
            end_date = self.end_date_entry.entry.get()
            mode = self.mode_var.get()
            price = self.price_entry.get()
            teacher_name = self.teacher_name.get()
            teacher_id = self.teacher_ids.get(teacher_name)
            number_of_students = 0
            students_limit = 10
            availability = 'Dostępny'


            if validation is True:
                query = """
                        INSERT INTO courses (
                        name, language, level, start_date, end_date, mode, price, teacher_id, number_of_students, 
                        students_limit, availability
                        )
                        VALUES (
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                        )
                        """
                cursor.execute(query, (name, language, level, start_date, end_date, mode, price, teacher_id, number_of_students,
                                       students_limit, availability))

            connection.commit()

            self.show_custom_information("Kurs został stworzony", "Info")
            self.course_name_var.set("")
            self.language_var.set("")
            self.language_dropdown.configure(text="Wybierz język")
            self.level_var.set("")
            self.level_dropdown.configure(text="Wybierz poziom")
            self.end_date_var.set("")
            self.mode_var.set("")
            self.mode_dropdown.configure(text="Wybierz tryb")
            self.price_var.set("")
            self.teacher_name.set("")
            self.teacher_selection_dropdown.configure(text="Wybierz nauczyciela")
            date_now = str(date.today()).split()[0]
            date_now_str = datetime.strptime(date_now, "%Y-%m-%d").strftime("%d.%m.%Y")
            self.reset_date = StringVar()
            self.start_date_entry.entry.configure(textvariable=self.reset_date)
            self.reset_date.set(date_now_str)

        finally:
            connection.close()


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
        self.unblock_dropdown()
        return selected_mode


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

    def dismiss_messagebox(self):
        pass

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
