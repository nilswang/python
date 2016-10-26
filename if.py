#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 注意:
# input()返回的是字符串
# 必须通过int()将字符串转换为整数
# 才能用于数值比较:

height = 1.75
weight = 80.5
bmi = weight/(height*height)
if bmi < 18.5:
   print('guoqing')
elif bmi > 18.5 and bmi < 25.0:
    print('正常')
elif bmi > 25.0 and bmi < 28.0:
    print('过重')
elif bmi > 28.0 and bmi < 32.0:
    print('肥胖')
else:
    print('严重肥胖')
