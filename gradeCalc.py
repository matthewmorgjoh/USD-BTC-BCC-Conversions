# BIO 181 Grade Cruncher

def bioAvg():

    grades = {
            'tests': [80, 84, 80, 88],
            'final': [86],
            'labs' : [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
            'inclass' : [86],
            'mastering' : [100]
              }


    def average():
        testicles = grades['tests'][0:]
        testAverage = ((sum(testicles))/len(testicles))
        testWeight = testAverage * 0.40

        finalExam = grades['final'][0:]
        finalAvg = ((sum(finalExam))/len(finalExam))
        finalWeight = finalAvg * 0.15

        labs = grades['labs']
        labAvg = ((sum(labs))/len(labs))
        labWeight = labAvg * 0.25

        mastering = grades['mastering']
        masteringAvg = ((sum(mastering))/len(mastering))
        masteringWeight = masteringAvg * 0.10

        attendance = grades['inclass']
        attendanceAvg = ((sum(attendance))/len(attendance))
        attendanceWeight = attendanceAvg * 0.10

        finalAverage = testWeight + finalWeight + labWeight + attendanceWeight + masteringWeight

        return finalAverage

    avg = average()
    print()
    print('Final BIO grade is ' + str(avg) + '.\n')
    #print(avg)




bioAvg()




# CSC 120 Grade Cruncher

def cscAvg():

    grades = {
        'tests': [64.38, 83.33],
        'final': [90],
        'labs':[74],
        # 'homework': [94, 95.24, 97.1, 97.7, 96.6, 97.8, 95.5],
        'homework' : [85]
    }



    def average():
        testicles = grades['tests'][0:]
        testAverage = ((sum(testicles)) / len(testicles))
        testWeight = testAverage * 0.30

        finalExam = grades['final'][0:]
        finalAvg = ((sum(finalExam)) / len(finalExam))
        finalWeight = finalAvg * 0.25

        labs = grades['labs']
        labAvg = ((sum(labs))/len(labs))
        labWeight = labAvg * 0.30


        homework = grades['homework']
        homeworkAvg = ((sum(homework))/ len(homework))
        homeworkWeight = homeworkAvg * 0.15

        finalAverage = testWeight + finalWeight + labWeight + homeworkWeight

        return finalAverage


    avg = average()
    print('Final CSC grade is ' + str(avg) + '.\n')
    #print(avg)



cscAvg()


def matAverage():

    grades = {
        'tests': [97],
        'midterm': 80,
        'final': 96
    }


    def average():
        testicles = grades['tests'][0:]
        testAverage = ((sum(testicles)) / len(testicles))
        testWeight = testAverage * 0.20

        finalExam = grades['final']
        finalWeight = finalExam * 0.40


        midterm = grades['midterm']
        midtermWeight = midterm * 0.40


        finalAverage = testWeight + finalWeight + midtermWeight

        return finalAverage


    avg = average()
    print()
    print('Final MAT grade is ' + str(avg) + '.\n')
    # print(avg)

matAverage()






'''


gradeEquivalent = {
    'A+': 12.0,
    'A': 11.0,
    'A-': 10.0,
    'B+': 9.0,
    'B': 8.0,
    'B-': 7.0,
    'C+': 6.0,
    'C': 5.0,
    'C-': 4.0,
    'D+': 3.0,
    'D': 2.0,
    'D-': 1.0,
    'F': 0.0
}

courses = {
    'BIO 181': [3, gradeEquivalent['B+']],
    'BIO Lab': [3, gradeEquivalent['C']],
    'PHY 101': [3, gradeEquivalent['A']],
    "PYH 102": [3, gradeEquivalent['A-']],
    'CHEM 101': [3, gradeEquivalent['B']],
    'MAT 210': [3, gradeEquivalent['B+']],
    'MAT 220': [3, gradeEquivalent['B+']],
    'PSY': [3, gradeEquivalent['A']],
    'PSY2': [3, gradeEquivalent['D']]
}
print(courses['BIO 181'][1])

'''

new = [94, 95.24, 97.1, 97.7, 96.6, 97.8, 95.5, 0, 96.6]
print(sum(new)/900)
