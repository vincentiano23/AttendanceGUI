import tkinter as tk
from tkinter import ttk, messagebox

# Data storage for attendance
attendance_data = {}

# Function to mark attendance
def mark_attendance():
    student_name = student_entry.get()
    attendance_status = attendance_var.get()

    if student_name == "":
        messagebox.showerror("Input Error", "Please enter a student's name")
        return

    attendance_data[student_name] = attendance_status
    attendance_label.config(text=f"Marked {student_name} as {attendance_status}")
    student_entry.delete(0, tk.END)

# Function to display the attendance report
def show_report():
    report_window = tk.Toplevel(root)
    report_window.title("Attendance Report")

    # Create a treeview widget for the report
    tree = ttk.Treeview(report_window, columns=("Name", "Status"), show="headings")
    tree.heading("Name", text="Student Name")
    tree.heading("Status", text="Attendance Status")
    
    for student, status in attendance_data.items():
        tree.insert("", tk.END, values=(student, status))

    tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Add a button to close the report
    close_btn = tk.Button(report_window, text="Close", command=report_window.destroy)
    close_btn.pack(pady=10)

# Function to reset attendance
def reset_attendance():
    global attendance_data
    attendance_data.clear()
    attendance_label.config(text="Attendance Reset")
    messagebox.showinfo("Reset", "Attendance has been reset.")

# Create the main window
root = tk.Tk()
root.title("Attendance System")
root.geometry("500x400")
root.configure(bg="#F3F4F6")

# Header
header_label = tk.Label(root, text="Attendance System", font=("Helvetica", 20, "bold"), fg="#4B5563", bg="#F3F4F6")
header_label.pack(pady=20)

# Student Entry Frame
entry_frame = tk.Frame(root, bg="#F3F4F6")
entry_frame.pack(pady=10)

student_label = tk.Label(entry_frame, text="Student Name:", font=("Helvetica", 12), bg="#F3F4F6", fg="#1F2937")
student_label.grid(row=0, column=0, padx=5)

student_entry = tk.Entry(entry_frame, width=30, font=("Helvetica", 12), bd=2, relief="solid")
student_entry.grid(row=0, column=1, padx=5)

# Attendance Options
attendance_var = tk.StringVar(value="Present")

present_radio = tk.Radiobutton(root, text="Present", variable=attendance_var, value="Present", font=("Helvetica", 12), bg="#F3F4F6")
absent_radio = tk.Radiobutton(root, text="Absent", variable=attendance_var, value="Absent", font=("Helvetica", 12), bg="#F3F4F6")

present_radio.pack(pady=5)
absent_radio.pack(pady=5)

# Buttons Frame
button_frame = tk.Frame(root, bg="#F3F4F6")
button_frame.pack(pady=20)

mark_btn = tk.Button(button_frame, text="Mark Attendance", command=mark_attendance, font=("Helvetica", 12), bg="#10B981", fg="white", width=15)
mark_btn.grid(row=0, column=0, padx=10)

report_btn = tk.Button(button_frame, text="View Report", command=show_report, font=("Helvetica", 12), bg="#3B82F6", fg="white", width=15)
report_btn.grid(row=0, column=1, padx=10)

reset_btn = tk.Button(button_frame, text="Reset", command=reset_attendance, font=("Helvetica", 12), bg="#EF4444", fg="white", width=15)
reset_btn.grid(row=1, column=0, columnspan=2, pady=10)

# Attendance Label
attendance_label = tk.Label(root, text="", font=("Helvetica", 12, "italic"), fg="#6B7280", bg="#F3F4F6")
attendance_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
