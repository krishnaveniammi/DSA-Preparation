def count_v_c(s):
    v = "aeiouAEIOU"
    v_cout =0
    c_cout =0
    for char in s:
        if char in v:
            v_cout +=1
        else:
            c_cout +=1
    return v_cout,c_cout
s = "sunny is a bad girl"
print(count_v_c(s))
