import json

count=1
while count!=13:
    fileName1=str(count)+".txt"
    print(fileName1)
    f = open(fileName1, "r")

    writer_dict  = json.loads(f.read())
    fileName2="writers_formatted"+str(count)+".txt"
    new = open(fileName2, "w")

    result = {}

    for i in writer_dict:
        fullname = writer_dict[i]["name"] +" "+ writer_dict[i]["surname"] 
        result[fullname] = writer_dict[i]["publications"]

    new.write(json.dumps(result))
    new.close
    f.close
    count+=1