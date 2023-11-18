import streamlit as st
import pyshorteners as ps
import qrcode
from PIL import Image
print('working')


def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants. ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("img.png")


def shortit(url):
    try:
        if url=="":
            return('')
        s=ps.Shortener()
        return(str(s.tinyurl.short(url)))
    except:
        return('')

st.header('URL Shortener')
title = st.text_input('Enter the url', '',placeholder='Url Here')


if st.button('Shorten Url'):
    rdb=shortit(title)
    generate_qrcode(rdb)
    st.write('Your Shortened URL : ',rdb,'\n')
    st.image('img.png', caption='QR',width=140)
