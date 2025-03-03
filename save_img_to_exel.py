import openpyxl
wb = openpyxl.load_workbook("Baz.xlsx")
ws = wb["Лист1"]
img = openpyxl.drawing.image.Image("some.jpg")
img.anchor = 'B1' # Or whatever cell location you want to use.
img.width = 100
img.height = 100
ws.add_image(img)
wb.save("Baz.xlsx")


