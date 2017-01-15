#Header function that explains what will be passed in
def can_pass(hw,exam):
    '''Returns wheter a student passed the course 
    based on his/hers hw and exam grade
    
    (integer,integer)->string 
    REQ:0<=hw<=100
    REQ:0<=Exam<=100
    
    >>>can_pass(90,80)
    "Yay, you passed!"
    >>>can_pass(40,30)
    "Boo, your exam grade is below 40% and and final grade is below 50%"
    >>>can_pass(90,30)
    "No, youe exam grade is below 40%"    
    >>>can_pass(10,40)
    "No your final grade is below 50%"
    '''
    
    #calculate the  passing grade
    final_grade=hw*0.35+exam*0.65
    #decide on overall passing grade
    has_passing_grade =(final_grade>=50)
    #calculate Exam passing grade
    has_exam_grade=(exam>=40)
    #Calculate result 
    if has_exam_grade and has_exam_grade:
        result="Yes,Good Job"
    else:
        if(has_passing_grade)and(passing_exam):
            result="Yes, good job" 
        else:
            if not(has_passing_grade) or (passing_exam):
                result="No, exam grade below 50%"
            return result  

#These are my tests
print(can_pass(40,80))
print(can_pass(0,0))
print(can_pass(90,30))
print(can_pass(80,80))