# Created on 3 Nov 2016
# Created by: Matthew Lourenco
# This is a program that converts letter grades to percents.

letter_grade = {}
letter_grade['NE'] = '0%'
letter_grade['R'] = '1-49%'
letter_grade['1-'] = '50-52%'
letter_grade['1'] = '53-56%'
letter_grade['1+'] = '57-59%'
letter_grade['2-'] = '60-62%'
letter_grade['2'] = '63-66%'
letter_grade['2+'] = '67-69%'
letter_grade['3-'] = '70-72%'
letter_grade['3'] = '73-76%'
letter_grade['3+'] = '77-79%'
letter_grade['4-'] = '80-87%'
letter_grade['4'] = '88-94%'
letter_grade['4+'] = '95-99%'
letter_grade['4++'] = '100%'

def grade_convert(input):
    #this function converts the inputted grade to a percent.
    if input == 'NE' or input == 'R' or input == '1-' or input == '1' or input == '1+' or input == '2-' or input == '2' or input == '2+' or input == '3-' or input == '3' or input == '3+' or input == '4-' or input == '4' or input == '4+' or input == '4++':
        return letter_grade[input]
    else:
        return -1

while True:
    grade = raw_input('Enter the letter grade to be converted: ')
    print(grade_convert(grade))
    if grade == 'break':
        break
