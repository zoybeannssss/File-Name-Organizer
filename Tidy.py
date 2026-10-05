import os

def format_title_case(text):
    # Memecah kata berdasarkan spasi dan mengubah huruf pertama tiap kata jadi kapital
    # Fungsi bawaan .title() bisa bikin karakter setelah angka ikut kapital/aneh, 
    # jadi kita pakai kombinasi split & capitalize biar angka/simbol tetap aman!
    words = text.split(" ")
    formatted_words = []
    
    for word in words:
        if word:
            # .capitalize() cuma ngubah huruf pertama jadi KAPITAL, sisanya huruf kecil
            formatted_words.append(word.capitalize())
        else:
            formatted_words.append("")
            
    return " ".join(formatted_words)

def rename_files_to_titlecase():
    folder_path = os.path.dirname(os.path.abspath(__file__))
    current_script = os.path.basename(__file__)
    
    count = 0
    print("🚀 Memulai proses merapikan nama file ke Title Case...\n")
    
    for filename in os.listdir(folder_path):
        # Abaikan file temporary bawaan Excel (~$)
        if filename.startswith("~$"):
            continue

        file_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(file_path) and filename != current_script:
            original_name, ext = os.path.splitext(filename)
            
            # Format nama file jadi Title Case (Simbol & Angka tidak terganggu)
            new_name = format_title_case(original_name)
            
            # Cek apakah ada perubahan nama
            if original_name != new_name:
                
                # 1. RENAME SEMENTARA (Bypass limitasi Windows Explorer)
                temp_filename = f"TEMPORARY_NAME_{count}{ext}"
                temp_file_path = os.path.join(folder_path, temp_filename)
                
                os.rename(file_path, temp_file_path)
                
                # 2. RENAME KE HASIL TITLE CASE
                final_filename = new_name + ext
                final_file_path = os.path.join(folder_path, final_filename)
                
                os.rename(temp_file_path, final_file_path)
                
                print(f"✅ Renamed: '{filename}' ➡️ '{final_filename}'")
                count += 1

    print(f"\n🎉 SELESAI! Total {count} file berhasil dirapikan!")

if __name__ == "__main__":
    rename_files_to_titlecase()