# def siblings(*sibling):
#     counting=len(sibling)
#     print('Your Siblings:')
#     for sblng in sibling:
#         print(sblng)
#     print(f'Total:{counting}')
# siblings('ayushi','gunjan','dhruv','aditi','rohan','sneha','komal','poonam','swati','pratibha','kuldeep','tanisha','vansh','rajan')

def student(subject,*students):
    print(f'Students in {subject} batch:')
    total=len(students)
    for student in students:
        print(student)
    print(f"Total Students:{total}")
student('Maths','Pulkit','Dhruv','Ashutosh','Sourav','Siya','Tanya','Vansh','Divyanshu','Anmol','Himanshi','Ziya','Pihu','Manu','abhishek')