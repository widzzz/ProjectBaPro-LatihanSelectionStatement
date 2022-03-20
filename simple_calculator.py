# simple_calculator

# fungsi menu
def menu():
    info = ('===== Kalkulator Sederhana =====\n'
			'1=> Tambah  (+)\n'
			'2=> Kurang  (-)\n'
			'3=> Kali    (*)\n'
			'4=> Bagi    (/)\n'
			'5=> Pangkat (^)\n'
			'6=> KELUAR')
    print(info)

    # input operator pilihan user
    choice = input()
    return choice

# fungsi untuk konfirmasi keluar program
def keluar():
    exitConfirm = input("Apakah anda ingin mengulang? (Y/N)")
    if (exitConfirm == 'Y' or exitConfirm == 'y'):
        # value dari exitConfirm dihapus agar dapat digunakan untuk selanjutnya
        del exitConfirm
        core()
    elif (exitConfirm == 'N' or exitConfirm == 'n'):
        exit()
    else:
        print("Input tidak diketahui")

# fungsi utama untuk perhitungan kalkulator
def core():
    # nilai dari menu() diambil
    operator = menu()
    if operator == '1':
        bil1 = float(input("Masukkan bilangan a :"))
        bil2 = float(input("Masukkan bilangan b :"))
        print(bil1 + bil2)
        # memanggil fungsi untuk konfirmasi pengulangan
        keluar()
    elif operator == '2':
        bil1 = float(input("Masukkan bilangan a :"))
        bil2 = float(input("Masukkan bilangan b :"))
        print(bil1 - bil2)
        keluar()
    elif operator == '3':
        bil1 = float(input("Masukkan bilangan a :"))
        bil2 = float(input("Masukkan bilangan b :"))
        print(bil1 * bil2)
        keluar()
    elif operator == '4':
        bil1 = float(input("Masukkan bilangan a :"))
        bil2 = float(input("Masukkan bilangan b :"))
        print(bil1 / bil2)
        keluar()
    elif operator == '5':
        bil1 = float(input("Masukkan bilangan a :"))
        bil2 = float(input("Masukkan bilangan b :"))
        print(bil1 ** bil2)
        keluar()
    else:
        exit()

# panggil core untuk memulai program
core()