import requests
import os
import sys

# --- Konfigurasi ---
# Mengambil konfigurasi dari environment variables
API_URL = os.getenv("prodURL")
TOKEN = os.getenv("tokenP")
# Nama file yang berisi daftar ID
IDS_FILE = "ids.txt"

# --- Fungsi Utama ---
def main():
    """
    Fungsi utama untuk menjalankan skrip.
    """
    # 1. Validasi environment variables
    if not API_URL or not TOKEN:
        print("❌ Error: Pastikan environment variable 'prodURL' dan 'tokenP' sudah di-set.")
        sys.exit(1)  # Keluar dari skrip dengan status error

    # 2. Baca daftar ID dari file
    try:
        with open(IDS_FILE, 'r') as f:
            # Membersihkan setiap baris dari spasi/baris baru yang tidak perlu
            ids = [line.strip() for line in f if line.strip()]
        print(f"✅ Berhasil memuat {len(ids)} ID dari file '{IDS_FILE}'.")
    except FileNotFoundError:
        print(f"❌ Error: File '{IDS_FILE}' tidak ditemukan. Silakan buat file tersebut.")
        sys.exit(1)

    # Payload yang akan dikirim, didefinisikan sekali di luar loop
    payload = {"monitoringCycleId": 9}

    # Gunakan session untuk efisiensi koneksi dan menjaga header
    with requests.Session() as s:
        s.headers.update({'Authorization': f'Bearer {TOKEN}'})

        print("\n🚀 Memulai proses update status...")
        # 3. Iterasi melalui setiap ID dan kirim request
        for an_id in ids:
            try:
                # Membentuk URL lengkap untuk setiap ID
                full_url = f'{API_URL.rstrip("/")}/activities/{an_id}'

                print(f"   -> Mengirim PATCH request untuk ID: {an_id}...")

                # Mengirim request PATCH dengan data JSON
                response = s.patch(full_url, json=payload, timeout=10)  # Tambahkan timeout

                # Memeriksa apakah ada error HTTP (spt. 404, 500, 401)
                response.raise_for_status()

                print(f"   ✅ Sukses! ID: {an_id}, Status: {response.status_code}\n")

            except requests.exceptions.HTTPError as e:
                # Error spesifik dari server (cth: 404 Not Found, 403 Forbidden)
                print(f"   ❌ Gagal! ID: {an_id}, Error HTTP: {e.response.status_code} {e.response.reason}")
                print(f"      Response Body: {e.response.text}\n")
            except requests.exceptions.RequestException as e:
                # Error umum (cth: masalah koneksi, timeout)
                print(f"   ❌ Gagal! ID: {an_id}, Error Koneksi: {e}\n")


# --- Titik Masuk Skrip ---
if __name__ == "__main__":
    main()