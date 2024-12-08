import json
import pandas as pd

# Membaca file intents.json
with open('intents.json', 'r') as file:
    data = json.load(file)

# Daftar tag yang akan digabungkan ke satu kategori "Gabungan"
combined_tags = [
    "Pengurus_TP_PKK_Anggota",
    "Perangkat_Desa",
    "Lembaga_Kemasyarakatan_BPD",
    "Daftar_Hotel",
    "Layanan_Masyarakat_Borobudur",
    "Transport",
    "Daftar_Wisata",
    "Kuliner",
    "Daftar_Agama",
    "Daftar_Wisata"
]

# Daftar awalan untuk kategori lainnya
categories = {
    "Mata_Pencaharian": [],
    "Agama": [],
    "Pengurus_TP": [],
    "Perangkat_Desa": [],
    "Lembaga_Kemasyarakatan": [],
    "Hotel": [],
    "Layanan": [],
    "Transport": [],
    "Wisata": [],
    "Kuliner": [],
    "Jumlah_Penduduk": [],
    "Pendidikan_Terakhir": []
}

# Tambahkan kategori "Gabungan"
categories["Gabungan"] = []

# Mengelompokkan intents berdasarkan kategori
for intent in data["intents"]:
    tag = intent["tag"]
    if tag in combined_tags:
        categories["Gabungan"].append(intent)
    elif tag.startswith("Agama"):
        categories["Agama"].append(intent)
    else:
        categorized = False
        for prefix in categories.keys():
            if tag.startswith(prefix) and prefix != "Gabungan":
                categories[prefix].append(intent)
                categorized = True
                break
        if not categorized:
            # Jika tidak cocok dengan kategori apa pun, masukkan ke kategori "Lainnya"
            if "Lainnya" not in categories:
                categories["Lainnya"] = []
            categories["Lainnya"].append(intent)

# Membuat file Excel dengan satu sheet per kategori
output_file = "intents.xlsx"
with pd.ExcelWriter(output_file) as writer:
    for category, intents in categories.items():
        df = pd.DataFrame(intents)

        # Mengonversi `patterns` dan `responses` ke format yang sesuai
        df['patterns'] = df['patterns'].apply(lambda x: "|".join(x) if isinstance(x, list) else x)
        df['responses'] = df['responses'].apply(lambda x: "|".join(x) if isinstance(x, list) else x)

        df.to_excel(writer, sheet_name=category[:30], index=False)  # Sheet name max 31 chars

print(f"File Excel berhasil dibuat: {output_file}")
