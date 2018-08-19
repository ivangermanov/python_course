from datetime import datetime
import glob2

def merge(files_paths):
    with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt", "w") as writer:
        for file in files_paths:
            with open(file) as reader:
                writer.write(reader.read() + "\n")

files_paths = glob2.glob("*.txt")
merge(files_paths)