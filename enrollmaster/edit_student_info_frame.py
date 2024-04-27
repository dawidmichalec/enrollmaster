from tkinter import *
import ttkbootstrap as ttk


class EditStudentInfoFrame(ttk.Frame):
    
    def __init__(self, master=None, amend_menu_content_func=None, **kw):
        super().__init__(master, **kw)
        self.amend_menu_content_func = amend_menu_content_func
        self.columnconfigure((0, 2, 3, 4, 5), weight=1, minsize=250)
        self.columnconfigure(1, weight=1, minsize=50)
        self.rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28),
            weight=1, minsize=30)

        ## Config variable responsible for setting state of the elements and inserting data from the database.
        free_state = ""
        readonly_state = 'readonly'
        disabled_state = 'disabled'
        disabled_state_button = 'disabled'
        student_id_var = ''
        first_name_var = ''
        last_name_var = ''
        street_var = ''
        building_no_var = ''
        local_no_var = ''
        city_var = ''
        postal_code_var = ''
        country_var = ''
        email_var = ''
        phone_number_var = ''
        personal_id_var = ''
        document_no_var = ''
        document_type_var = ''
        course_name_var = ''
        language_db = ""
        status_var = ''
        level_db = ""
        mode_db = ""

        ## name of the frame/page

        student_label = ttk.Label(self, text='EDYTUJ UCZNIA', font=('Open Sans', 14, 'bold'),
                                  bootstyle='default')
        student_label.grid(row=0, column=3, sticky='w')

        ## student_id used for search purposes

        id_label = ttk.Label(self, text='ID Ucznia', font=('Open Sans', 12), bootstyle='default')
        id_label.grid(row=2, column=2, sticky='w')

        id_entry = ttk.Entry(self, bootstyle='light', width=20)
        id_entry.grid(row=3, column=2, sticky='w')

        ## first_name

        first_name_label = ttk.Label(self, text="Imię", font=('Open Sans', 12), bootstyle='default')
        first_name_label.grid(row=2, column=3, sticky='w')

        first_name = ttk.Entry(self, width=20, bootstyle='light')
        first_name.grid(row=3, column=3, sticky='w')

        ## last_name

        last_name_label = ttk.Label(self, text="Nazwisko", font=('Open Sans', 12), bootstyle='default')
        last_name_label.grid(row=2, column=4, sticky='w')

        last_name = ttk.Entry(self, width=20, bootstyle='light')
        last_name.grid(row=3, column=4, sticky='w')

        ## submit button

        submit_button_style = ttk.Style()
        submit_button_style.configure('success.TButton', font=('Open Sans', 16))

        submit_button = ttk.Button(self, bootstyle='success', text='SZUKAJ', width=13,
                                   style='success.TButton')
        submit_button.grid(row=5, column=3, sticky='w')

        ## student_id

        student_id_label = ttk.Label(self, text='ID Ucznia', font=('Open Sans', 12), bootstyle='default')
        student_id_label.grid(row=8, column=0, sticky='w')

        student_id = ttk.Entry(self, bootstyle='default', width=15)
        student_id.insert('end', student_id_var)
        student_id.configure(state='readonly')
        student_id.grid(row=9, column=0, sticky='w')

        ## output_first_name

        output_first_name_label = ttk.Label(self, text='Imię', font=('Open Sans', 12),
                                            bootstyle='default')
        output_first_name_label.grid(row=8, column=2, sticky='w')

        output_first_name = ttk.Entry(self, bootstyle='default', width=15)
        output_first_name.insert('end', first_name_var)
        output_first_name.configure(state=f'{readonly_state}')
        output_first_name.grid(row=9, column=2, sticky='w')

        ## output_last_name

        output_last_name_label = ttk.Label(self, text='Nazwisko', font=('Open Sans', 12),
                                           bootstyle='default')
        output_last_name_label.grid(row=8, column=3, sticky='w')

        output_last_name = ttk.Entry(self, bootstyle='default', width=15)
        output_last_name.insert('end', last_name_var)
        output_last_name.configure(state=f'{readonly_state}')
        output_last_name.grid(row=9, column=3, sticky='w')

        ## output_street

        output_street_label = ttk.Label(self, text='Ulica', font=('Open Sans', 12), bootstyle='default')
        output_street_label.grid(row=8, column=4, sticky='w')

        output_street = ttk.Entry(self, bootstyle='default', width=30)
        output_street.insert('end', street_var)
        output_street.configure(state=f'{readonly_state}')
        output_street.grid(row=9, column=4, sticky='w')

        ## output_building_no

        output_building_no_label = ttk.Label(self, text='Nr domu', font=('Open Sans', 12),
                                             bootstyle='default')
        output_building_no_label.grid(row=11, column=0, sticky='w')

        output_building_no = ttk.Entry(self, bootstyle='default', width=15)
        output_building_no.insert('end', building_no_var)
        output_building_no.configure(state=f'{readonly_state}')
        output_building_no.grid(row=12, column=0, sticky='w')

        ## local_no_output

        local_no_output_label = ttk.Label(self, text='Nr lokalu', font=('Open Sans', 12),
                                          bootstyle='default')
        local_no_output_label.grid(row=11, column=2, sticky='w')

        local_no_output = ttk.Entry(self, bootstyle='default', width=15)
        local_no_output.insert('end', local_no_var)
        local_no_output.configure(state=f'{readonly_state}')
        local_no_output.grid(row=12, column=2, sticky='w')

        ## city_output

        city_output_label = ttk.Label(self, text='Miasto', font=('Open Sans', 12), bootstyle='default')
        city_output_label.grid(row=11, column=3, sticky='w')

        city_output = ttk.Entry(self, bootstyle='default', width=20)
        city_output.insert('end', city_var)
        city_output.configure(state=f'{readonly_state}')
        city_output.grid(row=12, column=3, sticky='w')

        ## postal_code_output

        postal_code_output_label = ttk.Label(self, text='Kod pocztowy', font=('Open Sans', 12),
                                             bootstyle='default')
        postal_code_output_label.grid(row=11, column=4, sticky='w')

        postal_code_output = ttk.Entry(self, bootstyle='default', width=15)
        postal_code_output.insert('end', postal_code_var)
        postal_code_output.configure(state=f'{readonly_state}')
        postal_code_output.grid(row=12, column=4, sticky='w')

        ## country_output

        country_output_label = ttk.Label(self, text='Państwo', font=('Open Sans', 12),
                                         bootstyle='default')
        country_output_label.grid(row=11, column=5, sticky='w')

        country_output = ttk.Entry(self, bootstyle='default', width=25)
        country_output.insert('end', country_var)
        country_output.configure(state=f'{readonly_state}')
        country_output.grid(row=12, column=5, sticky='w')

        ## email_output

        email_output_label = ttk.Label(self, text='Adres e-mail', font=('Open Sans', 12),
                                       bootstyle='default')
        email_output_label.grid(row=14, column=0, sticky='w')

        email_output = ttk.Entry(self, bootstyle='default', width=25)
        email_output.insert('end', email_var)
        email_output.configure(state=f'{readonly_state}')
        email_output.grid(row=15, column=0, sticky='w')

        ## phone_number_output

        phone_number_output_label = ttk.Label(self, text='Nr telefonu', font=('Open Sans', 12),
                                              bootstyle='default')
        phone_number_output_label.grid(row=14, column=2, sticky='w')

        phone_number_output = ttk.Entry(self, bootstyle='default', textvariable=phone_number_var,
                                        width=25)
        phone_number_output.insert('end', phone_number_var)
        phone_number_output.configure(state=f'{readonly_state}', )
        phone_number_output.grid(row=15, column=2, sticky='w')

        ## personal_id_output

        personal_id_output_label = ttk.Label(self, text='PESEL', font=('Open Sans', 12),
                                             bootstyle='default')
        personal_id_output_label.grid(row=14, column=3, sticky='w')

        personal_id_output = ttk.Entry(self, bootstyle='default', width=25)
        personal_id_output.insert('end', personal_id_var)
        personal_id_output.configure(state=f'{readonly_state}')
        personal_id_output.grid(row=15, column=3, sticky='w')

        ## document_no_output

        document_no_output_label = ttk.Label(self, text='Nr dokumentu', font=('Open Sans', 12),
                                             bootstyle='default')
        document_no_output_label.grid(row=14, column=4, sticky='w')

        document_no_output = ttk.Entry(self, bootstyle='default', width=25)
        document_no_output.insert('end', document_no_var)
        document_no_output.configure(state=f'{readonly_state}')
        document_no_output.grid(row=15, column=4, sticky='w')

        ## document_type_output

        document_type_output_label = ttk.Label(self, text='Rodzaj dokumentu', font=('Open Sans', 12),
                                               bootstyle='default')
        document_type_output_label.grid(row=14, column=5, sticky='w')

        document_type_output = ttk.Menubutton(self, bootstyle='dark', text=f'{document_type_var}')
        document_type_output.configure(state=f'{disabled_state}')
        document_type_output.grid(row=15, column=5, sticky='w')

        document_type_content = ttk.Menu(document_type_output)

        item_var = StringVar()
        for x in ['Dowód osobisty', 'Paszport', 'Karta pobytu']:
            document_type_content.add_radiobutton(label=x, variable=item_var,
                                                  command=lambda x=x: self.amend_menu_content(document_type_output, x))

        document_type_output['menu'] = document_type_content

        ## course_name_output

        course_name_output_label = ttk.Label(self, text='Nazwa kursu', font=('Open Sans', 12),
                                             bootstyle='default')
        course_name_output_label.grid(row=17, column=0, sticky='w')

        course_name_output = ttk.Menubutton(self, bootstyle='dark', text=f'{course_name_var}')
        course_name_output.configure(state=f'{disabled_state}')
        course_name_output.grid(row=18, column=0, sticky='w')

        course_name_output_content = ttk.Menu(course_name_output)

        course_var = StringVar()

        ## course_language_output

        course_language_output_label = ttk.Label(self, text='Język kursu', font=('Open Sans', 12),
                                                 bootstyle='default')
        course_language_output_label.grid(row=17, column=2, sticky='w')

        course_language_output = ttk.Menubutton(self, bootstyle='dark', text=f'{language_db}')
        course_language_output.configure(state=f'{disabled_state}')
        course_language_output.grid(row=18, column=2, sticky='w')

        course_language_output_content = ttk.Menu(course_language_output)

        language_var = StringVar()
        for x in ['Angielski', 'Niemiecki', 'Francuski', 'Włoski', 'Hiszpański']:
            course_language_output_content.add_radiobutton(label=x, variable=language_var,
                                                           command=lambda x=x: self.amend_menu_content(
                                                               course_language_output, x))

        course_language_output['menu'] = course_language_output_content

        ## status_output

        status_output_label = ttk.Label(self, text='Status', font=('Open Sans', 12), bootstyle='default')
        status_output_label.grid(row=17, column=3, sticky='w')

        status_output = ttk.Entry(self, bootstyle='default', state='readonly', width=25)
        status_output.insert('end', status_var)
        status_output.configure(state='readonly')
        status_output.grid(row=18, column=3, sticky='w')

        ## level_output

        level_output_label = ttk.Label(self, text='Poziom', font=('Open Sans', 12), bootstyle='default')
        level_output_label.grid(row=17, column=4, sticky='w')

        level_output = ttk.Menubutton(self, bootstyle='dark', text=f'{level_db}')
        level_output.configure(state=f'{disabled_state}')
        level_output.grid(row=18, column=4, sticky='w')

        level_output_content = ttk.Menu(level_output)

        level_var = StringVar()

        for x in ['Początkujący', 'Zaawansowany']:
            level_output_content.add_radiobutton(label=x, variable=level_var,
                                                 command=lambda x=x: self.amend_menu_content(level_output, x))

        level_output['menu'] = level_output_content

        ## mode_output POPRAWIĆ NA DROPDOWN

        mode_output_label = ttk.Label(self, text='Tryb', font=('Open Sans', 12), bootstyle='default')
        mode_output_label.grid(row=17, column=5, sticky='w')

        mode_output = ttk.Menubutton(self, bootstyle='dark', text=f'{mode_db}')
        mode_output.configure(state=f'{disabled_state}')
        mode_output.grid(row=18, column=5, sticky='w')

        mode_output_content = ttk.Menu(mode_output)

        mode_var = StringVar()

        for x in ['Normalny', 'Przyspieszony']:
            mode_output_content.add_radiobutton(label=x, variable=mode_var,
                                                command=lambda x=x: self.amend_menu_content(mode_output, x))

        mode_output['menu'] = mode_output_content

        ## start_date_output

        start_date_output_label = ttk.Label(self, text='Data rozpoczęcia', font=('Open Sans', 12),
                                            bootstyle='default')
        start_date_output_label.grid(row=20, column=2, sticky='w')

        start_date_output = ttk.DateEntry(self, bootstyle='primary')
        start_date_output.configure(state=f'{readonly_state}')
        start_date_output.grid(row=21, column=2, sticky='w')

        ## end_date_output

        end_date_output_label = ttk.Label(self, text='Data zakończenia', font=('Open Sans', 12),
                                          bootstyle='default')
        end_date_output_label.grid(row=20, column=4, sticky='w')

        end_date_output = ttk.DateEntry(self, bootstyle='primary')
        end_date_output.configure(state=f'{readonly_state}')
        end_date_output.grid(row=21, column=4, sticky='w')

        ## edit button
        """
        When clicked, the entries change status from readonly to editable. 
        """

        edit_button_style = ttk.Style()
        edit_button_style.configure('primary.TButton', font=('Open Sans', 15))

        edit_button = ttk.Button(self, bootstyle='primary', text='EDYTUJ', width=15,
                                 style='primary.TButton', state=f'{disabled_state_button}')
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