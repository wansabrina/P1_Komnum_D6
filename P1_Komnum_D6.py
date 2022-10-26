# Anggota Kelompok:
#
# Najma Ulya Agustina      5025211239
# Syarifah Talitha Erfany  5025211175
# Wan Sabrina Mayzura      5025211023

import numpy as np
import matplotlib.pyplot as plt

# Persamaan
def func(x):
    # x^3 - 3x^2 -9x + 18
    return pow(x, 3) - 3 * x + 1

# Set x dan y untuk plot
x = np.linspace(-5, 5, 100)
y = pow(x, 3) - 3 * x + 1

# Input a, b, iterasi maksimum, dan ketelitian
a = float(input("Masukkan batas atas: "))       
b = float(input("Masukkan batas bawah: "))   
max_repetition = int(input("Masukkan jumlah iterasi maksimal: "))
accuracy = float(input("Masukkan ketelitian: "))

# Cek terlebih dahulu apakah batas atas dan bawah sesuai dengan syarat dari bolzano
if func(a) * func(b) > 0:
    print('Numbers do not meet Bolzano\'s criteria')
    exit()

# Membuat plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.plot(x, y, 'r')

plt.show()

# Cetak header tabel
print('------------------------------------------------------------------------------------------------------')
print('iterasi \t a\t\t b\t\t f(a) \t\t f(b)\t\t mp\t\t f(mp)        ')
print('------------------------------------------------------------------------------------------------------')

for i in range(max_repetition):
    # Mencari middle point
    mp = (a + b)/2
    fa = func(a)
    fb = func(b)
    fmp = func(mp)

    # Output hasil sesuai iterasi
    print(str(i + 1)+'\t    % 10.5f\t    % 10.5f\t    % 10.5f\t    % 10.5f\t    % 10.5f\t    % 10.5f\t' %(a, b, fa, fb, mp, fmp))

    if np.abs(func(mp)) < accuracy:
        print('------------------------------------------------------------------------------------------------------')
        print('The value of root is : '+ str(mp))
        exit();
        
    if func(a) * func(mp) < 0:
        b = mp

    elif func(a) * func(mp) > 0: 
        a = mp

print('----------------------------------------------------------------------------')
if i == max_repetition - 1:
    print('\n\nMaximum Iteration!')
    print('The value of root is : '+ str(mp))

print("\n")
