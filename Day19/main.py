import turtle
import os
import random

colors = ["red", "blue", "green", "yellow", "black", "brown"]
turtle_shift = 0
turtle_list = []

def create(model):
    model.penup()
    model.shape("turtle")