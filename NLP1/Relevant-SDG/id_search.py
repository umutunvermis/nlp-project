import json
import concurrent.futures
from difflib import SequenceMatcher
import threading as th
from multiprocessing import Manager, Pool
import multiprocessing

START_INDEX = 2000
END_INDEX = 4000
THREAD_COUNT = 16


# Read the pubs
f = open("encoded_12/writers_formatted12.txt", "r", encoding="utf-8")
papers = json.loads(f.read())
f.close()
data = []
count = 0
result = []


for paper in papers:
    value = {}
    value["name"] = paper
    value["papers"] = []
    for i in papers[paper]:
        value["papers"].append(i["title"].lower())
    data.append(value)

class Reader():

    def __init__(self, start_index):
        self.start_index = start_index

        with concurrent.futures.ProcessPoolExecutor() as executor:
            indexessss = []
            for indexes in range(THREAD_COUNT):
                indexessss.append(start_index+indexes)
            executor.map(self.read, indexessss)

    def read(self, index):
        file_name="outputs_deneme12/"
        file_name+= str(index)
        file_name+=".txt"
        f2 = open(file_name, "w+", encoding="utf-8")
        try:
            fileName = "s2-corpus-" + str(index)
            f = open(fileName, "r", encoding="utf-8")
            lines = f.readlines()
            for line in lines:
                pub = json.loads(line)
                for paper in data:
                    if paper["papers"].__contains__(pub["title"].lower()):
                        for auth in pub["authors"]:
                                if 0.7 < SequenceMatcher(None, auth["name"]  , paper["name"]).ratio():

                                    val = {}
                                    val["corpusName"] = auth["name"]
                                    val["ids"] = auth["ids"]
                                    val["name"] = paper["name"]
                                    f2.write(json.dumps(val))
                                    print("file num is: ",index)
            f2.close()                           
        except Exception as e:
            print(e)
            f2.close


def main():
    i = START_INDEX
    while i<= END_INDEX - THREAD_COUNT:
        Reader(i)
        i += THREAD_COUNT

if __name__ == "__main__":
    main()
