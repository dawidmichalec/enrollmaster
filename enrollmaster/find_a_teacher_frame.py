from tkinter import *
import ttkbootstrap as ttk


class FindATeacherFrame(ttk.Frame):

    def __init__(self, master=None, amend_menu_content_func=None, **kw):
        super().__init__(master, **kw)
        self.amend_menu_content_func = amend_menu_content_func
        self.columnconfigure((0, 1, 2, 3, 4), weight=1, minsize=250)
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

        last_name = ttk.Entry(self, width=20, bootstyle='light')
        last_name.grid(column=1, row=3, sticky='w')

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

        for contract in ['Umowa o pracę', 'Umowa zlecenie']:
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

        employment_start_from_var = StringVar()
        employment_start_from_var.set("")

        employment_start_from_label = ttk.Label(self, text='Data zatrudnienia od', font=('Open Sans', 12),
                                     bootstyle='default')
        employment_start_from_label.grid(row=5, column=1, sticky='w')

        employment_start_from = ttk.DateEntry(self, bootstyle='primary')
        employment_start_from.grid(row=6, column=1, sticky='w')
        employment_start_from.entry.configure(textvariable=employment_start_from_var)

        # employment_start_to

        employment_start_to_var = StringVar()
        employment_start_to_var.set("")

        employment_start_to_label = ttk.Label(self, text='Data zatrudnienia do', font=('Open Sans', 12),
                                   bootstyle='default')
        employment_start_to_label.grid(row=5, column=2, sticky='w')

        employment_start_to = ttk.DateEntry(self, bootstyle='primary')
        employment_start_to.grid(row=6, column=2, sticky='w')
        employment_start_to.entry.configure(textvariable=employment_start_to_var)

        # submit

        submit_button_style = ttk.Style()
        submit_button_style.configure('success.TButton', font=('Open Sans', 16))

        submit_button = ttk.Button(self, bootstyle='success', text='SZUKAJ', width=15,
                                   style='success.TButton')
        submit_button.grid(row=9, column=2, sticky='w')

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
