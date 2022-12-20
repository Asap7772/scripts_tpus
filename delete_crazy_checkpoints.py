import os
path = '/home/raid/asap7772/exps'

files_to_delete = []
for root, dirs, files in os.walk(path):
    for file in files:
        if 'checkpoint' in file and '.' not in file and 'tmp' not in file and int(file.split('checkpoint')[1]) > 400000:
            files_to_delete.append(os.path.join(root, file))
            
for file in files_to_delete:
    print('Deleting: ', file)
    os.remove(file)

print('Done')

print(os.system('df -h'))
print(os.system(f'du -sh {path}/* | sort -h'))