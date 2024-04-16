from tkinter import *
import ttkbootstrap as ttk
from datetime import datetime, timedelta

class NewStudentFrame(ttk.Frame):

    def __init__(self, master=None, amend_menu_content_func=None, **kw):
        super().__init__(master, **kw)
        self.amend_menu_content_func = amend_menu_content_func
        self.columnconfigure((0, 2, 3, 4, 5), weight=1, minsize=250)
        self.columnconfigure(1, weight=1, minsize=50)
        self.rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28),
            weight=1, minsize=30)

        new_student_label = ttk.Label(self, text="NOWY UCZEŃ", font=('Open Sans', 14, 'bold'),
                                      bootstyle='default')
        new_student_label.grid(column=3, row=0, sticky='w')

        ## first_name

        first_name_label = ttk.Label(self, text="Imię", font=('Open Sans', 12), bootstyle='default')
        first_name_label.grid(row=2, column=0, sticky='w')

        first_name = ttk.Entry(self, width=30, bootstyle='light')
        first_name.grid(row=3, column=0)

        ## last_name

        last_name_label = ttk.Label(self, text="Nazwisko", font=('Open Sans', 12), bootstyle='default')
        last_name_label.grid(row=2, column=2, sticky='w')

        last_name = ttk.Entry(self, width=30, bootstyle='light')
        last_name.grid(row=3, column=2)

        ## street

        street_label = ttk.Label(self, text='Ulica', font=('Open Sans', 12), bootstyle='default')
        street_label.grid(row=5, column=0, sticky='w')

        street = ttk.Entry(self, width=30, bootstyle='light')
        street.grid(row=6, column=0)

        ## building_no

        building_no_label = ttk.Label(self, text='Nr domu', font=('Open Sans', 12), bootstyle='default')
        building_no_label.grid(row=5, column=2, sticky='w')

        building_no = ttk.Entry(self, width=10, bootstyle='light')
        building_no.grid(row=6, column=2, sticky='w')

        ## local_no

        local_no_label = ttk.Label(self, text='Nr lokalu', font=('Open Sans', 12), bootstyle='default')
        local_no_label.grid(row=5, column=3, sticky='w')

        local_no = ttk.Entry(self, width=10, bootstyle='light')
        local_no.grid(row=6, column=3, sticky='w')

        ## city

        city_label = ttk.Label(self, text="Miasto", font=('Open Sans', 12), bootstyle='default')
        city_label.grid(row=8, column=0, sticky='w')

        city = ttk.Entry(self, width=30, bootstyle='light')
        city.grid(row=9, column=0, sticky='w')

        ## postal_code

        postal_code_label = ttk.Label(self, text="Kod pocztowy", font=('Open Sans', 12),
                                      bootstyle='default')
        postal_code_label.grid(row=8, column=2, sticky='w')

        postal_code = ttk.Entry(self, width=15, bootstyle='light')
        postal_code.grid(row=9, column=2, sticky='w')

        ## country

        country_label = ttk.Label(self, text="Państwo", font=('Open Sans', 12), bootstyle='default')
        country_label.grid(row=8, column=3, sticky='w')

        country = ttk.Entry(self, width=30, bootstyle='light')
        country.grid(row=9, column=3, sticky='w')

        ## email

        email_label = ttk.Label(self, text="Adres e-mail", font=('Open Sans', 12), bootstyle='default')
        email_label.grid(row=11, column=0, sticky='w')

        email = ttk.Entry(self, width=30, bootstyle='light')
        email.grid(row=12, column=0, sticky='w')

        ## phone number

        phone_number_label = ttk.Label(self, text="Nr telefonu", font=('Open Sans', 12),
                                       bootstyle='default')
        phone_number_label.grid(row=11, column=2, sticky='w')

        phone_number = ttk.Entry(self, width=20, bootstyle='light')
        phone_number.grid(row=12, column=2, sticky='w')

        ## personal id

        personal_id_label = ttk.Label(self, text="PESEL", font=('Open Sans', 12), bootstyle='default')
        personal_id_label.grid(row=14, column=0, sticky='w')

        personal_id = ttk.Entry(self, width=20, bootstyle='light')
        personal_id.grid(row=15, column=0, sticky='w')

        ## document_no

        document_no_label = ttk.Label(self, text="Nr dokumentu", font=('Open Sans', 12),
                                      bootstyle='default')
        document_no_label.grid(row=14, column=2, sticky='w')

        document_no = ttk.Entry(self, width=20, bootstyle='light')
        document_no.grid(row=15, column=2, sticky='w')

        ## document_type

        document_type_label = ttk.Label(self, text="Rodzaj dokumentu", font=('Open Sans', 12),
                                        bootstyle='default')
        document_type_label.grid(row=14, column=3, sticky='w')

        self.document_type = ttk.Menubutton(self, bootstyle='dark', text="Wybierz dokument")
        self.document_type.grid(row=15, column=3, sticky='w')

        document_type_content = ttk.Menu(self.document_type)

        self.document_var = ttk.StringVar()
        self.document_var.set("Dowód osobisty")

        for document in ['Dowód osobisty', 'Paszport', 'Karta pobytu']:
            document_type_content.add_radiobutton(label=document, variable=self.document_var, value=document,
                                                  command=self.on_document_type_select)

        self.document_type['menu'] = document_type_content

        ## language

        language_label = ttk.Label(self, text="Język kursu", font=('Open Sans', 12), bootstyle='default')
        language_label.grid(row=17, column=0, sticky='w')

        self.language_dropdown = ttk.Menubutton(self, bootstyle='dark', text="Wybierz język")
        self.language_dropdown.grid(row=18, column=0, sticky='w')

        language_dropdown_content = ttk.Menu(self.language_dropdown)

        self.language_var = ttk.StringVar()
        self.language_var.set("Angielski")

        for language in ['Angielski', 'Niemiecki', 'Francuski', 'Włoski', 'Hiszpański']:
            language_dropdown_content.add_radiobutton(label=language, variable=self.language_var, value=language,
                                                      command=self.on_language_select)

        self.language_dropdown['menu'] = language_dropdown_content

        ## level

        level_label = ttk.Label(self, text="Poziom", font=('Open Sans', 12), bootstyle='default')
        level_label.grid(row=17, column=2, sticky='w')

        self.level_dropdown = ttk.Menubutton(self, bootstyle='dark', text="Wybierz poziom")
        self.level_dropdown.grid(row=18, column=2, sticky='w')

        level_dropdown_content = ttk.Menu(self.level_dropdown)

        self.level_var = StringVar()
        self.level_var.set("Początkujący")

        for level in ['Początkujący', 'Zaawansowany']:
            level_dropdown_content.add_radiobutton(label=level, variable=self.level_var, value=level,
                                                   command=self.on_level_select)

        self.level_dropdown['menu'] = level_dropdown_content

        ## mode

        mode_label = ttk.Label(self, text="Tryb", font=('Open Sans', 12), bootstyle='default')
        mode_label.grid(row=17, column=3, sticky='w')

        self.mode_dropdown = ttk.Menubutton(self, bootstyle='dark', text="Wybierz tryb")
        self.mode_dropdown.grid(row=18, column=3, sticky='w')

        mode_dropdown_content = ttk.Menu(self.mode_dropdown)

        self.mode_var = StringVar()
        self.mode_var.set("Normalny")

        for mode in ['Normalny', 'Przyspieszony']:
            mode_dropdown_content.add_radiobutton(label=mode, variable=self.mode_var, value=mode,
                                                  command=self.on_mode_select)

        self.mode_dropdown['menu'] = mode_dropdown_content

        ## course

        course_label = ttk.Label(self, text="Wybierz dostępny kurs", font=('Open Sans', 12),
                                 bootstyle='default')
        course_label.grid(row=17, column=4, sticky='w')

        course_dropdown = ttk.Menubutton(self, bootstyle='dark', text="Wybierz kurs")
        course_dropdown.grid(row=18, column=4, sticky='w')

        course_dropdown_content = ttk.Menu(course_dropdown)

        course_var = StringVar()

        ## start_date

        start_date_label = ttk.Label(self, text="Data rozpoczęcia", font=('Open Sans', 12),
                                     bootstyle='default')
        start_date_label.grid(row=20, column=0, sticky='w')

        start_date_entry = ttk.DateEntry(self, bootstyle='primary')
        start_date_entry.configure(state='readonly')
        start_date_entry.grid(row=21, column=0, sticky='w')

        ## end_date

        end_date_label = ttk.Label(self, text="Data zakończenia", font=('Open Sans', 12),
                                   bootstyle='default')
        end_date_label.grid(row=20, column=2, sticky='w')

        end_date_entry = ttk.DateEntry(self, bootstyle='primary')
        end_date_entry.configure(state='readonly')
        end_date_entry.grid(row=21, column=2, sticky='w')

        ## payment

        payment_label = ttk.Label(self, text="Płatność", font=('Open Sans', 12), bootstyle='default')
        payment_label.grid(row=20, column=3, sticky='w')

        self.payment_dropdown = ttk.Menubutton(self, bootstyle='dark', text="Wybierz sposób płatności")
        self.payment_dropdown.grid(row=21, column=3, sticky='w')

        payment_dropdown_content = ttk.Menu(self.payment_dropdown)

        self.payment_var = ttk.StringVar()
        self.payment_var.set("W placówce")  # Set default payment method

        for payment_method in ['W placówce', 'Przelew']:
            payment_dropdown_content.add_radiobutton(label=payment_method, variable=self.payment_var, value=payment_method,
                                                     command=self.on_payment_select)

        self.payment_dropdown['menu'] = payment_dropdown_content

        ## prize

        prize_label = ttk.Label(self, text="Cena", font=('Open Sans', 12), bootstyle='default')
        prize_label.grid(row=20, column=4, sticky='w')

        prize_var = ''

        prize_entry = ttk.Entry(self, bootstyle='default', width=15)
        prize_entry.insert('end', prize_var)
        prize_entry.configure(state='readonly')
        prize_entry.grid(row=21, column=4, sticky='w')

        ## submit

        submit_button_style = ttk.Style()
        submit_button_style.configure('success.TButton', font=('Open Sans', 16))

        submit_button = ttk.Button(self, bootstyle='success', text='ZAPISZ', width=20,
                                   style='success.TButton')
        submit_button.grid(row=24, column=3, sticky='w')

        self.pack()

    def on_document_type_select(self):
        selected_document_type = self.document_var.get()
        print("Selected document type:", selected_document_type)
        self.amend_menu_content_func(self.document_type, selected_document_type)
        return selected_document_type

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

    def on_payment_select(self):
        selected_payment_method = self.payment_var.get()
        print("Selected payment method:", selected_payment_method)
        self.amend_menu_content_func(self.payment_dropdown, selected_payment_method)
        return selected_payment_method
