from tkinter import *
import ttkbootstrap as ttk
import psycopg2
from datetime import datetime


class GenerateReportFrame(ttk.Frame):

    def __init__(self, master=None, amend_menu_content_func=None, **kw):
        super().__init__(master, **kw)
        self.amend_menu_content_func = amend_menu_content_func
        self.columnconfigure((0, 1, 2, 3, 4), weight=1, minsize=50)
        self.rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28),
            weight=1, minsize=30)

        generate_report_label = ttk.Label(self, text='WYGENERUJ RAPORT',
                                          font=('Open Sans', 14, 'bold'),
                                          bootstyle='default')
        generate_report_label.grid(row=0, column=2, sticky='w')

        self.pack()

        # start_date

        start_date_label = ttk.Label(self, text='Data od', bootstyle='default', font=('Open Sans', 12))
        start_date_label.grid(row=2, column=0, sticky='w')

        self.start_date_var = StringVar()
        self.start_date_var.set("")

        self.start_date_entry = ttk.DateEntry(self, bootstyle='primary')
        self.start_date_entry.entry.configure(textvariable=self.start_date_var)
        self.start_date_entry.grid(row=3, column=0, sticky='w')

        # end_date

        end_date_label = ttk.Label(self, text='Data do', bootstyle='default', font=('Open Sans', 12))
        end_date_label.grid(row=2, column=1, sticky='w')

        self.end_date_var = StringVar()
        self.end_date_var.set("")

        self.end_date_entry = ttk.DateEntry(self, bootstyle='primary')
        self.end_date_entry.entry.configure(textvariable=self.end_date_var)
        self.end_date_entry.grid(row=3, column=1, sticky='w')

        # language

        course_language_label = ttk.Label(self, text="Język kursu", font=('Open Sans', 12),
                                          bootstyle='default')
        course_language_label.grid(row=2, column=2, sticky='w')

        self.language_dropdown = ttk.Menubutton(self, bootstyle='dark', text="Wybierz język")
        self.language_dropdown.grid(row=3, column=2, sticky='w')

        language_dropdown_content = ttk.Menu(self.language_dropdown)

        self.language_var = StringVar()
        self.language_var.set('')
        for x in ['Wszystkie', 'Angielski', 'Niemiecki', 'Francuski', 'Włoski', 'Hiszpański']:
            language_dropdown_content.add_radiobutton(label=x, variable=self.language_var,
                                                             command=self.on_language_select)

        self.language_dropdown['menu'] = language_dropdown_content

        # payment_status

        payment_status_label = ttk.Label(self, text='Status płatności', font=('Open Sans', 12),
                                         bootstyle='default')
        payment_status_label.grid(row=2, column=3, sticky='w')

        self.payment_status = ttk.Menubutton(self, bootstyle='dark', text='Wybierz status')
        self.payment_status.grid(row=3, column=3, sticky='w')

        payment_status_content = ttk.Menu(self.payment_status)
        self.status_var = StringVar()
        self.status_var.set('')

        for x in ['Wszystkie', 'Do zapłaty', 'Zapłacone']:
            payment_status_content.add_radiobutton(label=x, variable=self.status_var,
                                                   command=self.on_payment_status_select)

        self.payment_status['menu'] = payment_status_content

        # payment_type

        payment_type_label = ttk.Label(self, text="Sposób płatności", font=('Open Sans', 12),
                                       bootstyle='default')
        payment_type_label.grid(row=2, column=4, sticky='w')

        self.payment_dropdown = ttk.Menubutton(self, bootstyle='dark', text="Wybierz sposób płatności")
        self.payment_dropdown.grid(row=3, column=4, sticky='w')

        payment_dropdown_content = ttk.Menu(self.payment_dropdown)

        self.payment_var = StringVar()
        self.payment_var.set('')

        for x in ['Wszystkie', 'W placówce', 'Przelew']:
            payment_dropdown_content.add_radiobutton(label=x, variable=self.payment_var,
                                                     command=self.on_payment_select)

        self.payment_dropdown['menu'] = payment_dropdown_content

        # submit_button

        submit_button_style = ttk.Style()
        submit_button_style.configure('success.TButton', font=('Open Sans', 14))

        submit_button = ttk.Button(self, bootstyle='success', text='SZUKAJ', width=16,
                                   style='success.TButton', command=self.search_function)
        submit_button.grid(row=6, column=2, sticky='w')

        # export_button

        export_button_style = ttk.Style()
        export_button_style.configure('primary.TButton', font=('Open Sans', 15))

        export_button = ttk.Button(self, bootstyle='primary', text='CSV', width=13,
                                   style='primary.TButton')
        export_button.grid(row=6, column=3, sticky='w')

        # Create a Treeview widget

        self.treeview = ttk.Treeview(self, columns=("payment_id", "student_id", "first_name", "last_name",
                                                    "course_id", "course_name", "language", "level", "mode", "amount",
                                                    "payment_type", "status", "date_due", "created"), show="headings")
        self.treeview.grid(row=12, column=0, columnspan=5, rowspan=10)

        # Define column headings
        self.treeview.heading("payment_id", text="ID płatności")
        self.treeview.heading("student_id", text="ID ucznia")
        self.treeview.heading("first_name", text="Imię ucznia")
        self.treeview.heading("last_name", text="Nazwisko ucznia")
        self.treeview.heading("course_id", text="ID kursu")
        self.treeview.heading("course_name", text="Nazwa kursu")
        self.treeview.heading("language", text="Język kursu")
        self.treeview.heading("level", text="Poziom")
        self.treeview.heading("mode", text="Tryb")
        self.treeview.heading("amount", text="Kwota")
        self.treeview.heading("payment_type", text="Rodzaj płatności")
        self.treeview.heading("status", text="Status płatności")
        self.treeview.heading("date_due", text="Termin płatności")
        self.treeview.heading("created", text="Data")

        # Set column widths

        self.treeview.column("payment_id", anchor='center')
        self.treeview.column("student_id", anchor='center')
        self.treeview.column("first_name", anchor='center')
        self.treeview.column("last_name", anchor='center')
        self.treeview.column("course_id", anchor='center')
        self.treeview.column("course_name", anchor='center')
        self.treeview.column("language", anchor='center')
        self.treeview.column("level", anchor='center')
        self.treeview.column("mode", anchor='center')
        self.treeview.column("amount", anchor='center')
        self.treeview.column("payment_type", anchor='center')
        self.treeview.column("status", anchor='center')
        self.treeview.column("date_due", anchor='center')
        self.treeview.column("created", anchor='center')

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

            start_date = self.start_date_entry.entry.get()
            end_date = self.end_date_entry.entry.get()
            language = self.language_var.get()
            payment_type = self.payment_var.get()
            status = self.status_var.get()

            conditions = []
            parameters = []

            if not start_date and not end_date and not language and not payment_type and not status:
                self.show_custom_information("Nie znaleziono pasujących wyników. "
                                             "Spróbuj zmodyfikować kryteria wyszukiwania",
                                             "Info")

            if start_date:
                conditions.append("p.created > %s")
                parameters.append(start_date)
            if end_date:
                conditions.append("p.created < %s")
                parameters.append(end_date)
            if start_date and end_date:
                conditions.append("p.created BETWEEN %s AND %s")
                parameters.extend([start_date, end_date])

            if language:
                if language == "Wszystkie":
                    conditions.append("c.language IN %s")
                    language_all = ['Angielski', 'Niemiecki', 'Francuski', 'Włoski', 'Hiszpański']
                    placeholders = ', '.join(['%s'] * len(language_all))
                    conditions[-1] = conditions[-1].replace('%s', f'({placeholders})')
                    parameters.extend(language_all)
                else:
                    conditions.append("c.language = %s")
                    parameters.append(language)

            if status:
                if status == "Wszystkie":
                    conditions.append("p.status IN %s")
                    status_all = ['Do zapłaty', 'Zapłacone']
                    placeholders = ', '.join(['%s'] * len(status_all))
                    conditions[-1] = conditions[-1].replace('%s', f'({placeholders})')
                    parameters.extend(status_all)
                else:
                    conditions.append("p.status = %s")
                    parameters.append(status)

            if payment_type:
                if payment_type == "Wszystkie":
                    conditions.append("p.payment_type IN %s")
                    payment_types_all = ['W placówce', 'Przelew']
                    placeholders = ', '.join(['%s'] * len(payment_types_all))
                    conditions[-1] = conditions[-1].replace('%s', f'({placeholders})')
                    parameters.extend(payment_types_all)
                else:
                    conditions.append("p.payment_type = %s")
                    parameters.append(payment_type)

            where_clause = " AND ".join(conditions)

            query = """
                    SELECT
                        p.payment_id,
                        p.student_id,
                        s.first_name,
                        s.last_name,
                        c.course_id,
                        c.name,
                        c.language,
                        c.level,
                        c.mode,
                        p.amount,
                        p.payment_type,
                        p.status,
                        p.date_due,
                        p.created
                    FROM payments p
                    JOIN students s ON p.student_id = s.student_id
                    JOIN courses c ON p.course_id = c.course_id
                    WHERE {};
                    """.format(where_clause)

            cursor.execute(query, parameters)
            results = cursor.fetchall()

            if not results:
                self.show_custom_information("Nie znaleziono pasujących wyników. "
                                             "Spróbuj zmodyfikować kryteria wyszukiwania",
                                             "Info")
            else:
                self.treeview.delete(*self.treeview.get_children())

                for row in results:
                    date_due_str = str(row[12]).split()[0]
                    date_due_db = datetime.strptime(date_due_str, "%Y-%m-%d").strftime("%d.%m.%Y")

                    created_str = str(row[13]).split()[0]
                    created_db = datetime.strptime(created_str, "%Y-%m-%d").strftime("%d.%m.%Y")

                    self.treeview.insert("", END, values=((row[0]), (row[1]), (row[2]), (row[3]), (row[4]),
                                                          (row[5]), (row[6]), (row[7]), (row[8]), (row[9]), (row[10]),
                                                          (row[11]), date_due_db, created_db))

        finally:
            connection.close()

    def on_language_select(self):
        selected_language = self.language_var.get()
        print("Selected language:", selected_language)
        self.amend_menu_content_func(self.language_dropdown, selected_language)
        return selected_language

    def on_payment_status_select(self):
        selected_payment_status = self.status_var.get()
        print("Selected payment status:", selected_payment_status)
        self.amend_menu_content_func(self.payment_status, selected_payment_status)
        return selected_payment_status

    def on_payment_select(self):
        selected_payment_method = self.payment_var.get()
        print("Selected payment method:", selected_payment_method)
        self.amend_menu_content_func(self.payment_dropdown, selected_payment_method)
        return selected_payment_method

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
