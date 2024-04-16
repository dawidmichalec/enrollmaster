from tkinter import *
import ttkbootstrap as ttk

def create_course_switch():
    delete_pages()
    create_course_frame = ttk.Frame(main_frame)

    create_course_frame.columnconfigure((0, 2, 3, 4, 5), weight=1, minsize=250)
    create_course_frame.columnconfigure(1, weight=1, minsize=50)
    create_course_frame.rowconfigure(
        (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28),
        weight=1, minsize=30)


    create_course_label = ttk.Label(create_course_frame, text='STWÓRZ KURS', font=('Open Sans', 14, 'bold'), bootstyle='default')
    create_course_label.grid(row=0, column=3, sticky='w')

    ## course_language

    language_label = ttk.Label(create_course_frame, text="Język kursu", font=('Open Sans', 12), bootstyle='default')
    language_label.grid(row=2, column=0, sticky='w')

    def on_language_select():
        selected_language = language_var.get()
        print("Selected language:", selected_language)
        amend_menu_content(language_dropdown, selected_language)
        return selected_language

    language_dropdown = ttk.Menubutton(create_course_frame, bootstyle='dark', text="Wybierz język")
    language_dropdown.grid(row=3, column=0, sticky='w')

    language_dropdown_content = ttk.Menu(language_dropdown)

    language_var = ttk.StringVar()
    language_var.set("Angielski")  # Set default payment method

    for language in ['Angielski', 'Niemiecki', 'Francuski', 'Włoski', 'Hiszpański']:
        language_dropdown_content.add_radiobutton(label=language, variable=language_var, value=language,
                                                  command=on_language_select)

    language_dropdown['menu'] = language_dropdown_content

    ## course_level

    course_level_label = ttk.Label(create_course_frame, text='Poziom', font=('Open Sans', 12), bootstyle='default')
    course_level_label.grid(row=2, column=2, sticky='w')

    def on_level_select():
        selected_level = level_var.get()
        print("Selected level:", selected_level)
        amend_menu_content(level_dropdown, selected_level)
        return selected_level

    level_dropdown = ttk.Menubutton(create_course_frame, bootstyle='dark', text='Wybierz poziom')
    level_dropdown.grid(row=3, column=2, sticky='w')

    level_dropdown_content = ttk.Menu(level_dropdown)

    level_var = StringVar()
    level_var.set("Początkujący")  # Set default payment method

    for level in ['Początkujący', 'Zaawansowany']:
        level_dropdown_content.add_radiobutton(label=level, variable=level_var, value=level,
                                               command=on_level_select)

    level_dropdown['menu'] = level_dropdown_content

    ## course_mode

    mode_label = ttk.Label(create_course_frame, text="Tryb", font=('Open Sans', 12), bootstyle='default')
    mode_label.grid(row=2, column=3, sticky='w')

    def on_mode_select():
        selected_mode = mode_var.get()
        print("Selected mode:", selected_mode)
        amend_menu_content(mode_dropdown, selected_mode)
        return selected_mode

    mode_dropdown = ttk.Menubutton(create_course_frame, bootstyle='dark', text="Wybierz tryb")
    mode_dropdown.grid(row=3, column=3, sticky='w')

    mode_dropdown_content = ttk.Menu(mode_dropdown)

    mode_var = StringVar()
    mode_var.set("Normalny")  # Set default mode

    for mode in ['Normalny', 'Przyspieszony']:
        mode_dropdown_content.add_radiobutton(label=mode, variable=mode_var, value=mode,
                                              command=on_mode_select)

    mode_dropdown['menu'] = mode_dropdown_content

    ## start_date

    start_date_label = ttk.Label(create_course_frame, text='Data rozpoczęcia', font=('Open Sans', 12), bootstyle='default')
    start_date_label.grid(row=2, column=4, sticky='w')

    start_date_entry = ttk.DateEntry(create_course_frame, bootstyle='primary')
    start_date_entry.grid(row=3, column=4, sticky='w')

    ## end date

    end_date_label = ttk.Label(create_course_frame, text='Data zakończenia', font=('Open Sans', 12), bootstyle='default')
    end_date_label.grid(row=5, column=0, sticky='w')

    end_date_entry = ttk.DateEntry(create_course_frame, bootstyle='primary')
    end_date_entry.configure(state="readonly")
    end_date_entry.grid(row=6, column=0, sticky='w')

    ## teacher_selection

    teacher_selection_label = ttk.Label(create_course_frame, text='Nauczyciel', font=('Open Sans', 12), bootstyle='default')
    teacher_selection_label.grid(row=5, column=2, sticky='w')

    teacher_selection_dropdown = ttk.Menubutton(create_course_frame, text='Wybierz nauczyciela', bootstyle='dark')
    teacher_selection_dropdown.grid(row=6, column=2, sticky='w')

    ## prize

    prize_label = ttk.Label(create_course_frame, text="Cena", font=('Open Sans', 12), bootstyle='default')
    prize_label.grid(row=5, column=3, sticky='w')

    prize_entry = ttk.Entry(create_course_frame, bootstyle='light', width=15)
    prize_entry.grid(row=6, column=3, sticky='w')

    ## course_name

    course_name_label = ttk.Label(create_course_frame, text='Nazwa kursu', font=('Open Sans', 12), bootstyle='default')
    course_name_label.grid(row=5, column=4, sticky='w')

    course_name_var = ''

    course_name_entry = ttk.Entry(create_course_frame, bootstyle='light', width=30)
    course_name_entry.insert('end', course_name_var)
    course_name_entry.configure(state='readonly')
    course_name_entry.grid(row=6, column=4, sticky='w')


    submit_button_style = ttk.Style()
    submit_button_style.configure('success.TButton', font=('Open Sans', 16))

    submit_button = ttk.Button(create_course_frame, bootstyle='success', text='ZAPISZ', width=20, style='success.TButton')
    submit_button.grid(row=9, column=3, sticky='w')

    create_course_frame.pack()