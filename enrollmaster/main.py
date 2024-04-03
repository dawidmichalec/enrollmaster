from tkinter import *
import ttkbootstrap as ttk

root = ttk.Window(themename='solar')
root.title('Enroll Master')
root.geometry('1920x1080')

logo = ttk.Label(text='Enroll Master', font=('Gotham', 48, 'bold'), bootstyle='default')
logo.place(x=10, y=30)

"""
Button styles.
"""

button_style = ttk.Style()
button_style.configure('light.Outline.TButton', font=('Open Sans', 14))
sub_button_style = ttk.Style()
sub_button_style.configure('info.TButton', font=('Open Sans', 14))

"""
Function that switches to new student creation frame. It also contains all the information about the design of this frame.
"""

def new_student_switch():
    delete_pages()
    new_student_frame = ttk.Frame(main_frame)
    new_student_frame.columnconfigure((0, 2, 3, 4, 5), weight=1, minsize=250)
    new_student_frame.columnconfigure(1, weight=1, minsize=50)
    new_student_frame.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28), weight=1, minsize=30)

    new_student_label = ttk.Label(new_student_frame, text="NOWY UCZEŃ", font=('Open Sans', 14, 'bold'), bootstyle='default')
    new_student_label.grid(column=3, row=0, sticky='w')

    ## first_name

    first_name_label = ttk.Label(new_student_frame, text="Imię", font=('Open Sans', 12), bootstyle='default')
    first_name_label.grid(row=2, column=0, sticky='w')

    first_name = ttk.Entry(new_student_frame, width=30, bootstyle='light')
    first_name.grid(row=3, column=0)

    ## last_name

    last_name_label = ttk.Label(new_student_frame, text="Nazwisko", font=('Open Sans', 12), bootstyle='default')
    last_name_label.grid(row=2, column=2, sticky='w')

    last_name= ttk.Entry(new_student_frame, width=30, bootstyle='light')
    last_name.grid(row=3, column=2)

    ## street

    street_label = ttk.Label(new_student_frame, text='Ulica', font=('Open Sans', 12), bootstyle='default')
    street_label.grid(row=5, column=0, sticky='w')

    street = ttk.Entry(new_student_frame, width=30, bootstyle='light')
    street.grid(row=6, column=0)

    ## building_no

    building_no_label = ttk.Label(new_student_frame, text='Nr domu', font=('Open Sans', 12), bootstyle='default')
    building_no_label.grid(row=5, column=2, sticky='w')

    building_no= ttk.Entry(new_student_frame, width=10, bootstyle='light')
    building_no.grid(row=6, column=2, sticky='w')

    ## local_no

    local_no_label = ttk.Label(new_student_frame, text='Nr lokalu', font=('Open Sans', 12), bootstyle='default')
    local_no_label.grid(row=5, column=3, sticky='w')

    local_no = ttk.Entry(new_student_frame, width=10, bootstyle='light')
    local_no.grid(row=6, column=3, sticky='w')

    ## city

    city_label = ttk.Label(new_student_frame, text="Miasto", font=('Open Sans', 12), bootstyle='default')
    city_label.grid(row=8, column=0, sticky='w')

    city = ttk.Entry(new_student_frame, width=30, bootstyle='light')
    city.grid(row=9, column=0, sticky='w')

    ## postal_code

    postal_code_label = ttk.Label(new_student_frame, text="Kod pocztowy", font=('Open Sans', 12), bootstyle='default')
    postal_code_label.grid(row=8, column=2, sticky='w')

    postal_code = ttk.Entry(new_student_frame, width=15, bootstyle='light')
    postal_code.grid(row=9, column=2, sticky='w')

    ## country

    country_label = ttk.Label(new_student_frame, text="Państwo", font=('Open Sans', 12), bootstyle='default')
    country_label.grid(row=8, column=3, sticky='w')

    country= ttk.Entry(new_student_frame, width=30, bootstyle='light')
    country.grid(row=9, column=3, sticky='w')

    ## email

    email_label = ttk.Label(new_student_frame, text="Adres e-mail", font=('Open Sans', 12), bootstyle='default')
    email_label.grid(row=11, column=0, sticky='w')

    email = ttk.Entry(new_student_frame, width=30, bootstyle='light')
    email.grid(row=12, column=0, sticky='w')

    ## phone number

    phone_number_label = ttk.Label(new_student_frame, text="Nr telefonu", font=('Open Sans', 12), bootstyle='default')
    phone_number_label.grid(row=11, column=2, sticky='w')

    phone_number = ttk.Entry(new_student_frame, width=20, bootstyle='light')
    phone_number.grid(row=12, column=2, sticky='w')

    ## personal id

    personal_id_label = ttk.Label(new_student_frame, text="PESEL", font=('Open Sans', 12), bootstyle='default')
    personal_id_label.grid(row=14, column=0, sticky='w')

    personal_id = ttk.Entry(new_student_frame, width=20, bootstyle='light')
    personal_id.grid(row=15, column=0, sticky='w')

    ## document_no

    document_no_label = ttk.Label(new_student_frame, text="Nr dokumentu", font=('Open Sans', 12), bootstyle='default')
    document_no_label.grid(row=14, column=2, sticky='w')

    document_no = ttk.Entry(new_student_frame, width=20, bootstyle='light')
    document_no.grid(row=15, column=2, sticky='w')

    ## document_type

    document_type_label = ttk.Label(new_student_frame, text="Rodzaj dokumentu", font=('Open Sans', 12), bootstyle='default')
    document_type_label.grid(row=14, column=3, sticky='w')

    document_type = ttk.Menubutton(new_student_frame, bootstyle='dark', text='Wybierz dokument')
    document_type.grid(row=15, column=3, sticky='w')

    document_type_content = ttk.Menu(document_type)

    item_var = StringVar()
    for x in ['Dowód osobisty', 'Paszport', 'Karta pobytu']:
        document_type_content.add_radiobutton(label=x, variable=item_var, command=lambda x=x:amend_menu_content(document_type, x))

    document_type['menu'] = document_type_content

    ## language

    language_label = ttk.Label(new_student_frame, text="Język kursu", font=('Open Sans', 12), bootstyle='default')
    language_label.grid(row=17, column=0, sticky='w')

    language_dropdown = ttk.Menubutton(new_student_frame, bootstyle='dark', text="Wybierz język")
    language_dropdown.grid(row=18, column=0, sticky='w')

    language_dropdown_content = ttk.Menu(language_dropdown)

    language_var = StringVar()
    for x in ['Angielski', 'Niemiecki', 'Francuski', 'Włoski', 'Hiszpański']:
        language_dropdown_content.add_radiobutton(label=x, variable=language_var, command=lambda x=x:amend_menu_content(language_dropdown, x))

    language_dropdown['menu'] = language_dropdown_content

    ## level

    level_label = ttk.Label(new_student_frame, text="Poziom", font=('Open Sans', 12), bootstyle='default')
    level_label.grid(row=17, column=2, sticky='w')

    level_dropdown = ttk.Menubutton(new_student_frame, bootstyle='dark', text="Wybierz poziom")
    level_dropdown.grid(row=18, column=2, sticky='w')

    level_dropdown_content = ttk.Menu(level_dropdown)

    level_var = StringVar()

    for x in ['Początkujący', 'Zaawansowany']:
        level_dropdown_content.add_radiobutton(label=x, variable=level_var, command=lambda x=x:amend_menu_content(level_dropdown, x))

    level_dropdown['menu'] = level_dropdown_content


    ## mode

    mode_label = ttk.Label(new_student_frame, text="Tryb", font=('Open Sans', 12), bootstyle='default')
    mode_label.grid(row=17, column=3, sticky='w')

    mode_dropdown = ttk.Menubutton(new_student_frame, bootstyle='dark', text="Wybierz poziom")
    mode_dropdown.grid(row=18, column=3, sticky='w')

    mode_dropdown_content = ttk.Menu(mode_dropdown)

    mode_var = StringVar()

    for x in ['Normalny', 'Przyspieszony']:
        mode_dropdown_content.add_radiobutton(label=x, variable=mode_var,
                                               command=lambda x=x: amend_menu_content(mode_dropdown, x))

    mode_dropdown['menu'] = mode_dropdown_content


    ## course

    course_label = ttk.Label(new_student_frame, text="Wybierz dostępny kurs", font=('Open Sans', 12),
                             bootstyle='default')
    course_label.grid(row=17, column=4, sticky='w')

    course_dropdown = ttk.Menubutton(new_student_frame, bootstyle='dark', text="Wybierz kurs")
    course_dropdown.grid(row=18, column=4, sticky='w')

    course_dropdown_content = ttk.Menu(course_dropdown)

    course_var = StringVar()

    start_date_label = ttk.Label(new_student_frame, text="Data rozpoczęcia", font=('Open Sans', 12), bootstyle='default')
    start_date_label.grid(row=20, column=0, sticky='w')

    start_date = ttk.Entry(new_student_frame, bootstyle='default', state='readonly', width=15)
    start_date.grid(row=21, column=0, sticky='w')

    end_date_label = ttk.Label(new_student_frame, text="Data zakończenia", font=('Open Sans', 12), bootstyle='default')
    end_date_label.grid(row=20, column=2, sticky='w')

    end_date = ttk.Entry(new_student_frame, bootstyle='default', state='readonly', width=15)
    end_date.grid(row=21, column=2, sticky='w')

    ## payment

    payment_label = ttk.Label(new_student_frame, text="Płatność", font=('Open Sans', 12), bootstyle='default')
    payment_label.grid(row=20, column=3, sticky='w')

    payment_dropdown = ttk.Menubutton(new_student_frame, bootstyle='dark', text="Wybierz sposób płatności")
    payment_dropdown.grid(row=21, column=3, sticky='w')

    payment_dropdown_content = ttk.Menu(payment_dropdown)

    payment_var = StringVar()

    for x in ['W placówce', 'Przelew']:
        payment_dropdown_content.add_radiobutton(label=x, variable=payment_var,
                                              command=lambda x=x: amend_menu_content(payment_dropdown, x))

    payment_dropdown['menu'] = payment_dropdown_content

    prize_label = ttk.Label(new_student_frame, text="Cena", font=('Open Sans', 12), bootstyle='default')
    prize_label.grid(row=20, column=4, sticky='w')

    prize_entry = ttk.Entry(new_student_frame, bootstyle='default', state='readonly', width=15)
    prize_entry.grid(row=21, column=4, sticky='w')

    submit_button_style = ttk.Style()
    submit_button_style.configure('success.TButton', font=('Open Sans', 16))

    submit_button = ttk.Button(new_student_frame, bootstyle='success', text='ZAPISZ', width=20, style='success.TButton')
    submit_button.grid(row=24, column=3, sticky='w')

    new_student_frame.pack(),

