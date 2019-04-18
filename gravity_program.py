def solution(arr_val, arr_unit) :
    compile = {arr_val[0] : arr_unit[0],
    arr_val[1] : arr_unit[1],
    arr_val[2] : arr_unit[2]
    }
    m1 = arr_val[0]
    m2 = arr_val[1]
    d1 = arr_val[2]
    for m_1 in arr_unit[0]:
        if arr_unit[0] == "kg":
            m1_conversion = 1#1 * 1 #kg
            m1 = m1_conversion * arr_val[0]
        elif arr_unit[0] == "g":
            m1_conversion = 1 * 0.001 #g
            m1 = m1_conversion * arr_val[0]
        elif arr_unit[0] == "mg":
            m1_conversion = 1 * 0.000001 #mg
            m1 = m1_conversion * arr_val[0]
        elif arr_unit[0] == "μg":
            m1_conversion = 1 * 0.000000001 #μg
            m1 = m1_conversion * arr_val[0]
        elif arr_unit[0] == "lb":
            m1_conversion = 1 * 0.453592 #lb
            m1 = m1_conversion * arr_val[0]
        else:
            pass
    for m_2 in arr_unit[1]:
        if arr_unit[1] == "kg":
            m2_conversion = 1#1 * 1 #kg
            m2 = m2_conversion * arr_val[1]
        elif arr_unit[1] == "g":
            m2_conversion = 1 * 0.001 #g
            m2 = m2_conversion * arr_val[1]
        elif arr_unit[1] == "mg":
            m2_conversion = 1 * 0.000001 #mg
            m2 = m2_conversion * arr_val[1]
        elif arr_unit[1] == "μg":
            m2_conversion = 1 * 0.000000001 #μg
            m2 = m2_conversion * arr_val[1]
        elif arr_unit[1] == "lb":
            m2_conversion = 1 * 0.453592 #lb
            m2 = m2_conversion * arr_val[1]
        else:
            pass
    for d_1 in arr_unit[2]:
        if arr_unit[2] == "m":
            d1_conversion = 1 * 1 #m
            d1 = d1_conversion * arr_val[2]
        elif arr_unit[2] == "cm":
            d1_conversion = 1 * 0.01 #cm
            d1 = d1_conversion * arr_val[2]
        elif arr_unit[2] == "mm":
            d1_conversion = 1 * 0.001 #mm
            d1 = d1_conversion * arr_val[2]
        elif arr_unit[2] == "μm":
            d1_conversion = 1 * 0.000001 #μm
            d1 = d1_conversion * arr_val[2]
        elif arr_unit[2] == "ft":
            d1_conversion = 1 * 0.3048 #ft
            d1 = d1_conversion * arr_val[2]
        else:
            pass
    gravity_F = 0.0000000000667 * ((m1 * m2)/(d1*d1))
    return (gravity_F)
