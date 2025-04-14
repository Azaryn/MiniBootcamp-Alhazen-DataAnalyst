import numpy as np
import random

# Membuat Array
tahun_pengalaman = np.array ([1,2,3,4,5])
print("Tahun Pengalaman: ",tahun_pengalaman)

# Basic Operasi
tahun_pengalaman_plust2 = tahun_pengalaman + 2
print("Tahung Pengalaman + 2: ", tahun_pengalaman_plust2)

#Array Slicing
print("Tahung Pengalaman index 0, 1 dan 2: ",tahun_pengalaman[0:3])

# Boolean Indexing
Pengalaman_3_tahun_lebih = tahun_pengalaman_plust2[tahun_pengalaman_plust2 > 4] #ngambil dari index yang nilainya lebih dari 4
print(Pengalaman_3_tahun_lebih)

# Math Operation
salary = [random.randint(100000,150000) for num in range(10)]
print(salary)

salary_array = np.array(salary)
print("Salary Array: ",salary_array)

total = np.sum(salary_array)
print("SUM (Total): ", total)

# Static Operation
avg_salary = np.mean(salary_array)
print("MEAN (rata-rata): ",avg_salary)

std_salary = np.std(salary_array)
print("Standar Deviasi (STD): ", std_salary)

min_salary = np.min(salary_array)
print("Minimal: ",min_salary)

max_salary = np.max(salary_array)
print("Maximal: ", max_salary)

NaN_Salary = np.isnan(salary_array)
print("Mencari Nilai NaN (kosong): ", NaN_Salary)

data = np.array([1,2,np.nan,4,np.nan,6])
nan_mask = np.isnan(data)
print("Array Asli: ",data)
print("Letak NaN: ",nan_mask)
print("Nilai NaN: ",data[nan_mask])