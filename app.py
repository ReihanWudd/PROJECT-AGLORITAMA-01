import json
import os

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
print("="*20+'CHOOSE ONE'+"="*20)
lgn = True

#untuk memasukkan nilai nilai register dari user
def register(regis):
    nama = input("nama         = ")
    umur = input("umur         = ")
    lahir = input("alamat        = ")
    email = input("email        = ")
    username = input("username     = ")
    password = input("password     = ")
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
    user_id = int(input('user number? ='))
    username = input("username     =")
    password = input("password      =")
    global lgn
    if user_regis[user_id]["username"] == username and user_regis[user_id]["password"] == password:
        print('Login success\n')  
        lgn = False
    else:
        print('maybe you put wrong character\ntry again!!')
        
#untuk menampung seluruh nilai/poin yang user pilih dan dijadikan satu untukhasil akhir
def hasil_daftar():
    print("_"*50)
    print("nama   :"+user_regis[user_id]["nama"]+"\nservis :"+servis_nilai+"\nPoli   :"+poli_nilai+"\ndokter :"+dokter_nilai+"\njadwal :"+jam_nilai)

#untuk menulis ulang data json atau fungsinya untuk menambahkan nilai baru yang di input kan
def readdata(file):
    with open(file,'w') as filenya:
        filenya.write(json.dumps(user_regis))

#untuk meload atau membaca file json itu sendiri
def loadfile(file):
    with open(file,'r') as output:
        if os.stat(file).st_size==0:
            return []
        else:
            _data = json.load(output)
            return _data

#untuk function yang menampilkan jadwal dokter, agar tidak menulis ulang pada setiap line nya
def displaytime(no1,no2,hari,jam):
    print('\n')
    print("| %2s | %-13s | %-15s |"%("no","hari","jam"))
    print("| %-2s | %-10s | %-15s |"%(no1,hari,jam))
    print("| %-2s | %-10s | %-15s |"%(no2,hari,jam))
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
        print("tidak ada jadwal")    
    
#fucntion untuk menampilkan daftar dokter yang ada pada setiap line, agar tidak menulis ulang pada setiap line nya
def displaydokter(dokter1,dokter2,hari,jam):
    print("_"*50)
    print("   DOKTER\n   1. "+dokter1+"\n   2. "+dokter2)
    pilih_dokter = int(input('Enter your Choise [1/2] = '))

    global dokter_nilai
    if pilih_dokter == 1:
        dokter_nilai =dokter1
        displaytime(1,2,hari,jam)

    elif pilih_dokter == 2:
        dokter_nilai = dokter2
        displaytime(1,2,hari,jam)
    
#membuat variabel untuk menampung file .json
DATA_USER = "data.json"
user_regis = loadfile(DATA_USER)


#ketika var lgn benar maka looping untuk pendaftaran akan bejalan
while lgn ==True:
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

#pertanyaan untuk memilih jasa yang disediiakan
print('_'*20+"WHAT CAN I HELP YOU?"+'_'*20)
print("""
    1. Appointment
    2. Pharmacy
    3. Health support
""")
pilih_servis = input('Enter your Choise [1/2/3] = ')

#looping untuk service program yang dipilih
servis_program = True
while servis_program:
    #kondisi keetika user memilih jasa Appointment
    if pilih_servis == "1":
        servis_nilai = "Appointment"
        print('Choose your complaint')
        print("""
            1. POLI MATA
            2. POLI KULIT
            3. POLI PENYAKIT DALAM
            4. POLI SARAF
        """)
        pilih_poli = int(input("Enter your Choise [1/2/3/4/5/6] = "))
        print('\n')
        #note : di displaydokter itu tinggal mengganti isinya saja ,untuk tampilan akan menyesuaikan isi itu
        if pilih_poli == 1:
            poli_nilai = "POLI MATA"
            displaydokter("dr. Putu Budi Sucitro","dr. Angel Benny","senin - kamis","07:30 - 13:00")
        elif pilih_poli == 2:
            poli_nilai = "POLI KULIT"
            displaydokter("dr. Ciko edo","dr. Angel Benny","senin - kamis","07:30 - 13:00")
        elif pilih_poli == 3:
            poli_nilai = "POLI PENYAKIT DALAM"
            displaydokter("dr. Putu Budi Sucitro","dr. Angel Benny","senin - kamis","07:30 - 13:00")
        elif pilih_poli == 4:
            poli_nilai = "POLI SARAF"
            displaydokter("dr. Putu Budi Sucitro","dr. Angel Benny","senin - kamis","07:30 - 13:00")
        else:
            print("POLI SUDAH TUTUP")

    elif pilih_servis == "2":
        servis_nilai = "Pharmacy"
        pass
    elif pilih_servis == "3":
        servis_nilai = "Health support"
        pass
    else:
        print("you entered the wrong number")