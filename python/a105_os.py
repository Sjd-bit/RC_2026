import os

def main():
    print(os.name)
    print(os.getcwd())
    print(os.listdir())
    folders = [name for name in os.listdir() if os.path.isdir(name)]
    print(folders)
    




if __name__ == "__main__":
        main()
