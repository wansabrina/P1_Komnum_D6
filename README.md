# P1_Komnum_D6
Praktikum 1 Komputasi Numerik


### Anggota Kelompok
| Nama                | NRP        | Kelas     |
| ---                 | ---        | ----------|
| Najma Ulya Agustina | 5025211239 |  Komnum D |
| Syarifah Thalita Erfany | 5025211175 |Komnum D |
| Wan Sabrina Mayzura | 5025211023 |Komnum D |

## Soal 
Anda sudah mengerti algoritma pemrosesan metode Bolzano, dan Anda sudah memahami cara kerjanya. Sekarang Anda tinggal mengimplementasikan algoritma tersebut menjadi sebuah program komputer metode Bolzano (yang dapat menampilkan proses iteratif numerik, lengkap dengan grafik fungsinya)

## Penjelasan Kode
Sebelum menjalankan kode, adapun beberapa module atau dependencies yang harus diinstall yaitu ```numpy``` dan ```matplotlib```. Sehingga dapat digunakan pada kode <br />
```R
import numpy as np
import matplotlib.pyplot as plt
```

Adapun persamaan yang kami gunakan untuk mencoba program dari kode ini adalah <br />
```x^3 - 3x + 1```

Yang didefinisikan menggunakan syntax: <br />
```R
def func(x):
    # x^3 - 3x^2 -9x + 18
    return pow(x, 3) - 3 * x + 1
```

Selanjutnya, diset nilai x dan y untuk membuat plot <br />
```R
x = np.linspace(-5, 5, 100)
y = pow(x, 3) - 3 * x + 1
```
Lalu akan diinput nilai ```batas atas```, ```batas bawah```, ```jumlah iterasi maksimal```, dan ```ketelitian```<br />
```R
a = float(input("Masukkan batas atas: "))       
b = float(input("Masukkan batas bawah: "))   
max_repetition = int(input("Masukkan jumlah iterasi maksimal: "))
accuracy = float(input("Masukkan ketelitian: "))
```

Setelah menginput nilai ```batas atas```, ```batas bawah``` maka akan di cek apakah keduanya memenuhi kriteria dan syarat dari bolzano <br />
```R
if func(a) * func(b) > 0:
    print('Numbers do not meet Bolzano\'s criteria')
    exit() #jika tidak memenuhi kriteria bolzano, akan keluar dari program
```

Didalam perulangan sebanyak iterasi maksimal, kita akan mencari ```middle point```, ```fa``` dan ```fmp```<br />
```R
for i in range(max_repetition):
    # Mencari middle point
    mp = (a + b)/2
    fa = func(a)
    fmp = func(mp)

    # Output hasil sesuai iterasi
    print(str(i + 1)+'\t    % 10.5f\t    % 10.5f\t    % 10.5f\t    % 10.5f\t    % 10.5f\t' %(a, b, fa, mp, fmp))

    if np.abs(func(mp)) < accuracy: #jika nilai fmp lebih kecil dari ketelitian, akan keluar dari program
        print('---------------------------------------------------------------------------------------')
        print('The value of root is : '+ str(mp))
        exit()

    if func(a) * func(mp) < 0:
        b = mp

    else: 
        a = mp
```

Jika pada suatu kasus nilai fmp tidak lebih kecil dari ketelitian, namun sudah sampai pada iterasi maksimum, maka program akan mencetak "Maximum Iteration!" yang menandakan sudah mencapai iterasi maksimum. Sehingga akan dicetak nilai akar dan keluar dari program.<br />
```R
if i == max_repetition - 1:
    print('\n\nMaximum Iteration!')
    print('The value of root is : '+ str(mp))
```

Pada program ini akan menamplikan plot grafik terlebih dahulu sebelum mencetak iterasi dan nilai akar, adapun source code untuk men-generate tabel dari persamaan yang digunakan: <br />
```R
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.plot(x, y, 'r')

plt.show() #untuk menampilkan grafik
```

Sehingga output setelah dijalankan akan terlihat seperti ini:
![image](https://user-images.githubusercontent.com/90106865/198066761-dc585522-e116-422a-b69b-2294722fd820.png) <br />
![image](https://user-images.githubusercontent.com/90106865/198066951-ec03e0e5-3dc4-4a59-8d2e-abd65ff01f58.png) <br />
