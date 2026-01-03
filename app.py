import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="Input Stok & LO SPBU", layout="centered")
st.title("📋 Input Stok & LO SPBU")

with st.form("form_input"):
    tanggal = st.date_input("Tanggal", datetime.today())
    kode_spbu = st.text_input("Kode SPBU")
    produk = st.selectbox("Produk", ["Pertalite", "Pertamax", "Solar", "Dexlite"])
    stok_aktual = st.number_input("Stok Saat Ini (Liter)", min_value=0)
    lo = st.number_input("LO Hari Ini (Liter)", min_value=0)
    keterangan = st.text_input("Keterangan LO (opsional)")
    submit = st.form_submit_button("KIRIM DATA")

if submit:
    data = pd.DataFrame([{
        "Tanggal": tanggal,
        "Waktu": datetime.now().strftime("%H:%M:%S"),
        "SPBU": kode_spbu,
        "Produk": produk,
        "Stok Aktual": stok_aktual,
        "LO": lo,
        "Keterangan": keterangan
    }])

    file = "data_stok_lo.csv"
    if os.path.exists(file):
        lama = pd.read_csv(file)
        data = pd.concat([lama, data], ignore_index=True)

    data.to_csv(file, index=False)
    st.success("✅ Data berhasil dikirim")
