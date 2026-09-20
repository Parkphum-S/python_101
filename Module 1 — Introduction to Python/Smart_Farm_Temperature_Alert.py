"""
START
รับค่า temperature

IF temperature > 38 THEN
    แสดง "DANGER: High Temperature"
ELSE IF temperature >= 30 THEN
    แสดง "WARNING: Temperature High"
ELSE
    แสดง "NORMAL"
END IF
END
"""
temperature = float(input("กรุณาใส่อุณหภูมิ: "))
if temperature > 38:
    print("DANGER: High Temperature")
elif temperature >= 30:
    print("WARNING: Temperature High")
else:
    print("NORMAL") 
    