import streamlit as st
from PIL import Image

# Set the title of the webpage
st.set_page_config(page_title="Sabrina Tiara Bachtiar's Blog", layout="wide")

# Header Section
st.markdown(
    """
    <style>
    .header-section {
        background-color: rgba(166, 142, 156, 0.3);
        padding: 50px;
        text-align: center;
        color: #fff;
    }
    .header-title {
        font-size: 50px;
        font-weight: bold;
        font-style: italic;
    }
    .header-buttons {
        margin-top: 20px;
    }
    .header-buttons .stButton {
        margin: 0 10px;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

st.markdown('<div class="header-section">', unsafe_allow_html=True)
st.markdown('<h1 class="header-title">Sabrina Tiara Bachtiar</h1>', unsafe_allow_html=True)

st.markdown(
    '<div class="header-buttons">',
    unsafe_allow_html=True,
)
col1, col2 = st.columns([1, 1])
with col1:
    st.button('Biografi')
with col2:
    st.button('Kontak')
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Biography Section
st.header("Biografi")
st.write(
    "Hai semua! Perkenalkan namaku Sabrina Tiara Bachtiar dengan panggilan akrab 'Sabrina' yang lahir pada tanggal 3 Maret 2003 di Surabaya. Saat ini aku sedang menjalankan studi S1 Teknologi Sains Data UNAIR dan sejak pandemi aku mulai mengembangkan hobi dan bakat lama yang terpendam yaitu memotret dan menonton film."
)

# Photos Section
st.header("Foto")
st.write(
    "Sejak kecil mempunyai minat dalam fotografi karena umur 7 tahun memiliki kamera pocket sendiri maka dari itu aku suka memotret hal - hal yang berada di sekitarku hingga saat ini. Inilah hasil memotretku!"
)

# Displaying Images
image1 = Image.open("assets/images/2020-0930-6191801-1139x641.jpeg")
image2 = Image.open("assets/images/2020-1101-6042400-1139x641.jpg")
image3 = Image.open("assets/images/img-20200920-084050-695-1139x1139.jpeg")

st.image([image1, image2, image3], width=300, caption=["Image 1", "Image 2", "Image 3"])

# Films Section
st.header("Film")
st.write(
    "Diselang kesibukan yang sangat padat membuat stres biasanya menonton film sebagai obat untuk melepas penat dan minimal sehari 1 film yang ku tonton. Berikut film - film yang tidak bosan ku tonton!"
)

# Displaying Movies
movies = {
    "Little Women": "https://www.imdb.com/title/tt3281548/?ref_=nv_sr_srsg_0",
    "The Hustle": "https://www.imdb.com/title/tt1298644/?ref_=nv_sr_srsg_0",
    "Coco": "https://www.imdb.com/title/tt2380307/",
}

movie_posters = [
    "assets/images/mv5byzc5ytyynmitmdy5ys00owmxlwizodktmzq4yjbmnzuzndhjxkeyxkfqcgdeqxvymtkzndyzntk.-v1-sy1000-cr007071000-al-707x1000.jpg",
    "assets/images/mv5bmtc3mdcynze5n15bml5banbnxkftztgwnze2mde0nzm.-v1-816x1195.jpg",
    "assets/images/mv5byjq5njm0y2ytnjzknc00zdhklwjjmwitn2qynzfkmde3zjaxxkeyxkfqcgdeqxvyodixmzk5nja.-v1-816x1166.jpg",
]

for i, movie in enumerate(movies.items()):
    st.image(movie_posters[i], width=200, caption=movie[0])
    st.markdown(f"[Watch {movie[0]}]({movie[1]})")

# Contact Section
st.header("Follow Me!")
st.write("You can follow me on the following platforms:")

st.markdown(
    """
    - [Instagram](https://instagram.com/sabrinatiarab?utm_medium=copy_link)
    - [YouTube](https://www.youtube.com/channel/UCfZUQl0PKU9xECA64Q-nrKA/featured)
    - [GitHub](https://github.com/sabrinatiarab)
    - [Email](mailto:sabrinatiarabachtiar@gmail.com)
    - [WhatsApp](https://wa.me/6289666534858)
    """
)

# Footer Section
st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
st.write("Download PDF Laporan UTS:")
st.markdown(
    "[Download Here](https://drive.google.com/file/d/1U-IoS09eEa56DD9zrQzD9881s-owakF1/view?usp=sharing)"
)
st.markdown('</div>', unsafe_allow_html=True)