import streamlit as st
import pyshorteners as ps
print('working')

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
rdb=shortit(title)

if st.button('Shorten Url'):
    rdb=shortit(title)
st.write('Your Shortened URL : ',rdb)


