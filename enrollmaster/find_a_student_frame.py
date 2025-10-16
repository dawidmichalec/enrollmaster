from tkinter import *
import ttkbootstrap as ttk
import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv


class FindAStudentFrame(ttk.Frame):

    def __init__(self, master=None, amend_menu_content_func=None, **kw):
        super().__init__(master, **kw)
        self.amend_menu_content_func = amend_menu_content_func
        self.columnconfigure((0, 1, 2, 3, 4), weight=1, minsize=50)
        self.rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28),
            weight=1, minsize=30)

        frame_label = ttk.Label(self, text='WYSZUKAJ UCZNIA', font=('Open Sans', 14, 'bold'), bootstyle='default')
        frame_label.grid(row=0, column=2)

        self.pack()

        # first_name

        first_name_label = ttk.Label(self, text="Imię", font=("Open Sans", 12), bootstyle='default')
        first_name_label.grid(column=0, row=2, sticky='w')

        self.first_name = ttk.Entry(self, width=20, bootstyle='light')
        self.first_name.grid(column=0, row=3, sticky='w')

        # last_name

        last_name_label = ttk.Label(self, text="Nazwisko", font=("Open Sans", 12), bootstyle='default')
        last_name_label.grid(column=1, row=2, sticky='w')

        self.last_name = ttk.Entry(self, width=20, bootstyle='light')
        self.last_name.grid(column=1, row=3, sticky='w')

        # course_id

        course_id_label = ttk.Label(self, text="ID kursu", font=("Open Sans", 12), bootstyle='default')
        course_id_label.grid(column=2, row=2, sticky='w')

        self.course_id_entry = ttk.Entry(self, width=20, bootstyle='light')
        self.course_id_entry.grid(column=2, row=3, sticky='w')

        # course_name

        course_name_label = ttk.Label(self, text="Nazwa kursu", font=("Open Sans", 12), bootstyle='default')
        course_name_label.grid(column=3, row=2, sticky='w')

        self.course_name_entry = ttk.Entry(self, width=20, bootstyle='light')
        self.course_name_entry.grid(column=3, row=3, sticky='w')

        # language

        language_label = ttk.Label(self, text="Język kursu", font=('Open Sans', 12), bootstyle='default')
        language_label.grid(row=2, column=4, sticky='w')

        self.language_dropdown = ttk.Menubutton(self, bootstyle='dark', text="Wybierz język")
        self.language_dropdown.grid(row=3, column=4, sticky='w')

        language_dropdown_content = ttk.Menu(self.language_dropdown)

        self.language_var = ttk.StringVar()
        self.language_var.set("")

        for language in ['Angielski', 'Niemiecki', 'Francuski', 'Włoski', 'Hiszpański']:
            language_dropdown_content.add_radiobutton(label=language, variable=self.language_var, value=language,
                                                      command=self.on_language_select)

        self.language_dropdown['menu'] = language_dropdown_content

        # level

        level_label = ttk.Label(self, text="Poziom", font=('Open Sans', 12), bootstyle='default')
        level_label.grid(row=5, column=0, sticky='w')

        self.level_dropdown = ttk.Menubutton(self, bootstyle='dark', text="Wybierz poziom")
        self.level_dropdown.grid(row=6, column=0, sticky='w')

        level_dropdown_content = ttk.Menu(self.level_dropdown)

        self.level_var = StringVar()
        self.level_var.set("")

        for level in ['Początkujący', 'Zaawansowany']:
            level_dropdown_content.add_radiobutton(label=level, variable=self.level_var, value=level,
                                                   command=self.on_level_select)

        self.level_dropdown['menu'] = level_dropdown_content

        # mode

        mode_label = ttk.Label(self, text="Tryb", font=('Open Sans', 12), bootstyle='default')
        mode_label.grid(row=5, column=1, sticky='w')

        self.mode_dropdown = ttk.Menubutton(self, bootstyle='dark', text="Wybierz tryb")
        self.mode_dropdown.grid(row=6, column=1, sticky='w')

        mode_dropdown_content = ttk.Menu(self.mode_dropdown)

        self.mode_var = StringVar()
        self.mode_var.set("")

        for mode in ['Normalny', 'Przyspieszony']:
            mode_dropdown_content.add_radiobutton(label=mode, variable=self.mode_var, value=mode,
                                                  command=self.on_mode_select)

        self.mode_dropdown['menu'] = mode_dropdown_content

        # enrollment_status

        enrollment_status_label = ttk.Label(self, text="Status ucznia", font=('Open Sans', 12), bootstyle='default')
        enrollment_status_label.grid(column=2, row=5, sticky='w')

        self.enrollment_status_dropdown = ttk.Menubutton(self, bootstyle='dark', text='Wybierz')
        self.enrollment_status_dropdown.grid(column=2, row=6, sticky='w')

        enrollment_status_dropdown_content = ttk.Menu(self.enrollment_status_dropdown)

        self.enrollment_status = StringVar()
        self.enrollment_status.set("")

        for status in ['Aktywny', 'Nieaktywny']:
            enrollment_status_dropdown_content.add_radiobutton(label=status, variable=self.enrollment_status,
                                                               value=status, command=self.on_enrollment_status_select)

        self.enrollment_status_dropdown['menu'] = enrollment_status_dropdown_content

        # submit

        submit_button_style = ttk.Style()
        submit_button_style.configure('success.TButton', font=('Open Sans', 14))

        submit_button = ttk.Button(self, bootstyle='success', text='SZUKAJ', width=16,
                                   style='success.TButton', command=self.search_function)
        submit_button.grid(row=9, column=2, sticky='w')

        self.treeview = ttk.Treeview(self, columns=("student_id", "first_name", "last_name", "course_id", "course_name",
                                                    "language", "level", "mode", "enrollment_status"),
                                     show="headings")
        self.treeview.grid(row=12, column=0, columnspan=5, rowspan=10)

        # Define column headings
        self.treeview.heading("student_id", text="ID Ucznia")
        self.treeview.heading("first_name", text="Imię")
        self.treeview.heading("last_name", text="Nazwisko")
        self.treeview.heading("course_id", text="ID Kursu")
        self.treeview.heading("course_name", text="Nazwa kursu")
        self.treeview.heading("language", text="Język")
        self.treeview.heading("level", text="Poziom")
        self.treeview.heading("mode", text="Tryb")
        self.treeview.heading("enrollment_status", text="Status ucznia")

        # Set column attributes
        self.treeview.column("student_id", anchor='center')
        self.treeview.column("first_name", anchor='center')
        self.treeview.column("last_name", anchor='center')
        self.treeview.column("course_id", anchor='center')
        self.treeview.column("course_name", anchor='center')
        self.treeview.column("language", anchor='center')
        self.treeview.column("level", anchor='center')
        self.treeview.column("mode", anchor='center')
        self.treeview.column("enrollment_status", anchor='center')

        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.treeview.yview)
        scrollbar.grid(row=13, column=5, sticky="ns")
        self.treeview.configure(yscrollcommand=scrollbar.set)

        # Add horizontal scrollbar
        hscrollbar = ttk.Scrollbar(self, orient="horizontal", command=self.treeview.xview)
        hscrollbar.grid(row=21, column=0, columnspan=5, sticky="ew")
        self.treeview.configure(xscrollcommand=hscrollbar.set)


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
            first_name = self.first_name.get()
            last_name = self.last_name.get()
            course_id = self.course_id_entry.get()
            course_name = self.course_name_entry.get()
            language = self.language_var.get()
            level = self.level_var.get()
            mode = self.mode_var.get()
            enrollment_status = self.enrollment_status.get()

            conditions = []
            parameters = []

            if not any([first_name, last_name, course_id, course_name, language, level, mode, enrollment_status]):
                self.show_custom_information(
                    "Nie znaleziono pasujących wyników. Spróbuj zmodyfikować kryteria wyszukiwania", "Info"
                )
                return

            if first_name:
                conditions.append(sql.SQL("s.first_name = %s"))
                parameters.append(first_name)
            if last_name:
                conditions.append(sql.SQL("s.last_name = %s"))
                parameters.append(last_name)
            if course_id:
                conditions.append(sql.SQL("c.course_id = %s"))
                parameters.append(course_id)
            if course_name:
                conditions.append(sql.SQL("c.name = %s"))
                parameters.append(course_name)
            if language:
                conditions.append(sql.SQL("c.language = %s"))
                parameters.append(language)
            if level:
                conditions.append(sql.SQL("c.level = %s"))
                parameters.append(level)
            if mode:
                conditions.append(sql.SQL("c.mode = %s"))
                parameters.append(mode)
            if enrollment_status:
                conditions.append(sql.SQL("es.status = %s"))
                parameters.append(enrollment_status)

            base_query = sql.SQL("""
                       SELECT
                           s.student_id,
                           s.first_name,
                           s.last_name,
                           c.course_id,
                           c.name,
                           c.language,
                           c.level,
                           c.mode,
                           es.status
                       FROM students s
                       JOIN enrollment_status es ON s.student_id = es.student_id
                       JOIN courses c ON es.course_id = c.course_id
                   """)

            if conditions:
                where_clause = sql.SQL(" WHERE ") + sql.SQL(" AND ").join(conditions)
                final_query = base_query + where_clause
            else:
                final_query = base_query

            cursor.execute(final_query, parameters)
            results = cursor.fetchall()

            if not results:
                self.show_custom_information(
                    "Nie znaleziono pasujących wyników. Spróbuj zmodyfikować kryteria wyszukiwania", "Info"
                )
            else:
                self.treeview.delete(*self.treeview.get_children())
                for row in results:
                    self.treeview.insert("", END, values=row)

        finally:
            connection.close()

    def on_enrollment_status_select(self):
        selected_status = self.enrollment_status.get()
        print("Selected enrollment status:", selected_status)
        self.amend_menu_content_func(self.enrollment_status_dropdown, selected_status)
        return selected_status

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
