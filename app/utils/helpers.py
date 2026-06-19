# app/utils/helpers.py
import random
import string

def generate_short_code(length: int = 6) -> str:
    """
    Fungsi untuk membuat string acak sepanjang 'length' karakter.
    Menggabungkan huruf besar, huruf kecil, dan angka (A-Z, a-z, 0-9).
    """
    # Kumpulan karakter yang akan diacak
    characters = string.ascii_letters + string.digits 
    
    # Mengacak dan menggabungkan menjadi satu string
    short_code = "".join(random.choice(characters) for _ in range(length))
    
    return short_code