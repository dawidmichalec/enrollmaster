from tkinter import *
import ttkbootstrap as ttk


class CourseInfoFrame(ttk.Frame):

    def __init__(self, master=None, amend_menu_content_func=None, **kw):
        super().__init__(master, **kw)
        self.amend_menu_content_func = amend_menu_content_func
        self.columnconfigure((0, 1, 2, 3, 4), weight=1, minsize=250)
        self.rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28),
            weight=1, minsize=30)

        course_info_label = ttk.Label(self, text='WYSZUKAJ KURS', font=('Open Sans', 14, 'bold'),
                                      bootstyle='default')
        course_info_label.grid(row=0, column=2, sticky='w')

        ## course_id

        course_id_label = ttk.Label(self, text='ID Kursu', font=('Open Sans', 12), bootstyle='default')
        course_id_label.grid(row=2, column=0, sticky='w')

        course_id = ttk.Entry(self, bootstyle='light', width=15)
        course_id.grid(row=3, column=0, sticky='w')

        ## name

        course_name_label = ttk.Label(self, text='Nazwa kursu', font=('Open Sans', 12),
                                      bootstyle='default')
        course_name_label.grid(row=2, column=1, sticky='w')

        course_name = ttk.Entry(self, bootstyle='light', width=20)
        course_name.grid(row=3, column=1, sticky='w')

        ## language

        language_label = ttk.Label(self, text="Język kursu", font=('Open Sans', 12),
                                          bootstyle='default')
        language_label.grid(row=2, column=2, sticky='w')

        self.language_dropdown = ttk.Menubutton(self, bootstyle='dark', text="Wybierz język")
        self.language_dropdown.grid(row=3, column=2, sticky='w')

        language_dropdown_content = ttk.Menu(self.language_dropdown)

        self.language_var = StringVar()
        self.language_var.set('Angielski')

        for x in ['Angielski', 'Niemiecki', 'Francuski', 'Włoski', 'Hiszpański']:
            language_dropdown_content.add_radiobutton(label=x, variable=self.language_var,
                                                             command=self.on_language_select)

        self.language_dropdown['menu'] = language_dropdown_content

        ## level

        course_level_label = ttk.Label(self, text='Poziom', font=('Open Sans', 12), bootstyle='default')
        course_level_label.grid(row=2, column=3, sticky='w')

        self.level_dropdown = ttk.Menubutton(self, bootstyle='dark', text='Wybierz poziom')
        self.level_dropdown.grid(row=3, column=3, sticky='w')

        level_dropdown_content = ttk.Menu(self.level_dropdown)

        self.level_var = StringVar()
        self.level_var.set('Początkujący')

        for x in ['Początkujący', 'Zaawansowany']:
            level_dropdown_content.add_radiobutton(label=x, variable=self.level_var,
                                                          command=self.on_level_select)

        self.level_dropdown['menu'] = level_dropdown_content

        ## mode

        mode_label = ttk.Label(self, text="Tryb", font=('Open Sans', 12), bootstyle='default')
        mode_label.grid(row=2, column=4, sticky='w')

        self.mode_dropdown = ttk.Menubutton(self, bootstyle='dark', text="Wybierz poziom")
        self.mode_dropdown.grid(row=3, column=4, sticky='w')

        mode_dropdown_content = ttk.Menu(self.mode_dropdown)

        self.mode_var = StringVar()
        self.mode_var.set('Normalny')

        for x in ['Normalny', 'Przyspieszony']:
            mode_dropdown_content.add_radiobutton(label=x, variable=self.mode_var,
                                                  command=self.on_mode_select)

        self.mode_dropdown['menu'] = mode_dropdown_content

        ## teacher_first_name

        teacher_first_name_label = ttk.Label(self, text='Imię nauczyciela', font=('Open Sans', 12),
                                             bootstyle='default')
        teacher_first_name_label.grid(row=5, column=0, sticky='w')

        teacher_first_name = ttk.Entry(self, bootstyle='light', width=20)
        teacher_first_name.grid(row=6, column=0, sticky='w')

        ## teacher_last_name

        teacher_last_name_label = ttk.Label(self, text='Nazwisko nauczyciela', font=('Open Sans', 12),
                                            bootstyle='default')
        teacher_last_name_label.grid(row=5, column=1, sticky='w')

        teacher_last_name = ttk.Entry(self, bootstyle='light', width=20)
        teacher_last_name.grid(row=6, column=1, sticky='w')

        # start_date

        start_date_var = StringVar()
        start_date_var.set("")

        start_date_label = ttk.Label(self, text='Data rozpoczęcia od', font=('Open Sans', 12),
                                     bootstyle='default')
        start_date_label.grid(row=5, column=2, sticky='w')

        start_date_entry = ttk.DateEntry(self, bootstyle='primary')
        start_date_entry.grid(row=6, column=2, sticky='w')
        start_date_entry.entry.configure(textvariable=start_date_var)

        # end date

        end_date_var = StringVar()
        end_date_var.set("")

        end_date_label = ttk.Label(self, text='Data rozpoczęcia do', font=('Open Sans', 12),
                                   bootstyle='default')
        end_date_label.grid(row=5, column=3, sticky='w')

        end_date_entry = ttk.DateEntry(self, bootstyle='primary')
        end_date_entry.grid(row=6, column=3, sticky='w')
        end_date_entry.entry.configure(textvariable=end_date_var)

        # submit

        submit_button_style = ttk.Style()
        submit_button_style.configure('success.TButton', font=('Open Sans', 14))

        submit_button = ttk.Button(self, bootstyle='success', text='SZUKAJ', width=15,
                                   style='success.TButton')
        submit_button.grid(row=9, column=2, sticky='w')

        output_label = ttk.Label(self, text="asdf", font=('Open Sans', 12), bootstyle='default')
        output_label.grid(row=12, column=2, sticky='nswe')

        self.pack()

    def on_language_select(self):
        selected_language = self.language_var.get()
        print("Selected language:", selected_language)
        self.amend_menu_content_func(self.language_dropdown, selected_language)
        return selected_language

    def on_level_select(self):
        selected_level = self.level_var.get()
        print("Selected level:", selected_level)
        self.amend_menu_content_func(self.level_dropdown, selected_level)
        return selected_level

    def on_mode_select(self):
        selected_mode = self.mode_var.get()
        print("Selected mode:", selected_mode)
        self.amend_menu_content_func(self.mode_dropdown, selected_mode)
        return selected_mode