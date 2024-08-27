import streamlit as st

# Custom CSS
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css?family=Merriweather:300,300i,400,400i,700,700i,900,900i&display=swap');
    @import url('https://fonts.googleapis.com/css?family=Jost:100,200,300,400,500,600,700,800,900,100i,200i,300i,400i,500i,600i,700i,800i,900i&display=swap');

    body {
        font-family: 'Merriweather', serif;
    }

    .header {
        background-color: rgba(166, 142, 156, 0.3);
        padding: 100px;
        text-align: left;
    }

    .header h1 {
        font-size: 64px;
        font-weight: bold;
    }

    .header .btn {
        margin-top: 20px;
    }

    .biography, .photos, .films {
        margin-top: 50px;
    }

    .biography h3, .photos h3, .films h3 {
        text-align: center;
    }

    .biography p, .films p {
        text-align: center;
        margin: 20px 0;
    }

    .images-grid {
        display: flex;
        justify-content: space-around;
        margin-top: 20px;
    }

    .images-grid img {
        width: 300px;
        height: auto;
    }

    .contacts h2 {
        text-align: center;
        margin-bottom: 30px;
    }

    .icons {
        display: flex;
        justify-content: center;
        gap: 15px;
    }

    .icons a {
        font-size: 40px;
    }

    .footer {
        margin-top: 50px;
        text-align: center;
        padding: 20px;
    }

    .footer a {
        font-size: 20px;
        color: #000;
        text-decoration: none;
    }

    </style>
    """, unsafe_allow_html=True
)

# Header Section
st.markdown(
    """
    <div class="header">
        <h1><em>Sabrina Tiara Bachtiar</em></h1>
        <a href="#biography" class="btn btn-danger-outline">Biografi</a>
        <a href="#contacts" class="btn btn-danger-outline">Kontak</a>
    </div>
    """, unsafe_allow_html=True
)

# Biography Section
st.markdown(
    """
    <div id="biography" class="biography">
        <h3>Biografi</h3>
        <p>Hai semua! Perkenalkan namaku Sabrina Tiara Bachtiar dengan panggilan akrab "Sabrina" yang lahir pada tanggal 3 Maret 2003 di Surabaya. Saat ini aku sedang menjalankan studi S1 Teknologi Sains Data UNAIR dan sejak pandemi aku mulai mengembangkan hobi dan bakat lama yang terpendam yaitu memotret dan menonton film.</p>
    </div>
    """, unsafe_allow_html=True
)

# Photos Section
st.markdown(
    """
    <div id="photos" class="photos">
        <h3>Foto</h3>
        <p>Sejak kecil mempunyai minat dalam fotografi karena umur 7 tahun memiliki kamera pocket sendiri maka dari itu aku suka memotret hal - hal yang berada di sekitarku hingga saat ini. Inilah hasil memotretku!</p>
        <div class="images-grid">
            <img src="assets/images/2020-0930-6191801-1139x641.jpeg" alt="Foto 1">
            <img src="assets/images/2020-1101-6042400-1139x641.jpg" alt="Foto 2">
            <img src="assets/images/img-20200920-084050-695-1139x1139.jpeg" alt="Foto 3">
        </div>
    </div>
    """, unsafe_allow_html=True
)

# Films Section
st.markdown(
    """
    <div id="films" class="films">
        <h3>Film</h3>
        <p>Diselang kesibukan yang sangat padat membuat stres biasanya menonton film sebagai obat untuk melepas penat dan minimal sehari 1 film yang ku tonton. Berikut film - film yang tidak bosan ku tonton!</p>
        <div class="images-grid">
            <a href="https://www.imdb.com/title/tt3281548/?ref_=nv_sr_srsg_0" target="_blank">
                <img src="assets/images/mv5byzc5ytyynmitmdy5ys00owmxlwizodktmzq4yjbmnzuzndhjxkeyxkfqcgdeqxvymtkzndyzntk.-v1-sy1000-cr007071000-al-707x1000.jpg" alt="Little Women">
            </a>
            <a href="https://www.imdb.com/title/tt1298644/?ref_=nv_sr_srsg_0" target="_blank">
                <img src="assets/images/mv5bmtc3mdcynze5n15bml5banbnxkftztgwnze2mde0nzm.-v1-816x1195.jpg" alt="The Hustle">
            </a>
            <a href="https://www.imdb.com/title/tt2380307/" target="_blank">
                <img src="assets/images/mv5byjq5njm0y2ytnjzknc00zdhklwjjmwitn2qynzfkmde3zjaxxkeyxkfqcgdeqxvyodixmzk5nja.-v1-816x1166.jpg" alt="Coco">
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True
)

# Contacts Section
st.markdown(
    """
    <div id="contacts" class="contacts">
        <h2>Follow Me!</h2>
        <div class="icons">
            <a href="https://instagram.com/sabrinatiarab?utm_medium=copy_link" target="_blank"><span class="socicon-instagram"></span></a>
            <a href="mailto:sabrinatiarabachtiar@gmail.com"><span class="mbrib-letter"></span></a>
            <a href="https://www.youtube.com/channel/UCfZUQl0PKU9xECA64Q-nrKA/featured" target="_blank"><span class="socicon-youtube"></span></a>
            <a href="https://wa.me/6289666534858"><span class="socicon-whatsapp"></span></a>
            <a href="https://github.com/sabrinatiarab" target="_blank"><span class="socicon-github"></span></a>
        </div>
    </div>
    """, unsafe_allow_html=True
)

# Footer Section
st.markdown(
    """
    <div class="footer">
        <p><a href="https://drive.google.com/file/d/1U-IoS09eEa56DD9zrQzD9881s-owakF1/view?usp=sharing" target="_blank">Download PDF Laporan UTS</a></p>
    </div>
    """, unsafe_allow_html=True
)