# -*- coding: UTF-8 -*-

['normal']
# 倾角[1,2,3]
# 设备子单元号[0,1,2]
# 实际倾角[123,12,32]


qj = [12,23,123]
qjno = [0,1,2]

sjqj = [2131,123,12313]
sjqjno = [0,2,3]

list1 =  zip(qjno,qj)
list2 = zip(sjqjno,sjqj)
print list1
print list2


for i in xrange(len(list1)):
    j = 0
    while j < len(list2):
        if list1[i][0] == list2[j][0]:
            print list1[i][1]
            print "next"
        j += 1
