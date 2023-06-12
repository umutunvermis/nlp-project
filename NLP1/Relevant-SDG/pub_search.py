import json
import concurrent.futures
from difflib import SequenceMatcher
import threading as th
START_INDEX = 4000
END_INDEX = 6000
THREAD_COUNT = 16


# Read the writers
f = open("output_file.txt", "r", encoding="utf-8")
writers = json.loads(f.read())
publications = []
f.close()
ids = []

for writer in writers:
    ids.append(int(writer["ids"][0]))
    writer["publications"] = []
class Reader():
    def __init__(self, start_index):
        self.start_index = start_index

        with concurrent.futures.ProcessPoolExecutor() as executor:
            indexessss = []
            for indexes in range(THREAD_COUNT):
                indexessss.append(start_index+indexes)
            executor.map(self.read, indexessss)

        

    def read(self, index):
        file_name="outputs_deneme1/"
        file_name+= str(index)
        file_name+=".txt"
        f2 = open(file_name, "w+", encoding="utf-8")  
        try:
            fileName = "s2-corpus-" + str(index)
            f = open(fileName, "r", encoding="utf-8")
            lines = f.readlines()
            for line in lines:
                pub = json.loads(line)
                for auth in pub["authors"]:
                    for id in auth["ids"]:
                        if ids.__contains__(int(id)):
                            publications.append(line.replace("\n", ""))
                            f2.write(line)
                            break
                            """"
                            for writer in writers:
                                if int(writer["ids"][0]) == int(id):
                                    writer["publications"].append(pub["id"])
                            """
            f2.close()
        except Exception as e:
            print(e)
            f2.close()

def main():
    i = START_INDEX
    while i<= END_INDEX - THREAD_COUNT:
        Reader(i)
        i += THREAD_COUNT

if __name__ == "__main__":

    main()

