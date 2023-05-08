import subprocess as sb
import json

def disk_test():
    once_disk = '/dev/sda'
    twice_disk = '/dev/sdb'

    test_output_1 = sb.check_output(['sudo', 'smartctl', '-H', once_disk]).decode()
    test_output_2 = sb.check_output(['sudo', 'smartctl', '-H', twice_disk]).decode()

    if 'PASSED' in test_output_1:
        once_disk_status = f'{once_disk} adli disk calisiyor \U0001F607'
    else:
        once_disk_status = f'{once_disk} adli disk calismiyor \U0001F620'

    if 'PASSED' in test_output_2:
        twice_disk_status = f'{twice_disk} adli disk calisiyor \U0001F607 '
    else:
        twice_disk_status = f'{twice_disk} adli disk calismiyor \U0001F620'

    data =	{
        'disk1': once_disk_status,
        'disk2': twice_disk_status
        }

    with open('veriler.json', 'w') as f:
        json.dump(data, f)

disk_test()
