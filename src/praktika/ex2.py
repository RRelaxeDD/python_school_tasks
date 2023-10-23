def check_empty_file(func):

    def inner(file_path):

        with open(file_path, 'r') as file:
            data = file.readline()

        if not data: raise Exception("empty file")

        func(file_path)

    return inner

@check_empty_file
def do_file(path):
    with open(path, 'r') as file:
        print(f"--- file: {path}\n{file.read()}\n---\n")

do_file("not_empty_file.txt")
do_file("empty_file.txt")