while True:
    x1, y1, x2, y2 = map(int, input().split())

    if (x1, y1, x2, y2) == (0, 0, 0, 0):
        break

    elif (x1, y1) == (x2, y2):
        print("0")

    elif x1 == x2 or y1 == y2:
        print("1")

    elif ((x1 + y1) == (x2 + y2) or 
          (x1 - y1) == (x2 - y2)):
        print("1")

    else:
        print("2")