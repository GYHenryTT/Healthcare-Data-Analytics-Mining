#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 04:50:48 2019

@author: heqi
"""
import pandas as pd
ed = pd.read_csv("/Users/heqi/Desktop/Healthcare/ed_withbool.csv")
ed_overdose = ed[ed.overdose ==1]
ed_overdose['TXTZIP'].value_counts().head(3)

import numpy as np
import re
all_drugs = np.concatenate([ed_overdose.DX1,ed_overdose.DX2,ed_overdose.DX3,ed_overdose.DX4,ed_overdose.DX5,ed_overdose.DX6,ed_overdose.DX7,ed_overdose.DX8,ed_overdose.DX9,ed_overdose.DX10,ed_overdose.DX11,ed_overdose.DX12,ed_overdose.DX13,ed_overdose.DX14,ed_overdose.DX15,ed_overdose.DX16,ed_overdose.DX17,ed_overdose.DX18,ed_overdose.DX19,ed_overdose.DX20])
all_drug = all_drugs.tolist()
r1 = re.compile("^T40")
r2 = re.compile("^T41")
r3 = re.compile("^T42")
r4 = re.compile("^T43")
newlist = list(filter(r1.match, all_drug))+list(filter(r2.match, all_drug))+list(filter(r3.match, all_drug))+list(filter(r4.match, all_drug))
print(newlist)

import collections
from collections import Counter
ctr = collections.Counter(newlist)
print(ctr)

pd.set_option('display.max_columns', 99)
my_pt = ed[ed.UNIQ==859382]
print(my_pt)

inpatient = pd.read_csv("/Users/heqi/Desktop/Healthcare/VTINP16.csv")
my_inpt = inpatient[inpatient.UNIQ==859382]
print(my_inpt)

rev = pd.read_csv("/Users/heqi/Desktop/Healthcare/VTREVCODE16.csv")
my_rev = rev[rev.Uniq==859382]
print(my_rev)

print(rev[rev['Uniq'] == 859382])