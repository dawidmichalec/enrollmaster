from tkinter import *
import ttkbootstrap as ttk

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

def on_document_type_select():
    selected_document_type = document_var.get()
    print("Selected document type:", selected_document_type )
    amend_menu_content(document_type, selected_document_type )
    return selected_document_type

document_type = ttk.Menubutton(add_a_teacher_frame, bootstyle='dark', text='Wybierz dokument')
document_type.grid(row=15, column=2, sticky='w')

document_type_content = ttk.Menu(document_type)

document_var = StringVar()
document_var.set("Dowód osobisty")
for document in ['Dowód osobisty', 'Paszport', 'Karta pobytu']:
    document_type_content.add_radiobutton(label=document, variable=document_var, value=document,
                                          command=on_document_type_select)

document_type['menu'] = document_type_content

## type_of_contract

type_of_contract_label = ttk.Label(add_a_teacher_frame, text="Rodzaj umowy", font=('Open Sans', 12), bootstyle='default')
type_of_contract_label.grid(row=14, column=3, sticky='w')

def on_contract_type_select():
    selected_contract_type = type_var.get()
    print("Selected type of contract:", selected_contract_type)
    amend_menu_content(type_of_contract, selected_contract_type)
    return selected_contract_type

type_of_contract = ttk.Menubutton(add_a_teacher_frame, bootstyle='dark', text='Wybierz umowę')
type_of_contract.grid(row=15, column=3, sticky='w')

type_of_contract_content = ttk.Menu(type_of_contract)

type_var = StringVar()
type_var.set("Umowa o pracę")

for contract in ['Umowa o pracę', 'Umowa zlecenie']:
    type_of_contract_content.add_radiobutton(label=contract, variable=type_var, value=contract, command=on_contract_type_select)

type_of_contract['menu'] = type_of_contract_content


## type_of_employment

type_of_employment_label = ttk.Label(add_a_teacher_frame, text='Rodzaj zatrudnienia', font=('Open Sans', 12), bootstyle='default')
type_of_employment_label.grid(row=14, column=4, sticky='w')

def on_employment_type_select():
    selected_employment_type = employment_var.get()
    print("Selected type of employment:", selected_employment_type)
    amend_menu_content(type_of_employment, selected_employment_type)
    return selected_employment_type

type_of_employment = ttk.Menubutton(add_a_teacher_frame, bootstyle='dark', text='Wybierz')
type_of_employment.grid(row=15, column=4, sticky='w')

type_of_employment_content = ttk.Menu(type_of_employment)

employment_var = StringVar()
employment_var.set("Pełny etat")

for employment in ['Pełny etat', 'Pół etatu']:
    type_of_employment_content.add_radiobutton(label=employment, variable=employment_var, value=employment ,command=on_employment_type_select)

type_of_employment['menu'] = type_of_employment_content

## salary

salary_label = ttk.Label(add_a_teacher_frame, text="Wynagrodzenie", font=('Open Sans', 12), bootstyle='default')
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

def on_language_to_teach_select():
    selected_language = lang_var.get()
    print("Selected language:", selected_language)
    amend_menu_content(language_to_teach, selected_language)
    return selected_language

language_to_teach = ttk.Menubutton(add_a_teacher_frame, bootstyle='dark', text='Wybierz')
language_to_teach.grid(row=18, column=4, sticky='w')

language_to_teach_content = ttk.Menu(language_to_teach)

lang_var = StringVar()
lang_var.set("Angielski")
for language in ['Angielski', 'Niemiecki', 'Francuski', 'Włoski', 'Hiszpański']:
    language_to_teach_content.add_radiobutton(label=language, variable=lang_var, value=language,
                                              command=on_language_to_teach_select)

language_to_teach['menu'] = language_to_teach_content


submit_button_style = ttk.Style()
submit_button_style.configure('success.TButton', font=('Open Sans', 16))

submit_button = ttk.Button(add_a_teacher_frame, bootstyle='success', text='ZAPISZ', width=20,
                           style='success.TButton')
submit_button.grid(row=21, column=3, sticky='w')


add_a_teacher_frame.pack()
