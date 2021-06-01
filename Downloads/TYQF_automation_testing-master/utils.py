#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
# @Time    : 2021/5/8 4:24 下午
# @Author  : 姜晖
# @Email   : jianghui@tianyancha.com
# @File    : utils.py
import yaml


def load_env():
    env = yaml.safe_load(open('../../env.yml'))
    return env

