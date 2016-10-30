#!/usr/bin/python
# -*- coding: utf-8 -*-
# myerror.py
# described by Kazushi Yamashina

class MyError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)