"""
Function that switches to the information about student. It also contains all the information about the design of this frame. 
"""

def student_info_switch():
    delete_pages()
    student_info_frame = ttk.Frame(main_frame)


    student_label = ttk.Label(student_info_frame, text='INFORMACJE O UCZNIU', font=('Open Sans', 14, 'bold'), bootstyle='default')
    student_label.pack()


    student_info_frame.pack()


"""
Function that switches to course creation frame. It also contains all the information about the design of this frame. 
"""

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

    ## course_name

    course_name_label = ttk.Label(create_course_frame, text='Nazwa kursu', font=('Open Sans', 12), bootstyle='default')
    course_name_label.grid(row=2, column=0, sticky='w')

    course_name_entry = ttk.Entry(create_course_frame, bootstyle='light', width=30)
    course_name_entry.grid(row=3, column=0, sticky='w')

    ## course_language

    course_language_label = ttk.Label(create_course_frame, text="Język kursu", font=('Open Sans', 12), bootstyle='default')
    course_language_label.grid(row=2, column=2, sticky='w')

    course_language_dropdown = ttk.Menubutton(create_course_frame, bootstyle='dark', text="Wybierz język")
    course_language_dropdown.grid(row=3, column=2, sticky='w')

    course_language_dropdown_content = ttk.Menu(course_language_dropdown)

    course_language_var = StringVar()
    for x in ['Angielski', 'Niemiecki', 'Francuski', 'Włoski', 'Hiszpański']:
        course_language_dropdown_content.add_radiobutton(label=x, variable=course_language_var,
                                                  command=lambda x=x: amend_menu_content(course_language_dropdown, x))

    course_language_dropdown['menu'] = course_language_dropdown_content

    ## course_level

    course_level_label = ttk.Label(create_course_frame, text='Poziom', font=('Open Sans', 12), bootstyle='default')
    course_level_label.grid(row=2, column=3, sticky='w')

    course_level_dropdown = ttk.Menubutton(create_course_frame, bootstyle='dark', text='Wybierz poziom')
    course_level_dropdown.grid(row=3, column=3, sticky='w')

    course_level_dropdown_content = ttk.Menu(course_level_dropdown)

    course_level_var= StringVar()

    for x in ['Początkujący', 'Zaawansowany']:
        course_level_dropdown_content.add_radiobutton(label=x, variable=course_level_var, command=lambda x=x: amend_menu_content(course_level_dropdown, x))

    course_level_dropdown['menu'] = course_level_dropdown_content

    ## course_mode

    mode_label = ttk.Label(create_course_frame, text="Tryb", font=('Open Sans', 12), bootstyle='default')
    mode_label.grid(row=2, column=4, sticky='w')

    mode_dropdown = ttk.Menubutton(create_course_frame, bootstyle='dark', text="Wybierz poziom")
    mode_dropdown.grid(row=3, column=4, sticky='w')

    mode_dropdown_content = ttk.Menu(mode_dropdown)

    mode_var = StringVar()

    choice = ""

    for x in ['Normalny', 'Przyspieszony']:
        mode_dropdown_content.add_radiobutton(label=x, variable=mode_var,
                                              command=lambda x=x: amend_menu_content(mode_dropdown, x))



    mode_dropdown['menu'] = mode_dropdown_content



    ## start_date

    start_date_label = ttk.Label(create_course_frame, text='Data rozpoczęcia', font=('Open Sans', 12), bootstyle='default')
    start_date_label.grid(row=5, column=0, sticky='w')

    start_date_entry = ttk.DateEntry(create_course_frame, bootstyle='primary')
    start_date_entry.grid(row=6, column=0, sticky='w')

    ## end date

    end_date_label = ttk.Label(create_course_frame, text='Data zakończenia', font=('Open Sans', 12), bootstyle='default')
    end_date_label.grid(row=5, column=2, sticky='w')

    end_date_entry = ttk.DateEntry(create_course_frame, bootstyle='primary')
    end_date_entry.configure(state="readonly")
    end_date_entry.grid(row=6, column=2, sticky='w')

    ## teacher_selection

    teacher_selection_label = ttk.Label(create_course_frame, text='Nauczyciel', font=('Open Sans', 12), bootstyle='default')
    teacher_selection_label.grid(row=5, column=3, sticky='w')

    teacher_selection_dropdown = ttk.Menubutton(create_course_frame, text='Wybierz nauczyciela', bootstyle='dark')
    teacher_selection_dropdown.grid(row=6, column=3, sticky='w')

    ## prize

    prize_label = ttk.Label(create_course_frame, text="Cena", font=('Open Sans', 12), bootstyle='default')
    prize_label.grid(row=5, column=4, sticky='w')

    prize_entry = ttk.Entry(create_course_frame, bootstyle='default', width=15)
    prize_entry.grid(row=6, column=4, sticky='w')

    submit_button_style = ttk.Style()
    submit_button_style.configure('success.TButton', font=('Open Sans', 16))

    submit_button = ttk.Button(create_course_frame, bootstyle='success', text='ZAPISZ', width=20, style='success.TButton')
    submit_button.grid(row=9, column=3, sticky='w')

    create_course_frame.pack()

