from tkinter import *
import ttkbootstrap as ttk

class EditCourseFrame(ttk.Frame):

    def __init__(self, master=None, amend_menu_content_func=None, **kw):
        super().__init__(master, **kw)
        self.amend_menu_content_func = amend_menu_content_func
        self.columnconfigure((0, 1, 2, 3, 4), weight=1, minsize=250)
        self.rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28),
            weight=1, minsize=30)

        ## Variables

        readonly_state = "readonly"
        disabled_state = "disabled"
        disabled_state_button = "disabled"

        course_id_var = ''
        course_name_var = ''
        language_db = ''
        level_db = ''
        mode_db = ''
        teacher_name = ''
        prize_var = ''

        ## edit_course_label

        edit_course_label = ttk.Label(self, text='EDYTUJ KURS', font=('Open Sans', 14, 'bold'),
                                      bootstyle='default')
        edit_course_label.grid(row=0, column=2, sticky='w')

        ## course_id search

        course_id_search_label = ttk.Label(self, text='ID kursu', font=('Open Sans', 12),
                                           bootstyle='default')
        course_id_search_label.grid(row=2, column=1, sticky='w')

        course_id_search_entry = ttk.Entry(self, bootstyle='light', width=20)
        course_id_search_entry.grid(row=3, column=1, sticky='w')

        ## course_name_search

        course_name_search_label = ttk.Label(self, text='Nazwa kursu', font=('Open Sans', 12),
                                             bootstyle='default')
        course_name_search_label.grid(row=2, column=2, sticky='w')

        course_name_search_entry = ttk.Entry(self, bootstyle='light', width=20)
        course_name_search_entry.grid(row=3, column=2, sticky='w')

        submit_button_style = ttk.Style()
        submit_button_style.configure('success.TButton', font=('Open Sans', 16))

        submit_button = ttk.Button(self, bootstyle='success', text='SZUKAJ', width=15,
                                   style='success.TButton')
        submit_button.grid(row=5, column=2, sticky='w')

        ## course_id

        course_id_label = ttk.Label(self, text='ID Kursu', font=('Open Sans', 12), bootstyle='default')
        course_id_label.grid(row=8, column=0, sticky='w')

        course_id_entry = ttk.Entry(self, bootstyle='default', width=20)
        course_id_entry.insert('end', course_id_var)
        course_id_entry.configure(state='readonly')
        course_id_entry.grid(row=9, column=0, sticky='w')

        ## course_name

        course_name_label = ttk.Label(self, text='Nazwa kursu', font=('Open Sans', 12),
                                      bootstyle='default')
        course_name_label.grid(row=8, column=1, sticky='w')

        course_name_entry = ttk.Entry(self, bootstyle='default', width=20)
        course_name_entry.insert('end', course_name_var)
        course_name_entry.configure(state='readonly')
        course_name_entry.grid(row=9, column=1, sticky='w')

        ## course_language

        course_language_label = ttk.Label(self, text="Język kursu", font=('Open Sans', 12),
                                          bootstyle='default')
        course_language_label.grid(row=8, column=2, sticky='w')

        course_language_dropdown = ttk.Menubutton(self, bootstyle='dark', text=f"{language_db}")
        course_language_dropdown.configure(state=f'{disabled_state}')
        course_language_dropdown.grid(row=9, column=2, sticky='w')

        course_language_dropdown_content = ttk.Menu(course_language_dropdown)

        course_language_var = StringVar()
        for x in ['Angielski', 'Niemiecki', 'Francuski', 'Włoski', 'Hiszpański']:
            course_language_dropdown_content.add_radiobutton(label=x, variable=course_language_var,
                                                             command=lambda x=x: self.amend_menu_content_func(
                                                                 course_language_dropdown, x))

        course_language_dropdown['menu'] = course_language_dropdown_content

        ## course_level

        course_level_label = ttk.Label(self, text='Poziom', font=('Open Sans', 12), bootstyle='default')
        course_level_label.grid(row=8, column=3, sticky='w')

        course_level_dropdown = ttk.Menubutton(self, bootstyle='dark', text=f'{level_db}')
        course_level_dropdown.configure(state=f'{disabled_state}')
        course_level_dropdown.grid(row=9, column=3, sticky='w')

        course_level_dropdown_content = ttk.Menu(course_level_dropdown)

        course_level_var = StringVar()

        for x in ['Początkujący', 'Zaawansowany']:
            course_level_dropdown_content.add_radiobutton(label=x, variable=course_level_var,
                                                          command=lambda x=x: self.amend_menu_content_func(course_level_dropdown,
                                                                                                 x))

        course_level_dropdown['menu'] = course_level_dropdown_content

        ## course_mode

        mode_label = ttk.Label(self, text=f"Tryb", font=('Open Sans', 12), bootstyle='default')
        mode_label.grid(row=8, column=4, sticky='w')

        mode_dropdown = ttk.Menubutton(self, bootstyle='dark', text=f"{mode_db}")
        mode_dropdown.configure(state=f'{disabled_state}')
        mode_dropdown.grid(row=9, column=4, sticky='w')

        mode_dropdown_content = ttk.Menu(mode_dropdown)

        mode_var = StringVar()

        choice = ""

        for x in ['Normalny', 'Przyspieszony']:
            mode_dropdown_content.add_radiobutton(label=x, variable=mode_var,
                                                  command=lambda x=x: self.amend_menu_content_func(mode_dropdown, x))

        mode_dropdown['menu'] = mode_dropdown_content

        ## start_date

        start_date_label = ttk.Label(self, text='Data rozpoczęcia', font=('Open Sans', 12),
                                     bootstyle='default')
        start_date_label.grid(row=11, column=0, sticky='w')

        start_date_entry = ttk.DateEntry(self, bootstyle='primary')
        start_date_entry.configure(state=f'{readonly_state}')
        start_date_entry.grid(row=12, column=0, sticky='w')

        ## end date

        end_date_label = ttk.Label(self, text='Data zakończenia', font=('Open Sans', 12),
                                   bootstyle='default')
        end_date_label.grid(row=11, column=1, sticky='w')

        end_date_entry = ttk.DateEntry(self, bootstyle='primary')
        end_date_entry.configure(state=f'{readonly_state}')
        end_date_entry.grid(row=12, column=1, sticky='w')

        ## teacher_selection

        teacher_selection_label = ttk.Label(self, text='Nauczyciel', font=('Open Sans', 12),
                                            bootstyle='default')
        teacher_selection_label.grid(row=11, column=2, sticky='w')

        teacher_selection_dropdown = ttk.Menubutton(self, text=f'{teacher_name}', bootstyle='dark')
        teacher_selection_dropdown.configure(state=f'{disabled_state}')
        teacher_selection_dropdown.grid(row=12, column=2, sticky='w')

        ## prize

        prize_label = ttk.Label(self, text="Cena", font=('Open Sans', 12), bootstyle='default')
        prize_label.grid(row=11, column=3, sticky='w')

        prize_entry = ttk.Entry(self, bootstyle='default', width=15)
        prize_entry.insert('end', prize_var)
        prize_entry.configure(state=f'{readonly_state}')
        prize_entry.grid(row=12, column=3, sticky='w')

        ## edit button
        """
        When clicked, the entries change status from readonly to editable. 
        """

        edit_button_style = ttk.Style()
        edit_button_style.configure('primary.TButton', font=('Open Sans', 15))

        edit_button = ttk.Button(self, bootstyle='primary', text='EDYTUJ', width=15,
                                 style='primary.TButton',
                                 state=f'{disabled_state_button}')
        edit_button.grid(row=16, column=1, sticky='w')

        ## save_button

        save_button = ttk.Button(self, bootstyle='info', text='ZAPISZ', width=16,
                                 state=f'{disabled_state_button}')
        save_button.grid(row=16, column=2, sticky='w')

        ## cancel_button - sets entries back to the readonly state and buttons do disabled state, including itself

        cancel_button_style = ttk.Style()
        cancel_button_style.configure('danger.TButton', font=('Open Sans', 15))

        cancel_button = ttk.Button(self, bootstyle='danger', text='ODRZUĆ', width=15,
                                   state=f'{disabled_state_button}')
        cancel_button.grid(row=16, column=3, sticky='w')

        self.pack()