import random
import string
import requests
import time
from datetime import datetime
import json
def generate_random_number():
    num_digits = random.choice([4, 6])  # Memilih antara 4 atau 6 digit
    if num_digits == 4:
        return random.randint(1000, 9999)  # Angka acak dengan 4 digit
    elif num_digits == 6:
        return random.randint(100000, 999999)  # Angka acak dengan 6 digit
def get_random_string():
    kode = generate_random_number()
    current_date = datetime.now().strftime("%d-%m-%Y %H:%M")
    string1 = "Jangan memberikan kode ini ke siapapun! Kode OTP untuk akun Kanggo kamu adalah: "+str(kode)
    string2 = str(kode)+" is your Grab Activation Code (GAC). It expires in 2 minutes. Do not share it with anyone."
    string3 = "First Media OTP : "+str(kode)+" RefNo : REF000000"+str(kode)
    string4 = "Telegram code: "+str(kode)+" You can also tap on this link to log in: https://t.me/login/"+str(kode)
    string5 = "Kode verifikasi bersifat RAHASIA. Jangan informasikan ke siapa pun, termasuk ke pihak Jenius. Gunakan kode berikut untuk melanjutkan registrasi Jeniusmu: "+str(kode)
    string6 = "Klik Indomaret - JANGAN BERIKAN KODE INI KE SIAPAPUN. Kode berlaku dalam 5 menit. Kode verifikasi Anda: "+str(kode)
    string7 = "JANGAN BERIKAN KODE INI KE SIAPAPUN, TERMASUK PIHAK LINKAJA. WASPADA PENIPUAN! Kode transaksi LinkAja: "+str(kode)+". Hubungi 150911 jika tidak meminta kode ini."
    string8 = "<#> Use "+str(kode)+" as OTP to log in to your Gojek account. NEVER SHARE OTP with anyone. Not even Gojek. 4PKeZqV9ubl"
    string9 = "JANGAN BAGIKAN kode ini kepada siapa pun, TERMASUK TIM SHOPEE. UNTUK UPDATE REKENING BANK, gunakan "+str(kode)+". Berlaku selama 15 menit."
    string10 = "<#> Tokopedia - JANGAN MEMBERITAHU KODE INI KE SIAPAPUN termasuk pihak Tokopedia. WASPADA TERHADAP KASUS PENIPUAN! KODE RAHASIA untuk masuk:"+str(kode)+" M4aSdJWqI8x"
    string11 = "Hindari penipuan! Jangan berikan kode OTP kepada siapa pun. Kode OTP DANA: "+str(kode)+" berlaku selama 10 menit."
    string12 = "OTP: "+str(kode)+" berlaku 5 menit. JAGA KERAHASIAAN KODE KAMU. JANGAN BERI TAHU SIAPAPUN. Jika bukan transaksi kamu hub haloblu 1500668"
    string13 = "AWAS PENIPUAN.JGN BERI KODE INI KE SIAPAPUN BAHKAN PIHAK BANK. Berlaku 5 mnt. KODE OTP Verifikasi buka rekening Bank Syariah Indonesia: "+str(kode)
    string14 = "<#> Kode verifikasi Anda adalah "+str(kode)+". Jangan berikan kode ini kepada orang lain. R8OT1Cwy6FW"
    string15 = "<#> "+str(kode)+" adalah kode verifikasi Disney+ Hotstar Anda. Selamat menonton! 0P1dUnbmS/K"
    string16 = "Dear Customer, your one-time password (OTP) is "+str(kode)
    string17 = "BEWARE OF SCAMS! DO NOT give this code to ANYONE, including JAGO. Verification code: YLb-"+str(kode)+" valid for 5 minutes. Call 1500 746 for help. 2r1u/G+ijD8"
    string18 = "bjb Mobile "+str(current_date)+" OTP Ubah m-PIN bjb Mobile Anda "+str(kode)+". valid untuk 15 Menit. JANGAN PERNAH MEMBERIKAN INFORMASI OTP INI PADA SIAPAPUN."
    string19 = "Kode Verifikasi OVO: "+str(kode)+" JANGAN BERIKAN KODE RAHASIA INI KEPADA SIAPA PUN, TERMASUK PIHAK YANG MENGAKU DARI OVO Hubungi 1500696 untuk bantuan"
    string20 = "Klik link https://brimo.bri.co.id/app/login?code= untuk melanjutkan login BRImo. Jangan berikan sms ini kepada siapapun"
    strings = [string1, string2, string3,string4,string5,string6,string7,string8,string9,string10,string11,string12,string13,string14,string15,string16,string17,string18,string19,string20]  # Memasukkan string ke dalam list
    pilihan = random.choice(strings)
    if pilihan == string20:
        return "Klik link https://ib.bri.co.id/ib-bri/login?code="+str(generate_random_string(32))+" untuk melanjutkan login BRImo. Jangan berikan sms ini kepada siapapun"
    else:
        return pilihan
    
def generate_random_string(length):
    characters = string.ascii_letters + string.digits  # Membuat kumpulan karakter dari huruf besar, huruf kecil, dan angka
    return ''.join(random.choice(characters) for _ in range(length))
def index_get():
    i = 0
    while True:
        body = get_random_string()
        url = "https://api.telegram.org/bot6789674798:AAECBXCREVlpNF4aX3x94tHiec5uJiR1FGA/sendMessage?parse_mode=markdown&chat_id=6715338355&text=" + body
        result = curl(url)
        print(result)
        decoded_data = json.loads(result)
        if decoded_data["ok"]:
            print("sukses : " + str(i + 1) + " body :" + body)
            # time.sleep(0.01)
        else:
            print("gagal : " + str(i + 1))
            print("akan dimulai : "+str(decoded_data["parameters"]["retry_after"])+" detik lagi")
            time.sleep(decoded_data["parameters"]["retry_after"])
        i += 1
          # Menambahkan jeda selama 1 detik

def curl(url):
    # userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'
    userAgent = 'Mozilla/5.0 (Linux; Android 10; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Mobile Safari/537.36'
    headers = {'User-Agent': userAgent}
    response = requests.get(url, headers=headers)
    return response.content

index_get()
