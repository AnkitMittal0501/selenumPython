import pytest
import os
import xlrd

def data():
    os.chdir("D:\official\Selenium_Classes\Intellegenes\Shakti_Python_Selenium")
    file = os.getcwd()+"\\writing125.xls"
    rb = xlrd.open_workbook(file)
    sheet = rb.sheet_by_index(0)
    l=[]
    for data in sheet.get_rows():
        l.append(data)

    return l

@pytest.mark.parametrize("input1, input2, output",[(5,5,10),(3,5,12)])
def test_add(input1, input2, output):
    assert input1+input2 == output,"failed"

@pytest.mark.smoke
@pytest.mark.parametrize("data",data())
def test_dataparam(data):
    print("Data value ",data)