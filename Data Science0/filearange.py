import os

def arrange_files(files, ext):
    files_with_ext = [f for f in files if f.endswith(ext)]
    print(files_with_ext)
    
    # if not(os.path.exists("folder name", ext[1:])):
    #     os.mkdir("folder name", ext[1:])
    
    # for i, file in enumerate(files_with_ext):
    #     new_name = f"{i + 1}{ext}"
    #     os.rename(file, new_name)

if __name__ == "__main__":
    files = os.listdir()
    arrange_files(files, ".jpg")