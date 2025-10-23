import tkinter as tk
import sqlite3

# Basic GUI 
root = tk.Tk()
root.title('Student')
root.geometry('300x350')

# student id label and entry
label_id = tk.Label(root, text='Student ID')
label_id.pack(pady=(10,5))
entry_id = tk.Entry(root, width=25)
entry_id.pack()

# student name label and entry
label_name = tk.Label(root, text='Student Name')
label_name.pack(pady=(10,5))
entry_name = tk.Entry(root, width=25)
entry_name.pack()


# def print_student() function
def print_student():
    student_id = entry_id.get()
    student_name = entry_name.get()
    
    print('-'*30)
    print('Student ID: {}'.format(student_id))
    print('Student Name: {}'.format(student_name))
    print('-'*30)
    
# new print button
button_print = tk.Button(root, text='Print', command=print_student)
button_print.pack(pady=15)

# connect to database and build environment
conn = sqlite3.connect('student.db')
cursor = conn.cursor()


# def create_student() function
def create_student():
    student_id = entry_id.get()
    student_name = entry_name.get()
    
    cursor.execute('INSERT INTO DB_student (DB_student_id, DB_student_name) VALUES (?, ?)', (student_id, student_name))
    conn.commit()
    
    print('Student ID: {}'.format(student_id))
    print('Student Name: {}'.format(student_name))
    print('has been created Successfully!')

button_create = tk.Button(root, text='Create', command=create_student)
button_create.pack(pady=20)

# def overview_student() function
def overview_student():
    cursor.execute('SELECT * FROM DB_student')
    overview = cursor.fetchall()
    print(overview)    
# new overview button
button_overview = tk.Button(root, text='Overview', command=overview_student)
button_overview.pack(pady=25)


root.mainloop() # must be at the end of the codes

