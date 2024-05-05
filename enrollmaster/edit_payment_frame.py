from tkinter import *
import ttkbootstrap as ttk


class EditPaymentFrame(ttk.Frame):

    def __init__(self, master=None, amend_menu_content_func=None, **kw):
        super().__init__(master, **kw)
        self.amend_menu_content_func = amend_menu_content_func
        self.columnconfigure((0, 1, 2, 3, 4), weight=1, minsize=310)
        self.rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28),
            weight=1, minsize=30)

        ## variables
        free_state = ''
        disabled_state_button = 'disabled'
        disabled_state = 'disabled'

        payment_id_var = ''
        student_id_var = ''
        student_first_name_var = ''
        student_last_name_var = ''
        course_id_var = ''
        course_name_var = ''
        prize_var = ''
        payment_type_var = ''
        date_due_var = ''
        status_var = ''

        ## edit_payment label

        edit_payment_label = ttk.Label(self, text='EDYTUJ PŁATNOŚĆ', font=('Open Sans', 14, 'bold'),
                                       bootstyle='default')
        edit_payment_label.grid(row=0, column=2, sticky='w')

        ## payment_id

        payment_id_label = ttk.Label(self, text='ID płatności', font=('Open Sans', 12),
                                     bootstyle='default')
        payment_id_label.grid(row=2, column=2, sticky='w')

        payment_id_entry = ttk.Entry(self, bootstyle='light', width=24)
        payment_id_entry.grid(row=3, column=2, sticky='w')

        ## submit_button

        submit_button_style = ttk.Style()
        submit_button_style.configure('success.TButton', font=('Open Sans', 14))

        submit_button = ttk.Button(self, bootstyle='success', text='SZUKAJ', width=16,
                                   style='success.TButton')
        submit_button.grid(row=5, column=2, sticky='w')

        ## payment_id_output

        payment_id_output_label = ttk.Label(self, text='ID płatności', font=('Open Sans', 12),
                                            bootstyle='default')
        payment_id_output_label.grid(row=8, column=0, sticky='w')

        payment_id_entry_output = ttk.Entry(self, bootstyle='default', width=20)
        payment_id_entry_output.insert('end', payment_id_var)
        payment_id_entry_output.configure(state='readonly')
        payment_id_entry_output.grid(row=9, column=0, sticky='w')

        ## student_id_output

        student_id_label = ttk.Label(self, text='ID ucznia', font=('Open Sans', 12), bootstyle='default')
        student_id_label.grid(row=8, column=1, sticky='w')

        student_id_output = ttk.Entry(self, bootstyle='default', width=20)
        student_id_output.insert('end', student_id_var)
        student_id_output.configure(state='readonly')
        student_id_output.grid(row=9, column=1, sticky='w')

        ## student_first_name

        student_first_name_label = ttk.Label(self, text='Imię ucznia', font=('Open Sans', 12),
                                             bootstyle='default')
        student_first_name_label.grid(row=8, column=2, sticky='w')

        student_first_name_output = ttk.Entry(self, bootstyle='default', width=20)
        student_first_name_output.insert('end', student_first_name_var)
        student_first_name_output.configure(state='readonly')
        student_first_name_output.grid(row=9, column=2, sticky='w')

        ## student_last_name

        student_last_name_label = ttk.Label(self, text='Nazwisko ucznia', font=('Open Sans', 12),
                                            bootstyle='default')
        student_last_name_label.grid(row=8, column=3, sticky='w')

        student_last_name_output = ttk.Entry(self, bootstyle='default', width=20)
        student_last_name_output.insert('end', student_last_name_var)
        student_last_name_output.configure(state='readonly')
        student_last_name_output.grid(row=9, column=3, sticky='w')

        ## course_id

        course_id_output_label = ttk.Label(self, text='ID kursu', font=('Open Sans', 12),
                                           bootstyle='default')
        course_id_output_label.grid(row=8, column=4, sticky='w')

        course_id_output = ttk.Entry(self, bootstyle='default', width=20)
        course_id_output.insert('end', course_id_var)
        course_id_output.configure(state='readonly')
        course_id_output.grid(row=9, column=4, sticky='w')

        ## course_name

        course_name_label = ttk.Label(self, text='Nazwa kursu', font=('Open Sans', 12),
                                      bootstyle='default')
        course_name_label.grid(row=11, column=0, sticky='w')

        course_name_output = ttk.Entry(self, bootstyle='default', width=20)
        course_name_output.insert('end', course_name_var)
        course_name_output.configure(state='readonly')
        course_name_output.grid(row=12, column=0, sticky='w')

        ## prize

        prize_label = ttk.Label(self, text='Do zapłaty', font=('Open Sans', 12),
                                bootstyle='default')
        prize_label.grid(row=11, column=1, sticky='w')

        prize_output = ttk.Entry(self, bootstyle='default', width=20)
        prize_output.insert('end', prize_var)
        prize_output.configure(state='readonly')
        prize_output.grid(row=12, column=1, sticky='w')

        ## payment_type

        payment_type_label = ttk.Label(self, text="Sposób płatności", font=('Open Sans', 12),
                                       bootstyle='default')
        payment_type_label.grid(row=11, column=2, sticky='w')

        payment_dropdown = ttk.Menubutton(self, bootstyle='dark', text=f"{payment_type_var}")
        payment_dropdown.configure(state=disabled_state)
        payment_dropdown.grid(row=12, column=2, sticky='w')

        payment_dropdown_content = ttk.Menu(payment_dropdown)

        payment_var = StringVar()

        for x in ['W placówce', 'Przelew']:
            payment_dropdown_content.add_radiobutton(label=x, variable=payment_var,
                                                     command=lambda x=x: self.amend_menu_content_func(payment_dropdown, x))

        payment_dropdown['menu'] = payment_dropdown_content

        ## date_due

        date_due_label = ttk.Label(self, text='Termin zapłaty', font=('Open Sans', 12),
                                   bootstyle='default')
        date_due_label.grid(row=11, column=3, sticky='w')

        date_due_entry = ttk.Entry(self, bootstyle='default', width=20)
        date_due_entry.insert('end', date_due_var)
        date_due_entry.configure(state='readonly')
        date_due_entry.grid(row=12, column=3, sticky='w')

        ## payment_status

        payment_status_label = ttk.Label(self, text='Status płatności', font=('Open Sans', 12),
                                         bootstyle='default')
        payment_status_label.grid(row=11, column=4, sticky='w')

        payment_status = ttk.Menubutton(self, bootstyle='dark', text=f'{status_var}')
        payment_status.configure(state=disabled_state)
        payment_status.grid(row=12, column=4, sticky='w')

        payment_status_content = ttk.Menu(payment_status)
        status_var_1 = StringVar()

        for x in ['Do zapłaty', 'Zaległość', 'Zapłacone']:
            payment_status_content.add_radiobutton(label=x, variable=status_var_1,
                                                   command=lambda x=x: self.amend_menu_content_func(
                                                       payment_status, x))

        payment_status['menu'] = payment_status_content

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
