for i in range(255):
    req = str(bin(i)[2:])
    req = ("0" * (8 - len(req) - 1)) + req
    N = ""
    for j in req:
        N += str(abs(int(j) - 1))
    # N = "0b" + N
    # N = int(N, 10)
    if int("0b" + N, 2) - i == 111:
        print(i)
        break
