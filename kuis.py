import streamlit as st

# Mengatur judul halaman web
st.set_page_config(page_title="Kuis Agama & Bahasa Indonesia", page_icon="📝", layout="centered")

# Daftar soal, pilihan ganda, dan kunci jawaban
soal_kuis = [
    # --- AGAMA ISLAM (1-25) ---
    {"soal": "Siapakah nabi dan rasul terakhir dalam Islam?", "pilihan": ["A. Nabi Isa AS", "B. Nabi Musa AS", "C. Nabi Muhammad SAW", "D. Nabi Ibrahim AS"], "jawaban": "C"},
    {"soal": "Kitab suci yang diturunkan kepada Nabi Daud AS adalah...", "pilihan": ["A. Taurat", "B. Zabur", "C. Injil", "D. Al-Qur'an"], "jawaban": "B"},
    {"soal": "Ada berapa jumlah Rukun Iman?", "pilihan": ["A. 5", "B. 6", "C. 7", "D. 4"], "jawaban": "B"},
    {"soal": "Malaikat yang bertugas mencabut nyawa adalah...", "pilihan": ["A. Jibril", "B. Mikail", "C. Izrail", "D. Israfil"], "jawaban": "C"},
    {"soal": "Shalat fardhu yang dilaksanakan pada pagi hari sebelum terbit matahari adalah...", "pilihan": ["A. Dzuhur", "B. Ashar", "C. Maghrib", "D. Subuh"], "jawaban": "D"},
    {"soal": "Surah Al-Fatihah memiliki arti...", "pilihan": ["A. Pembukaan", "B. Sapi Betina", "C. Kemurnian", "D. Manusia"], "jawaban": "A"},
    {"soal": "Rukun Islam yang ketiga adalah...", "pilihan": ["A. Syahadat", "B. Shalat", "C. Zakat", "D. Puasa"], "jawaban": "C"},
    {"soal": "Peristiwa hijrahnya Nabi Muhammad SAW terjadi dari kota Makkah menuju kota...", "pilihan": ["A. Yaman", "B. Madinah", "C. Mesir", "D. Taif"], "jawaban": "B"},
    {"soal": "Malaikat yang bertugas meniup sangkakala pada hari kiamat adalah...", "pilihan": ["A. Malik", "B. Ridwan", "C. Israfil", "D. Munkar"], "jawaban": "C"},
    {"soal": "Sikap jujur dan dapat dipercaya merupakan arti dari sifat wajib...", "pilihan": ["A. Siddiq", "B. Amanah", "C. Tabligh", "D. Fathonah"], "jawaban": "B"},
    {"soal": "Surah terpendek dalam Al-Qur'an yang terdiri dari 3 ayat adalah...", "pilihan": ["A. Al-Ikhlas", "B. Al-Kautsar", "C. An-Nas", "D. Al-Falaq"], "jawaban": "B"},
    {"soal": "Berapakah jumlah rakaat shalat fardhu dalam sehari semalam?", "pilihan": ["A. 15", "B. 17", "C. 20", "D. 12"], "jawaban": "B"},
    {"soal": "Puasa wajib yang dilaksanakan umat Islam selama satu bulan penuh adalah puasa...", "pilihan": ["A. Senin-Kamis", "B. Syawal", "C. Ramadhan", "D. Arafah"], "jawaban": "C"},
    {"soal": "Asmaul Husna Al-Khaliq memiliki arti...", "pilihan": ["A. Maha Pengasih", "B. Maha Penyayang", "C. Maha Pencipta", "D. Maha Merajai"], "jawaban": "C"},
    {"soal": "Bulan pertama dalam kalender Hijriah adalah bulan...", "pilihan": ["A. Ramadhan", "B. Muharram", "C. Syawal", "D. Dzulhijjah"], "jawaban": "B"},
    {"soal": "Siapakah nama ibu kandung Nabi Muhammad SAW?", "pilihan": ["A. Aminah", "B. Khadijah", "C. Fatimah", "D. Halimah"], "jawaban": "A"},
    {"soal": "Hukum memandikan jenazah bagi umat Islam adalah...", "pilihan": ["A. Fardhu 'Ain", "B. Sunnah Muakkad", "C. Fardhu Kifayah", "D. Mubah"], "jawaban": "C"},
    {"soal": "Tempat dikumpulkannya seluruh manusia setelah hari kebangkitan dinamakan Padang...", "pilihan": ["A. Arafah", "B. Mahsyar", "C. Karbala", "D. Uhud"], "jawaban": "B"},
    {"soal": "Sifat mustahil bagi Allah 'Al-Maut' artinya...", "pilihan": ["A. Mati", "B. Bodoh", "C. Lemah", "D. Tuli"], "jawaban": "A"},
    {"soal": "Siapakah sahabat Nabi yang mendapat julukan Al-Faruq?", "pilihan": ["A. Abu Bakar", "B. Umar bin Khattab", "C. Utsman bin Affan", "D. Ali bin Abi Thalib"], "jawaban": "B"},
    {"soal": "Zakat yang wajib dikeluarkan sebelum hari raya Idul Fitri dinamakan zakat...", "pilihan": ["A. Mal", "B. Fitrah", "C. Profesi", "D. Perniagaan"], "jawaban": "B"},
    {"soal": "Mengusap muka dan kedua tangan dengan debu suci sebagai pengganti wudhu disebut...", "pilihan": ["A. Istinja", "B. Mandi wajib", "C. Tayammum", "D. Berhias"], "jawaban": "C"},
    {"soal": "Nabi yang memiliki mukjizat tidak hangus dibakar api adalah Nabi...", "pilihan": ["A. Ibrahim AS", "B. Musa AS", "C. Isa AS", "D. Yusuf AS"], "jawaban": "A"},
    {"soal": "Perilaku mementingkan diri sendiri dan tidak peduli orang lain dalam Islam disebut...", "pilihan": ["A. Tawadhu", "B. Ananiah", "C. Ghibah", "D. Hasad"], "jawaban": "B"},
    {"soal": "Kitab suci Al-Qur'an diturunkan secara berangsur-angsur selama kurang lebih...", "pilihan": ["A. 10 tahun", "B. 23 tahun", "C. 30 tahun", "D. 5 tahun"], "jawaban": "B"},

    # --- BAHASA INDONESIA (26-50) ---
    {"soal": "Ide pokok yang mendasari sebuah cerita disebut...", "pilihan": ["A. Alur", "B. Latar", "C. Tema", "D. Amanat"], "jawaban": "C"},
    {"soal": "Manakah penulisan kata depan yang benar di bawah ini?", "pilihan": ["A. dirumah", "B. di rumah", "C. di-rumah", "D. dI rumah"], "jawaban": "B"},
    {"soal": "Lawan kata (antonom) dari kata 'Pakar' adalah...", "pilihan": ["A. Ahli", "B. Mahir", "C. Awam", "D. Pandai"], "jawaban": "C"},
    {"soal": "Kalimat yang memerlukan objek disebut kalimat...", "pilihan": ["A. Intransitif", "B. Transitif", "C. Majemuk", "D. Pasif"], "jawaban": "B"},
    {"soal": "Kata 'Apotek' merupakan bentuk baku dari kata...", "pilihan": ["A. Apotik", "B. Apotek", "C. Apoteka", "D. Aputik"], "jawaban": "A"},
    {"soal": "Berikut ini yang termasuk kata kerja (verba) adalah...", "pilihan": ["A. Cantik", "B. Berlari", "C. Rumah", "D. Sangat"], "jawaban": "B"},
    {"soal": "Bagian akhir dari sebuah teks prosedur biasanya berisi...", "pilihan": ["A. Tujuan", "B. Langkah-langkah", "C. Alat dan Bahan", "D. Penutup/Kesimpulan"], "jawaban": "D"},
    {"soal": "Majas yang membandingkan benda mati seolah-olah hidup seperti manusia disebut...", "pilihan": ["A. Hiperbola", "B. Metafora", "C. Personifikasi", "D. Litotes"], "jawaban": "C"},
    {"soal": "Persamaan bunyi di akhir baris pada puisi disebut...", "pilihan": ["A. Bait", "B. Rima", "C. Ritme", "D. Majas"], "jawaban": "B"},
    {"soal": "Kalimat yang isinya memberikan perintah untuk melakukan sesuatu disebut kalimat...", "pilihan": ["A. Deklaratif", "B. Interogatif", "C. Imperatif", "D. Berita"], "jawaban": "C"},
    {"soal": "Kata tanya yang digunakan untuk menanyakan alasan atau sebab adalah...", "pilihan": ["A. Bagaimana", "B. Mengapa", "C. Kapan", "D. Di mana"], "jawaban": "B"},
    {"soal": "Unsur intrinsik karya sastra yang merupakan pesan moral pembuat cerita dinamakan...", "pilihan": ["A. Tokoh", "B. Sudut pandang", "C. Amanat", "D. Plot"], "jawaban": "C"},
    {"soal": "Kata 'Bus' merupakan bentuk baku. Bentuk tidak bakunya adalah...", "pilihan": ["A. Bis", "B. Bas", "C. Boes", "D. Oto"], "jawaban": "A"},
    {"soal": "Gabungan dua kata atau lebih yang susunannya tetap dan memiliki arti kiasan disebut...", "pilihan": ["A. Frasa", "B. Klausa", "C. Ungkapan/Idiom", "D. Peribahasa"], "jawaban": "C"},
    {"soal": "Kalimat yang menggunakan tanda baca yang benar adalah...", "pilihan": ["A. Wah besar sekali rumah ini!", "B. Wah, besar sekali rumah ini!", "C. Wah besar sekali rumah ini.", "D. Wah, besar sekali rumah ini?"], "jawaban": "B"},
    {"soal": "Sinonim dari kata 'Egois' adalah...", "pilihan": ["A. Peduli", "B. Individualis", "C. Sosial", "D. Dermawan"], "jawaban": "B"},
    {"soal": "Teks yang berisi opini atau argumen penulis terhadap suatu isu disebut teks...", "pilihan": ["A. Deskripsi", "B. Narasi", "C. Eksposisi", "D. Prosedur"], "jawaban": "C"},
    {"soal": "Kata 'mengonsumsi' berasal dari kata dasar...", "pilihan": ["A. Konsumsi", "B. Ngonsumsi", "C. Somasi", "D. Mengonsumsi"], "jawaban": "A"},
    {"soal": "Latar tempat, waktu, dan suasana dalam cerita disebut juga dengan istilah...", "pilihan": ["A. Setting", "B. Plot", "C. Character", "D. Theme"], "jawaban": "A"},
    {"soal": "Kalimat yang terdiri atas satu klausa utama dinamakan kalimat...", "pilihan": ["A. Majemuk", "B. Tunggal", "C. Pasif", "D. Langsung"], "jawaban": "B"},
    {"soal": "Penulisan gelar akademik yang benar di bawah ini adalah...", "pilihan": ["A. Dr. Budi, M.Pd.", "B. Dr Budi M.Pd", "C. Dr. Budi M.Pd.", "D. Dr, Budi, MPd"], "jawaban": "A"},
    {"soal": "Informasi tambahan yang berfungsi menjelaskan gagasan pokok disebut gagasan...", "pilihan": ["A. Utama", "B. Pendukung/Penjelas", "C. Pokok", "D. Inti"], "jawaban": "B"},
    {"soal": "Cerita rakyat yang mengisahkan asal-usul suatu tempat dinamakan...", "pilihan": ["A. Fabel", "B. Mite", "C. Legenda", "D. Sage"], "jawaban": "C"},
    {"soal": "Karya tulis yang menyajikan fakta secara sistematis untuk menyatukan pendapat disebut...", "pilihan": ["A. Cerpen", "B. Puisi", "C. Karya Ilmiah", "D. Novel"], "jawaban": "C"},
    {"soal": "Kata bercetak tebal yang benar ejaannya menurut PUEBI/KBBI adalah...", "pilihan": ["A. Jadwal kuliah sudah keluar.", "B. Jadual kuliah sudah keluar.", "C. Jadval kuliah sudah keluar.", "D. Satwal kuliah sudah keluar."], "jawaban": "A"}
]

