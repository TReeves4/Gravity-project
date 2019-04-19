def solution(arr_val, arr_unit) :
    compile = { "kg" : 1 , "g" : 0.001 , "mg" : 0.000001 , "μg" : 0.000000001 , "lb" : 0.453592 ,\
    "m" : 1 , "cm" : 0.01 , "mm" : 0.001 , "μm" : 0.000001 , "ft" : 0.3048
    }
    m1 = arr_val[0] * compile[arr_unit[0]]
    m2 = arr_val[1] * compile[arr_unit[1]]
    d1 = arr_val[2] * compile[arr_unit[2]]
    gravity_F = 0.0000000000667 * ((m1 * m2)/(d1*d1))
    return (gravity_F)
    
    
