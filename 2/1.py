two = 0
three = 0
with open("input") as f:
    for line in f.readlines():
        chars = {}
        for c in line:
            if(c == "\n"): break
            if(not c in chars.keys()): chars[c] = 0
            chars[c] += 1

        filtered = [x for x in chars if chars[x] > 1 and chars[x] <= 3]

        two_added = False
        three_added = False
        for x in filtered:
            if (chars[x] == 2):
                if not two_added:
                    two += 1
                    two_added = True
            elif (chars[x] == 3):
                if not three_added:
                    three += 1
                    three_added = True

print("Result: ", two, "*", three, "=", two*three)