# import os

# dirinput = input('파일 경로를 입력해주세요 : ')

# def search(dirname):
#     try:
#         filenames = os.listdir(dirname)
#         for filename in filenames:
#             full_filename = os.path.join(dirname, filename)
            
#             if os.path.isdir(full_filename):
#                 search(full_filename)
#             else:
#                 ext = os.path.splitext(full_filename)[-1]
#                 if ext == ".py":
#                     print(full_filename)
#     except PermissionError:
#         pass

# search(dirinput)

import os

dirinput = input('파일 경로를 입력해주세요 : ')

for (path, dir, files) in os.walk(dirinput):#현재 디렉토리, 하위디렉토리들, 현재디렉토리의파일이름들
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == ".py":
          print(f"{path}/{filename}")