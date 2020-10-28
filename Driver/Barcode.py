# coding=utf-8
import barcode
import tkinter as tk

from barcode.writer import ImageWriter
def Run_Barcode(data):
    print(barcode.PROVIDED_BARCODES)
    EAN = barcode.get_barcode_class('code128')
    ean = EAN(data, writer=ImageWriter())
    fullname = ean.save('/AutomationApiTest//Report//Img//ean13_barcode6')
    return fullname

run_test =Run_Barcode
run_test('JY202004230017')

