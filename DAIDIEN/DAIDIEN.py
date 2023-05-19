f = open("DAIDIEN.inp", "r")
line1 = f.readline().strip().split()
line2 = f.readline().strip().split()
f.close()
line1 = [int(i) for i in line1]
line2 = [int(i) for i in line2]

K = line1[1]


def question1():
    result = -1
    for i in line2:
        if i > K and (result == -1 or i < result):
            result = i
    return result

#Sliding window algorithm
def question2():
    result = 0

    i = 0
    while i < K:
        result += line2[i]
        i += 1
    sum = result
    i += 1
    while i < len(line2):
        if sum > result:
            result = sum
        sum = sum + line2[i] - line2[i - K - 1]
        i += 1
    return result


f = open("DAIDIEN.out", "a")
print(question2())
f.writelines([str(question1()), "\n" + str(question2())])
f.close()
