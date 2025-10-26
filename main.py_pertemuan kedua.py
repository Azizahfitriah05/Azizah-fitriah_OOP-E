# aplikasikan instance variable pada code pertemuan lalu

class kendaraan :
    def __init__ (self,merk,tahun,warna):
        self.merk = merk
        self.tahun = tahun 
        self.warna = warna
        
    def tampilkan_info (self):
        print(f"merk : {self.merk}")
        print(f"tahun : {self.tahun}")
        print(f"warna : {self.warna}")
        
motor = kendaraan(
    merk = "honda",
    tahun = 2020,
    warna = "putih"
    )
motor.tampilkan_info()