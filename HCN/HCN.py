f = open("HCN.inp")
line1 = f.readline().strip().split(" ")
line2 = f.readline().strip().split(" ")
f.close()

line1 = [int(i) for i in line1]
line2 = [int(i) for i in line2]

#Just brute force the solution
s1 = abs(line1[0] - line1[2]) * abs(line1[1] - line1[3])
s2 = abs(line2[0] - line2[2]) * abs(line2[1] - line2[3])

f = open("HCN.out", "w")
if s1 > s2:
    f.writelines(str(s1))
else:
    f.writelines(str(s2))
f.close()
