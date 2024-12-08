import pandas as pd
import json

# Fungsi untuk mengonversi Excel ke JSON dengan struktur tetap
def excel_to_json(input_file, output_file):
    try:
        # Membaca file Excel
        df = pd.read_excel(input_file, sheet_name=None, dtype=str)  # Membaca semua sheet

        intents = []

        # Loop melalui setiap sheet
        for sheet_name, data in df.items():
            # Pastikan kolom yang dibutuhkan ada
            if 'tag' in data.columns and 'patterns' in data.columns and 'responses' in data.columns:
                for _, row in data.iterrows():
                    # Mengonversi pola dan respons menjadi list
                    patterns = row['patterns'].split('|') if pd.notna(row['patterns']) else []
                    responses = row['responses'].split('|') if pd.notna(row['responses']) else []

                    # Menambahkan intent ke dalam list
                    intents.append({
                        "tag": row['tag'],
                        "patterns": patterns,
                        "responses": responses
                    })

        # Menyimpan hasil ke file JSON dengan struktur tetap
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump({"intents": intents}, json_file, indent=4, ensure_ascii=False)

        print(f"Data berhasil dikonversi dari Excel ke JSON: {output_file}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Jalankan fungsi
input_excel_file = "intents.xlsx"  # File Excel yang telah diedit
output_json_file = "intents.json"  # File JSON hasil konversi
excel_to_json(input_excel_file, output_json_file)
