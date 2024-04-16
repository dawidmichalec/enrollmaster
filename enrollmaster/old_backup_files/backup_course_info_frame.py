from tkinter import *
import ttkbootstrap as ttk

course_info_frame = ttk.Frame(main_frame)
course_info_frame.columnconfigure((0, 1, 2, 3, 4), weight=1, minsize=250)
course_info_frame.rowconfigure(
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28),
    weight=1, minsize=30)

course_info_label = ttk.Label(course_info_frame, text='INFORMACJE O KURSACH', font=('Open Sans', 14, 'bold'), bootstyle='default')
course_info_label.grid(row=0, column=2, sticky='w')

## course_id

course_id_label = ttk.Label(course_info_frame, text='ID Kursu', font=('Open Sans', 12), bootstyle='default')
course_id_label.grid(row=2, column=0, sticky='w')

course_id = ttk.Entry(course_info_frame, bootstyle='light', width=15)
course_id.grid(row=3, column=0, sticky='w')

## name

course_name_label = ttk.Label(course_info_frame, text='Nazwa kursu', font=('Open Sans', 12), bootstyle='default')
course_name_label.grid(row=2, column=1, sticky='w')

course_name = ttk.Entry(course_info_frame, bootstyle='light', width=20)
course_name.grid(row=3, column=1, sticky='w')

## language

course_language_label = ttk.Label(course_info_frame, text="Język kursu", font=('Open Sans', 12),
                                  bootstyle='default')
course_language_label.grid(row=2, column=2, sticky='w')

course_language_dropdown = ttk.Menubutton(course_info_frame, bootstyle='dark', text="Wybierz język")
course_language_dropdown.grid(row=3, column=2, sticky='w')

course_language_dropdown_content = ttk.Menu(course_language_dropdown)

course_language_var = StringVar()
for x in ['Angielski', 'Niemiecki', 'Francuski', 'Włoski', 'Hiszpański']:
    course_language_dropdown_content.add_radiobutton(label=x, variable=course_language_var,
                                                     command=lambda x=x: amend_menu_content(
                                                         course_language_dropdown, x))

course_language_dropdown['menu'] = course_language_dropdown_content

## level

course_level_label = ttk.Label(course_info_frame, text='Poziom', font=('Open Sans', 12), bootstyle='default')
course_level_label.grid(row=2, column=3, sticky='w')

course_level_dropdown = ttk.Menubutton(course_info_frame, bootstyle='dark', text='Wybierz poziom')
course_level_dropdown.grid(row=3, column=3, sticky='w')

course_level_dropdown_content = ttk.Menu(course_level_dropdown)

course_level_var = StringVar()

for x in ['Początkujący', 'Zaawansowany']:
    course_level_dropdown_content.add_radiobutton(label=x, variable=course_level_var,
                                                  command=lambda x=x: amend_menu_content(course_level_dropdown, x))

course_level_dropdown['menu'] = course_level_dropdown_content

## mode

mode_label = ttk.Label(course_info_frame, text="Tryb", font=('Open Sans', 12), bootstyle='default')
mode_label.grid(row=2, column=4, sticky='w')

mode_dropdown = ttk.Menubutton(course_info_frame, bootstyle='dark', text="Wybierz poziom")
mode_dropdown.grid(row=3, column=4, sticky='w')

mode_dropdown_content = ttk.Menu(mode_dropdown)

mode_var = StringVar()

choice = ""

for x in ['Normalny', 'Przyspieszony']:
    mode_dropdown_content.add_radiobutton(label=x, variable=mode_var,
                                          command=lambda x=x: amend_menu_content(mode_dropdown, x))

mode_dropdown['menu'] = mode_dropdown_content

## teacher_first_name

teacher_first_name_label = ttk.Label(course_info_frame, text='Imię nauczyciela', font=('Open Sans', 12), bootstyle='default')
teacher_first_name_label.grid(row=5, column=0, sticky='w')

teacher_first_name = ttk.Entry(course_info_frame, bootstyle='light', width=20)
teacher_first_name.grid(row=6, column=0, sticky='w')

## teacher_last_name

teacher_last_name_label = ttk.Label(course_info_frame, text='Nazwisko nauczyciela', font=('Open Sans', 12),
                                     bootstyle='default')
teacher_last_name_label.grid(row=5, column=1, sticky='w')

teacher_last_name = ttk.Entry(course_info_frame, bootstyle='light', width=20)
teacher_last_name.grid(row=6, column=1, sticky='w')

## start_date

start_date_label = ttk.Label(course_info_frame, text='Data rozpoczęcia od', font=('Open Sans', 12),
                             bootstyle='default')
start_date_label.grid(row=5, column=2, sticky='w')

start_date_entry = ttk.DateEntry(course_info_frame, bootstyle='primary')
start_date_entry.grid(row=6, column=2, sticky='w')

## end date

end_date_label = ttk.Label(course_info_frame, text='Data rozpoczęcia do', font=('Open Sans', 12),
                           bootstyle='default')
end_date_label.grid(row=5, column=3, sticky='w')

end_date_entry = ttk.DateEntry(course_info_frame, bootstyle='primary')
end_date_entry.grid(row=6, column=3, sticky='w')

## submit

submit_button_style = ttk.Style()
submit_button_style.configure('success.TButton', font=('Open Sans', 16))

submit_button = ttk.Button(course_info_frame, bootstyle='success', text='SZUKAJ', width=20,
                           style='success.TButton')
submit_button.grid(row=9, column=2, sticky='w')


output_label = ttk.Label(course_info_frame, text="asdf", font=('Open Sans', 12), bootstyle='default')
output_label.grid(row=12, column=2, sticky='nswe')

course_info_frame.pack()
