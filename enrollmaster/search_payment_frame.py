from tkinter import *
import ttkbootstrap as ttk
import psycopg2
from datetime import datetime
from dotenv import load_dotenv
import os


class SearchPaymentFrame(ttk.Frame):

    def __init__(self, master=None, amend_menu_content_func=None, **kw):
        super().__init__(master, **kw)
        self.amend_menu_content_func = amend_menu_content_func
        self.columnconfigure((0, 1, 2, 3, 4), weight=1, minsize=50)
        self.rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28),
            weight=1, minsize=30)

        self.pack()

        # search_payment_label

        search_payment_label = ttk.Label(self, text='WYSZUKAJ PŁATNOŚĆ', font=('Open Sans', 14, 'bold'),
                                         bootstyle='default')
        search_payment_label.grid(row=0, column=2)

        # student_id

        student_id_label = ttk.Label(self, text='ID ucznia', font=('Open Sans', 12),
                                     bootstyle='default')
        student_id_label.grid(row=2, column=0, sticky='w')

        self.student_id_entry = ttk.Entry(self, bootstyle='light', width=20)
        self.student_id_entry.grid(row=3, column=0, sticky='w')

        # student_first_name

        student_first_name_label = ttk.Label(self, text='Imię ucznia', font=('Open Sans', 12),
                                             bootstyle='default')
        student_first_name_label.grid(row=2, column=1, sticky='w')

        self.first_name = ttk.Entry(self, bootstyle='light', width=20)
        self.first_name.grid(row=3, column=1, sticky='w')

        # student_last_name

        student_last_name_label = ttk.Label(self, text='Nazwisko ucznia', font=('Open Sans', 12),
                                            bootstyle='default')
        student_last_name_label.grid(row=2, column=2, sticky='w')

        self.last_name = ttk.Entry(self, bootstyle='light', width=20)
        self.last_name.grid(row=3, column=2, sticky='w')

        # course_id

        course_id_label = ttk.Label(self, text='ID kursu', font=('Open Sans', 12),
                                    bootstyle='default')
        course_id_label.grid(row=2, column=3, sticky='w')

        self.course_id = ttk.Entry(self, bootstyle='light', width=20)
        self.course_id.grid(row=3, column=3, sticky='w')

        # course_name

        course_name_label = ttk.Label(self, text='Nazwa kursu', bootstyle='default',
                                      font=('Open Sans', 12))
        course_name_label.grid(row=2, column=4, sticky='w')

        self.course_name = ttk.Entry(self, bootstyle='light', width=20)
        self.course_name.grid(row=3, column=4, sticky='w')

        # date_due

        date_due_label = ttk.Label(self, text='Termin płatności', font=('Open Sans', 12),
                                   bootstyle='default')
        date_due_label.grid(row=5, column=0, sticky='w')

        self.date_var = StringVar()
        self.date_var.set("")

        self.date_due_entry = ttk.DateEntry(self, bootstyle='default')
        self.date_due_entry.entry.configure(textvariable=self.date_var)
        self.date_due_entry.grid(row=6, column=0, sticky='w')

        # amount

        amount_label = ttk.Label(self, text='Kwota', font=('Open Sans', 12), bootstyle='default')
        amount_label.grid(row=5, column=1, sticky='w')

        self.amount = ttk.Entry(self, bootstyle='light', width=20)
        self.amount.grid(row=6, column=1, sticky='w')

        # payment_status

        payment_status_label = ttk.Label(self, text='Status płatności', font=('Open Sans', 12),
                                         bootstyle='default')
        payment_status_label.grid(row=5, column=2, sticky='w')

        self.payment_status = ttk.Menubutton(self, bootstyle='dark', text='Wybierz status')
        self.payment_status.grid(row=6, column=2, sticky='w')

        payment_status_content = ttk.Menu(self.payment_status)
        self.status_var = StringVar()
        self.status_var.set('')

        for x in ['Do zapłaty', 'Zapłacone']:
            payment_status_content.add_radiobutton(label=x, variable=self.status_var,
                                                   command=self.on_payment_status_select)

        self.payment_status['menu'] = payment_status_content

        # submit button

        submit_button_style = ttk.Style()
        submit_button_style.configure('success.TButton', font=('Open Sans', 14))

        submit_button = ttk.Button(self, bootstyle='success', text='SZUKAJ', width=16,
                                   style='success.TButton', command=self.search_function)
        submit_button.grid(row=8, column=2, sticky='w')

        # Create a Treeview widget

        self.treeview = ttk.Treeview(self, columns=("payment_id", "student_id", "first_name", "last_name",
                                                    "course_id", "course_name", "amount", "payment_type", "status",
                                                    "date_due"), show="headings")
        self.treeview.grid(row=12, column=0, columnspan=5, rowspan=10)

        # Define column headings
        self.treeview.heading("payment_id", text="ID płatności")
        self.treeview.heading("student_id", text="ID ucznia")
        self.treeview.heading("first_name", text="Imię ucznia")
        self.treeview.heading("last_name", text="Nazwisko ucznia")
        self.treeview.heading("course_id", text="ID kursu")
        self.treeview.heading("course_name", text="Nazwa kursu")
        self.treeview.heading("amount", text="Kwota")
        self.treeview.heading("payment_type", text="Rodzaj płatności")
        self.treeview.heading("status", text="Status płatności")
        self.treeview.heading("date_due", text="Termin płatności")

        # Set column widths

        self.treeview.column("payment_id", anchor='center')
        self.treeview.column("student_id", anchor='center')
        self.treeview.column("first_name", anchor='center')
        self.treeview.column("last_name", anchor='center')
        self.treeview.column("course_id", anchor='center')
        self.treeview.column("course_name", anchor='center')
        self.treeview.column("amount", anchor='center')
        self.treeview.column("payment_type", anchor='center')
        self.treeview.column("status", anchor='center')
        self.treeview.column("date_due", anchor='center')

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
            student_id = self.student_id_entry.get()
            first_name = self.first_name.get()
            last_name = self.last_name.get()
            course_id = self.course_id.get()
            course_name = self.course_name.get()
            amount = self.amount.get()
            date_due = self.date_due_entry.entry.get()
            status = self.status_var.get()

            conditions = []
            parameters = []

            # Brak kryteriów wyszukiwania
            if not any([student_id, first_name, last_name, course_id, course_name, amount, date_due, status]):
                self.show_custom_information(
                    "Nie znaleziono pasujących wyników. Spróbuj zmodyfikować kryteria wyszukiwania",
                    "Info"
                )
                return

            # Tworzenie warunków SQL
            if student_id:
                conditions.append("p.student_id = %s")
                parameters.append(student_id)
            if first_name:
                conditions.append("s.first_name = %s")
                parameters.append(first_name)
            if last_name:
                conditions.append("s.last_name = %s")
                parameters.append(last_name)
            if course_id:
                conditions.append("c.course_id = %s")
                parameters.append(course_id)
            if course_name:
                conditions.append("c.name = %s")
                parameters.append(course_name)
            if amount:
                conditions.append("p.amount = %s")
                parameters.append(amount)
            if date_due:
                conditions.append("p.date_due = %s")
                parameters.append(date_due)
            if status:
                conditions.append("p.status = %s")
                parameters.append(status)

            where_clause = " AND ".join(conditions)

            query = f"""
                        SELECT
                            p.payment_id,
                            p.student_id,
                            s.first_name,
                            s.last_name,
                            c.course_id,
                            c.name,
                            p.amount,
                            p.payment_type,
                            p.status,
                            p.date_due
                        FROM payments p
                        JOIN students s ON p.student_id = s.student_id
                        JOIN courses c ON p.course_id = c.course_id
                        WHERE {where_clause};
                        """

            cursor.execute(query, tuple(parameters))
            results = cursor.fetchall()

            if not results:
                self.show_custom_information(
                    "Nie znaleziono pasujących wyników. Spróbuj zmodyfikować kryteria wyszukiwania",
                    "Info"
                )
            else:
                self.treeview.delete(*self.treeview.get_children())

                for row in results:
                    date_str = str(row[9]).split()[0]
                    formatted_date = datetime.strptime(date_str, "%Y-%m-%d").strftime("%d.%m.%Y")

                    self.treeview.insert(
                        "",
                        END,
                        values=(
                            row[0], row[1], row[2], row[3],
                            row[4], row[5], row[6], row[7],
                            row[8], formatted_date
                        )
                    )

        except psycopg2.Error as e:
            self.show_custom_information(f"Błąd bazy danych: {e}", "Błąd")

        finally:
            connection.close()

    def on_payment_status_select(self):
        selected_payment_status = self.status_var.get()
        print("Selected payment status:", selected_payment_status)
        self.amend_menu_content_func(self.payment_status, selected_payment_status)
        return selected_payment_status

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
