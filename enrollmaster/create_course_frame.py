from tkinter import *
import ttkbootstrap as ttk


class CreateCourseFrame(ttk.Frame):
    
    def __init__(self, master=None, amend_menu_content_func=None, **kw):
        super().__init__(master, **kw)
        self.amend_menu_content_func = amend_menu_content_func

        self.columnconfigure((0, 2, 3, 4, 5), weight=1, minsize=250)
        self.columnconfigure(1, weight=1, minsize=50)
        self.rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28),
            weight=1, minsize=30)

        create_course_label = ttk.Label(self, text='STWÓRZ KURS', font=('Open Sans', 14, 'bold'),
                                        bootstyle='default')
        create_course_label.grid(row=0, column=3, sticky='w')

        ## course_language

        language_label = ttk.Label(self, text="Język kursu", font=('Open Sans', 12), bootstyle='default')
        language_label.grid(row=2, column=0, sticky='w')

        self.language_dropdown = ttk.Menubutton(self, bootstyle='dark', text="Wybierz język")
        self.language_dropdown.grid(row=3, column=0, sticky='w')

        language_dropdown_content = ttk.Menu(self.language_dropdown)

        self.language_var = ttk.StringVar()
        self.language_var.set("Angielski")  # Set default payment method

        for language in ['Angielski', 'Niemiecki', 'Francuski', 'Włoski', 'Hiszpański']:
            language_dropdown_content.add_radiobutton(label=language, variable=self.language_var, value=language,
                                                      command=self.on_language_select)

        self.language_dropdown['menu'] = language_dropdown_content

        ## course_level

        level_label = ttk.Label(self, text='Poziom', font=('Open Sans', 12), bootstyle='default')
        level_label.grid(row=2, column=2, sticky='w')

        self.level_dropdown = ttk.Menubutton(self, bootstyle='dark', text='Wybierz poziom')
        self.level_dropdown.grid(row=3, column=2, sticky='w')

        level_dropdown_content = ttk.Menu(self.level_dropdown)

        self.level_var = StringVar()
        self.level_var.set("Początkujący")  # Set default payment method

        for level in ['Początkujący', 'Zaawansowany']:
            level_dropdown_content.add_radiobutton(label=level, variable=self.level_var, value=level,
                                                   command=self.on_level_select)

        self.level_dropdown['menu'] = level_dropdown_content

        ## course_mode

        mode_label = ttk.Label(self, text="Tryb", font=('Open Sans', 12), bootstyle='default')
        mode_label.grid(row=2, column=3, sticky='w')

        self.mode_dropdown = ttk.Menubutton(self, bootstyle='dark', text="Wybierz tryb")
        self.mode_dropdown.grid(row=3, column=3, sticky='w')

        mode_dropdown_content = ttk.Menu(self.mode_dropdown)

        self.mode_var = StringVar()
        self.mode_var.set("Normalny")  # Set default mode

        for mode in ['Normalny', 'Przyspieszony']:
            mode_dropdown_content.add_radiobutton(label=mode, variable=self.mode_var, value=mode,
                                                  command=self.on_mode_select)

        self.mode_dropdown['menu'] = mode_dropdown_content

        ## start_date

        start_date_label = ttk.Label(self, text='Data rozpoczęcia', font=('Open Sans', 12),
                                     bootstyle='default')
        start_date_label.grid(row=2, column=4, sticky='w')

        start_date_entry = ttk.DateEntry(self, bootstyle='primary')
        start_date_entry.grid(row=3, column=4, sticky='w')

        ## end date

        end_date_label = ttk.Label(self, text='Data zakończenia', font=('Open Sans', 12),
                                   bootstyle='default')
        end_date_label.grid(row=5, column=0, sticky='w')

        end_date_entry = ttk.DateEntry(self, bootstyle='primary')
        end_date_entry.configure(state="readonly")
        end_date_entry.grid(row=6, column=0, sticky='w')

        ## teacher_selection

        teacher_selection_label = ttk.Label(self, text='Nauczyciel', font=('Open Sans', 12),
                                            bootstyle='default')
        teacher_selection_label.grid(row=5, column=2, sticky='w')

        teacher_selection_dropdown = ttk.Menubutton(self, text='Wybierz nauczyciela', bootstyle='dark')
        teacher_selection_dropdown.grid(row=6, column=2, sticky='w')

        ## prize

        prize_label = ttk.Label(self, text="Cena", font=('Open Sans', 12), bootstyle='default')
        prize_label.grid(row=5, column=3, sticky='w')

        prize_entry = ttk.Entry(self, bootstyle='light', width=15)
        prize_entry.grid(row=6, column=3, sticky='w')

        ## course_name

        course_name_label = ttk.Label(self, text='Nazwa kursu', font=('Open Sans', 12),
                                      bootstyle='default')
        course_name_label.grid(row=5, column=4, sticky='w')

        course_name_var = ''

        course_name_entry = ttk.Entry(self, bootstyle='light', width=30)
        course_name_entry.insert('end', course_name_var)
        course_name_entry.configure(state='readonly')
        course_name_entry.grid(row=6, column=4, sticky='w')

        submit_button_style = ttk.Style()
        submit_button_style.configure('success.TButton', font=('Open Sans', 16))

        submit_button = ttk.Button(self, bootstyle='success', text='ZAPISZ', width=20,
                                   style='success.TButton')
        submit_button.grid(row=9, column=3, sticky='w')

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