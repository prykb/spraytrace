with open("/home/priyanshu/Code/python/hello/.venv/logs.csv") as f:
    a = -1
    b=0
    seperated=[]
    set_values = set()
    for i in f:

        print(i, end=" ")
        a += 1
        if 'failed' in i:
            b+=1

        seperated.append(i.split(","))

    seperated.remove(['timestamp', 'source_ip', 'username', 'result\n'])


    count = {}
    for j in seperated :
            set_values.add(j[1])
            if j[1] in count:
                count[j[1]] += 1
            else:
                count[j[1]] = 1




    print("Total lines:", a)
    print("Total failed attempts:", b)
    print("unique IPs", set_values)
    print(count)
