# Min-Max Normalization function
def min_max_norm(data, new_min, new_max):
    old_min, old_max = min(data), max(data)
    xscaled = [new_min + (x - old_min) * (new_max - new_min) / (old_max - old_min) for x in data]
    return xscaled

# Create Data Vector of ages 
age = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]

# Perfomr Min-Max Normalization on age
new_min = 0
new_max = 1

# Call the min_max_norm function
age_norm = min_max_norm(age, new_min, new_max)

# zip the age and age_norm
age_age_norm = list(zip(age, age_norm))

# Print the normalized age
print("(Age, Age_Norm)", age_age_norm)
