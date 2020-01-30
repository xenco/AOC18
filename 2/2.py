with open("input") as f:

    lines = f.readlines()
    common = []
    num_diff = 0

    for line_a in lines:
        for line_b in lines:

            if line_a == line_b: break
            if len(line_a) != len(line_b): break

            num_diff = 0
            common = []

            for i in range(0, len(line_a) - 1):
                if line_a[i] == line_b[i]:
                    common.append(line_a[i])
                else:
                    num_diff += 1

            if num_diff == 1: break
        if num_diff == 1: break

    print("".join(common))