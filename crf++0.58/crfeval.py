2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
# !/usr/bin/python
# -*- coding: utf-8 -*-

import sys

if __name__ == "__main__":
    try:
        file = open(sys.argv[1], "r")
    except:
        print("result file is not specified, or open failed!")
        sys.exit()

    wc_of_test = 0
    wc_of_gold = 0
    wc_of_correct = 0
    flag = True

    for l in file:
        if l == '\n': continue

        _, _, g, r = l.strip().split()

        if r != g:
            flag = False

        if r in ('E', 'S'):
            wc_of_test += 1
            if flag:
                wc_of_correct += 1
            flag = True

        if g in ('E', 'S'):
            wc_of_gold += 1

    print("WordCount from test result:", wc_of_test)
    print("WordCount from golden data:", wc_of_gold)
    print("WordCount of correct segs :", wc_of_correct)

    # 查全率
    P = wc_of_correct / float(wc_of_test)
    # 查准率，召回率
    R = wc_of_correct / float(wc_of_gold)

    print("P = %f, R = %f, F-score = %f" % (P, R, (2 * P * R) / (P + R)))