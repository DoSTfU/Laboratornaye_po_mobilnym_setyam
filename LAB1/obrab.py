# -*- coding: utf-8 -*-
import pandas as pd

def sum_Tel(k, T):
    return T * k


def sum_sms(k, N):
    return N * k

def int_r(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num

obrab = pd.read_csv('data.csv')