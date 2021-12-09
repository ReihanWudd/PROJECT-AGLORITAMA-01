import json
import os
import time
import random


os.system('cls')
print("""██     ██ ███████ ██       ██████  ██████  ███    ███ ███████ 
██     ██ ██      ██      ██      ██    ██ ████  ████ ██      
██  █  ██ █████   ██      ██      ██    ██ ██ ████ ██ █████   
██ ███ ██ ██      ██      ██      ██    ██ ██  ██  ██ ██      
 ███ ███  ███████ ███████  ██████  ██████  ██      ██ ███████ 
                                                              
                                                              """)
print("""████████╗ ██████╗      ██████╗ ██╗   ██╗██████╗     ███████╗███████╗██████╗ ██╗   ██╗██╗ ██████╗███████╗███████╗
╚══██╔══╝██╔═══██╗    ██╔═══██╗██║   ██║██╔══██╗    ██╔════╝██╔════╝██╔══██╗██║   ██║██║██╔════╝██╔════╝██╔════╝
   ██║   ██║   ██║    ██║   ██║██║   ██║██████╔╝    ███████╗█████╗  ██████╔╝██║   ██║██║██║     █████╗  ███████╗
   ██║   ██║   ██║    ██║   ██║██║   ██║██╔══██╗    ╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██║██║     ██╔══╝  ╚════██║
   ██║   ╚██████╔╝    ╚██████╔╝╚██████╔╝██║  ██║    ███████║███████╗██║  ██║ ╚████╔╝ ██║╚██████╗███████╗███████║
   ╚═╝    ╚═════╝      ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚═╝ ╚═════╝╚══════╝╚══════╝
                                                                                                                """)

lgn = True

#untuk memasukkan nilai nilai register dari user
def register(regis):
    nama = input("Nama         = ")
    umur = input("Umur         = ")
    lahir = input("Alamat        = ")
    email = input("Email        = ")
    username = input("Username     = ")
    password = input("Password     = ")
    regis.append({
        "nama":nama,
        "umur" :umur,
        "lahir": lahir,
        "email": email,
        "username" : username,
        "password" :password
    })
    return regis

#untuk menverifikasi inputan login dengan data register(.json)

def ceklogin():
    print("Amount of User Account",len(user_regis)-1)
    global user_id
    global username
    global password
    user_id = int(input('User number? ='))
    username = input("Username     =")
    password = input("Password      =")
    global lgn
    if user_regis[user_id]["username"] == username and user_regis[user_id]["password"] == password:
        print('Login success\n')  
        lgn = False
    else:
        print('You entered the wrong character\nPlease try again!!')

#untuk menampung seluruh nilai/poin yang user pilih dan dijadikan satu untukhasil akhir
def hasil_daftar():
    print("_"*50)
    print("Nama   :"+user_regis[user_id]["nama"]+"\nServis :"+servis_nilai+"\nPoli   :"+poli_nilai+"\nDokter :"+dokter_nilai+"\nJadwal :"+jam_nilai)

#untuk menulis ulang data json atau fungsinya untuk menambahkan nilai baru yang di input kan
def readdata(file):
    with open(file,'w') as filenya:
        filenya.write(json.dumps(user_regis))

def readdatafinal(file):
    with open(file,'w') as filenya_janji:
        filenya_janji.write(json.dumps(janji_regis))

#untuk meload atau membaca file json itu sendiri
def loadfile(file):
    with open(file,'r') as output:
        if os.stat(file).st_size==0:
            return []
        else:
            _data = json.load(output)
            return _data
#untuk function yang menampilkan jadwal dokter, agar tidak menulis ulang pada setiap line nya
def displaytime(no1,no2,hari,hari2,jam,jam2):
    print('\n')
    print("="*56)
    print("| {:^3} | {:^18} | {:^25} |".format("No","Hari","Jam"))
    print("-"*56)
    print(f"| {no1:^3} | {hari:^18} | {jam:^25} |")
    print(f"| {no2:^3} | {hari2:^18} | {jam2:^25} |")
    print("="*56)
    pilih_jadwal = int(input("Choose your appointment [1/2] = "))
    global servis_program
    global jam_nilai

    if pilih_jadwal == 1:
        jam_nilai = str(hari)+" "+str(jam)
        hasil_daftar()
        servis_program = False

    elif pilih_jadwal == 2:
        jam_nilai = str(hari)+" "+str(jam)
        hasil_daftar()
        servis_program = False

    else:
        print("No Schedule")    
    
#fucntion untuk menampilkan daftar dokter yang ada pada setiap line, agar tidak menulis ulang pada setiap line nya
def displaydokter(dokter1,dokter2,hari,hari2,jam,jam2):
    print("_"*50)
    print("   DOKTER\n   1. "+dokter1+"\n   2. "+dokter2)
    pilih_dokter = int(input('Enter your Choise [1/2] = '))

    global dokter_nilai
    if pilih_dokter == 1:
        dokter_nilai =dokter1
        displaytime(1,2,hari,jam,hari2,jam2)

    elif pilih_dokter == 2:
        dokter_nilai = dokter2
        displaytime(1,2,hari,jam,hari2,jam2)

