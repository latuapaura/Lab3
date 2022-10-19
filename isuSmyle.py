print('Введите номер ИСУ: ')
isu_number = int(input())
eye = [':', ';', 'X', '8', '=']
nose = ['-', '<', '-{', '<{']
mouth = ['(', ')', 'O', '|', '\ ', '/', 'P']
e, n, m = int(isu_number % 5), int(isu_number % 4), int(isu_number % 7)
isu_eye = eye[e]
isu_nose = nose[n]
isu_mouth = mouth[m]
print('Смайлик по номеру ИСУ: ')
smyle = isu_eye + isu_nose + isu_mouth
print(smyle)