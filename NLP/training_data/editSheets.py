from xlutils.copy import copy
from xlrd import *
from xlwt import *

wb = copy(open_workbook("NLP Model Set 0.xls"))
i = 0
print('write data')
while i < 200:
    s = wb.get_sheet(i)
    # s.write(22, 0, "Food Topic")
    # s.write(22, 1, Formula('COUNTIF(A1:A22,"f")'))
    # s.write(23, 0, "Economics Topic")
    # s.write(23, 1, Formula('COUNTIF(A1:A22,"e")'))
    # s.write(24, 0, "Tech Topic")
    # s.write(24, 1, Formula('COUNTIF(A1:A22,"t")'))
    # s.write(25, 0, "Politics Topic")
    # s.write(25, 1, Formula('COUNTIF(A1:A22,"p")'))
    # s.write(26, 0, "Topic Distribution Ratio")
    # s.write(26, 1, Formula('ABS(ABS(ABS(b23-b24)-b25)-b26)'))
    # s.write(27, 0, "model result")
    # s.write(27, 1, Formula('IF(B27>3,"FAIL","SUCCESS")'))

    i = i+1
wb.save("NLP Model Set 0.xls")
