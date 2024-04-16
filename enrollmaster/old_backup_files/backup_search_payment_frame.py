search_payment_frame = ttk.Frame(main_frame)

search_payment_frame.columnconfigure((0, 1, 2, 3, 4), weight=1, minsize=250)
search_payment_frame.rowconfigure(
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28),
    weight=1, minsize=30)

## search_payment_label

search_payment_label = ttk.Label(search_payment_frame, text='WYSZUKAJ PŁATNOŚĆ', font=('Open Sans', 14, 'bold'),
                              bootstyle='default')
search_payment_label.grid(row=0, column=2)

## student_id

student_id_label = ttk.Label(search_payment_frame, text='ID ucznia', font=('Open Sans', 12), bootstyle='default')
student_id_label.grid(row=2, column=0, sticky='w')

student_id_entry = ttk.Entry(search_payment_frame, bootstyle='light', width=20)
student_id_entry.grid(row=3, column=0, sticky='w')

## student_first_name

student_first_name_label = ttk.Label(search_payment_frame, text='Imię ucznia', font=('Open Sans', 12),
                                     bootstyle='default')
student_first_name_label.grid(row=2, column=1, sticky='w')

student_first_name_entry = ttk.Entry(search_payment_frame, bootstyle='light', width=20)
student_first_name_entry.grid(row=3, column=1, sticky='w')

## student_last_name

student_last_name_label = ttk.Label(search_payment_frame, text='Nazwisko ucznia', font=('Open Sans', 12),
                                    bootstyle='default')
student_last_name_label.grid(row=2, column=2, sticky='w')

student_last_name_entry = ttk.Entry(search_payment_frame, bootstyle='light', width=20)
student_last_name_entry.grid(row=3, column=2, sticky='w')

## course_id

course_id_label = ttk.Label(search_payment_frame, text='ID kursu', font=('Open Sans', 12),
                            bootstyle='default')
course_id_label.grid(row=2, column=3, sticky='w')

course_id_entry = ttk.Entry(search_payment_frame, bootstyle='light', width=20)
course_id_entry.grid(row=3, column=3, sticky='w')

## course_name

course_name_label = ttk.Label(search_payment_frame, text='Nazwa kursu', bootstyle='default', font=('Open Sans', 12))
course_name_label.grid(row=2, column=4, sticky='w')

course_name_entry = ttk.Entry(search_payment_frame, bootstyle='light', width=20)
course_name_entry.grid(row=3, column=4, sticky='w')

## date_due

date_due_label = ttk.Label(search_payment_frame, text='Termin płatności', font=('Open Sans', 12),
                            bootstyle='default')
date_due_label.grid(row=5, column=0, sticky='w')

date_due_entry = ttk.DateEntry(search_payment_frame, bootstyle='default')
date_due_entry.grid(row=6, column=0, sticky='w')

## amount

amount_label = ttk.Label(search_payment_frame, text='Cena', font=('Open Sans', 12), bootstyle='default')
amount_label.grid(row=5, column=1, sticky='w')

amount_entry = ttk.Entry(search_payment_frame, bootstyle='light', width=20)
amount_entry.grid(row=6, column=1, sticky='w')

## payment_status

payment_status_label = ttk.Label(search_payment_frame, text='Status płatności', font=('Open Sans', 12), bootstyle='default')
payment_status_label.grid(row=5, column=2, sticky='w')

payment_status = ttk.Menubutton(search_payment_frame, bootstyle='dark', text='Wybierz status')
payment_status.grid(row=6, column=2, sticky='w')

payment_status_content = ttk.Menu(payment_status)
status_var = StringVar()

for x in ['Do zapłaty', 'Zaległość', 'Zapłacone']:
    payment_status_content.add_radiobutton(label=x, variable=status_var,
                                                      command=lambda x=x: amend_menu_content(
                                                          payment_status, x))

payment_status['menu'] = payment_status_content


## submit button

submit_button_style = ttk.Style()
submit_button_style.configure('success.TButton', font=('Open Sans', 16))

submit_button = ttk.Button(search_payment_frame, bootstyle='success', text='SZUKAJ', width=13,
                           style='success.TButton')
submit_button.grid(row=8, column=2, sticky='w')


## output label

output_label = ttk.Label(search_payment_frame, font=('Open Sans',12), bootstyle='default', text='asdfasdf')
output_label.grid(row=11, column=2, sticky='w')

search_payment_frame.pack()