"""
Function that switches to course information frame. It also contains all the information about the design of this frame. 
"""

def course_info_switch():
    delete_pages()
    course_info_frame = ttk.Frame(main_frame)

    course_info_label = ttk.Label(course_info_frame, text='INFORMACJE O KURSACH', font=('Open Sans', 14, 'bold'), bootstyle='default')
    course_info_label.pack()

    course_info_frame.pack()


"""
Function that switches to add a teacher frame. It also contains all the information about the design of this frame. 
"""


def add_a_teacher_switch():
    delete_pages()
    add_a_teacher_frame = ttk.Frame(main_frame)

    add_a_teacher_frame.columnconfigure((0, 2, 3, 4, 5), weight=1, minsize=250)
    add_a_teacher_frame.columnconfigure(1, weight=1, minsize=50)
    add_a_teacher_frame.rowconfigure(
        (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28),
        weight=1, minsize=30)

    add_a_teacher_label = ttk.Label(add_a_teacher_frame, text='DODAJ NAUCZYCIELA', font=('Open Sans', 14, 'bold'),
                                  bootstyle='default')
    add_a_teacher_label.grid(row=0, column=3, sticky='w')

    ## first_name

    first_name_label = ttk.Label(add_a_teacher_frame, text="Imię", font=('Open Sans', 12), bootstyle='default')
    first_name_label.grid(row=2, column=0, sticky='w')

    first_name = ttk.Entry(add_a_teacher_frame, width=30, bootstyle='light')
    first_name.grid(row=3, column=0)

    ## last_name

    last_name_label = ttk.Label(add_a_teacher_frame, text="Nazwisko", font=('Open Sans', 12), bootstyle='default')
    last_name_label.grid(row=2, column=2, sticky='w')

    last_name = ttk.Entry(add_a_teacher_frame, width=30, bootstyle='light')
    last_name.grid(row=3, column=2)

    ## street

    street_label = ttk.Label(add_a_teacher_frame, text='Ulica', font=('Open Sans', 12), bootstyle='default')
    street_label.grid(row=5, column=0, sticky='w')

    street = ttk.Entry(add_a_teacher_frame, width=30, bootstyle='light')
    street.grid(row=6, column=0, sticky='e')

    ## building_no

    building_no_label = ttk.Label(add_a_teacher_frame, text='Nr domu', font=('Open Sans', 12), bootstyle='default')
    building_no_label.grid(row=5, column=2, sticky='w')

    building_no = ttk.Entry(add_a_teacher_frame, width=10, bootstyle='light')
    building_no.grid(row=6, column=2, sticky='w')

    ## local_no

    local_no_label = ttk.Label(add_a_teacher_frame, text='Nr lokalu', font=('Open Sans', 12), bootstyle='default')
    local_no_label.grid(row=5, column=3, sticky='w')

    local_no = ttk.Entry(add_a_teacher_frame, width=10, bootstyle='light')
    local_no.grid(row=6, column=3, sticky='w')

    ## city

    city_label = ttk.Label(add_a_teacher_frame, text="Miasto", font=('Open Sans', 12), bootstyle='default')
    city_label.grid(row=8, column=0, sticky='w')

    city = ttk.Entry(add_a_teacher_frame, width=30, bootstyle='light')
    city.grid(row=9, column=0, sticky='w')

    ## postal_code

    postal_code_label = ttk.Label(add_a_teacher_frame, text="Kod pocztowy", font=('Open Sans', 12), bootstyle='default')
    postal_code_label.grid(row=8, column=2, sticky='w')

    postal_code = ttk.Entry(add_a_teacher_frame, width=15, bootstyle='light')
    postal_code.grid(row=9, column=2, sticky='w')

    ## country

    country_label = ttk.Label(add_a_teacher_frame, text="Państwo", font=('Open Sans', 12), bootstyle='default')
    country_label.grid(row=8, column=3, sticky='w')

    country = ttk.Entry(add_a_teacher_frame, width=30, bootstyle='light')
    country.grid(row=9, column=3, sticky='w')

    ## email

    email_label = ttk.Label(add_a_teacher_frame, text="Adres e-mail", font=('Open Sans', 12), bootstyle='default')
    email_label.grid(row=11, column=0, sticky='w')

    email = ttk.Entry(add_a_teacher_frame, width=30, bootstyle='light')
    email.grid(row=12, column=0, sticky='w')

    ## phone number

    phone_number_label = ttk.Label(add_a_teacher_frame, text="Nr telefonu", font=('Open Sans', 12), bootstyle='default')
    phone_number_label.grid(row=11, column=2, sticky='w')

    phone_number = ttk.Entry(add_a_teacher_frame, width=20, bootstyle='light')
    phone_number.grid(row=12, column=2, sticky='w')

    ## personal id

    personal_id_label = ttk.Label(add_a_teacher_frame, text="PESEL", font=('Open Sans', 12), bootstyle='default')
    personal_id_label.grid(row=11, column=3, sticky='w')

    personal_id = ttk.Entry(add_a_teacher_frame, width=20, bootstyle='light')
    personal_id.grid(row=12, column=3, sticky='w')

    ## document_no

    document_no_label = ttk.Label(add_a_teacher_frame, text="Nr dokumentu", font=('Open Sans', 12), bootstyle='default')
    document_no_label.grid(row=14, column=0, sticky='w')

    document_no = ttk.Entry(add_a_teacher_frame, width=20, bootstyle='light')
    document_no.grid(row=15, column=0, sticky='w')

    ## document_type

    document_type_label = ttk.Label(add_a_teacher_frame, text="Rodzaj dokumentu", font=('Open Sans', 12),
                                    bootstyle='default')
    document_type_label.grid(row=14, column=2, sticky='w')

    document_type = ttk.Menubutton(add_a_teacher_frame, bootstyle='dark', text='Wybierz dokument')
    document_type.grid(row=15, column=2, sticky='w')

    document_type_content = ttk.Menu(document_type)

    item_var = StringVar()
    for x in ['Dowód osobisty', 'Paszport', 'Karta pobytu']:
        document_type_content.add_radiobutton(label=x, variable=item_var,
                                              command=lambda x=x: amend_menu_content(document_type, x))

    document_type['menu'] = document_type_content

    ## type_of_contract

    type_of_contract_label = ttk.Label(add_a_teacher_frame, text="Rodzaj umowy", font=('Open Sans', 12), bootstyle='default')
    type_of_contract_label.grid(row=14, column=3, sticky='w')

    type_of_contract = ttk.Menubutton(add_a_teacher_frame, bootstyle='dark', text='Wybierz umowę')
    type_of_contract.grid(row=15, column=3, sticky='w')

    type_of_contract_content = ttk.Menu(type_of_contract)

    type_var = StringVar()

    for x in ['Umowa o pracę', 'Umowa zlecenie']:
        type_of_contract_content.add_radiobutton(label=x, variable=type_var, command=lambda x=x: amend_menu_content(type_of_contract, x))

    type_of_contract['menu'] = type_of_contract_content


    ## type_of_employment

    type_of_employment_label = ttk.Label(add_a_teacher_frame, text='Rodzaj zatrudnienia', font=('Open Sans', 12), bootstyle='default')
    type_of_employment_label.grid(row=14, column=4, sticky='w')

    type_of_employment = ttk.Menubutton(add_a_teacher_frame, bootstyle='dark', text='Wybierz')
    type_of_employment.grid(row=15, column=4, sticky='w')

    type_of_employment_content = ttk.Menu(type_of_employment)

    employment_var = StringVar()

    for x in ['Pełny etat', 'Pół etatu']:
        type_of_employment_content.add_radiobutton(label=x, variable=employment_var, command=lambda x=x:amend_menu_content(type_of_employment, x))

    type_of_employment['menu'] = type_of_employment_content

    ## salary

    salary_label = ttk.Label(add_a_teacher_frame, text="Wysokość wypłaty", font=('Open Sans', 12), bootstyle='default')
    salary_label.grid(row=17, column=0, sticky='w')

    salary = ttk.Entry(add_a_teacher_frame, width=20, bootstyle='light')
    salary.grid(row=18, column=0, sticky='w')


    ## employment_start

    employment_start_label = ttk.Label(add_a_teacher_frame, text='Data rozpoczęcia pracy', font=('Open Sans', 12),
                               bootstyle='default')
    employment_start_label.grid(row=17, column=2, sticky='w')

    employment_start_entry = ttk.DateEntry(add_a_teacher_frame, bootstyle='primary')
    employment_start_entry.grid(row=18, column=2, sticky='w')


    # native_language

    native_language_label = ttk.Label(add_a_teacher_frame, text='Język ojczysty', font=('Open Sans', 12),
                               bootstyle='default')
    native_language_label.grid(row=17, column=3, sticky='w')

    native_language_entry = ttk.Entry(add_a_teacher_frame, width=20, bootstyle='light')
    native_language_entry.grid(row=18, column=3, sticky='w')


    # language_to_teach

    language_to_teach_label = ttk.Label(add_a_teacher_frame, text='Język nauczania', font=('Open Sans', 12),
                                      bootstyle='default')
    language_to_teach_label.grid(row=17, column=4, sticky='w')

    language_to_teach = ttk.Menubutton(add_a_teacher_frame, bootstyle='dark', text='Wybierz')
    language_to_teach.grid(row=18, column=4, sticky='w')

    language_to_teach_content = ttk.Menu(language_to_teach)

    lang_var = StringVar()

    for x in ['Angielski', 'Niemiecki', 'Francuski', 'Włoski', 'Hiszpański']:
        language_to_teach_content.add_radiobutton(label=x, variable=lang_var, command=lambda x=x:amend_menu_content(language_to_teach, x))

    language_to_teach['menu'] = language_to_teach_content


    submit_button_style = ttk.Style()
    submit_button_style.configure('success.TButton', font=('Open Sans', 16))

    submit_button = ttk.Button(add_a_teacher_frame, bootstyle='success', text='ZAPISZ', width=20,
                               style='success.TButton')
    submit_button.grid(row=21, column=3, sticky='w')


    add_a_teacher_frame.pack()

