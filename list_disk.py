import os

def list_disk():
    os.system('lsblk')
    input("Press enter to continue...")
    print('1 - List Disk *')
    print('2 - Test Disk')

    select_ps = input('Please select a prosses: ')
    if select_ps == '1':
        list_disk()
    elif select_ps == '2':
        test_disk()
    else:
        print('cannot prosses')
