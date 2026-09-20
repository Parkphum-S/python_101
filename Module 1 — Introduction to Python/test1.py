"""
Input: ค่าความชื้นดิน = 22%
Process: ตรวจสอบว่า 22 < 30 หรือไม่
Output: สั่งเปิดปั๊มน้ำ
Pump: ON
"""

input_humidity = int(input("Enter soil humidity (%): ")) 
if input_humidity < 30:
    print("Pump: ON")
else:
    print("Pump: OFF")