"""
Function that switches to teacher_info frame. It also contains all the information about the design of this frame. 
"""


def teacher_info_switch():
    delete_pages()
    teacher_info_frame = ttk.Frame(main_frame)

    teacher_info_label = ttk.Label(teacher_info_frame, text='WYSZUKAJ NAUCZYCIELI', font=('Open Sans', 14, 'bold'),
                                  bootstyle='default')
    teacher_info_label.pack()

    teacher_info_frame.pack()

"""
Function that switches to search_payment frame. It also contains all the information about the design of this frame. 
"""


def search_payment_switch():
    delete_pages()
    search_payment_frame = ttk.Frame(main_frame)

    search_payment_label = ttk.Label(search_payment_frame, text='WYSZUKAJ PŁATNOŚĆ', font=('Open Sans', 14, 'bold'),
                                  bootstyle='default')
    search_payment_label.pack()

    search_payment_frame.pack()


"""
Function that switches to generate_report frame. It also contains all the information about the design of this frame. 
"""


def generate_report_switch():
    delete_pages()
    generate_report_frame = ttk.Frame(main_frame)

    generate_report_label = ttk.Label(generate_report_frame, text='WYGENERUJ RAPORT', font=('Open Sans', 14, 'bold'),
                                  bootstyle='default')
    generate_report_label.pack()

    generate_report_frame.pack()


