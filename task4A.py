# Filename: task4A.py
# Authors: Eni Mustafaraj & Minjia Wu
# Date: April 2, 2016
# Purpose: Given a nested dictionary, generate a flat-structured dictionary. 


import json
scheduleByYear = json.load(open('wellesley_courses.json', 'r'))

def createCoursesDictionary(scheduleByYear):
    """ Given a deeply nested dictionary where data is organized in: 
    
        years:
           semesters within years: Fall, Spring
              programs within semesters: departments
                 courses within programs:
                     enrollment size within courses
        
        return a flatly-structured dictionary of course titles, organized as
    
        crsNumber: [
            {'enrollment': val, 'program': val, 'semester': val, 'year': val}, 
            ...
        ]
        Remember that dictionaries are collections and the way they are printed
        doesn't reflect the order in which key/value pairs were added to it.
    """
    newDict = {}
    for courses in linesFromFile(scheduleByYear):
        newDict[courses] = []
    return newDict 



#Helper functions
#Will yield the all the individual courses
def linesFromFile(scheduleByYear):
    courseList = []
    for key, val in scheduleByYear.items(): #val gets us the semester (Fall,Spring)
        for key2, val2 in val.items(): #val2 gets us the department (i.e. MUS)
            for key3, val3 in val2.items(): #val3 gets us the course as the key, the enrollment as the val, but only for that year and only for that semester
                #print val3
                for key4, val4 in val3.items(): #key4 will yield individual courses, val4 will yield enrollment: enrollment number 
                    if key4 not in courseList:
                        courseList.append(key4)

    return courseList
                    

#coursesDct = createCoursesDictionary(scheduleByYear)
    
                                        
# DO NOT MODIFY THIS CODE HERE. Run your file as normally.   
         
if __name__ == '__main__':  
    # 1. Invoke function to get the result
    coursesDct = createCoursesDictionary(scheduleByYear)
    
    # 2. Store the dictionary in a file
    json.dump(coursesDct, open("courses_studentSolution.json", "w"))
    
    # 3. Load staff solution
    solutionDct = json.load(open('courses_staffSolution.json'))
    
    # 4. Test the solution 
    if coursesDct != None:
        if sorted(solutionDct) == sorted(coursesDct):
            print "\nRESULT: Your solution is correct."
    else:
        print "\nRESULT: You aren't there yet."
    
    