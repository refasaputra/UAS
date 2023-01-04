from view.input_nilai import masukan_data, cari_hapus, cari_ubah
from view.view_nilai import tampilkan
from model.daftar_nilai import cari_data





while True:
    print('\n|================|')
    print('|  Pilihan Menu  |')
    print('|================|')
    print('\n1. Tambah Data')
    print('2. Hapus Data')
    print('3. Ubah Data')
    print('4. Cari Data')
    print('5. Lihat Semua Data')
    print('6. Keluar ')

    pilihan = input('\nMasukan Pilihan Menu = ')

    if pilihan == '1':
        masukan_data()
    elif pilihan == '2':
        cari_hapus()
    elif pilihan == '3':
        cari_ubah()
    elif pilihan == '4':
        cari_data()
    elif pilihan == '5':
        tampilkan()
    elif pilihan == '6':
        break
    else:
        print('Masukan Pilihan yang Benar!!')
