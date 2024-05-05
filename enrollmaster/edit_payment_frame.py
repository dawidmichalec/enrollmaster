from tkinter import *
import ttkbootstrap as ttk
import psycopg2
from datetime import datetime


class EditPaymentFrame(ttk.Frame):

    def __init__(self, master=None, amend_menu_content_func=None, **kw):
        super().__init__(master, **kw)
        self.amend_menu_content_func = amend_menu_content_func
        self.columnconfigure((0, 1, 2, 3, 4), weight=1, minsize=310)
        self.rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28),
            weight=1, minsize=30)

        self.payment_id_var = StringVar()
        self.student_id_var = StringVar()
        self.first_name_var = StringVar()
        self.last_name_var = StringVar()
        self.course_id_var = StringVar()
        self.course_name_var = StringVar()
        self.price_var = StringVar()
        self.payment_var = StringVar()
        self.date_due_var = StringVar()
        self.status_var = StringVar()

        # edit_payment label

        edit_payment_label = ttk.Label(self, text='EDYTUJ PŁATNOŚĆ', font=('Open Sans', 14, 'bold'),
                                       bootstyle='default')
        edit_payment_label.grid(row=0, column=2, sticky='w')

        # payment_id

        payment_id_label = ttk.Label(self, text='ID płatności', font=('Open Sans', 12),
                                     bootstyle='default')
        payment_id_label.grid(row=2, column=2, sticky='w')

        self.payment_id_entry = ttk.Entry(self, bootstyle='light', width=27)
        self.payment_id_entry.grid(row=3, column=2, sticky='w')

        # submit_button

        submit_button_style = ttk.Style()
        submit_button_style.configure('success.TButton', font=('Open Sans', 14))

        submit_button = ttk.Button(self, bootstyle='success', text='SZUKAJ', width=16,
                                   style='success.TButton', command=self.search_function)
        submit_button.grid(row=5, column=2, sticky='w')

        # payment_id_output

        payment_id_output_label = ttk.Label(self, text='ID płatności', font=('Open Sans', 12),
                                            bootstyle='default')
        payment_id_output_label.grid(row=8, column=0, sticky='w')

        self.payment_id_output = ttk.Entry(self, bootstyle='default', width=20, textvariable=self.payment_id_var)
        self.payment_id_output.configure(state='readonly')
        self.payment_id_output.grid(row=9, column=0, sticky='w')

        # student_id_output

        student_id_label = ttk.Label(self, text='ID ucznia', font=('Open Sans', 12), bootstyle='default')
        student_id_label.grid(row=8, column=1, sticky='w')

        self.student_id = ttk.Entry(self, bootstyle='default', width=20, textvariable=self.student_id_var)
        self.student_id.configure(state='readonly')
        self.student_id.grid(row=9, column=1, sticky='w')

        # student_first_name

        student_first_name_label = ttk.Label(self, text='Imię ucznia', font=('Open Sans', 12),
                                             bootstyle='default')
        student_first_name_label.grid(row=8, column=2, sticky='w')

        self.first_name = ttk.Entry(self, bootstyle='default', width=20, textvariable=self.first_name_var)
        self.first_name.configure(state='readonly')
        self.first_name.grid(row=9, column=2, sticky='w')

        # student_last_name

        student_last_name_label = ttk.Label(self, text='Nazwisko ucznia', font=('Open Sans', 12),
                                            bootstyle='default')
        student_last_name_label.grid(row=8, column=3, sticky='w')

        self.last_name = ttk.Entry(self, bootstyle='default', width=20, textvariable=self.last_name_var)
        self.last_name.configure(state='readonly')
        self.last_name.grid(row=9, column=3, sticky='w')

        # course_id

        course_id_output_label = ttk.Label(self, text='ID kursu', font=('Open Sans', 12),
                                           bootstyle='default')
        course_id_output_label.grid(row=8, column=4, sticky='w')

        self.course_id = ttk.Entry(self, bootstyle='default', width=20, textvariable=self.course_id_var)
        self.course_id.configure(state='readonly')
        self.course_id.grid(row=9, column=4, sticky='w')

        # course_name

        course_name_label = ttk.Label(self, text='Nazwa kursu', font=('Open Sans', 12),
                                      bootstyle='default')
        course_name_label.grid(row=11, column=0, sticky='w')

        self.course_name = ttk.Entry(self, bootstyle='default', width=20, textvariable=self.course_name_var)
        self.course_name.configure(state='readonly')
        self.course_name.grid(row=12, column=0, sticky='w')

        # price

        price_label = ttk.Label(self, text='Do zapłaty', font=('Open Sans', 12),
                                bootstyle='default')
        price_label.grid(row=11, column=1, sticky='w')

        self.price = ttk.Entry(self, bootstyle='default', width=20, textvariable=self.price_var)
        self.price.configure(state='readonly')
        self.price.grid(row=12, column=1, sticky='w')

        # payment_type

        payment_type_label = ttk.Label(self, text="Sposób płatności", font=('Open Sans', 12),
                                       bootstyle='default')
        payment_type_label.grid(row=11, column=2, sticky='w')

        self.payment_type = ttk.Entry(self, bootstyle='default', width=20, textvariable=self.payment_var)
        self.payment_type.configure(state='readonly')
        self.payment_type.grid(row=12, column=2, sticky='w')

        # date_due

        date_due_label = ttk.Label(self, text='Termin zapłaty', font=('Open Sans', 12),
                                   bootstyle='default')
        date_due_label.grid(row=11, column=3, sticky='w')

        self.date_due_entry = ttk.Entry(self, bootstyle='default', width=20, textvariable=self.date_due_var)
        self.date_due_entry.configure(state='readonly')
        self.date_due_entry.grid(row=12, column=3, sticky='w')

        # payment_status

        payment_status_label = ttk.Label(self, text='Status płatności', font=('Open Sans', 12),
                                         bootstyle='default')
        payment_status_label.grid(row=11, column=4, sticky='w')

        self.payment_status = ttk.Menubutton(self, bootstyle='dark')
        self.payment_status.configure(state='disabled')
        self.payment_status.grid(row=12, column=4, sticky='w')

        payment_status_content = ttk.Menu(self.payment_status)

        for status in ['Do zapłaty', 'Zapłacone']:
            payment_status_content.add_radiobutton(label=status, variable=self.status_var, value=status,
                                                   command=self.on_payment_status_select)

        self.payment_status['menu'] = payment_status_content

        # edit button
        """
        When clicked, the entries change status from readonly to editable. 
        """

        edit_button_style = ttk.Style()
        edit_button_style.configure('primary.TButton', font=('Open Sans', 14))

        self.edit_button = ttk.Button(self, bootstyle='primary', text='EDYTUJ', width=16,
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

        self.cancel_button = ttk.Button(self, bootstyle='danger', text='ODRZUĆ', width=16,
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

        try:
            cursor = connection.cursor()
            payment_id = self.payment_id_var.get()
            status = self.status_var.get()

            query = """
                    UPDATE payments
                    SET status = %s
                    WHERE payment_id = %s;
                    """
            cursor.execute(query, (status, payment_id))
            connection.commit()

            self.clear_entries()
            self.block_entries()
            self.cancel_button['state'] = 'disabled'
            self.save_button['state'] = 'disabled'
            self.edit_button['state'] = 'disabled'
            self.show_custom_information("Dane kursu zostały zaktualizowane", "Info")
        finally:
            connection.close()

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

    def block_entries(self):
        self.payment_status.configure(state='disabled')

    def clear_entries(self):
        self.payment_id_var.set("")
        self.student_id_var.set("")
        self.first_name_var.set("")
        self.last_name_var.set("")
        self.course_id_var.set("")
        self.course_name_var.set("")
        self.price_var.set("")
        self.payment_var.set("")
        self.date_due_var.set("")
        self.status_var.set("")
        self.payment_status.configure(text="")

    def edit_function(self):
        self.save_button['state'] = 'normal'
        self.cancel_button['state'] = 'normal'

        self.payment_status.configure(state='normal')

    def search_function(self):
        connection = self.establish_database_connection()
        payment_id_entry = self.payment_id_entry.get()

        try:
            cursor = connection.cursor()

            if not payment_id_entry:
                self.show_custom_information("Należy podać ID płatności", "Błąd")
                return

            if payment_id_entry:
                query = """
                        SELECT
                            p.payment_id,
                            p.student_id,
                            s.first_name,
                            s.last_name,
                            c.course_id,
                            c.name,
                            p.amount,
                            p.payment_type,
                            p.date_due,
                            p.status
                        FROM payments p
                        JOIN students s ON p.student_id = s.student_id
                        JOIN courses c ON p.course_id = c.course_id 
                        WHERE p.payment_id = %s;
                        """
                cursor.execute(query, (payment_id_entry,))
                results = cursor.fetchone()

                if not results:
                    self.show_custom_information("Nie znaleziono nauczyciela. Sprawdź czy podałeś poprawne ID kursu",
                                                 "Info")
                else:
                    self.edit_button['state'] = 'normal'
                    payment_id, student_id, first_name, last_name, course_id, course_name, amount, payment_type, \
                        date_due, status = results

                    self.payment_id_var.set(payment_id)
                    self.student_id_var.set(student_id)
                    self.first_name_var.set(first_name)
                    self.last_name_var.set(last_name)
                    self.course_id_var.set(course_id)
                    self.course_name_var.set(course_name)
                    self.price_var.set(amount)
                    self.payment_var.set(payment_type)
                    date_due_str = str(date_due).split()[0]
                    date_due_db = datetime.strptime(date_due_str, "%Y-%m-%d").strftime("%d.%m.%Y")
                    self.date_due_var.set(date_due_db)
                    self.status_var.set(status)
                    self.payment_status.configure(text=status)
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

    def on_payment_select(self):
        selected_payment_method = self.payment_var.get()
        print("Selected payment method:", selected_payment_method)
        self.amend_menu_content_func(self.payment_dropdown, selected_payment_method)
        return selected_payment_method

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
