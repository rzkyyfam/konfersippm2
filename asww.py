import streamlit as st

st.title(':violet[Kelompok 4]')
st.header('Webbs :blue[Konfersi PPM]')

from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Main Menu", ["Tabel Periodik", 'Konfersi PPM'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=1)
    selected
    
if selected == 'Tabel Periodik':
    st.subheader(':red[Data Tabel Periodik]')
    from PIL import Image
    
    image = Image.open('LPK.png')

    st.image(image, caption='Tabel Periodik')
        

if selected == 'Konfersi PPM':
    option = st.selectbox('Konfersi PPM Ke?',('Normalitas','Molaritas','%(b/b)','%(b/v)'))
    if option == 'Normalitas':
        ppm = st.number_input('Masukkan Nilai PPM')
        be = st.number_input('Masukkan Nilai Berat Ekivalen(BE)',value = 1.00)
    
        st.button('Hitung Nilai Normalitas')
        nilai_normalitas = round(((ppm/be)/1000),4)
        st.success(f'Nilai Normalitas Adalah {nilai_normalitas}')
    elif option == 'Molaritas':
        ppm = st.number_input('Masukkan Nilai PPM')
        bm = st.number_input('Masukkan Nilai Berat Molekul(BM)',value = 1.00) 
    
        st.button('Hitung Nilai Molaritas')
        nilai_molaritas = round(((ppm/bm)/1000),4)
        st.success(f'Nilai Molaritas Adalah {nilai_molaritas}')
    
    elif option == '%(b/b)':
        ppm = st.number_input('Masukkan Nilai PPM mg/Kg')
        st.button('Hitung Nilai %(b/b)')
        nilai_bb = round((ppm/10000),2)
        st.success(f'Nilai %(b/b) adalah {nilai_bb}%')
    
    else :
        ppm = st.number_input('Masukkan Nilai PPM mg/L') 
        st.button('Hitung Nilai %(b/v)')
        nilai_bv = round((ppm/10000),2)
        st.success(f'Nilai %(b/v) adalah {nilai_bv}%')
    
    
    

    
    
    

