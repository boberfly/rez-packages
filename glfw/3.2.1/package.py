# -*- coding: utf-8 -*-

name = "glfw"

version = "3.2.1"

description = "GLFW3"

variants = [
    ['gcc-4.8.3'],
]

def commands():
    env.LD_LIBRARY_PATH.append("{root}/lib")
