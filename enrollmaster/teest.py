def on_language_to_teach_select():
    selected_language = mode_var.get()
    print("Selected mode:", selected_language)
    amend_menu_content(language_to_teach , selected_language)
    return selected_language

language_to_teach = ttk.Menubutton(add_a_teacher_frame, bootstyle='dark', text='Wybierz')
language_to_teach.grid(row=18, column=4, sticky='w')

language_to_teach_content = ttk.Menu(language_to_teach)

lang_var = StringVar()
lang_var.set("Angielski")
for language in ['Angielski', 'Niemiecki', 'Francuski', 'Włoski', 'Hiszpański']:
    language_to_teach_content.add_radiobutton(label=language, variable=lang_var, value=language,command=on_language_to_teach_select)

language_to_teach['menu'] = language_to_teach_content


