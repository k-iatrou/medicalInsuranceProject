# person data
age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0

# calculating insurance cost
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

print("This person's insurance cost is " + str(insurance_cost) + " dollars.")

# age change
age += 4

# calculate new insurance cost
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

# calculate change in insurance cost
change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost) + " dollars.")

# age change
age = 28

# bmi change
bmi += 3.1

# calculate new insurance cost with new bmi
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

# calculate new change in insurance cost with new BMI
change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated insurance cost after increasing BMI by 3.1 is " + str(change_in_insurance_cost) + " dollars.")

# change bmi
bmi = 26.2

# change sex to male
sex = 1

# calculating new insurance cost with new sex
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

# calculating new change in insurance cost with new sex
change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost for being male instead of female is " + str(change_in_insurance_cost) + " dollars.")

# change sex back to female
sex = 0

# change smoker from non-smoker to smoker
smoker = 1

# calculating new insurance cost with smoker instead of non-smoker
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

# calculating new change in insurance cost with smoker instead of non-smoker
change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost for being smoker instead of non smoker is " + str(change_in_insurance_cost) + " dollars.")
