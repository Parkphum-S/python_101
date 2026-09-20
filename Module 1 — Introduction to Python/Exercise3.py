"""
ออกแบบ Pseudocode ของระบบเปิด/ปิดปั๊มน้ำตามเงื่อนไข:
เปิดปั๊มน้ำ เมื่อ:
- ความชื้นดิน > 30%
- และฝนไม่ตก

กรณีอื่น:
- ปิดปั๊มน้ำ
กำหนดข้อมูลทดสอบ:
soil_moisture = 25
rainfall = 0
"""

input_soil_moisture = float(input("กรุณาใส่ความชื้นดิน (%): "))
input_rainfall = float(input("กรุณาใส่ฝนตกหรือไม่ (True:1/False:0): "))
if input_soil_moisture < 30 and input_rainfall == 0:
    print("เปิดปั๊มน้ำ")
else:
    print("ปิดปั๊มน้ำ")
