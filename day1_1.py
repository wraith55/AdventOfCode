
def run():
    f=open(".\\files\\commands1_1.txt", "r")
    if (f.mode == "r"):
        contents = f.readlines()

    frequencies_seen = []
    sum = 0
    frequencies_seen.append(sum)
    dup_found = False
    while not dup_found:
        for line in contents:
            sum += (int(line))
            if sum in frequencies_seen:
                dup_found = True
                break
            else:
                frequencies_seen.append(sum)
        
    print(sum)