"""
Function that changes the default text in the Menubutton.
"""
def amend_menu_content(element,x):
    element.config(text=x)


"""
Function that deletes the page everytime the user enters it. It had to be implemented as without it, everytime the user
enters the particular page, it will keep overwriting the main frame. Basically, it would put the pages on top of 
the previous ones.
"""
def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()


"""
Design of the menu on the left side and the initial screen.
"""

students = ttk.Button(text='UCZNIOWIE', bootstyle='light-outline', width=22, style='light.Outline.TButton', state='disabled')
students.place(x=10, y=140)

new_student = ttk.Button(text='NOWY UCZEŃ', bootstyle='info', width=22, command=lambda: new_student_switch())
new_student.place(x=10, y=178)

student_info = ttk.Button(text='INFORMACJE O UCZNIU', bootstyle='info', width=22, command=lambda: student_info_switch())
student_info.place(x=10, y=216)

courses = ttk.Button(text='KURSY', bootstyle='light-outline', width=22, style='light.Outline.TButton', state='disabled')
courses.place(x=10, y=255)

create_course = ttk.Button(text='STWÓRZ KURS', bootstyle='info', width=22, command=lambda: create_course_switch())
create_course.place(x=10, y=293)

course_info = ttk.Button(text='INFORMACJE O KURSACH', bootstyle='info', width=22, command=lambda: course_info_switch())
course_info.place(x=10, y=331)

