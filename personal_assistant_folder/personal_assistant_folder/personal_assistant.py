from sorting_files.Sorting import Sorting

"""
PythonCore 17 group №6 personal assistant project
"""

"""
Данный код носит временный характер для теста работы кода.
"""
while True:
    command = input('Path to folder for sorting: ')

    if command in ('stop', 'exit'):
        break

    if command.startswith('sort'):
        command = command.split(' ')
        sorting = Sorting(command[1])
        sorting.sort()
        print('Finish')
        break
