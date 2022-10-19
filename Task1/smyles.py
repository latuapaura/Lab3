import re
#ису = 367933


def check(filename):
    #isu = input('Введите номер ИСУ: ')
    #if isu == 367933:
        #return True

    pattern = re.compile(r'8<P')
    file_to_open = open(filename)
    file_in_string = file_to_open.read()
    return len(pattern.findall(file_in_string))

def main():
    for i in range(1, 6):
        test = 'test' + str(i) + '.txt'
        print(check(test))

if __name__ == '__main__':
    main()