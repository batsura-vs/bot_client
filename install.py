import re, os, pip

regex = r"^(import|from) (?!\.)(.*?)( |\.|$|,)"
file_dir = os.path.dirname(os.path.abspath(__file__))
clear = lambda: os.system("clear")


def load_files(path):
    files = []
    for dir in os.listdir(path):
        is_file = os.path.isfile(f'{path}/{dir}')
        if dir[0] == "." or (dir.split('.')[-1] != "py" and is_file) or dir == "venv":
            continue
        if is_file:
            files.append(f'{path}/{dir}')
        else:
            for i in load_files(f'{path}/{dir}'):
                files.append(i)
    return files


files = load_files(file_dir)
all_libs = []
for file in files:
    clear()
    print(f"checking file {file}")
    libs = set()
    with open(file, "r") as f:
        for i in f.readlines():
            result = re.search(regex, i, re.MULTILINE)
            if result:
                libs.add(result.group(2))
    for i in libs:
        all_libs.append(i)
        try:
            exec(f"import {i}")
            print(f"Library {i} - exists")
        except:
            print(f"Downloading {i}")
            pip.main(["install", i])
            try:
                exec(f"import {i}")
            except:
                pip.main(["install", f'py{i}'])
clear()
print("Library downloading done!")
print(f"Files checked: {len(files)}")
print("Success")
