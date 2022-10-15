def count_occurences(input_string):
    sum = {}
    b = input_string.replace(" ", "")
    c = b.split(",")
    for thing in c:
        if thing in sum:
            sum[thing] += 1
        else:
            sum[thing] = 1
    highest = max(sum.values())
    h = []
    for key, value in sum.items():
        if value == highest:
            h.append(key)
            h.append(value)
    new_list = [h[i:i+2] for i in range(0, len(h), 2)]
    return new_list
