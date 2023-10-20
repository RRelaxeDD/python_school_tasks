import os

def print_docs(direct):
    all_files = os.walk(direct)
    for catalog in all_files:
        print(f"dir {catalog[0]} contains:")
    print(f"dirs: {', '.join([folder for folder in catalog[1]])}")
    print(f"files: {', '.join([file for file in catalog[2]])}")
    print("-" * 20)

print_docs(".")