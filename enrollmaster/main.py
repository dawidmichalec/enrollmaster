from tkinter import *
import ttkbootstrap as ttk
from new_student_frame import NewStudentFrame
from student_info_frame import StudentInfoFrame
from create_course_frame import CreateCourseFrame
from edit_course_frame import EditCourseFrame
from course_info_frame import CourseInfoFrame
from add_a_teacher_frame import AddATeacherFrame
from teacher_info_frame import TeacherInfoFrame
from search_payment_frame import SearchPaymentFrame
from edit_payment_frame import EditPaymentFrame
from generate_report_frame import GenerateReportFrame

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
Function that switches to new student creation frame.
"""
def new_student_switch():
    delete_pages()
    new_student_frame = NewStudentFrame(main_frame, amend_menu_content)


"""
Function that switches to the information about student.
"""
def student_info_switch():
    delete_pages()
    student_info_frame = StudentInfoFrame(main_frame, amend_menu_content)


"""
Function that switches to course creation frame. 
"""
def create_course_switch():
    delete_pages()
    create_course_frame = CreateCourseFrame(main_frame, amend_menu_content)


"""
Function that switches to edit course frame.
"""
def edit_course_switch():
    delete_pages()
    edit_course_frame = EditCourseFrame(main_frame, amend_menu_content)


"""
Function that switches to course information frame.
"""
def course_info_switch():
    delete_pages()
    course_info_frame = CourseInfoFrame(main_frame, amend_menu_content)


"""
Function that switches to add a teacher frame. 
"""
def add_a_teacher_switch():
    delete_pages()
    add_a_teacher_frame = AddATeacherFrame(main_frame, amend_menu_content)


"""
Function that switches to teacher_info frame.
"""
def teacher_info_switch():
    delete_pages()
    teacher_info_frame = TeacherInfoFrame(main_frame, amend_menu_content)


"""
Function that switches to search_payment frame.
"""
def search_payment_switch():
    delete_pages()
    search_payment_frame = SearchPaymentFrame(main_frame, amend_menu_content)


"""
Function that switches to edit_payment frame.
"""
def edit_payment_switch():
    delete_pages()
    edit_payment_frame = EditPaymentFrame(main_frame, amend_menu_content)


"""
Function that switches to generate_report frame. 
"""
def generate_report_switch():
    delete_pages()
    generate_report_frame = GenerateReportFrame(main_frame, amend_menu_content)


"""
Function that changes the default text in the Menubuttons.
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

edit_course =ttk.Button(text='EDYTUJ KURS', bootstyle='info', width=22, command=lambda: edit_course_switch())
edit_course.place(x=10, y=331)

course_info = ttk.Button(text='INFORMACJE O KURSACH', bootstyle='info', width=22, command=lambda: course_info_switch())
course_info.place(x=10, y=369)

teachers = ttk.Button(text='NAUCZYCIELE', bootstyle='light-outline', width=22, style='light.Outline.TButton', state='disabled')
teachers.place(x=10, y=407)

add_a_teacher = ttk.Button(text='DODAJ NAUCZYCIELA', bootstyle='info', width=22, command=lambda: add_a_teacher_switch())
add_a_teacher.place(x=10, y=445)

teacher_info = ttk.Button(text='WYSZUKAJ NAUCZYCIELA', bootstyle='info', width=22, command=lambda: teacher_info_switch())
teacher_info.place(x=10, y=483)

payments = ttk.Button(text='PŁATNOŚCI', bootstyle='light-outline', width=22, style='light.Outline.TButton', state='disabled')
payments.place(x=10, y=521)

search_payment = ttk.Button(text='WYSZUKAJ PŁATNOŚĆ', bootstyle='info', width=22, command=lambda: search_payment_switch())
search_payment.place(x=10, y=559)

edit_payment = ttk.Button(text='EDYTUJ PŁATNOŚĆ', bootstyle='info', width=22, command=lambda: edit_payment_switch())
edit_payment.place(x=10, y=597)

generate_report = ttk.Button(text='WYGENERUJ RAPORT', bootstyle='info', width=22, command=lambda: generate_report_switch())
generate_report.place(x=10, y=635)


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
