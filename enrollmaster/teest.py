from tkinter import *
import ttkbootstrap as ttk

def teacher_info_switch():
    teacher_info_frame = ttk.Frame(main_frame)

    teacher_info_frame.columnconfigure((0, 2, 3, 4, 5), weight=1, minsize=250)
    teacher_info_frame.columnconfigure(1, weight=1, minsize=50)
    teacher_info_frame.rowconfigure(
        (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28),
        weight=1, minsize=30)

    ## Config variable responsible for setting state of the elements

    disabled_state = 'disabled'

    ## name of the frame/page

    teacher_label = ttk.Label(teacher_info_frame, text='WYSZUKAJ NAUCZYCIELA', font=('Open Sans', 14, 'bold'),
                              bootstyle='default')
    teacher_label.grid(row=0, column=3, sticky='w')

    ## teacher_id used for search purposes

    id_label = ttk.Label(teacher_info_frame, text='ID Ucznia', font=('Open Sans', 12), bootstyle='default')
    id_label.grid(row=2, column=2, sticky='w')

    id_entry = ttk.Entry(teacher_info_frame, bootstyle='light', width=20)
    id_entry.grid(row=3, column=2, sticky='w')

    ## first_name

    first_name_label = ttk.Label(teacher_info_frame, text="Imię", font=('Open Sans', 12), bootstyle='default')
    first_name_label.grid(row=2, column=3, sticky='w')

    first_name = ttk.Entry(teacher_info_frame, width=20, bootstyle='light')
    first_name.grid(row=3, column=3, sticky='w')

    ## last_name

    last_name_label = ttk.Label(teacher_info_frame, text="Nazwisko", font=('Open Sans', 12), bootstyle='default')
    last_name_label.grid(row=2, column=4, sticky='w')

    last_name = ttk.Entry(teacher_info_frame, width=20, bootstyle='light')
    last_name.grid(row=3, column=4, sticky='w')

    ## submit button

    submit_button_style = ttk.Style()
    submit_button_style.configure('success.TButton', font=('Open Sans', 16))

    submit_button = ttk.Button(teacher_info_frame, bootstyle='success', text='SZUKAJ', width=13,
                               style='success.TButton')
    submit_button.grid(row=5, column=3, sticky='w')

    ## teacher_id

    teacher_id_label = ttk.Label(teacher_info_frame, text='ID Ucznia', font=('Open Sans', 12), bootstyle='default')
    teacher_id_label.grid(row=8, column=0, sticky='w')

    teacher_id = ttk.Entry(teacher_info_frame, bootstyle='default', state='readonly', width=15)
    teacher_id.configure(state=f'{disabled_state}')
    teacher_id.grid(row=9, column=0, sticky='w')

    ## output_first_name

    output_first_name_label = ttk.Label(teacher_info_frame, text='Imię', font=('Open Sans', 12), bootstyle='default')
    output_first_name_label.grid(row=8, column=2, sticky='w')

    output_first_name = ttk.Entry(teacher_info_frame, bootstyle='default', state='readonly', width=15)
    output_first_name.configure(state=f'{disabled_state}')
    output_first_name.grid(row=9, column=2, sticky='w')

    ## output_last_name

    output_last_name_label = ttk.Label(teacher_info_frame, text='Nazwisko', font=('Open Sans', 12), bootstyle='default')
    output_last_name_label.grid(row=8, column=3, sticky='w')

    output_last_name = ttk.Entry(teacher_info_frame, bootstyle='default', state='readonly', width=15)
    output_last_name.configure(state=f'{disabled_state}')
    output_last_name.grid(row=9, column=3, sticky='w')

    ## output_street

    output_street_label = ttk.Label(teacher_info_frame, text='Ulica', font=('Open Sans', 12), bootstyle='default')
    output_street_label.grid(row=8, column=4, sticky='w')

    output_street = ttk.Entry(teacher_info_frame, bootstyle='default', state='readonly', width=30)
    output_street.configure(state=f'{disabled_state}')
    output_street.grid(row=9, column=4, sticky='w')

    ## output_building_no

    output_building_no_label = ttk.Label(teacher_info_frame, text='Nr domu', font=('Open Sans', 12),
                                         bootstyle='default')
    output_building_no_label.grid(row=11, column=0, sticky='w')

    output_building_no = ttk.Entry(teacher_info_frame, bootstyle='default', state='readonly', width=15)
    output_building_no.configure(state=f'{disabled_state}')
    output_building_no.grid(row=12, column=0, sticky='w')

    ## local_no_output

    local_no_output_label = ttk.Label(teacher_info_frame, text='Nr lokalu', font=('Open Sans', 12), bootstyle='default')
    local_no_output_label.grid(row=11, column=2, sticky='w')

    local_no_output = ttk.Entry(teacher_info_frame, bootstyle='default', state='readonly', width=15)
    local_no_output.configure(state=f'{disabled_state}')
    local_no_output.grid(row=12, column=2, sticky='w')

    ## city_output

    city_output_label = ttk.Label(teacher_info_frame, text='Miasto', font=('Open Sans', 12), bootstyle='default')
    city_output_label.grid(row=11, column=3, sticky='w')

    city_output = ttk.Entry(teacher_info_frame, bootstyle='default', state='readonly', width=20)
    city_output.configure(state=f'{disabled_state}')
    city_output.grid(row=12, column=3, sticky='w')

    ## postal_code_output

    postal_code_output_label = ttk.Label(teacher_info_frame, text='Kod pocztowy', font=('Open Sans', 12),
                                         bootstyle='default')
    postal_code_output_label.grid(row=11, column=4, sticky='w')

    postal_code_output = ttk.Entry(teacher_info_frame, bootstyle='default', state='readonly', width=15)
    postal_code_output.configure(state=f'{disabled_state}')
    postal_code_output.grid(row=12, column=4, sticky='w')

    ## country_output

    country_output_label = ttk.Label(teacher_info_frame, text='Państwo', font=('Open Sans', 12), bootstyle='default')
    country_output_label.grid(row=11, column=5, sticky='w')

    country_output = ttk.Entry(teacher_info_frame, bootstyle='default', state='readonly', width=25)
    country_output.configure(state=f'{disabled_state}')
    country_output.grid(row=12, column=5, sticky='w')

    ## email_output

    email_output_label = ttk.Label(teacher_info_frame, text='Adres e-mail', font=('Open Sans', 12), bootstyle='default')
    email_output_label.grid(row=14, column=0, sticky='w')

    email_output = ttk.Entry(teacher_info_frame, bootstyle='default', state='readonly', width=25)
    email_output.configure(state=f'{disabled_state}')
    email_output.grid(row=15, column=0, sticky='w')

    ## phone_number_output

    phone_number_output_label = ttk.Label(teacher_info_frame, text='Nr telefonu', font=('Open Sans', 12),
                                          bootstyle='default')
    phone_number_output_label.grid(row=14, column=2, sticky='w')

    phone_number_output = ttk.Entry(teacher_info_frame, bootstyle='default', state='readonly', width=25)
    phone_number_output.configure(state=f'{disabled_state}')
    phone_number_output.grid(row=15, column=2, sticky='w')

    ## personal_id_output

    personal_id_output_label = ttk.Label(teacher_info_frame, text='PESEL', font=('Open Sans', 12), bootstyle='default')
    personal_id_output_label.grid(row=14, column=3, sticky='w')

    personal_id_output = ttk.Entry(teacher_info_frame, bootstyle='default', state='readonly', width=25)
    personal_id_output.configure(state=f'{disabled_state}')
    personal_id_output.grid(row=15, column=3, sticky='w')

    ## document_no_output

    document_no_output_label = ttk.Label(teacher_info_frame, text='Nr dokumentu', font=('Open Sans', 12),
                                         bootstyle='default')
    document_no_output_label.grid(row=14, column=4, sticky='w')

    document_no_output = ttk.Entry(teacher_info_frame, bootstyle='default', state='readonly', width=25)
    document_no_output.configure(state=f'{disabled_state}')
    document_no_output.grid(row=15, column=4, sticky='w')

    ## document_type_output

    document_type_output_label = ttk.Label(teacher_info_frame, text='Rodzaj dokumentu', font=('Open Sans', 12),
                                           bootstyle='default')
    document_type_output_label.grid(row=14, column=5, sticky='w')

    document_type_output = ttk.Entry(teacher_info_frame, bootstyle='default', state='readonly', width=25)
    document_type_output.configure(state=f'{disabled_state}')
    document_type_output.grid(row=15, column=5, sticky='w')

    ## course_name_output

    course_name_output_label = ttk.Label(teacher_info_frame, text='Nazwa kursu', font=('Open Sans', 12),
                                         bootstyle='default')
    course_name_output_label.grid(row=17, column=0, sticky='w')

    course_name_output = ttk.Entry(teacher_info_frame, bootstyle='default', state='readonly', width=25)
    course_name_output.configure(state=f'{disabled_state}')
    course_name_output.grid(row=18, column=0, sticky='w')

    ## course_language_output

    course_language_output_label = ttk.Label(teacher_info_frame, text='Język kursu', font=('Open Sans', 12),
                                             bootstyle='default')
    course_language_output_label.grid(row=17, column=2, sticky='w')

    course_language_output = ttk.Entry(teacher_info_frame, bootstyle='default', state='readonly', width=25)
    course_language_output.configure(state=f'{disabled_state}')
    course_language_output.grid(row=18, column=2, sticky='w')

    ## status_output

    status_output_label = ttk.Label(teacher_info_frame, text='Status', font=('Open Sans', 12), bootstyle='default')
    status_output_label.grid(row=17, column=3, sticky='w')

    status_output = ttk.Entry(teacher_info_frame, bootstyle='default', state='readonly', width=25)
    status_output.configure(state=f'{disabled_state}')
    status_output.grid(row=18, column=3, sticky='w')

    ## level_output

    level_output_label = ttk.Label(teacher_info_frame, text='Poziom', font=('Open Sans', 12), bootstyle='default')
    level_output_label.grid(row=17, column=4, sticky='w')

    level_output = ttk.Entry(teacher_info_frame, bootstyle='default', state='readonly', width=25)
    level_output.configure(state=f'{disabled_state}')
    level_output.grid(row=18, column=4, sticky='w')

    ## mode_output

    mode_output_label = ttk.Label(teacher_info_frame, text='Tryb', font=('Open Sans', 12), bootstyle='default')
    mode_output_label.grid(row=17, column=5, sticky='w')

    mode_output = ttk.Entry(teacher_info_frame, bootstyle='default', state='readonly', width=25)
    mode_output.configure(state=f'{disabled_state}')
    mode_output.grid(row=18, column=5, sticky='w')

    ## start_date_output

    start_date_output_label = ttk.Label(teacher_info_frame, text='Data rozpoczęcia', font=('Open Sans', 12),
                                        bootstyle='default')
    start_date_output_label.grid(row=20, column=2, sticky='w')

    start_date_output = ttk.DateEntry(teacher_info_frame, bootstyle='primary')
    start_date_output.configure(state=f'{disabled_state}')
    start_date_output.grid(row=21, column=2, sticky='w')

    ## end_date_output

    end_date_output_label = ttk.Label(teacher_info_frame, text='Data zakończenia', font=('Open Sans', 12),
                                      bootstyle='default')
    end_date_output_label.grid(row=20, column=4, sticky='w')

    end_date_output = ttk.DateEntry(teacher_info_frame, bootstyle='primary')
    end_date_output.configure(state=f'{disabled_state}')
    end_date_output.grid(row=21, column=4, sticky='w')

    ## edit button
    """
    When clicked, the entries change status from readonly to editable. 
    """

    edit_button_style = ttk.Style()
    edit_button_style.configure('primary.TButton', font=('Open Sans', 15))

    edit_button = ttk.Button(teacher_info_frame, bootstyle='primary', text='EDYTUJ', width=15, style='primary.TButton',
                             state=f'{disabled_state}')
    edit_button.grid(row=24, column=2, sticky='w')

    ## save_button

    save_button = ttk.Button(teacher_info_frame, bootstyle='info', text='ZAPISZ', width=16, state=f'{disabled_state}')
    save_button.grid(row=24, column=3, sticky='w')

    ## block_button

    block_button_style = ttk.Style()
    block_button_style.configure('warning.TButton', font=('Open Sans', 15))

    block_button = ttk.Button(teacher_info_frame, bootstyle='warning', text='ZABLOKUJ', width=15,
                              state=f'{disabled_state}')
    block_button.grid(row=24, column=4, sticky='w')

    ## cancel_button - sets entries back to the readonly state and buttons do disabled state, including itself

    cancel_button_style = ttk.Style()
    cancel_button_style.configure('danger.TButton', font=('Open Sans', 15))

    cancel_button = ttk.Button(teacher_info_frame, bootstyle='danger', text='ODRZUĆ', width=15,
                               state=f'{disabled_state}')
    cancel_button.grid(row=26, column=3, sticky='w')

    teacher_info_frame.pack()