# Inisialisasi state halaman di Streamlit
if "nomor_soal" not in st.session_state:
    st.session_state.nomor_soal = 0
if "skor_benar" not in st.session_state:
    st.session_state.skor_benar = 0
if "skor_salah" not in st.session_state:
    st.session_state.skor_salah = 0

st.title("📝 Kuis Agama Islam & Bahasa Indonesia")
st.write("Jawablah 50 soal pilihan ganda di bawah ini dengan teliti!")
st.divider()

total_soal = len(soal_kuis)

if st.session_state.nomor_soal < total_soal:
    # Menampilkan progress bar kuis
    progress = (st.session_state.nomor_soal) / total_soal
    st.progress(progress)
    
    # Ambil data soal aktif
    index = st.session_state.nomor_soal
    soal_sekarang = soal_kuis[index]
    
    st.subheader(f"Soal No. {index + 1} dari {total_soal}")
    st.write(soal_sekarang["soal"])
    
    # Formulir pilihan jawaban berupa Radio Button
    pilihan_user = st.radio("Pilih jawaban Anda:", soal_sekarang["pilihan"], key=f"radio_{index}")
    
    # Tombol kirim jawaban
    if st.button("Kirim Jawaban & Lanjut"):
        huruf_pilihan = pilihan_user[0] # Mengambil huruf depannya saja (A/B/C/D)
        
        # Logika Benar/Salah
        if huruf_pilihan == soal_sekarang["jawaban"]:
            st.session_state.skor_benar += 1
        else:
            st.session_state.skor_salah += 1
            
        # Pindah ke nomor berikutnya
        st.session_state.nomor_soal += 1
        st.rerun()

else:
    # --- HALAMAN HASIL AKHIR ---
    nilai_akhir = (st.session_state.skor_benar / total_soal) * 100
    
    st.balloons() # Efek balon perayaan
    st.header("🎉 Kuis Selesai!")
    st.subheader("Hasil Penilaian:")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Jawaban Benar", f"✅ {st.session_state.skor_benar}")
    col2.metric("Jawaban Salah", f"❌ {st.session_state.skor_salah}")
    col3.metric("Total Soal", f"📋 {total_soal}")
    
    st.markdown(f"### **Nilai Akhir Anda:** `{nilai_akhir:.2f} / 100`")
    
    if nilai_akhir >= 75:
        st.success("Selamat! Anda lulus kuis ini dengan nilai yang baik.")
    else:
        st.warning("Anda belum mencapai batas kelulusan (75). Tetap semangat dan coba lagi!")
        
    # Tombol Reset Kuis
    if st.button("Ulangi Kuis Dari Awal"):
        st.session_state.nomor_soal = 0
        st.session_state.skor_benar = 0
        st.session_state.skor_salah = 0
        st.rerun()
