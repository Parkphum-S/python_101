"""
ออกแบบ IPO สำหรับโปรแกรมคำนวณค่าไฟฟ้า โดยกำหนดว่า:
จำนวนหน่วยไฟ = 120 หน่วย
ราคาต่อหน่วย = 4 บาท
ให้ระบุ:
Input 
Process
Output
คำตอบราคารวม
"""
units = float(input("Enter temperature: "))
price_per_unit = 4
total_cost = units * price_per_unit


input_data = f"จำนวนหน่วยไฟ = {units} หน่วย\nราคาต่อหน่วย = {price_per_unit} บาท"
process_data = f"คำนวณราคารวม: {units} * {price_per_unit}"
output_data = f"ราคารวม: {total_cost} บาท"


print(input_data)
print(process_data)
print(output_data)
