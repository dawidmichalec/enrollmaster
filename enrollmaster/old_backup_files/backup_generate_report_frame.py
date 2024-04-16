generate_report_frame = ttk.Frame(main_frame)

generate_report_frame.columnconfigure((0, 1, 2, 3, 4), weight=1, minsize=250)
generate_report_frame.rowconfigure(
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28),
    weight=1, minsize=30)

generate_report_label = ttk.Label(generate_report_frame, text='WYGENERUJ RAPORT', font=('Open Sans', 14, 'bold'),
                              bootstyle='default')
generate_report_label.grid(row=0, column=2, sticky='w')

## start_date

start_date_label = ttk.Label(generate_report_frame, text='Data od', bootstyle='default', font=('Open Sans', 12))
start_date_label.grid(row=2, column=0, sticky='w')

start_date_entry = ttk.DateEntry(generate_report_frame, bootstyle='primary')
start_date_entry.grid(row=3, column=0, sticky='w')

## end_date

end_date_label = ttk.Label(generate_report_frame, text='Data do', bootstyle='default', font=('Open Sans', 12))
end_date_label.grid(row=2, column=1, sticky='w')

end_date_entry = ttk.DateEntry(generate_report_frame, bootstyle='primary')
end_date_entry.grid(row=3, column=1, sticky='w')

## language

course_language_label = ttk.Label(generate_report_frame, text="Język kursu", font=('Open Sans', 12),
                                  bootstyle='default')
course_language_label.grid(row=2, column=2, sticky='w')

course_language_dropdown = ttk.Menubutton(generate_report_frame, bootstyle='dark', text="Wybierz język")
course_language_dropdown.grid(row=3, column=2, sticky='w')

course_language_dropdown_content = ttk.Menu(course_language_dropdown)

course_language_var = StringVar()
for x in ['Angielski', 'Niemiecki', 'Francuski', 'Włoski', 'Hiszpański']:
    course_language_dropdown_content.add_radiobutton(label=x, variable=course_language_var,
                                                     command=lambda x=x: amend_menu_content(
                                                         course_language_dropdown, x))

course_language_dropdown['menu'] = course_language_dropdown_content

## payment_status

payment_status_label = ttk.Label(generate_report_frame, text='Status płatności', font=('Open Sans', 12),
                                 bootstyle='default')
payment_status_label.grid(row=2, column=3, sticky='w')

payment_status = ttk.Menubutton(generate_report_frame, bootstyle='dark', text='Wybierz status')
payment_status.grid(row=3, column=3, sticky='w')

payment_status_content = ttk.Menu(payment_status)
status_var_1 = StringVar()

for x in ['Do zapłaty', 'Zaległość', 'Zapłacone']:
    payment_status_content.add_radiobutton(label=x, variable=status_var_1,
                                           command=lambda x=x: amend_menu_content(
                                               payment_status, x))

payment_status['menu'] = payment_status_content

## payment_type

payment_type_label = ttk.Label(generate_report_frame, text="Sposób płatności", font=('Open Sans', 12),
                               bootstyle='default')
payment_type_label.grid(row=2, column=4, sticky='w')

payment_dropdown = ttk.Menubutton(generate_report_frame, bootstyle='dark', text="Wybierz sposób płatności")
payment_dropdown.grid(row=3, column=4, sticky='w')

payment_dropdown_content = ttk.Menu(payment_dropdown)

payment_var = StringVar()

for x in ['W placówce', 'Przelew']:
    payment_dropdown_content.add_radiobutton(label=x, variable=payment_var,
                                             command=lambda x=x: amend_menu_content(payment_dropdown, x))

payment_dropdown['menu'] = payment_dropdown_content

## submit_button

submit_button_style = ttk.Style()
submit_button_style.configure('success.TButton', font=('Open Sans', 16))

submit_button = ttk.Button(generate_report_frame, bootstyle='success', text='SZUKAJ', width=13,
                           style='success.TButton')
submit_button.grid(row=6, column=2, sticky='w')

## export_button

export_button_style = ttk.Style()
export_button_style.configure('primary.TButton', font=('Open Sans', 15))

export_button = ttk.Button(generate_report_frame, bootstyle='primary', text='CSV', width=13, style='primary.TButton')
export_button.grid(row=6, column=3, sticky='w')

## output_label

output_label = ttk.Label(generate_report_frame, font=('Open Sans', 12), bootstyle='default', text='asdfasdf')
output_label.grid(row=9, column=2, sticky='w')



generate_report_frame.pack()