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

    for j in seperated :
            set_values.add(j[1])

    count = 0
    for k in set_values:
        for l in seperated:
            if k == l[1]:




    print("Total lines:", a)
    print("Total failed attempts:", b)
    print("unique IPs", set_values)


    #first well want to associate each ip with a success/failure tag. most likely a dictionary.
    #key = ip, value = how many failures.


    #dictionaries are of the format {"----" : ----}

