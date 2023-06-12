
import json

f = open("out-authors.txt", "r", encoding="utf-8")
writers = json.loads(f.read())
f.close()
d2l = []
for writer in writers:
    writer = writers[writer]
    id = []
    id.append(int(writer["authorId"]))
    writer["ids"] = id
    d2l.append(writer)
f1 = open("newAuthors.txt", "w+", encoding="utf-8")
f1.write("[")
for item in d2l:
    f1.write(json.dumps(item))
    #f1.write(str)
    f1.write(",\n")
f1.write("]")