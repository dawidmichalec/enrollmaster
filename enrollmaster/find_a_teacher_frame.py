from tkinter import *
import ttkbootstrap as ttk
import psycopg2
from datetime import datetime


class FindATeacherFrame(ttk.Frame):

    def __init__(self, master=None, amend_menu_content_func=None, **kw):
        super().__init__(master, **kw)
        self.amend_menu_content_func = amend_menu_content_func
        self.columnconfigure((0, 1, 2, 3, 4), weight=1, minsize=50)
        self.rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28),
            weight=1, minsize=30)

        frame_label = ttk.Label(self, text='ZNAJDŹ NAUCZYIELA', font=('Open Sans', 14, 'bold'), bootstyle='default')
        frame_label.grid(row=0, column=2, sticky='w')

        self.pack()

        first_name_label = ttk.Label(self, text="Imię", font=("Open Sans", 12), bootstyle='default')
        first_name_label.grid(column=0, row=2, sticky='w')

        self.first_name = ttk.Entry(self, width=20, bootstyle='light')
        self.first_name.grid(column=0, row=3, sticky='w')

        last_name_label = ttk.Label(self, text="Nazwisko", font=("Open Sans", 12), bootstyle='default')
        last_name_label.grid(column=1, row=2, sticky='w')

        self.last_name = ttk.Entry(self, width=20, bootstyle='light')
        self.last_name.grid(column=1, row=3, sticky='w')

        # language_to_teach

        language_to_teach_label = ttk.Label(self, text='Język nauczania', font=('Open Sans', 12),
                                            bootstyle='default')
        language_to_teach_label.grid(row=2, column=2, sticky='w')

        self.language_to_teach = ttk.Menubutton(self, bootstyle='dark', text='Wybierz')
        self.language_to_teach.grid(row=3, column=2, sticky='w')

        language_to_teach_content = ttk.Menu(self.language_to_teach)

        self.lang_var = StringVar()
        self.lang_var.set("")

        for language in ['Angielski', 'Niemiecki', 'Francuski', 'Włoski', 'Hiszpański']:
            language_to_teach_content.add_radiobutton(label=language, variable=self.lang_var, value=language,
                                                      command=self.on_language_to_teach_select)

        self.language_to_teach['menu'] = language_to_teach_content

        ## type_of_contract

        type_of_contract_label = ttk.Label(self, text="Rodzaj umowy", font=('Open Sans', 12),
                                           bootstyle='default')
        type_of_contract_label.grid(row=2, column=3, sticky='w')

        self.type_of_contract = ttk.Menubutton(self, bootstyle='dark', text='Wybierz umowę')
        self.type_of_contract.grid(row=3, column=3, sticky='w')

        type_of_contract_content = ttk.Menu(self.type_of_contract)

        self.type_var = StringVar()
        self.type_var.set("")

        for contract in ['Umowa O Pracę', 'Umowa Zlecenie']:
            type_of_contract_content.add_radiobutton(label=contract, variable=self.type_var, value=contract,
                                                     command=self.on_contract_type_select)

        self.type_of_contract['menu'] = type_of_contract_content

        ## type_of_employment

        type_of_employment_label = ttk.Label(self, text='Rodzaj zatrudnienia', font=('Open Sans', 12),
                                             bootstyle='default')
        type_of_employment_label.grid(row=2, column=4, sticky='w')

        self.type_of_employment = ttk.Menubutton(self, bootstyle='dark', text='Wybierz')
        self.type_of_employment.grid(row=3, column=4, sticky='w')

        type_of_employment_content = ttk.Menu(self.type_of_employment)

        self.employment_var = StringVar()
        self.employment_var.set("")

        for employment in ['Pełny etat', 'Pół etatu']:
            type_of_employment_content.add_radiobutton(label=employment, variable=self.employment_var, value=employment,
                                                       command=self.on_employment_type_select)

        self.type_of_employment['menu'] = type_of_employment_content

        ## status_of_employment

        status_of_employment_label = ttk.Label(self, text='Status zatrudnienia', font=('Open Sans', 12),
                                               bootstyle='default')
        status_of_employment_label.grid(row=5, column=0, sticky='w')

        self.status_of_employment = ttk.Menubutton(self, bootstyle='dark', text="Wybierz")
        self.status_of_employment.grid(row=6, column=0, sticky='w')

        status_of_employment_content = ttk.Menu(self.status_of_employment)

        self.status_var = StringVar()
        self.status_var.set("")

        for status in ['Aktywny', 'Nieaktywny']:
            status_of_employment_content.add_radiobutton(label=status, variable=self.status_var, value=status,
                                                         command=self.on_status_select)

        self.status_of_employment['menu'] = status_of_employment_content

        # employment_start_from

        self.employment_start_from_var = StringVar()
        self.employment_start_from_var.set("")

        employment_start_from_label = ttk.Label(self, text='Data zatrudnienia od', font=('Open Sans', 12),
                                                bootstyle='default')
        employment_start_from_label.grid(row=5, column=1, sticky='w')

        self.employment_start_from = ttk.DateEntry(self, bootstyle='primary')
        self.employment_start_from.grid(row=6, column=1, sticky='w')
        self.employment_start_from.entry.configure(textvariable=self.employment_start_from_var)

        # employment_start_to

        self.employment_start_to_var = StringVar()
        self.employment_start_to_var.set("")

        employment_start_to_label = ttk.Label(self, text='Data zatrudnienia do', font=('Open Sans', 12),
                                              bootstyle='default')
        employment_start_to_label.grid(row=5, column=2, sticky='w')

        self.employment_start_to = ttk.DateEntry(self, bootstyle='primary')
        self.employment_start_to.grid(row=6, column=2, sticky='w')
        self.employment_start_to.entry.configure(textvariable=self.employment_start_to_var)

        # submit

        submit_button_style = ttk.Style()
        submit_button_style.configure('success.TButton', font=('Open Sans', 14))

        submit_button = ttk.Button(self, bootstyle='success', text='SZUKAJ', width=16,
                                   style='success.TButton', command=self.search_function)
        submit_button.grid(row=9, column=2, sticky='w')

        # Create a Treeview widget

        self.treeview = ttk.Treeview(self, columns=("teacher_id", "first_name", "last_name", "language_to_teach",
                                                    "type_of_contract", "type_of_employment", "status_of_employment",
                                                    "salary", "employment_start"), show="headings")
        self.treeview.grid(row=12, column=0, columnspan=5, rowspan=10)

        # Define column headings
        self.treeview.heading("teacher_id", text="ID")
        self.treeview.heading("first_name", text="Imię")
        self.treeview.heading("last_name", text="Nazwisko")
        self.treeview.heading("language_to_teach", text="Język nauczania")
        self.treeview.heading("type_of_contract", text="Rodzaj umowy")
        self.treeview.heading("type_of_employment", text="Rodzaj zatrudnienia")
        self.treeview.heading("status_of_employment", text="Status zatrudnienia")
        self.treeview.heading("salary", text="Wypłata")
        self.treeview.heading("employment_start", text="Data zatrudnienia")

        # Set column widths
        self.treeview.column("teacher_id", anchor='center')
        self.treeview.column("first_name", anchor='center')
        self.treeview.column("last_name", anchor='center')
        self.treeview.column("language_to_teach", anchor='center')
        self.treeview.column("type_of_contract", anchor='center')
        self.treeview.column("type_of_employment", anchor='center')
        self.treeview.column("status_of_employment", anchor='center')
        self.treeview.column("salary", anchor='center')
        self.treeview.column("employment_start", anchor='center')

        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.treeview.yview)
        scrollbar.grid(row=13, column=5, sticky="ns")
        self.treeview.configure(yscrollcommand=scrollbar.set)

        # Add horizontal scrollbar
        hscrollbar = ttk.Scrollbar(self, orient="horizontal", command=self.treeview.xview)
        hscrollbar.grid(row=21, column=0, columnspan=5, sticky="ew")
        self.treeview.configure(xscrollcommand=hscrollbar.set)

    def search_function(self):

        connection = psycopg2.connect(
            database='enroll_proto',
            host='localhost',
            user='postgres',
            password='kulek',
            port='5432'
        )

        try:
            cursor = connection.cursor()
            first_name = self.first_name.get()
            last_name = self.last_name.get()
            language_to_teach = self.lang_var.get()
            type_of_contract = self.type_var.get()
            type_of_employment = self.employment_var.get()
            status = self.status_var.get()
            employment_start_from = self.employment_start_from.entry.get()
            employment_start_to = self.employment_start_to.entry.get()

            conditions = []
            parameters = []

            if not first_name and not last_name and not language_to_teach and not type_of_contract \
                and not type_of_employment and not status and not employment_start_from and not employment_start_to:
                self.show_custom_information("Nie znaleziono pasujących wyników. "
                                             "Spróbuj zmodyfikować kryteria wyszukiwania",
                                             "Info")
                return

            if first_name:
                conditions.append("first_name = %s")
                parameters.append(first_name)
            if last_name:
                conditions.append("last_name = %s")
                parameters.append(last_name)
            if language_to_teach:
                conditions.append("language_to_teach = %s")
                parameters.append(language_to_teach)
            if type_of_contract:
                conditions.append("type_of_contract = %s")
                parameters.append(type_of_contract)
            if type_of_employment:
                conditions.append("type_of_employment = %s")
                parameters.append(type_of_employment)
            if status:
                conditions.append("status_of_employment = %s")
                parameters.append(status)
            if employment_start_from:
                conditions.append("employment_start > %s")
                parameters.append(employment_start_from)
            if employment_start_to:
                conditions.append("employment_start < %s")
                parameters.append(employment_start_to)

            if employment_start_from and employment_start_to:
                conditions.append("employment_start > %s AND employment_start < %s")
                parameters.extend([employment_start_from, employment_start_to])

            where_clause = " AND ".join(conditions)

            query = """
                    SELECT
                        teacher_id,
                        first_name,
                        last_name,
                        language_to_teach,
                        type_of_contract,
                        type_of_employment,
                        status_of_employment,
                        salary,
                        employment_start
                    FROM teachers
                    WHERE {}
                    """.format(where_clause)
            cursor.execute(query, tuple(parameters))
            results = cursor.fetchall()

            if not results:
                self.show_custom_information("Nie znaleziono pasujących wyników. "
                                             "Spróbuj zmodyfikować kryteria wyszukiwania",
                                             "Info")
            else:
                self.treeview.delete(*self.treeview.get_children())

                for row in results:
                    date_str = str(row[8]).split()[0]
                    # Parse the date string into a datetime object
                    db_date = datetime.strptime(date_str, "%Y-%m-%d").strftime("%d-%m-%Y")
                    new_date = db_date.replace("-", ".")

                    self.treeview.insert("", END, values=((row[0]), (row[1]), (row[2]), (row[3]),
                                                          (row[4]), (row[5]), (row[6]), (row[7]), new_date))
        finally:
            connection.close()

    """
    Functions for dropdowns
    """

    def on_status_select(self):
        selected_status = self.status_var.get()
        print("Selected status:", selected_status)
        self.amend_menu_content_func(self.status_of_employment, selected_status)
        return selected_status

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
