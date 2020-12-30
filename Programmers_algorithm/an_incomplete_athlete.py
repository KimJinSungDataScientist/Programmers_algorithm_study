participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

participant = sorted(participant)
completion = sorted(completion)


for i in range(len(participant)):

    if i == len(participant)-1:
        save = participant[i]
        break

    if participant[i] != completion[i]:
        save = participant[i]
        break


print(save)