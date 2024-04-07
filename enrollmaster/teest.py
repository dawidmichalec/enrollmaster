from tkinter import *
import ttkbootstrap as ttk

def teacher_info_switch():
    edit_course_frame = ttk.Frame(main_frame)
    ## course_name

    course_name_label = ttk.Label(edit_course_frame, text='Nazwa kursu', font=('Open Sans', 12), bootstyle='default')
    course_name_label.grid(row=2, column=0, sticky='w')

    course_name_entry = ttk.Entry(edit_course_frame, bootstyle='light', width=30)
    course_name_entry.grid(row=3, column=0, sticky='w')

    ## course_language

    course_language_label = ttk.Label(edit_course_frame, text="Język kursu", font=('Open Sans', 12),
                                      bootstyle='default')
    course_language_label.grid(row=2, column=2, sticky='w')

    course_language_dropdown = ttk.Menubutton(edit_course_frame, bootstyle='dark', text="Wybierz język")
    course_language_dropdown.grid(row=3, column=2, sticky='w')

    course_language_dropdown_content = ttk.Menu(course_language_dropdown)

    course_language_var = StringVar()
    for x in ['Angielski', 'Niemiecki', 'Francuski', 'Włoski', 'Hiszpański']:
        course_language_dropdown_content.add_radiobutton(label=x, variable=course_language_var,
                                                         command=lambda x=x: amend_menu_content(
                                                             course_language_dropdown, x))

    course_language_dropdown['menu'] = course_language_dropdown_content

    ## course_level

    course_level_label = ttk.Label(edit_course_frame, text='Poziom', font=('Open Sans', 12), bootstyle='default')
    course_level_label.grid(row=2, column=3, sticky='w')

    course_level_dropdown = ttk.Menubutton(edit_course_frame, bootstyle='dark', text='Wybierz poziom')
    course_level_dropdown.grid(row=3, column=3, sticky='w')

    course_level_dropdown_content = ttk.Menu(course_level_dropdown)

    course_level_var = StringVar()

    for x in ['Początkujący', 'Zaawansowany']:
        course_level_dropdown_content.add_radiobutton(label=x, variable=course_level_var,
                                                      command=lambda x=x: amend_menu_content(course_level_dropdown, x))

    course_level_dropdown['menu'] = course_level_dropdown_content

    ## course_mode

    mode_label = ttk.Label(edit_course_frame, text="Tryb", font=('Open Sans', 12), bootstyle='default')
    mode_label.grid(row=2, column=4, sticky='w')

    mode_dropdown = ttk.Menubutton(edit_course_frame, bootstyle='dark', text="Wybierz poziom")
    mode_dropdown.grid(row=3, column=4, sticky='w')

    mode_dropdown_content = ttk.Menu(mode_dropdown)

    mode_var = StringVar()

    choice = ""

    for x in ['Normalny', 'Przyspieszony']:
        mode_dropdown_content.add_radiobutton(label=x, variable=mode_var,
                                              command=lambda x=x: amend_menu_content(mode_dropdown, x))

    mode_dropdown['menu'] = mode_dropdown_content

    ## start_date

    start_date_label = ttk.Label(edit_course_frame, text='Data rozpoczęcia', font=('Open Sans', 12),
                                 bootstyle='default')
    start_date_label.grid(row=5, column=0, sticky='w')

    start_date_entry = ttk.DateEntry(edit_course_frame, bootstyle='primary')
    start_date_entry.grid(row=6, column=0, sticky='w')

    ## end date

    end_date_label = ttk.Label(edit_course_frame, text='Data zakończenia', font=('Open Sans', 12),
                               bootstyle='default')
    end_date_label.grid(row=5, column=2, sticky='w')

    end_date_entry = ttk.DateEntry(edit_course_frame, bootstyle='primary')
    end_date_entry.configure(state="readonly")
    end_date_entry.grid(row=6, column=2, sticky='w')

    ## teacher_selection

    teacher_selection_label = ttk.Label(edit_course_frame, text='Nauczyciel', font=('Open Sans', 12),
                                        bootstyle='default')
    teacher_selection_label.grid(row=5, column=3, sticky='w')

    teacher_selection_dropdown = ttk.Menubutton(edit_course_frame, text='Wybierz nauczyciela', bootstyle='dark')
    teacher_selection_dropdown.grid(row=6, column=3, sticky='w')

    ## prize

    prize_label = ttk.Label(edit_course_frame, text="Cena", font=('Open Sans', 12), bootstyle='default')
    prize_label.grid(row=5, column=4, sticky='w')

    prize_entry = ttk.Entry(edit_course_frame, bootstyle='light', width=15)
    prize_entry.grid(row=6, column=4, sticky='w')

