# This program will convert kilograms to pounds 

# 4 killogram samples 
kg_value_1 = 1
kg_value_2 = 23
kg_value_3 = 55
kg_value_4 = 83

# conversion factor : 1 kg = 2.20462 lb
conversion_factor = 2.20462

lb_value_1 = kg_value_1 * conversion_factor 
lb_value_2 = kg_value_2 * conversion_factor
lb_value_3 = kg_value_3 * conversion_factor
lb_value_4 = kg_value_4 * conversion_factor

# Output the results 

print(f"{lb_value_1:0.2f} pounds is equal to  {kg_value_1} kilograms")
print(f"{lb_value_2:0.2f} pounds is equal to {kg_value_2} kilograms")
print(f"{lb_value_3:0.2f} pounds is equal to  {kg_value_3} kilograms")
print(f"{lb_value_4:0.2f} pounds is equal to {kg_value_4} kilograms")

# print(f"pounds{lb_value_4 :0.2f}") = right , "f round up" works only with the string 
# print(f(lb_value_4:0.2f)) = wrong 
# print(f{lb_value_4:0.2f}) = wrong