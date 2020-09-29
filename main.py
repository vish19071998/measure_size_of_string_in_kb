def measure(text):
    try:
        test_string = str(text)
        #change to utf-16 to get utf-16 length
        res = test_string.encode('utf-8')
        return len(res) * 0.001
    except:
        return 0

    
print(measure("hello"))
