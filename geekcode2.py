for x in range(1,1000):
    resp = []
    resp.append("#".center(2*x))
    for i in range(1,x):
        resp.append(("#"+" "*(2*i-1)+"#").center(2*x))
    print("\n".join(resp+resp[::-1][1:]))