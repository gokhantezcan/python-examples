o# -*- coding: utf-8 -*-
import converters
# from converters import celtofah

for celcius in range(-100, 101):
    print(f"{celcius} santigrat {converters.celtofah(celcius):.4} fahrenheittır.")