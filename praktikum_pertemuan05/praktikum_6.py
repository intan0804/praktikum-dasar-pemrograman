def konversi_menit_ke_detik(menit):
    """Mengonversi waktu dari menit ke detik.
    
    Parameter:
        menit (int/float): jumlah menit yang akan dikonversi.
        
    Returns:
        int/float: jumlah detik (menit dikali 60). 
    """
    detik = menit * 60
    return detik

print(konversi_menit_ke_detik(3))
print(konversi_menit_ke_detik.__doc__)