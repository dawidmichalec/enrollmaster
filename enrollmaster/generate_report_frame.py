from tkinter import *
import ttkbootstrap as ttk


class GenerateReportFrame(ttk.Frame):

    def __init__(self, master=None, amend_menu_content_func=None, **kw):
        super().__init__(master, **kw)
        self.amend_menu_content_func = amend_menu_content_func
        self.columnconfigure((0, 1, 2, 3, 4), weight=1, minsize=310)
        self.rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28),
            weight=1, minsize=30)

        generate_report_label = ttk.Label(self, text='WYGENERUJ RAPORT',
                                          font=('Open Sans', 14, 'bold'),
                                          bootstyle='default')
        generate_report_label.grid(row=0, column=2, sticky='w')

        ## start_date

        start_date_label = ttk.Label(self, text='Data od', bootstyle='default', font=('Open Sans', 12))
        start_date_label.grid(row=2, column=0, sticky='w')

        start_date_entry = ttk.DateEntry(self, bootstyle='primary')
        start_date_entry.grid(row=3, column=0, sticky='w')

        ## end_date

        end_date_label = ttk.Label(self, text='Data do', bootstyle='default', font=('Open Sans', 12))
        end_date_label.grid(row=2, column=1, sticky='w')

        end_date_entry = ttk.DateEntry(self, bootstyle='primary')
        end_date_entry.grid(row=3, column=1, sticky='w')

        ## language

        course_language_label = ttk.Label(self, text="Język kursu", font=('Open Sans', 12),
                                          bootstyle='default')
        course_language_label.grid(row=2, column=2, sticky='w')

        self.language_dropdown = ttk.Menubutton(self, bootstyle='dark', text="Wybierz język")
        self.language_dropdown.grid(row=3, column=2, sticky='w')

        language_dropdown_content = ttk.Menu(self.language_dropdown)

        self.language_var = StringVar()
        self.language_var.set('Angielski')
        for x in ['Angielski', 'Niemiecki', 'Francuski', 'Włoski', 'Hiszpański']:
            language_dropdown_content.add_radiobutton(label=x, variable=self.language_var,
                                                             command=self.on_language_select)

        self.language_dropdown['menu'] = language_dropdown_content

        ## payment_status

        payment_status_label = ttk.Label(self, text='Status płatności', font=('Open Sans', 12),
                                         bootstyle='default')
        payment_status_label.grid(row=2, column=3, sticky='w')

        self.payment_status = ttk.Menubutton(self, bootstyle='dark', text='Wybierz status')
        self.payment_status.grid(row=3, column=3, sticky='w')

        payment_status_content = ttk.Menu(self.payment_status)
        self.status_var = StringVar()
        self.status_var.set('Do zapłaty')

        for x in ['Do zapłaty', 'Zaległość', 'Zapłacone']:
            payment_status_content.add_radiobutton(label=x, variable=self.status_var,
                                                   command=self.on_payment_status_select)

        self.payment_status['menu'] = payment_status_content

        ## payment_type

        payment_type_label = ttk.Label(self, text="Sposób płatności", font=('Open Sans', 12),
                                       bootstyle='default')
        payment_type_label.grid(row=2, column=4, sticky='w')

        self.payment_dropdown = ttk.Menubutton(self, bootstyle='dark', text="Wybierz sposób płatności")
        self.payment_dropdown.grid(row=3, column=4, sticky='w')

        payment_dropdown_content = ttk.Menu(self.payment_dropdown)

        self.payment_var = StringVar()
        self.payment_var.set('W placówce')

        for x in ['W placówce', 'Przelew']:
            payment_dropdown_content.add_radiobutton(label=x, variable=self.payment_var,
                                                     command=self.on_payment_select)

        self.payment_dropdown['menu'] = payment_dropdown_content

        ## submit_button

        submit_button_style = ttk.Style()
        submit_button_style.configure('success.TButton', font=('Open Sans', 16))

        submit_button = ttk.Button(self, bootstyle='success', text='SZUKAJ', width=13,
                                   style='success.TButton')
        submit_button.grid(row=6, column=2, sticky='w')

        ## export_button

        export_button_style = ttk.Style()
        export_button_style.configure('primary.TButton', font=('Open Sans', 15))

        export_button = ttk.Button(self, bootstyle='primary', text='CSV', width=13,
                                   style='primary.TButton')
        export_button.grid(row=6, column=3, sticky='w')

        ## output_label

        output_label = ttk.Label(self, font=('Open Sans', 12), bootstyle='default', text='asdfasdf')
        output_label.grid(row=9, column=2, sticky='w')

        self.pack()

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