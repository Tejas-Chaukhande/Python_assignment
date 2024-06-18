"""
Assignment-1:
WAP to create a one student info in dictionary. Dictionary should contain
'student_name, age, roll_no, class, section, percentage, college_name' student data.
Retrieve the student percentage from the dictionary.
"""
student_info={'student_name':'Tejas',
              'age':23,
              'roll_no':52,
              'class':12,
              'section':'A',
              'percentage':87,
              'college_name':'Pote Patil college'
              }
print(student_info['percentage'])
#-----------------------------------------------------------------------------------------------------------
"""
Assignment-2:
WAP to create a 3 students info in dictionary. Dictionary should contain 3 students data with 'student_names,
ages, roll_nos, classes, sections, percentages, university_names' keys. values can be stored in list/tuple.
Retrieve the student_3 class from the dictionary.
"""
student_info1={'student_names':["Tejas","sanket","Ajay"],
               'ages':[23,24,25],
               'roll_nos':[51,61,71],
               'classes':[10,11,12],
               'sections':['A','B','C'],
               'percentages':[88,97,67],
               'university_names':['Maratha University','Amravati University','Nagpur University']
               }


print(student_info1['classes'][2])

#-----------------------------------------------------------------------------------------------------------

"""
Assignment-3:
WAP to create a 4 employees data in a nested dictionary.
Dictionary should contain 4 employees data, each employee data should be represented in a dictionary
Each sub dictionary should have 'employee_name,salary,Designation' keys.
Retrieve the 3rd employee designation from the nested dictionary.
"""
employees_data={'emp1':{'employee_name':'Arjun','salary':25000,'Designation':'Software Eng'},
                'emp2':{'employee_name':'Saket','salary':35000,'Designation':'Embedded Eng'},
                'emp3':{'employee_name':'Paven','salary':40000,'Designation':'Firmware Eng'}
                }

print(employees_data['emp3']['Designation'])
