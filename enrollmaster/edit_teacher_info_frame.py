from tkinter import *
import ttkbootstrap as ttk


class EditTeacherInfoFrame(ttk.Frame):

    def __init__(self, master=None, amend_menu_content_func=None, **kw):
        super().__init__(master, **kw)
        self.amend_menu_content_func = amend_menu_content_func
        self.columnconfigure((0, 2, 3, 4, 5), weight=1, minsize=250)
        self.columnconfigure(1, weight=1, minsize=50)
        self.rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28),
            weight=1, minsize=30)

        ## Config variable responsible for setting state of the elements

        free_state = ''
        disabled_state = 'disabled'
        readonly_state = 'readonly'
        disabled_state_button = 'disabled'

        self.teacher_id_var = StringVar()
        self.first_name_var = StringVar()
        self.last_name_var = StringVar()
        self.street_var = StringVar()
        self.building_no_var = StringVar()
        self.local_no_var = StringVar()
        self.city_var = StringVar()
        self.postal_code_var = StringVar()
        self.country_var = StringVar()
        self.email_var = StringVar()
        self.phone_number_var = StringVar()
        self.personal_id_var = StringVar()
        self.document_no_var = StringVar()
        self.document_type_var = StringVar()
        self.type_of_contract_var = StringVar()
        self.type_of_employment_var = StringVar()
        self.salary_var = StringVar()
        self.native_language_var = StringVar()
        self.language_to_teach_var = StringVar()
        self.employment_status_var = StringVar()

        ## name of the frame/page

        teacher_label = ttk.Label(self, text='EDYTUJ NAUCZYCIELA', font=('Open Sans', 14, 'bold'),
                                  bootstyle='default')
        teacher_label.grid(row=0, column=3, sticky='w')

        ## teacher_id used for search purposes

        id_label = ttk.Label(self, text='ID Nauczyciela', font=('Open Sans', 12), bootstyle='default')
        id_label.grid(row=2, column=2, sticky='w')

        self.id_entry = ttk.Entry(self, bootstyle='light', width=20)
        self.id_entry.grid(row=3, column=2, sticky='w')

        ## first_name

        first_name_label = ttk.Label(self, text="Imię", font=('Open Sans', 12), bootstyle='default')
        first_name_label.grid(row=2, column=3, sticky='w')

        self.first_name = ttk.Entry(self, width=20, bootstyle='light')
        self.first_name.grid(row=3, column=3, sticky='w')

        ## last_name

        last_name_label = ttk.Label(self, text="Nazwisko", font=('Open Sans', 12), bootstyle='default')
        last_name_label.grid(row=2, column=4, sticky='w')

        self.last_name = ttk.Entry(self, width=20, bootstyle='light')
        self.last_name.grid(row=3, column=4, sticky='w')

        ## submit button

        submit_button_style = ttk.Style()
        submit_button_style.configure('success.TButton', font=('Open Sans', 16))

        submit_button = ttk.Button(self, bootstyle='success', text='SZUKAJ', width=13,
                                   style='success.TButton')
        submit_button.grid(row=5, column=3, sticky='w')

        # teacher_id

        teacher_id_label = ttk.Label(self, text='ID Nauczyciela', font=('Open Sans', 12),
                                     bootstyle='default')
        teacher_id_label.grid(row=8, column=0, sticky='w')

        self.teacher_id = ttk.Entry(self, bootstyle='default', width=15, textvariable=self.teacher_id_var)
        self.teacher_id.configure(state=f'{readonly_state}')
        self.teacher_id.grid(row=9, column=0, sticky='w')

        # output_first_name

        output_first_name_label = ttk.Label(self, text='Imię', font=('Open Sans', 12),
                                            bootstyle='default')
        output_first_name_label.grid(row=8, column=2, sticky='w')

        self.output_first_name = ttk.Entry(self, bootstyle='default', width=15, textvariable=self.first_name_var)
        self.output_first_name.configure(state=f'{readonly_state}')
        self.output_first_name.grid(row=9, column=2, sticky='w')

        # output_last_name

        output_last_name_label = ttk.Label(self, text='Nazwisko', font=('Open Sans', 12),
                                           bootstyle='default')
        output_last_name_label.grid(row=8, column=3, sticky='w')

        self.output_last_name = ttk.Entry(self, bootstyle='default', width=15, textvariable=self.last_name_var)
        self.output_last_name.configure(state=f'{readonly_state}')
        self.output_last_name.grid(row=9, column=3, sticky='w')

        # output_street

        output_street_label = ttk.Label(self, text='Ulica', font=('Open Sans', 12), bootstyle='default')
        output_street_label.grid(row=8, column=4, sticky='w')

        self.output_street = ttk.Entry(self, bootstyle='default', width=30, textvariable=self.street_var)
        self.output_street.configure(state=f'{readonly_state}')
        self.output_street.grid(row=9, column=4, sticky='w')

        # output_building_no

        output_building_no_label = ttk.Label(self, text='Nr domu', font=('Open Sans', 12),
                                             bootstyle='default')
        output_building_no_label.grid(row=11, column=0, sticky='w')

        self.output_building_no = ttk.Entry(self, bootstyle='default', width=15, textvariable=self.building_no_var)
        self.output_building_no.configure(state=f'{readonly_state}')
        self.output_building_no.grid(row=12, column=0, sticky='w')

        # local_no_output

        local_no_output_label = ttk.Label(self, text='Nr lokalu', font=('Open Sans', 12),
                                          bootstyle='default')
        local_no_output_label.grid(row=11, column=2, sticky='w')

        self.local_no_output = ttk.Entry(self, bootstyle='default', width=15, textvariable=self.local_no_var)
        self.local_no_output.configure(state=f'{readonly_state}')
        self.local_no_output.grid(row=12, column=2, sticky='w')

        # city_output

        city_output_label = ttk.Label(self, text='Miasto', font=('Open Sans', 12), bootstyle='default')
        city_output_label.grid(row=11, column=3, sticky='w')

        self.city_output = ttk.Entry(self, bootstyle='default', width=20, textvariable=self.city_var)
        self.city_output.configure(state=f'{readonly_state}')
        self.city_output.grid(row=12, column=3, sticky='w')

        # postal_code_output

        postal_code_output_label = ttk.Label(self, text='Kod pocztowy', font=('Open Sans', 12),
                                             bootstyle='default')
        postal_code_output_label.grid(row=11, column=4, sticky='w')

        self.postal_code_output = ttk.Entry(self, bootstyle='default', width=15, textvariable=self.postal_code_var)
        self.postal_code_output.configure(state=f'{readonly_state}')
        self.postal_code_output.grid(row=12, column=4, sticky='w')

        # country_output

        country_output_label = ttk.Label(self, text='Państwo', font=('Open Sans', 12),
                                         bootstyle='default')
        country_output_label.grid(row=11, column=5, sticky='w')

        self.country_output = ttk.Entry(self, bootstyle='default', width=25, textvariable=self.country_var)
        self.country_output.configure(state=f'{readonly_state}')
        self.country_output.grid(row=12, column=5, sticky='w')

        # email_output

        email_output_label = ttk.Label(self, text='Adres e-mail', font=('Open Sans', 12),
                                       bootstyle='default')
        email_output_label.grid(row=14, column=0, sticky='w')

        self.email_output = ttk.Entry(self, bootstyle='default', width=25, textvariable=self.email_var)
        self.email_output.configure(state=f'{readonly_state}')
        self.email_output.grid(row=15, column=0, sticky='w')

        # phone_number_output

        phone_number_output_label = ttk.Label(self, text='Nr telefonu', font=('Open Sans', 12),
                                              bootstyle='default')
        phone_number_output_label.grid(row=14, column=2, sticky='w')

        self.phone_number_output = ttk.Entry(self, bootstyle='default', width=25, textvariable=self.phone_number_var)
        self.phone_number_output.configure(state=f'{readonly_state}')
        self.phone_number_output.grid(row=15, column=2, sticky='w')

        # personal_id_output

        personal_id_output_label = ttk.Label(self, text='PESEL', font=('Open Sans', 12),
                                             bootstyle='default')
        personal_id_output_label.grid(row=14, column=3, sticky='w')

        self.personal_id_output = ttk.Entry(self, bootstyle='default', width=25, textvariable=self.personal_id_var)
        self.personal_id_output.configure(state=f'{readonly_state}')
        self.personal_id_output.grid(row=15, column=3, sticky='w')

        # document_no_output

        document_no_output_label = ttk.Label(self, text='Nr dokumentu', font=('Open Sans', 12),
                                             bootstyle='default')
        document_no_output_label.grid(row=14, column=4, sticky='w')

        self.document_no_output = ttk.Entry(self, bootstyle='default', width=25, textvariable=self.document_no_var)
        self.document_no_output.configure(state=f'{readonly_state}')
        self.document_no_output.grid(row=15, column=4, sticky='w')

        # document_type_output

        document_type_output_label = ttk.Label(self, text='Rodzaj dokumentu', font=('Open Sans', 12),
                                               bootstyle='default')
        document_type_output_label.grid(row=14, column=5, sticky='w')



        self.document_type_output = ttk.Menubutton(self, bootstyle='dark')
        self.document_type_output.configure(state=f'{disabled_state}')
        self.document_type_output.grid(row=15, column=5, sticky='w')

        document_type_content = ttk.Menu(self.document_type_output)

        item_var = StringVar()
        for x in ['Dowód osobisty', 'Paszport', 'Karta pobytu']:
            document_type_content.add_radiobutton(label=x, variable=item_var,
                                                  command=lambda x=x: self.amend_menu_content_func(self.document_type_output, x))

        self.document_type_output['menu'] = document_type_content

        # type_of_contract_output

        type_of_contract_output_label = ttk.Label(self, text='Rodzaj umowy', font=('Open Sans', 12),
                                                  bootstyle='default')
        type_of_contract_output_label.grid(row=17, column=0, sticky='w')

        type_of_contract_output = ttk.Menubutton(self, bootstyle='dark', text=f'{self.type_of_contract_var}')
        type_of_contract_output.configure(state=f'{disabled_state}')
        type_of_contract_output.grid(row=18, column=0, sticky='w')

        type_of_contract_output_content = ttk.Menu(type_of_contract_output)

        type_var = StringVar()

        for x in ['Umowa o pracę', 'Umowa zlecenie']:
            type_of_contract_output_content.add_radiobutton(label=x, variable=type_var,
                                                            command=lambda x=x: self.amend_menu_content_func(
                                                                type_of_contract_output, x))

        type_of_contract_output['menu'] = type_of_contract_output_content

        # type_of_employment_output

        type_of_employment_output_label = ttk.Label(self, text='Rodzaj zatrudnienia',
                                                    font=('Open Sans', 12),
                                                    bootstyle='default')
        type_of_employment_output_label.grid(row=17, column=2, sticky='w')

        self.type_of_employment_output = ttk.Menubutton(self, bootstyle='dark',
                                                   text=f'{self.type_of_employment_var}')
        self.type_of_employment_output.configure(state=f'{disabled_state}')
        self.type_of_employment_output.grid(row=18, column=2, sticky='w')

        type_of_employment_output_content = ttk.Menu(self.type_of_employment_output)

        employment_var = StringVar()

        for x in ['Pełny etat', 'Pół etatu']:
            type_of_employment_output_content.add_radiobutton(label=x, variable=employment_var,
                                                              command=lambda x=x: self.amend_menu_content_func(
                                                                  self.type_of_employment_output, x))

        self.type_of_employment_output['menu'] = type_of_employment_output_content

        # salary_output

        salary_output_label = ttk.Label(self, text='Wynagrodzenie', font=('Open Sans', 12),
                                        bootstyle='default')
        salary_output_label.grid(row=17, column=3, sticky='w')

        self.salary_output = ttk.Entry(self, bootstyle='default', width=25, textvariable=self.salary_var)
        self.salary_output.configure(state=f'{readonly_state}')
        self.salary_output.grid(row=18, column=3, sticky='w')

        ## native_language_output

        native_language_output_label = ttk.Label(self, text='Język ojczysty', font=('Open Sans', 12),
                                                 bootstyle='default')
        native_language_output_label.grid(row=17, column=4, sticky='w')

        self.native_language_output = ttk.Entry(self, bootstyle='default', width=25, textvariable=self.native_language_var)
        self.native_language_output.configure(state='readonly')
        self.native_language_output.grid(row=18, column=4, sticky='w')

        ## language_to_teach_output

        language_to_teach_output_label = ttk.Label(self, text='Język nauczania', font=('Open Sans', 12),
                                                   bootstyle='default')
        language_to_teach_output_label.grid(row=17, column=5, sticky='w')

        self.language_to_teach_output = ttk.Entry(self, bootstyle='default', width=25, textvariable=self.language_to_teach_var)
        self.language_to_teach_output.configure(state='readonly')
        self.language_to_teach_output.grid(row=18, column=5, sticky='w')

        ## start_date_output

        start_date_output_label = ttk.Label(self, text='Data rozpoczęcia pracy', font=('Open Sans', 12),
                                            bootstyle='default')
        start_date_output_label.grid(row=20, column=0, sticky='w')

        self.start_date_output = ttk.DateEntry(self, bootstyle='primary')
        self.start_date_output.configure(state=f'{readonly_state}')
        self.start_date_output.grid(row=21, column=0, sticky='w')

        ## status_of_employment

        status_of_employment_label = ttk.Label(self, text='Status zatrudnienia', font=('Open Sans', 12),
                                               bootstyle='default')
        status_of_employment_label.grid(row=20, column=2, sticky='w')

        self.status_of_employment = ttk.Entry(self, bootstyle='default', width=25, textvariable=self.employment_status_var)
        self.status_of_employment.configure(state='readonly')
        self.status_of_employment.grid(row=21, column=2, sticky='w')

        ## edit button
        """
        When clicked, the entries change status from readonly to editable. 
        """

        edit_button_style = ttk.Style()
        edit_button_style.configure('primary.TButton', font=('Open Sans', 15))

        edit_button = ttk.Button(self, bootstyle='primary', text='EDYTUJ', width=15,
                                 style='primary.TButton',
                                 state=f'{disabled_state_button}')
        edit_button.grid(row=24, column=2, sticky='w')

        ## save_button

        save_button = ttk.Button(self, bootstyle='info', text='ZAPISZ', width=16,
                                 state=f'{disabled_state_button}')
        save_button.grid(row=24, column=3, sticky='w')

        ## block_button

        block_button_style = ttk.Style()
        block_button_style.configure('warning.TButton', font=('Open Sans', 15))

        block_button = ttk.Button(self, bootstyle='warning', text='ZABLOKUJ', width=15,
                                  state=f'{disabled_state_button}')
        block_button.grid(row=24, column=4, sticky='w')

        ## cancel_button - sets entries back to the readonly state and buttons do disabled state, including itself

        cancel_button_style = ttk.Style()
        cancel_button_style.configure('danger.TButton', font=('Open Sans', 15))

        cancel_button = ttk.Button(self, bootstyle='danger', text='ODRZUĆ', width=15,
                                   state=f'{disabled_state_button}')
        cancel_button.grid(row=26, column=3, sticky='w')

        self.pack()

    """
    Functions for dropdown selection.
    """

    def on_document_type_select(self):
        selected_document_type = self.document_var.get()
        print("Selected document type:", selected_document_type)
        self.amend_menu_content_func(self.document_type_output, selected_document_type)
        return selected_document_type

    def on_contract_type_select(self):
        selected_contract_type = self.type_var.get()
        print("Selected type of contract:", selected_contract_type)
        self.amend_menu_content_func(self.ou, selected_contract_type)
        return selected_contract_type

    def on_language_to_teach_select(self):
        selected_language = self.lang_var.get()
        print("Selected language:", selected_language)
        self.amend_menu_content_func(self.language_to_teach_output, selected_language)
        return selected_language

    def on_employment_type_select(self):
        selected_employment_type = self.employment_var.get()
        print("Selected type of employment:", selected_employment_type)
        self.amend_menu_content_func(self.type_of_employment_output, selected_employment_type)
        return selected_employment_type