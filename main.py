def measure(text):
    test_string = str(text)
    res = test_string.encode('utf-8')
    return len(res) * 0.001

print(measure("hello"))
