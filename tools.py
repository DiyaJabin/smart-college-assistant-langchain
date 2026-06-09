from langchain_core.tools import tool
from students import student_list

@tool
def attendance_calculator(total_classes:int,attended_classes:int)->str:
    """Use to calculate attendance from total classes and number of attended classes"""
    attendance_percentage=(attended_classes/total_classes)*100
    if attendance_percentage>=75:
        status="Eligible for exam"
    else:
        status="Not eligible for exam"
    return f"Attendance: {attendance_percentage:.2f}% | Status: {status}\n"

@tool
def result_calculator(marks: list[float])->str:
    """Use to calculate average marks, grade and pass/fail status"""
    average_marks=sum(marks)/len(marks)
    if average_marks>=90:
        grade='A'
    elif average_marks>=75:
        grade='B'
    elif average_marks>=60:
        grade='C'
    else:
        grade='D'

    status="pass" if average_marks>=50 else "fail"

    return f"Average marks: {average_marks:.2f}% Grade: {grade} | Status: {status}\n"

@tool
def fee_balance_calculator(total_fee: float, amount_paid: float)->str:
    """Use to calculate the fee balance after paying hostel fees"""
    return f"Pending fees: ₹{total_fee-amount_paid:.2f}\n"

@tool
def library_fine_calculator(delayed_days: int)->str:
    """Use to calculate the library fine from number of delayed days"""
    return f"Library Fine: ₹{delayed_days*5}\n"

@tool
def hostel_fee_calculator(monthly_fee: float,months_stayed:int)->str:
    """Use to calculate the hostel fee from number of months stayed and monthly fee """
    return f"Hostel fee: ₹{monthly_fee*months_stayed:.2f}\n"

@tool
def student_info_tool(student_id:str)->str:
    """Use to retrieve student info from given student id"""
    if student_id in student_list:
        student=student_list[student_id]
        return (f"Student ID: {student_id} | Name: {student['name']} | "
                f" Scores: {student['scores']} | Average Score: {student['average']} |"
                f"Grade: {student['grade']} | Status: {student['status']}\n")
    else:
        return f"Student with student id : {student_id} not found\n"

tool_list=[
    attendance_calculator,
    result_calculator,
    fee_balance_calculator,
    library_fine_calculator,
    hostel_fee_calculator,
    student_info_tool
]