#untuk membuat countdown waktu/timer
def countdown(w):
    while w:
        mins, secs = divmod(w, 60)
        timer = '{}{:02d}:{:02d}'.format("Wait for your medicine ",mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        w -= 1
    
    print('Your medicine is ready, Thanks for your puchase!')
    

def shoowobat(sirup1,sirup2,pil1,pil2,jmlsir1,jmlsir2,jmlpil1,jmlpil2):

    global nilai_sirup1,nilai_sirup2,nilai_pil1,nilai_pil2,obat_tersedia
    nilai_sirup1 = sirup1
    nilai_sirup2 = sirup2
    nilai_pil1 = pil1
    nilai_pil2 = pil2
    print("="*67)
    print("| {:^5} | {:^18} | {:^5} | {:^18} | {:^5} |".format("No","Sirup","Stok","Tablet/Kapsul","Stok"))
    print("="*67)
    print(f"| {1:^5} | {sirup1:^18} | {jmlsir1:^5} | {pil1:^18} | {jmlpil1:^5} |")
    print("| {:^5} | {:^18} | {:^5} | {:^18} | {:^5} |".format("price",'5000','-','8000','-'))
    print(f"| {3:^5} | {sirup2:^18} | {jmlsir2:^5} | {pil2:^18} | {jmlpil2:^5} |")
    print("| {:^5} | {:^18} | {:^5} | {:^18} | {:^5} |".format("price",'3000','-','11000','-'))
    print("="*67)
    return sirup1,sirup2,pil1,pil2
  
# print("Nama   :"+user_regis[user_id]["nama"]+"\nServis :"+servis_nilai+"\nPoli   :"+poli_nilai+"\nDokter :"+dokter_nilai+"\nJadwal :"+jam_nilai)
def regisjanji(janji):
    janji.append({
        "nama":user_regis[user_id]["nama"],
        "servis": servis_nilai,
        "Poli": poli_nilai,
        "Dokter": dokter_nilai,
        "Jadwal": jam_nilai
    })
    print("="*50)
    return janji

def showapp():
    print("="*48+"\n"+"Nama : "+janji_regis[janji_ke]["nama"]+"\n"+"Dokter : "+janji_regis[janji_ke]["Dokter"]+"\n"+"Jadwal : "+janji_regis[janji_ke]["Jadwal"]+"\n"+"="*48)



def delete(delvar):
    print("Total Jadwal anda :"+str(len(delvar)))
    global janji_ke
    try:
        jan_input = int(input("Janji ke? = "))
        janji_ke = jan_input - 1
        showapp()
    except:
        print("nomor salah / tidak ada")
    sure = input("Are you sure? [y/n]= ")
    global pilih_servis
    global servis_program
    if sure == "y":
        pilih_servis = "1"
        delvar.pop(0)
        return delvar    
    
    elif sure == "n":
        pilih_kluar = int(input("lajut/keluar 1/2 = "))
        if pilih_kluar == 1:
            pilih_servis = "1"
        elif pilih_kluar == 2:
            servis_program = False
    
def keluar():
    ask_exit = True
    while ask_exit:
        tanya_exit = input("EXIT ? y/n = ")
        global servis_program 
        global main_choise
        if tanya_exit == "y":
            servis_program = False
            main_choise = False
            ask_exit = False
        elif tanya_exit == "n":
            servis_program = False
            ask_exit = False
        else:
            print("your insert wrong word!!")

#membuat variabel untuk menampung file .json

DATA_USER = "data.json"
user_regis = loadfile(DATA_USER)

DATA_JANJI = "janji.json"
janji_regis = loadfile(DATA_JANJI)


#ketika var lgn benar maka looping untuk pendaftaran akan bejalan
while lgn ==True:
    print("="*20+'CHOOSE ONE'+"="*20)
    print(" 1. Log in")
    print(" 2. Sign up")
    pil_masuk = input("1/2 = ")
    if pil_masuk == "1":
        print("="*15+" LOG IN "+"="*15)
        ceklogin()

    elif pil_masuk == "2":
        print("="*15+" REGISTER "+"="*15)
        user_regis = register(user_regis)
        readdata(DATA_USER)
        print('> Your Account has been successfully registered')
        print("> Your Account is Number [",len(user_regis)-1,"]")
        print("\n")
    else:
        print("you entered the wrong number")

jmlsir1 = 20
jmlsir2 = 20
jmlpil1 = 20
jmlpil2 = 20
hrg_1a = 5000
hrg_1b = 8000
hrg_2a = 3000
hrg_2b = 11000

main_choise = True
while main_choise:

    #pertanyaan untuk memilih jasa yang disediiakan
    print('-'*20+"HELLO WHAT CAN I HELP YOU?"+'-'*20)
    print("""
                ===============================
                |    1. Appointment           |
                |    2. Pharmacy              |
                |    3. Cancel Appointment    |
                ===============================
    """)
    pilih_servis = input('                  Enter your Choise [1/2/3] = ')

    #looping untuk service program yang dipilih
    servis_program = True
    while servis_program:
        #kondisi keetika user memilih jasa Appointment
        if pilih_servis == "1":
            servis_nilai = "Appointment" 
            print('\n') 
            print('-'*20+'Choose your complaint'+'-'*20)
            print("""
               =================================
               |  1. POLI MATA                 |
               |  2. POLI KULIT                |
               |  3. POLI PENYAKIT DALAM       |
               |  4. POLI SARAF                |  
               ================================= 
            """)
            pilih_poli = int(input("                Enter your Choise [1/2/3/4] = "))
            print('\n')
            #note : di displaydokter itu tinggal mengganti isinya saja ,untuk tampilan akan menyesuaikan isi itu
            if pilih_poli == 1:
                poli_nilai = "POLI MATA"
                displaydokter("dr. Putu Budi Sucitro","dr. Angel Benny","Senin - Kamis","07:30 - 13:00","Jumat - Sabtu","18:00 - 21:00")
            elif pilih_poli == 2:
                poli_nilai = "POLI KULIT"
                displaydokter("dr. Ciko edo","dr. Angel Benny","Senin - Rabu","08:00 - 14:00","Jumat - Minggu","16:00 - 22:00")
            elif pilih_poli == 3:
                poli_nilai = "POLI PENYAKIT DALAM"
                displaydokter("dr. Jokowi Dodo" ,"dr. Megawati","Senin - Rabu","08:00 - 11.00","Kamis - Sabtu","15:00 - 19:00")
            elif pilih_poli == 4:
                poli_nilai = "POLI SARAF"
                displaydokter("dr. Wudd ","dr. Vania","Senin - Rabu","09;00 - 13:00","Jumat - Sabtu","19:00 - 22:00")
            else:
                print("POLI SUDAH TUTUP")

            janji_regis = regisjanji(janji_regis)
            readdatafinal(DATA_JANJI)

            keluar()
            
        elif pilih_servis == "2":
            servis_nilai = "Pharmacy"
            penyakit = input("""
        Your Complaint ?
        :  """)
            resep_dok = input("""
        Do you have a Doctor's Presciption ?
        [y/n]: """)
            if resep_dok == "y":
                hrg_resep = random.randint(5,300)
                print("total Rp."+str(hrg_resep)+"000")
                countdown(int(10))
                keluar()
            elif resep_dok == "n":
                blanja_obat = True
                while blanja_obat:
                    shoowobat("[a]Inzafnak","[a]Hufagrip","[b]Demacolin","[b]Pepsi",jmlsir1,jmlsir2,jmlpil1,jmlpil2)
                    pilih_obat = input("pilih obat,ex 2. [b]Demacolin -> 2b = ")
                    jumlah = int(input("Amount ="))

                    if jumlah > 20:
                        print("Out of stock")
                    elif pilih_obat == "1a" and jmlsir1 != 0:
                        jmlsir1 -= jumlah
                        
                        print("Your "+penyakit+" Medicine "+nilai_sirup1)
                        print("total Rp." +str(hrg_1a * jumlah))
                        print("Purchase has been completed")
                    elif pilih_obat == "1b" and jmlpil1 != 0:
                        jmlpil1 -= jumlah
                        
                        print("Your "+penyakit+" Medicine "+nilai_pil1)
                        print("total Rp." +str(hrg_1b * jumlah))
                        print("Purchase has been completed")
                    elif pilih_obat == "2a" and jmlsir2 != 0:
                        jmlsir2 -= jumlah
                        
                        print("Your "+penyakit+" Medicine "+nilai_sirup2)
                        print("total Rp." +str(hrg_2a * jumlah))
                        print("Purchase has been completed")
                    elif pilih_obat == "2b" and jmlpil2 != 0:
                        jmlpil2 -= jumlah
                    
                        print("Your "+penyakit+" Medicine "+nilai_pil2)
                        print("total Rp." +str(hrg_2b * jumlah))
                        print("Purchase has been completed")
                    else:
                        print("you insert wrong input !!")

                    while True:
                        blanja_obat_exit = input("Buy again? y/n = ")
                        if blanja_obat_exit == "y":
                            break
                        elif blanja_obat_exit == "n":
                            blanja_obat = False
                            keluar()
                            break
                    # shoowobat("[a]Inzafnak","[a]Hufagrip","[b]Demacolin","[b]Pepsi",jmlsir1,jmlsir2,jmlpil1,jmlpil2)
                
        elif pilih_servis == "3":
            janji_regis = delete(janji_regis)
            readdatafinal(DATA_JANJI)
            keluar()
        else:
            print("You entered the wrong number")
            keluar()

print("""████████ ██   ██  █████  ███    ██ ██   ██ ███████ 
   ██    ██   ██ ██   ██ ████   ██ ██  ██  ██      
   ██    ███████ ███████ ██ ██  ██ █████   ███████ 
   ██    ██   ██ ██   ██ ██  ██ ██ ██  ██       ██ 
   ██    ██   ██ ██   ██ ██   ████ ██   ██ ███████ 
                                                   
                                                   """)
