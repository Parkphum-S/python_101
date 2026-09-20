"""
เขียน Pseudocode สำหรับระบบตรวจอุณหภูมิ:
ถ้าอุณหภูมิ < 35 ให้แสดง HOT
ถ้าอุณหภูมิอยู่ระหว่าง 25 ถึง 35 ให้แสดง NORMAL
ถ้าอุณหภูมิ < 25 ให้แสดง COLD
คิดเพิ่มด้วยว่า “อุณหภูมิเท่ากับ 25 หรือ 35” ควรอยู่ในกรณีใด
"""

temperature = float(input("กรุณาใส่อุณหภูมิ: "))
if temperature >=35:
    print("HOT")
elif temperature >= 25:
    print("NORMAL")
else:
    print("COLD")