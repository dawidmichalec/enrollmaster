from tkinter import *
import ttkbootstrap as ttk
import psycopg2
import re
import decimal

class EditTeacherInfoFrame(ttk.Frame):

    def __init__(self, master=None, amend_menu_content_func=None, **kw):
        super().__init__(master, **kw)
        self.amend_menu_content_func = amend_menu_content_func
        self.columnconfigure((0, 2, 3, 4, 5), weight=1, minsize=250)
        self.columnconfigure(1, weight=1, minsize=50)
        self.rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28),
            weight=1, minsize=30)

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
        self.document_var = StringVar()
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
                                   style='success.TButton', command=self.search_function)
        submit_button.grid(row=5, column=3, sticky='w')

        # teacher_id

        teacher_id_label = ttk.Label(self, text='ID Nauczyciela', font=('Open Sans', 12),
                                     bootstyle='default')
        teacher_id_label.grid(row=8, column=0, sticky='w')

        self.teacher_id = ttk.Entry(self, bootstyle='default', width=15, textvariable=self.teacher_id_var)
        self.teacher_id.configure(state='readonly')
        self.teacher_id.grid(row=9, column=0, sticky='w')

        # output_first_name

        output_first_name_label = ttk.Label(self, text='Imię', font=('Open Sans', 12),
                                            bootstyle='default')
        output_first_name_label.grid(row=8, column=2, sticky='w')

        self.output_first_name = ttk.Entry(self, bootstyle='default', width=15, textvariable=self.first_name_var)
        self.output_first_name.configure(state='readonly')
        self.output_first_name.grid(row=9, column=2, sticky='w')

        # output_last_name

        output_last_name_label = ttk.Label(self, text='Nazwisko', font=('Open Sans', 12),
                                           bootstyle='default')
        output_last_name_label.grid(row=8, column=3, sticky='w')

        self.output_last_name = ttk.Entry(self, bootstyle='default', width=15, textvariable=self.last_name_var)
        self.output_last_name.configure(state='readonly')
        self.output_last_name.grid(row=9, column=3, sticky='w')

        # output_street

        output_street_label = ttk.Label(self, text='Ulica', font=('Open Sans', 12), bootstyle='default')
        output_street_label.grid(row=8, column=4, sticky='w')

        self.output_street = ttk.Entry(self, bootstyle='default', width=30, textvariable=self.street_var)
        self.output_street.configure(state='readonly')
        self.output_street.grid(row=9, column=4, sticky='w')

        # output_building_no

        output_building_no_label = ttk.Label(self, text='Nr domu', font=('Open Sans', 12),
                                             bootstyle='default')
        output_building_no_label.grid(row=11, column=0, sticky='w')

        self.output_building_no = ttk.Entry(self, bootstyle='default', width=15, textvariable=self.building_no_var)
        self.output_building_no.configure(state='readonly')
        self.output_building_no.grid(row=12, column=0, sticky='w')

        # local_no_output

        local_no_output_label = ttk.Label(self, text='Nr lokalu', font=('Open Sans', 12),
                                          bootstyle='default')
        local_no_output_label.grid(row=11, column=2, sticky='w')

        self.local_no_output = ttk.Entry(self, bootstyle='default', width=15, textvariable=self.local_no_var)
        self.local_no_output.configure(state='readonly')
        self.local_no_output.grid(row=12, column=2, sticky='w')

        # city_output

        city_output_label = ttk.Label(self, text='Miasto', font=('Open Sans', 12), bootstyle='default')
        city_output_label.grid(row=11, column=3, sticky='w')

        self.city_output = ttk.Entry(self, bootstyle='default', width=20, textvariable=self.city_var)
        self.city_output.configure(state='readonly')
        self.city_output.grid(row=12, column=3, sticky='w')

        # postal_code_output

        postal_code_output_label = ttk.Label(self, text='Kod pocztowy', font=('Open Sans', 12),
                                             bootstyle='default')
        postal_code_output_label.grid(row=11, column=4, sticky='w')

        self.postal_code_output = ttk.Entry(self, bootstyle='default', width=15, textvariable=self.postal_code_var)
        self.postal_code_output.configure(state='readonly')
        self.postal_code_output.grid(row=12, column=4, sticky='w')

        # country_output

        country_output_label = ttk.Label(self, text='Państwo', font=('Open Sans', 12),
                                         bootstyle='default')
        country_output_label.grid(row=11, column=5, sticky='w')

        self.country_output = ttk.Entry(self, bootstyle='default', width=25, textvariable=self.country_var)
        self.country_output.configure(state='readonly')
        self.country_output.grid(row=12, column=5, sticky='w')

        # email_output

        email_output_label = ttk.Label(self, text='Adres e-mail', font=('Open Sans', 12),
                                       bootstyle='default')
        email_output_label.grid(row=14, column=0, sticky='w')

        self.email_output = ttk.Entry(self, bootstyle='default', width=25, textvariable=self.email_var)
        self.email_output.configure(state='readonly')
        self.email_output.grid(row=15, column=0, sticky='w')

        # phone_number_output

        phone_number_output_label = ttk.Label(self, text='Nr telefonu', font=('Open Sans', 12),
                                              bootstyle='default')
        phone_number_output_label.grid(row=14, column=2, sticky='w')

        self.phone_number_output = ttk.Entry(self, bootstyle='default', width=25, textvariable=self.phone_number_var)
        self.phone_number_output.configure(state='readonly')
        self.phone_number_output.grid(row=15, column=2, sticky='w')

        # personal_id_output

        personal_id_output_label = ttk.Label(self, text='PESEL', font=('Open Sans', 12),
                                             bootstyle='default')
        personal_id_output_label.grid(row=14, column=3, sticky='w')

        self.personal_id_output = ttk.Entry(self, bootstyle='default', width=25, textvariable=self.personal_id_var)
        self.personal_id_output.configure(state='readonly')
        self.personal_id_output.grid(row=15, column=3, sticky='w')

        # document_no_output

        document_no_output_label = ttk.Label(self, text='Nr dokumentu', font=('Open Sans', 12),
                                             bootstyle='default')
        document_no_output_label.grid(row=14, column=4, sticky='w')

        self.document_no_output = ttk.Entry(self, bootstyle='default', width=25, textvariable=self.document_no_var)
        self.document_no_output.configure(state='readonly')
        self.document_no_output.grid(row=15, column=4, sticky='w')

        # document_type_output

        document_type_output_label = ttk.Label(self, text='Rodzaj dokumentu', font=('Open Sans', 12),
                                               bootstyle='default')
        document_type_output_label.grid(row=14, column=5, sticky='w')

        self.document_type_output = ttk.Menubutton(self, bootstyle='dark')
        self.document_type_output.configure(state='disabled')
        self.document_type_output.grid(row=15, column=5, sticky='w')

        document_type_content = ttk.Menu(self.document_type_output)

        self.document_var.set("")
        for document in ['Dowód osobisty', 'Paszport', 'Karta pobytu']:
            document_type_content.add_radiobutton(label=document, variable=self.document_var, value=document,
                                                  command=self.on_document_type_select)

        self.document_type_output['menu'] = document_type_content

        # type_of_contract_output

        type_of_contract_label = ttk.Label(self, text='Rodzaj umowy', font=('Open Sans', 12),
                                                  bootstyle='default')
        type_of_contract_label.grid(row=17, column=0, sticky='w')

        self.type_of_contract = ttk.Menubutton(self, bootstyle='dark')
        self.type_of_contract.configure(state='disabled')
        self.type_of_contract.grid(row=18, column=0, sticky='w')

        type_of_contract_output_content = ttk.Menu(self.type_of_contract)

        self.type_of_contract_var.set("")

        for contract in ['Umowa o pracę', 'Umowa zlecenie']:
            type_of_contract_output_content.add_radiobutton(label=contract, variable=self.type_of_contract_var,
                                                            value=contract, command=self.on_contract_type_select)

        self.type_of_contract['menu'] = type_of_contract_output_content

        # type_of_employment_output

        type_of_employment_output_label = ttk.Label(self, text='Rodzaj zatrudnienia',
                                                    font=('Open Sans', 12),
                                                    bootstyle='default')
        type_of_employment_output_label.grid(row=17, column=2, sticky='w')

        self.type_of_employment_output = ttk.Menubutton(self, bootstyle='dark')
        self.type_of_employment_output.configure(state='disabled')
        self.type_of_employment_output.grid(row=18, column=2, sticky='w')

        type_of_employment_output_content = ttk.Menu(self.type_of_employment_output)

        self.type_of_employment_var.set("")

        for employment in ['Pełny etat', 'Pół etatu']:
            type_of_employment_output_content.add_radiobutton(label=employment, variable=self.type_of_employment_var,
                                                              value=employment, command=self.on_employment_type_select)

        self.type_of_employment_output['menu'] = type_of_employment_output_content

        # salary_output

        salary_output_label = ttk.Label(self, text='Wynagrodzenie', font=('Open Sans', 12),
                                        bootstyle='default')
        salary_output_label.grid(row=17, column=3, sticky='w')

        self.salary_output = ttk.Entry(self, bootstyle='default', width=25, textvariable=self.salary_var)
        self.salary_output.configure(state='readonly')
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

        self.language_to_teach = ttk.Menubutton(self, bootstyle='dark')
        self.language_to_teach.configure(state='disabled')
        self.language_to_teach.grid(row=18, column=5, sticky='w')

        language_to_teach_content = ttk.Menu(self.language_to_teach)

        self.language_to_teach_var.set("")

        for language in ['Angielski', 'Niemiecki', 'Francuski', 'Włoski', 'Hiszpański']:
            language_to_teach_content.add_radiobutton(label=language, variable=self.language_to_teach_var, value=language,
                                                      command=self.on_language_to_teach_select)

        self.language_to_teach['menu'] = language_to_teach_content

        ## start_date_output

        start_date_output_label = ttk.Label(self, text='Data rozpoczęcia pracy', font=('Open Sans', 12),
                                            bootstyle='default')
        start_date_output_label.grid(row=20, column=0, sticky='w')

        self.start_date_output = ttk.DateEntry(self, bootstyle='primary')
        self.start_date_output.configure(state='readonly')
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

        self.edit_button = ttk.Button(self, bootstyle='primary', text='EDYTUJ', width=15,
                                 style='primary.TButton', command=self.edit_function)
        self.edit_button.grid(row=24, column=2, sticky='w')
        self.edit_button['state'] = 'disabled'

        ## save_button

        self.save_button = ttk.Button(self, bootstyle='info', text='ZAPISZ', width=16)
        self.save_button.grid(row=24, column=3, sticky='w')
        self.save_button['state'] = 'disabled'

        ## block_button

        block_button_style = ttk.Style()
        block_button_style.configure('warning.TButton', font=('Open Sans', 15))

        self.block_button = ttk.Button(self, bootstyle='warning', text='ZABLOKUJ', width=15, command=self.block_function)
        self.block_button.grid(row=24, column=4, sticky='w')
        self.block_button['state'] = 'disabled'

        ## cancel_button - sets entries back to the readonly state and buttons do disabled state, including itself

        cancel_button_style = ttk.Style()
        cancel_button_style.configure('danger.TButton', font=('Open Sans', 15))

        self.cancel_button = ttk.Button(self, bootstyle='danger', text='ODRZUĆ', width=15, command=self.cancel_button_function)
        self.cancel_button.grid(row=26, column=3, sticky='w')
        self.cancel_button['state'] = 'disabled'

        self.pack()


    def search_function(self):
        self.edit_button['state'] = 'normal'
        self.block_button['state'] = 'normal'

    def edit_function(self):

        # unblock cancel and save buttons
        self.cancel_button['state'] = 'normal'
        self.save_button['state'] = 'normal'

        # allow the user to change the data

        self.output_first_name.configure(state='')
        self.output_last_name.configure(state='')
        self.output_street.configure(state='')
        self.output_building_no.configure(state='')
        self.local_no_output.configure(state='')
        self.city_output.configure(state='')
        self.postal_code_output.configure(state='')
        self.country_output.configure(state='')
        self.email_output.configure(state='')
        self.phone_number_output.configure(state='')
        self.personal_id_output.configure(state='')
        self.document_no_output.configure(state='')
        self.document_type_output.configure(state='')
        self.type_of_contract.configure(state='')
        self.type_of_employment_output.configure(state='')
        self.salary_output.configure(state='')
        self.native_language_output.configure(state='')
        self.language_to_teach.configure(state='')
        self.start_date_output.configure(state='normal')





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
        self.block_button['state'] = 'disabled'


    def block_function(self):
        self.show_custom_messagebox("Czy na pewno chcesz zablokować tego nauczyciela?",
                                    "Ostrzeżenie",
                                    self.block_teacher,
                                    self.dismiss_messagebox)

    def block_teacher(self):
        self.clear_entries()
        self.block_entries()
        self.cancel_button['state'] = 'disabled'
        self.save_button['state'] = 'disabled'
        self.edit_button['state'] = 'disabled'
        self.block_button['state'] = 'disabled'

        self.show_custom_information("Nauczyciel został zablokowany", "Info")
        # Update the status to "inactive"
        print("Teacher blocked. Status updated to inactive.")

    def clear_entries(self):

        self.teacher_id_var.set("")
        self.first_name_var.set("")
        self.last_name_var.set("")
        self.street_var.set("")
        self.building_no_var.set("")
        self.local_no_var.set("")
        self.city_var.set("")
        self.postal_code_var.set("")
        self.country_var.set("")
        self.email_var.set("")
        self.phone_number_var.set("")
        self.personal_id_var.set("")
        self.document_no_var.set("")
        self.document_var.set("")
        self.document_type_output.configure(text='')
        self.type_of_contract_var.set("")
        self.type_of_contract.configure(text='')
        self.type_of_employment_var.set("")
        self.type_of_employment_output.configure(text='')
        self.salary_var.set("")
        self.native_language_var.set("")
        self.language_to_teach_var.set("")
        self.language_to_teach.configure(text='')
        self.employment_status_var.set("")

    def block_entries(self):
        self.output_first_name.configure(state='readonly')
        self.output_last_name.configure(state='readonly')
        self.output_street.configure(state='readonly')
        self.output_building_no.configure(state='readonly')
        self.local_no_output.configure(state='readonly')
        self.city_output.configure(state='readonly')
        self.postal_code_output.configure(state='readonly')
        self.country_output.configure(state='readonly')
        self.email_output.configure(state='readonly')
        self.phone_number_output.configure(state='readonly')
        self.personal_id_output.configure(state='readonly')
        self.document_no_output.configure(state='readonly')
        self.document_type_output.configure(state='disabled')
        self.type_of_contract.configure(state='disabled')
        self.type_of_employment_output.configure(state='disabled')
        self.salary_output.configure(state='readonly')
        self.native_language_output.configure(state='readonly')
        self.language_to_teach.configure(state='disabled')
        self.start_date_output.configure(state='readonly')

    def dismiss_messagebox(self):
        # Do nothing, just dismiss the messagebox
        print("Messagebox dismissed.")

    """
    Functions for dropdown selection.
    """

    def on_document_type_select(self):
        selected_document_type = self.document_var.get()
        print("Selected document type:", selected_document_type)
        self.amend_menu_content_func(self.document_type_output, selected_document_type)
        return selected_document_type

    def on_language_to_teach_select(self):
        selected_language = self.language_to_teach_var.get()
        print("Selected language:", selected_language)
        self.amend_menu_content_func(self.language_to_teach, selected_language)
        return selected_language

    def on_contract_type_select(self):
        selected_contract_type = self.type_of_contract_var.get()
        print("Selected type of contract:", selected_contract_type)
        self.amend_menu_content_func(self.type_of_contract, selected_contract_type)
        return selected_contract_type

    def on_employment_type_select(self):
        selected_employment_type = self.type_of_employment_var.get()
        print("Selected type of employment:", selected_employment_type)
        self.amend_menu_content_func(self.type_of_employment_output, selected_employment_type)
        return selected_employment_type

    # Custom messagebox

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

    def show_custom_information(self, message, title):
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
        Button(custom_mb, text="OK", command=custom_mb.destroy, width=20, height=1, font=('Open Sans', 12)).pack()

    def yesno_response(self, custom_mb, response, action):
        # Do something with the response (True for "Yes", False for "No")
        print("User response:", response)
        # Call the associated action
        action()
        # Close the messagebox
        custom_mb.destroy()