teachers = ttk.Button(text='NAUCZYCIELE', bootstyle='light-outline', width=22, style='light.Outline.TButton', state='disabled')
teachers.place(x=10, y=369)

add_a_teacher = ttk.Button(text='DODAJ NAUCZYCIELA', bootstyle='info', width=22, command=lambda: add_a_teacher_switch())
add_a_teacher.place(x=10, y=407)

teacher_info = ttk.Button(text='WYSZUKAJ NAUCZYCIELI', bootstyle='info', width=22, command=lambda: teacher_info_switch())
teacher_info.place(x=10, y=445)

payments = ttk.Button(text='PŁATNOŚCI', bootstyle='light-outline', width=22, style='light.Outline.TButton', state='disabled')
payments.place(x=10, y=483)

search_payment = ttk.Button(text='WYSZUKAJ PŁATNOŚĆ', bootstyle='info', width=22, command=lambda: search_payment_switch())
search_payment.place(x=10, y=521)

generate_report = ttk.Button(text='WYGENERUJ RAPORT', bootstyle='info', width=22, command=lambda: generate_report_switch())
generate_report.place(x=10, y=559)

"""
Main frame that will serve as the base for other pages.
"""

main_frame =ttk.Frame(bootstyle='dark')
main_frame.pack_propagate(False)
main_frame.configure(width=1545, height= 870)
main_frame.pack()
main_frame.place(x=300, y=140)

"""
Activation of the application main loop. 
"""

root.mainloop()

