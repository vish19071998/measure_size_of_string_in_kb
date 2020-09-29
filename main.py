def measure(text,encType=1):
    try:
        test_string = str(text)
        #change to utf-16 to get utf-16 length
        if encType == 1:
            res = test_string.encode('utf-8')
        if encType == 2:
            res = test_string.encode('utf-16')
        return len(res) * 0.001
    except:
        return 0

    
print(measure("hello",1))
