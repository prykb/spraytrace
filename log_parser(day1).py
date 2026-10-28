with open("/home/priyanshu/Code/python/hello/.venv/logs.csv") as f:
    a = -1
    b=0
    for i in f:
        print(i, end=" ")
        a += 1
        if 'failed' in i:
            b+=1

    print("Total lines:", a)
    print("Total failed attempts:", b)

