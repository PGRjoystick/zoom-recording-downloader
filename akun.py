from dateutil.parser import parse
import datetime
from datetime import date
from dateutil import relativedelta
from datetime import date, timedelta

# HAPUS TANDA # SEBELUM VARIABEL UNTUK MENGAKTIFKAN
# DAN BERI TANDA # SEBELUM VARIABEL UNTUK MEMATIKAN

# UNTUK MEDAPATKAN TOKEN JWT, LOGIN DAN AMBIL DI https://marketplace.zoom.us/develop/create

##################################
##      LOKASI PENYIMPANAN      ##
##################################
# Ubah bagian ini untuk menentukan lokasi tempat penyimpanan rekaman video

# bisa folder root langung jika script dan folder nya berada di lokasi yang sama
# atau bisa tulis lokasi lengkap seperti ini 
#          DOWNLOAD_DIRECTORY = r'C:\Users\pgrjo\Desktop\account1'

#account1@company.com
DOWNLOAD_DIRECTORY = r'account1'

#account2@company.com 
#DOWNLOAD_DIRECTORY = r'account2'


#######################################
##      RENTANG TANGGAL REKAMAN      ##
#######################################
# Sesuaikan tanggal di bawah ini pada rekaman zoom yang paling lama
RECORDING_START_YEAR = 2020
RECORDING_START_MONTH = 6
RECORDING_START_DAY = 17

# Jika ingin Mendownload sampai tanggal hari ini, hapus tanda #
RECORDING_END_DATE = date.today()

# Sebaliknya Jika ingin mendownload sampai tanggal yg di tentukan
# Hapus tanda # dan tentukan tanggal nya dan berikan tanda # di variabel atas, Format YYYY, MM, DD
#RECORDING_END_DATE = date(2021, 8, 1)

#############################
##      DAFTAR AKUN        ##
#############################
# AKUN HARUS AKTIF PADA SALAH SATU AKUN DIBAWAH
# DAN TIDAK DAPAT DI AKTIFKAN SECARA BERSAMAAN SEKALIGUS

#account1@company.com
JWT_TOKEN = 'PASTE_TOKEN_DISINI'

#account2@company.com
#JWT_TOKEN = 'PASTE_TOKEN_DISINI'

#account3@company.com
#JWT_TOKEN = 'PASTE_TOKEN_DISINI'
