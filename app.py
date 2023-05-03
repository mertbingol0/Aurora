from list_disk import list_disk
from test_disk import test_disk

print('1 - List Disk')
print('2 - Test Disk')

select_ps = input('Please select a prosses: ')
if select_ps == '1':
    list_disk()
elif select_ps == '2':
    test_disk()
else:
    print('cannot prosses')
