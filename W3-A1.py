# ---------------------------------------------------------------
# File Reader
# Author: Roxanne Prajapati
# Description:
#      Program that read a file and count *
# ---------------------------------------------------------------

class FileReader:

    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        with open(self.filename, "r", encoding="utf-8") as content:
            count = 0
            for line in content:
                count += line.count('*')

            return count




# Run the program only when executed directly
if __name__ == "__main__":
    filename = "demo_file.txt"
    filereader = FileReader(filename)
    result = filereader.read_file()
    if result is not None:
        print("Number of '*' characters: ", result)

