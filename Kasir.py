makanan={
    "Bakso Biasa":18000,
    "Bakso Special":25000,
    "Bakso Jumbo":50000,
    "Bakso Jumbo Special":80000,
    "Soto Lamongan":18000,
    "Soto Makassar":18000,
    "Sop Buntut":20000
}

def list_menu():
    print("============================")
    print("     Menu Yang Tersedia")
    print("----------------------------")
    for key, value in makanan.items():
        print("Nama  :",key)
        print("Harga : Rp.",value)
        print("----------------------------")

def tambah():
    print(">Tambah Menu Baru")
    input_baru=input(" Masukkan Nama : ")
    in_baru=int(input(" Masukkan Harga : Rp."))
    makanan[input_baru] = in_baru

def update():
    print(">Update Menu")
    input_baru=input(" Masukkan Nama : ")
    in_baru=int(input(" Update Harga : "))
    makanan[input_baru]=in_baru

def delete():
    del makanan [input("Nama menu yang ingin dihapus : ")]

def main_menu():
    while True:
        print("=======================")
        print("       Menu Admin")
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        print("1. List menu")
        print("2. Tambahkan")
        print("3. Update Harga")
        print("4. Hapus")
        print("5. Kembali ke Menu Awal")
        print("-----------------------")
        choice=input("Masukan pilihan : ")
        if choice=="1":
            list_menu()
            print("\nTekan [Enter] untuk kembali")
            input()
        elif choice=="2":
            tambah()
            print("\nTekan [Enter] untuk kembali")
            input()
        elif choice=="3":
            update()
            print("\nTekan [Enter] untuk kembali")
            input()
        elif choice=="4":
            delete()
            print("\nTekan [Enter] untuk kembali")
            input()
        elif choice=="5":
            print("Anda telah keluar")
            break
        else:
            print("Pilihan yang anda masukkan salah")
            main_menu()

def program_kasir():
    while True:
        print("=======================")
        print("       Menu User")
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        print("1.Pesan Makanan")
        print("2.Kembali Ke Menu Awal")
        print("-----------------------")
        pilih=input("Pilih Menu : ")
        print("")
        if pilih=="1":
            print("===================================")
            print("Selamat Datang di Warung Mas Dhimas")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("        Menu Yang Tersedia")
            print("-----------------------------------")
            for key, value in makanan.items():
                print("Nama  :",key)
                print("Harga : Rp.",value)
                print("-----------------------------------")
            a=makanan[input("Ketik Pesanan anda? : ")]
            b=int(input("Jumlah pembelian : "))
            total=a*b
            print("Total Harga: Rp.", total)
            uang=int(input("Uang Tunai Pembeli = Rp. "))
            kembalian=int(uang-total)
            print("======================================")
            print("Pembayaran Tunai : Rp.",uang)
            print("Total Pembayaran : Rp.",total)
            print("Kembalian        : Rp.",kembalian)
            print("======================================")
            print("\nTekan [Enter] untuk kembali")
            input()
        elif pilih=="2":
            print("Anda Telah Keluar")
            break
        else:
            print("Pilihan yang anda masukkan salah")
            program_kasir()

while True:
    print("===================================")
    print("             Menu Awal")
    print("-----------------------------------")
    print("1. Menu Admin")
    print("2. User")
    print("0. Keluar dari program")
    print("-----------------------------------")
    pilih=input("Pilih Menu : ")
    print("-----------------------------------")
    if pilih=="1":
        def admin():
            name=input("Masukkan Username : ")
            if name=="DhimasEko":
                print("")
            else:
                print("Username salah")
                admin()
            passward=input("Masukkan Kode Admin : ")
            if passward=="068":
                main_menu()
            else:
                print("Kode yang anda masukkan salah")
                admin()
        admin()
    elif pilih=="2":
        def user():
            print("Masukkan Kode ini : 210")
            passward=input("Masukkan Kode diatas : ")
            if passward=="210":
                print("")
                program_kasir()
            else:
                print("Kode yang anda masukkan salah")
                user()
        user()
    elif pilih=="0":
        break
    else:
        print("Menu yang anda pilih salah!!!")