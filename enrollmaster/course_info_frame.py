from tkinter import *
import ttkbootstrap as ttk
import psycopg2
from datetime import datetime
import os
from dotenv import load_dotenv


class CourseInfoFrame(ttk.Frame):

    def __init__(self, master=None, amend_menu_content_func=None, **kw):
        super().__init__(master, **kw)
        self.amend_menu_content_func = amend_menu_content_func
        self.columnconfigure((0, 1, 2, 3, 4), weight=1, minsize=50)
        self.rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28),
            weight=1, minsize=30)

        course_info_label = ttk.Label(self, text='WYSZUKAJ KURS', font=('Open Sans', 14, 'bold'),
                                      bootstyle='default')
        course_info_label.grid(row=0, column=2, sticky='w')

        # teacher_first_name

        teacher_first_name_label = ttk.Label(self, text='Imię nauczyciela', font=('Open Sans', 12),
                                             bootstyle='default')
        teacher_first_name_label.grid(row=2, column=0, sticky='w')

        self.teacher_first_name = ttk.Entry(self, bootstyle='light', width=20)
        self.teacher_first_name.grid(row=3, column=0, sticky='w')

        # teacher_last_name

        teacher_last_name_label = ttk.Label(self, text='Nazwisko nauczyciela', font=('Open Sans', 12),
                                            bootstyle='default')
        teacher_last_name_label.grid(row=2, column=1, sticky='w')

        self.teacher_last_name = ttk.Entry(self, bootstyle='light', width=20)
        self.teacher_last_name.grid(row=3, column=1, sticky='w')

        # name

        course_name_label = ttk.Label(self, text='Nazwa kursu', font=('Open Sans', 12),
                                      bootstyle='default')
        course_name_label.grid(row=2, column=2, sticky='w')

        self.course_name = ttk.Entry(self, bootstyle='light', width=20)
        self.course_name.grid(row=3, column=2, sticky='w')

        # language

        language_label = ttk.Label(self, text="Język kursu", font=('Open Sans', 12), bootstyle='default')
        language_label.grid(row=2, column=3, sticky='w')

        self.language_dropdown = ttk.Menubutton(self, bootstyle='dark', text="Wybierz język")
        self.language_dropdown.grid(row=3, column=3, sticky='w')

        language_dropdown_content = ttk.Menu(self.language_dropdown)

        self.language_var = StringVar()
        self.language_var.set('')

        for language in ['Angielski', 'Niemiecki', 'Francuski', 'Włoski', 'Hiszpański']:
            language_dropdown_content.add_radiobutton(label=language, variable=self.language_var, value=language,
                                                             command=self.on_language_select)

        self.language_dropdown['menu'] = language_dropdown_content

        # level

        course_level_label = ttk.Label(self, text='Poziom', font=('Open Sans', 12), bootstyle='default')
        course_level_label.grid(row=2, column=4, sticky='w')

        self.level_dropdown = ttk.Menubutton(self, bootstyle='dark', text='Wybierz poziom')
        self.level_dropdown.grid(row=3, column=4, sticky='w')

        level_dropdown_content = ttk.Menu(self.level_dropdown)

        self.level_var = StringVar()
        self.level_var.set('')

        for level in ['Początkujący', 'Zaawansowany']:
            level_dropdown_content.add_radiobutton(label=level, variable=self.level_var, value=level,
                                                   command=self.on_level_select)

        self.level_dropdown['menu'] = level_dropdown_content

        # mode

        mode_label = ttk.Label(self, text="Tryb", font=('Open Sans', 12), bootstyle='default')
        mode_label.grid(row=5, column=0, sticky='w')

        self.mode_dropdown = ttk.Menubutton(self, bootstyle='dark', text="Wybierz poziom")
        self.mode_dropdown.grid(row=6, column=0, sticky='w')

        mode_dropdown_content = ttk.Menu(self.mode_dropdown)

        self.mode_var = StringVar()
        self.mode_var.set('')

        for mode in ['Normalny', 'Przyspieszony']:
            mode_dropdown_content.add_radiobutton(label=mode, variable=self.mode_var, value=mode,
                                                  command=self.on_mode_select)

        self.mode_dropdown['menu'] = mode_dropdown_content

        # availability

        availability_label = ttk.Label(self, text="Dostępność", font=('Open Sans', 12), bootstyle='default')
        availability_label.grid(row=5, column=1, sticky='w')

        self.availability_dropdown = ttk.Menubutton(self, bootstyle='dark', text='Wybierz')
        self.availability_dropdown.grid(row=6, column=1, sticky='w')

        availability_dropdown_content = ttk.Menu(self.availability_dropdown)

        self.availability_var = StringVar()
        self.availability_var.set("")

        for availability in ['Dostępny', 'Brak miejsc']:
            availability_dropdown_content.add_radiobutton(label=availability, variable=self.availability_var,
                                                          value=availability, command=self.on_availability_select)

        self.availability_dropdown['menu'] = availability_dropdown_content

        # start_date

        self.start_date_var = StringVar()
        self.start_date_var.set("")

        start_date_label = ttk.Label(self, text='Data rozpoczęcia od', font=('Open Sans', 12),
                                     bootstyle='default')
        start_date_label.grid(row=5, column=2, sticky='w')

        self.start_date_entry = ttk.DateEntry(self, bootstyle='primary')
        self.start_date_entry.grid(row=6, column=2, sticky='w')
        self.start_date_entry.entry.configure(textvariable=self.start_date_var)

        # end date

        self.end_date_var = StringVar()
        self.end_date_var.set("")

        end_date_label = ttk.Label(self, text='Data rozpoczęcia do', font=('Open Sans', 12),
                                   bootstyle='default')
        end_date_label.grid(row=5, column=3, sticky='w')

        self.end_date_entry = ttk.DateEntry(self, bootstyle='primary')
        self.end_date_entry.grid(row=6, column=3, sticky='w')
        self.end_date_entry.entry.configure(textvariable=self.end_date_var)

        # submit

        submit_button_style = ttk.Style()
        submit_button_style.configure('success.TButton', font=('Open Sans', 14))

        submit_button = ttk.Button(self, bootstyle='success', text='SZUKAJ', width=15,
                                   style='success.TButton', command=self.search_function)
        submit_button.grid(row=9, column=2, sticky='w')

        # Create a Treeview widget

        self.treeview = ttk.Treeview(self, columns=("course_id", "name", "language", "level",
                                                    "mode", "teacher_name", "number_of_students", "students_limit",
                                                    "start_date", "end_date"), show="headings")
        self.treeview.grid(row=12, column=0, columnspan=5, rowspan=10)

        # Define column headings
        self.treeview.heading("course_id", text="ID kursu")
        self.treeview.heading("name", text="Nazwa kursu")
        self.treeview.heading("language", text="Język")
        self.treeview.heading("level", text="Poziom")
        self.treeview.heading("mode", text="Tryb")
        self.treeview.heading("teacher_name", text="Nauczyciel")
        self.treeview.heading("number_of_students", text="Liczba uczniów")
        self.treeview.heading("students_limit", text="Limit uczniów")
        self.treeview.heading("start_date", text="Data rozpoczęcia")
        self.treeview.heading("end_date", text="Data zakończenia")

        # Set column widths
        self.treeview.column("course_id", anchor='center')
        self.treeview.column("name", anchor='center')
        self.treeview.column("language", anchor='center')
        self.treeview.column("level", anchor='center')
        self.treeview.column("mode", anchor='center')
        self.treeview.column("teacher_name", anchor='center')
        self.treeview.column("number_of_students", anchor='center')
        self.treeview.column("students_limit", anchor='center')
        self.treeview.column("start_date", anchor='center')
        self.treeview.column("end_date", anchor='center')

        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.treeview.yview)
        scrollbar.grid(row=13, column=5, sticky="ns")
        self.treeview.configure(yscrollcommand=scrollbar.set)

        # Add horizontal scrollbar
        hscrollbar = ttk.Scrollbar(self, orient="horizontal", command=self.treeview.xview)
        hscrollbar.grid(row=21, column=0, columnspan=5, sticky="ew")
        self.treeview.configure(xscrollcommand=hscrollbar.set)

        self.pack()


    load_dotenv()

    def search_function(self):
        connection = psycopg2.connect(
            database=os.getenv('DB_NAME'),
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            port=os.getenv('DB_PORT')
        )

        try:
            cursor = connection.cursor()
            teacher_first_name = self.teacher_first_name.get()
            teacher_last_name = self.teacher_last_name.get()
            course_name = self.course_name.get()
            language = self.language_var.get()
            level = self.level_var.get()
            mode = self.mode_var.get()
            availability = self.availability_var.get()
            start_date = self.start_date_entry.entry.get()
            end_date = self.end_date_entry.entry.get()

            conditions = []
            parameters = []

            if teacher_first_name:
                conditions.append("t.first_name = %s")
                parameters.append(teacher_first_name)
            if teacher_last_name:
                conditions.append("t.last_name = %s")
                parameters.append(teacher_last_name)
            if course_name:
                conditions.append("c.name = %s")
                parameters.append(course_name)
            if language:
                conditions.append("c.language = %s")
                parameters.append(language)
            if level:
                conditions.append("c.level = %s")
                parameters.append(level)
            if mode:
                conditions.append("c.mode = %s")
                parameters.append(mode)
            if availability:
                conditions.append("c.availability = %s")
                parameters.append(availability)
            if start_date:
                conditions.append("c.start_date > %s")
                parameters.append(start_date)
            if end_date:
                conditions.append("c.end_date < %s")
                parameters.append(end_date)

            if not conditions:
                self.show_custom_information(
                    "Nie znaleziono pasujących wyników. Spróbuj zmodyfikować kryteria wyszukiwania",
                    "Info"
                )
                return

            base_query = """
                        SELECT
                            c.course_id,
                            c.name,
                            c.language,
                            c.level, 
                            c.mode,
                            CONCAT(t.first_name, ' ', t.last_name) as teacher_name,
                            c.number_of_students,
                            c.students_limit,
                            c.start_date,
                            c.end_date
                        FROM courses c
                        JOIN teachers t ON c.teacher_id = t.teacher_id
                    """

            where_clause = " WHERE " + " AND ".join(conditions)
            full_query = base_query + where_clause

            cursor.execute(full_query, tuple(parameters))
            results = cursor.fetchall()

            if not results:
                self.show_custom_information("Nie znaleziono pasujących wyników. "
                                             "Spróbuj zmodyfikować kryteria wyszukiwania",
                                             "Info")
            else:
                self.treeview.delete(*self.treeview.get_children())

                for row in results:
                    start_date_str = str(row[8]).split()[0]
                    start_date_db = datetime.strptime(start_date_str, "%Y-%m-%d").strftime("%d.%m.%Y")

                    end_date_str = str(row[9]).split()[0]
                    end_date_db = datetime.strptime(end_date_str, "%Y-%m-%d").strftime("%d.%m.%Y")

                    self.treeview.insert("", END, values=((row[0]), (row[1]), (row[2]), (row[3]), (row[4]),
                                                          (row[5]), (row[6]), (row[7]), start_date_db, end_date_db))
        finally:
            connection.close()

    """
    Functions for dropdowns
    """
    def on_availability_select(self):
        selected_availability = self.availability_var.get()
        print("Selected availability:", selected_availability)
        self.amend_menu_content_func(self.availability_dropdown, selected_availability)
        return selected_availability

    def on_language_select(self):
        selected_language = self.language_var.get()
        print("Selected language:", selected_language)
        self.amend_menu_content_func(self.language_dropdown, selected_language)
        return selected_language

    def on_level_select(self):
        selected_level = self.level_var.get()
        print("Selected level:", selected_level)
        self.amend_menu_content_func(self.level_dropdown, selected_level)
        return selected_level

    def on_mode_select(self):
        selected_mode = self.mode_var.get()
        print("Selected mode:", selected_mode)
        self.amend_menu_content_func(self.mode_dropdown, selected_mode)
        return selected_mode

    def show_custom_information(self, message, title):
        custom_mb = Toplevel(self.master)
        custom_mb.title(title)

        width = 750
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
