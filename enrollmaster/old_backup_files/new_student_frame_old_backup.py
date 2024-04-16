from tkinter import *
import ttkbootstrap as ttk
from datetime import datetime, timedelta
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

    def on_document_type_select():
        selected_document_type = document_var.get()
        print("Selected document type:", selected_document_type)
        amend_menu_content(document_type, selected_document_type)
        return selected_document_type

    document_type = ttk.Menubutton(new_student_frame, bootstyle='dark', text="Wybierz dokument")
    document_type.grid(row=15, column=3, sticky='w')

    document_type_content = ttk.Menu(document_type)

    document_var = ttk.StringVar()
    document_var.set("Dowód osobisty")  # Set default document_type

    for document in ['Dowód osobisty', 'Paszport', 'Karta pobytu']:
        document_type_content.add_radiobutton(label=document, variable=document_var, value=document,
                                              command=on_document_type_select)

    document_type['menu'] = document_type_content

    ## language

    language_label = ttk.Label(new_student_frame, text="Język kursu", font=('Open Sans', 12), bootstyle='default')
    language_label.grid(row=17, column=0, sticky='w')

    def on_language_select():
        selected_language = language_var.get()
        print("Selected language:", selected_language)
        amend_menu_content(language_dropdown, selected_language)
        return selected_language

    language_dropdown = ttk.Menubutton(new_student_frame, bootstyle='dark', text="Wybierz język")
    language_dropdown.grid(row=18, column=0, sticky='w')

    language_dropdown_content = ttk.Menu(language_dropdown)

    language_var = ttk.StringVar()
    language_var.set("Angielski")  # Set default payment method

    for language in ['Angielski', 'Niemiecki', 'Francuski', 'Włoski', 'Hiszpański']:
        language_dropdown_content.add_radiobutton(label=language, variable=language_var, value=language,
                                                  command=on_language_select)

    language_dropdown['menu'] = language_dropdown_content

    ## level

    level_label = ttk.Label(new_student_frame, text="Poziom", font=('Open Sans', 12), bootstyle='default')
    level_label.grid(row=17, column=2, sticky='w')

    def on_level_select():
        selected_level = level_var.get()
        print("Selected level:", selected_level)
        amend_menu_content(level_dropdown, selected_level)
        return selected_level

    level_dropdown = ttk.Menubutton(new_student_frame, bootstyle='dark', text="Wybierz poziom")
    level_dropdown.grid(row=18, column=2, sticky='w')

    level_dropdown_content = ttk.Menu(level_dropdown)

    level_var = StringVar()
    level_var.set("Początkujący")  # Set default payment method

    for level in ['Początkujący', 'Zaawansowany']:
        level_dropdown_content.add_radiobutton(label=level, variable=level_var, value=level,
                                               command=on_level_select)

    level_dropdown['menu'] = level_dropdown_content


    ## mode

    mode_label = ttk.Label(new_student_frame, text="Tryb", font=('Open Sans', 12), bootstyle='default')
    mode_label.grid(row=17, column=3, sticky='w')

    def on_mode_select():
        selected_mode = mode_var.get()
        print("Selected mode:", selected_mode)
        amend_menu_content(mode_dropdown, selected_mode)
        return selected_mode

    mode_dropdown = ttk.Menubutton(new_student_frame, bootstyle='dark', text="Wybierz tryb")
    mode_dropdown.grid(row=18, column=3, sticky='w')

    mode_dropdown_content = ttk.Menu(mode_dropdown)

    mode_var = StringVar()
    mode_var.set("Normalny")  # Set default mode

    for mode in ['Normalny', 'Przyspieszony']:
        mode_dropdown_content.add_radiobutton(label=mode, variable=mode_var, value=mode,
                                              command=on_mode_select)

    mode_dropdown['menu'] = mode_dropdown_content


    ## course

    course_label = ttk.Label(new_student_frame, text="Wybierz dostępny kurs", font=('Open Sans', 12),
                             bootstyle='default')
    course_label.grid(row=17, column=4, sticky='w')

    course_dropdown = ttk.Menubutton(new_student_frame, bootstyle='dark', text="Wybierz kurs")
    course_dropdown.grid(row=18, column=4, sticky='w')

    course_dropdown_content = ttk.Menu(course_dropdown)

    course_var = StringVar()

    ## start_date

    start_date_label = ttk.Label(new_student_frame, text="Data rozpoczęcia", font=('Open Sans', 12), bootstyle='default')
    start_date_label.grid(row=20, column=0, sticky='w')

    start_date_entry = ttk.DateEntry(new_student_frame, bootstyle='primary')
    start_date_entry.configure(state='readonly')
    start_date_entry.grid(row=21, column=0, sticky='w')

    ## end_date

    end_date_label = ttk.Label(new_student_frame, text="Data zakończenia", font=('Open Sans', 12), bootstyle='default')
    end_date_label.grid(row=20, column=2, sticky='w')

    end_date_entry = ttk.DateEntry(new_student_frame, bootstyle='primary')
    end_date_entry.configure(state='readonly')
    end_date_entry.grid(row=21, column=2, sticky='w')

    ## payment

    payment_label = ttk.Label(new_student_frame, text="Płatność", font=('Open Sans', 12), bootstyle='default')
    payment_label.grid(row=20, column=3, sticky='w')

    def on_payment_select():
        selected_payment_method = payment_var.get()
        print("Selected payment method:", selected_payment_method)
        amend_menu_content(payment_dropdown, selected_payment_method)
        return selected_payment_method

    payment_dropdown = ttk.Menubutton(new_student_frame, bootstyle='dark', text="Wybierz sposób płatności")
    payment_dropdown.grid(row=21, column=3, sticky='w')

    payment_dropdown_content = ttk.Menu(payment_dropdown)

    payment_var = ttk.StringVar()
    payment_var.set("W placówce")  # Set default payment method

    for payment_method in ['W placówce', 'Przelew']:
        payment_dropdown_content.add_radiobutton(label=payment_method, variable=payment_var, value=payment_method,
                                                 command=on_payment_select)

    payment_dropdown['menu'] = payment_dropdown_content

    ## prize

    prize_label = ttk.Label(new_student_frame, text="Cena", font=('Open Sans', 12), bootstyle='default')
    prize_label.grid(row=20, column=4, sticky='w')

    prize_var = ''

    prize_entry = ttk.Entry(new_student_frame, bootstyle='default', width=15)
    prize_entry.insert('end', prize_var)
    prize_entry.configure(state='readonly')
    prize_entry.grid(row=21, column=4, sticky='w')

    ## submit

    submit_button_style = ttk.Style()
    submit_button_style.configure('success.TButton', font=('Open Sans', 16))

    submit_button = ttk.Button(new_student_frame, bootstyle='success', text='ZAPISZ', width=20, style='success.TButton')
    submit_button.grid(row=24, column=3, sticky='w')

    new_student_frame.pack(),


