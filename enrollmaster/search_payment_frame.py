from tkinter import *
import ttkbootstrap as ttk


class SearchPaymentFrame(ttk.Frame):

    def __init__(self, master=None, amend_menu_content_func=None, **kw):
        super().__init__(master, **kw)
        self.amend_menu_content_func = amend_menu_content_func
        self.columnconfigure((0, 1, 2, 3, 4), weight=1, minsize=250)
        self.rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28),
            weight=1, minsize=30)

        ## search_payment_label

        search_payment_label = ttk.Label(self, text='WYSZUKAJ PŁATNOŚĆ', font=('Open Sans', 14, 'bold'),
                                         bootstyle='default')
        search_payment_label.grid(row=0, column=2)

        ## student_id

        student_id_label = ttk.Label(self, text='ID ucznia', font=('Open Sans', 12),
                                     bootstyle='default')
        student_id_label.grid(row=2, column=0, sticky='w')

        student_id_entry = ttk.Entry(self, bootstyle='light', width=20)
        student_id_entry.grid(row=3, column=0, sticky='w')

        ## student_first_name

        student_first_name_label = ttk.Label(self, text='Imię ucznia', font=('Open Sans', 12),
                                             bootstyle='default')
        student_first_name_label.grid(row=2, column=1, sticky='w')

        student_first_name_entry = ttk.Entry(self, bootstyle='light', width=20)
        student_first_name_entry.grid(row=3, column=1, sticky='w')

        ## student_last_name

        student_last_name_label = ttk.Label(self, text='Nazwisko ucznia', font=('Open Sans', 12),
                                            bootstyle='default')
        student_last_name_label.grid(row=2, column=2, sticky='w')

        student_last_name_entry = ttk.Entry(self, bootstyle='light', width=20)
        student_last_name_entry.grid(row=3, column=2, sticky='w')

        ## course_id

        course_id_label = ttk.Label(self, text='ID kursu', font=('Open Sans', 12),
                                    bootstyle='default')
        course_id_label.grid(row=2, column=3, sticky='w')

        course_id_entry = ttk.Entry(self, bootstyle='light', width=20)
        course_id_entry.grid(row=3, column=3, sticky='w')

        ## course_name

        course_name_label = ttk.Label(self, text='Nazwa kursu', bootstyle='default',
                                      font=('Open Sans', 12))
        course_name_label.grid(row=2, column=4, sticky='w')

        course_name_entry = ttk.Entry(self, bootstyle='light', width=20)
        course_name_entry.grid(row=3, column=4, sticky='w')

        ## date_due

        date_due_label = ttk.Label(self, text='Termin płatności', font=('Open Sans', 12),
                                   bootstyle='default')
        date_due_label.grid(row=5, column=0, sticky='w')

        date_due_entry = ttk.DateEntry(self, bootstyle='default')
        date_due_entry.grid(row=6, column=0, sticky='w')

        ## amount

        amount_label = ttk.Label(self, text='Cena', font=('Open Sans', 12), bootstyle='default')
        amount_label.grid(row=5, column=1, sticky='w')

        amount_entry = ttk.Entry(self, bootstyle='light', width=20)
        amount_entry.grid(row=6, column=1, sticky='w')

        ## payment_status

        payment_status_label = ttk.Label(self, text='Status płatności', font=('Open Sans', 12),
                                         bootstyle='default')
        payment_status_label.grid(row=5, column=2, sticky='w')

        self.payment_status = ttk.Menubutton(self, bootstyle='dark', text='Wybierz status')
        self.payment_status.grid(row=6, column=2, sticky='w')

        payment_status_content = ttk.Menu(self.payment_status)
        self.status_var = StringVar()
        self.status_var.set('Do zapłaty')

        for x in ['Do zapłaty', 'Zaległość', 'Zapłacone']:
            payment_status_content.add_radiobutton(label=x, variable=self.status_var,
                                                   command=self.on_payment_status_select)

        self.payment_status['menu'] = payment_status_content

        ## submit button

        submit_button_style = ttk.Style()
        submit_button_style.configure('success.TButton', font=('Open Sans', 16))

        submit_button = ttk.Button(self, bootstyle='success', text='SZUKAJ', width=13,
                                   style='success.TButton')
        submit_button.grid(row=8, column=2, sticky='w')

        ## output label

        output_label = ttk.Label(self, font=('Open Sans', 12), bootstyle='default', text='asdfasdf')
        output_label.grid(row=11, column=2, sticky='w')

        self.pack()

    def on_payment_status_select(self):
        selected_payment_status = self.status_var.get()
        print("Selected payment status:", selected_payment_status)
        self.amend_menu_content_func(self.payment_status, selected_payment_status)
        return selected_payment_status