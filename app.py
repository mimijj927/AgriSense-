import streamlit as st
import joblib
import pandas as pd


# =========================================================
# IMPORT CROP INFORMATION
# =========================================================

from crop_info import crop_info

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Agrisense",
    page_icon="🌱",
    layout="wide"
)


# =========================================================
# LOAD MODEL
# =========================================================

model = joblib.load("crop_model.pkl")


# =========================================================
# LANGUAGE SELECTION
# =========================================================

language = st.sidebar.selectbox(
    "🌐 Language / भाषा / भाषा",
    ["English", "हिन्दी", "मराठी"]
)


# =========================================================
# TRANSLATIONS
# =========================================================

translations = {

    "English": {

        "title": "🌱Agrisense",
        "subtitle": "Smart Crop Recommendation System",

        "mode": "Choose your mode",
        "farmer": "👨‍🌾 Farmer Mode",
        "expert": "🔬 Expert Mode",

        "soil": "🧪 Soil Conditions",
        "climate": "☁️ Climate Conditions",

        "soil_type": "What type of soil do you have?",
        "moisture": "How is your soil moisture?",
        "weather": "What is the weather like?",
        "rain": "How much rainfall does your area receive?",

        "black": "🟤 Black Soil",
        "red": "🔴 Red Soil",
        "sandy": "🟡 Sandy Soil",
        "loamy": "🟢 Loamy Soil",
        "unknown": "❓ I don't know",

        "dry": "☀️ Dry",
        "normal": "🌱 Normal",
        "wet": "💧 Wet",

        "hot": "☀️ Hot",
        "moderate": "🌤️ Moderate",
        "cold": "❄️ Cold",

        "low": "🌧️ Low",
        "medium": "🌧️🌧️ Medium",
        "high": "🌧️🌧️🌧️ High",

        "nitrogen": "Nitrogen (N)",
        "phosphorus": "Phosphorus (P)",
        "potassium": "Potassium (K)",
        "ph": "Soil pH",
        "temperature": "Temperature (°C)",
        "humidity": "Humidity (%)",
        "rainfall": "Rainfall (mm)",

        "predict": "🌾 FIND BEST CROP",

        "recommendation": "🌾 Crop Recommendation",
        "recommended": "Recommended Crop",
        "summary": "📋 Input Summary",
        "about": "🌱 About the Recommended Crop",

        "soil_condition": "Soil Conditions",
        "climate_condition": "Climate Conditions",

        "suitable_soil": "🌍 Suitable Soil",
        "water": "💧 Water Requirement",
        "climate_info": "🌡️ Climate",
        "season": "📅 Typical Season",

        "feature": "📊 Model Feature Importance",

        "note": (
            "⚠️ Farmer Mode uses approximate values based on "
            "the selected conditions. For more accurate results, "
            "use a soil testing report."
        ),

        "pH_note": "Soil pH normally ranges from 0 to 14."
    },


    "हिन्दी": {

        "title": "🌱 CropWise AI",
        "subtitle": "स्मार्ट फसल अनुशंसा प्रणाली",

        "mode": "अपना मोड चुनें",
        "farmer": "👨‍🌾 किसान मोड",
        "expert": "🔬 विशेषज्ञ मोड",

        "soil": "🧪 मिट्टी की जानकारी",
        "climate": "☁️ जलवायु की जानकारी",

        "soil_type": "आपके खेत की मिट्टी किस प्रकार की है?",
        "moisture": "आपकी मिट्टी में नमी कैसी है?",
        "weather": "मौसम कैसा है?",
        "rain": "आपके क्षेत्र में कितनी वर्षा होती है?",

        "black": "🟤 काली मिट्टी",
        "red": "🔴 लाल मिट्टी",
        "sandy": "🟡 रेतीली मिट्टी",
        "loamy": "🟢 दोमट मिट्टी",
        "unknown": "❓ मुझे नहीं पता",

        "dry": "☀️ सूखी",
        "normal": "🌱 सामान्य",
        "wet": "💧 गीली",

        "hot": "☀️ गर्म",
        "moderate": "🌤️ सामान्य",
        "cold": "❄️ ठंडा",

        "low": "🌧️ कम",
        "medium": "🌧️🌧️ मध्यम",
        "high": "🌧️🌧️🌧️ अधिक",

        "nitrogen": "नाइट्रोजन (N)",
        "phosphorus": "फॉस्फोरस (P)",
        "potassium": "पोटैशियम (K)",
        "ph": "मिट्टी का pH",
        "temperature": "तापमान (°C)",
        "humidity": "नमी (%)",
        "rainfall": "वर्षा (mm)",

        "predict": "🌾 सबसे अच्छी फसल खोजें",

        "recommendation": "🌾 फसल की अनुशंसा",
        "recommended": "अनुशंसित फसल",
        "summary": "📋 इनपुट जानकारी",
        "about": "🌱 अनुशंसित फसल के बारे में",

        "soil_condition": "मिट्टी की स्थिति",
        "climate_condition": "जलवायु की स्थिति",

        "suitable_soil": "🌍 उपयुक्त मिट्टी",
        "water": "💧 पानी की आवश्यकता",
        "climate_info": "🌡️ जलवायु",
        "season": "📅 सामान्य मौसम",

        "feature": "📊 मॉडल में फीचर का महत्व",

        "note": (
            "⚠️ किसान मोड में चुनी गई परिस्थितियों के आधार पर "
            "अनुमानित मानों का उपयोग किया जाता है। अधिक सटीक "
            "परिणामों के लिए मिट्टी की जांच रिपोर्ट का उपयोग करें।"
        ),

        "pH_note": "मिट्टी का pH सामान्यतः 0 से 14 के बीच होता है।"
    },


    "मराठी": {

        "title": "🌱 CropWise AI",
        "subtitle": "स्मार्ट पीक शिफारस प्रणाली",

        "mode": "तुमचा मोड निवडा",
        "farmer": "👨‍🌾 शेतकरी मोड",
        "expert": "🔬 तज्ञ मोड",

        "soil": "🧪 मातीची माहिती",
        "climate": "☁️ हवामानाची माहिती",

        "soil_type": "तुमच्या शेतातील माती कोणत्या प्रकारची आहे?",
        "moisture": "तुमच्या मातीमध्ये ओलावा किती आहे?",
        "weather": "हवामान कसे आहे?",
        "rain": "तुमच्या भागात किती पाऊस पडतो?",

        "black": "🟤 काळी माती",
        "red": "🔴 लाल माती",
        "sandy": "🟡 वालुकामय माती",
        "loamy": "🟢 पोयट्याची माती",
        "unknown": "❓ मला माहित नाही",

        "dry": "☀️ कोरडी",
        "normal": "🌱 सामान्य",
        "wet": "💧 ओली",

        "hot": "☀️ उष्ण",
        "moderate": "🌤️ मध्यम",
        "cold": "❄️ थंड",

        "low": "🌧️ कमी",
        "medium": "🌧️🌧️ मध्यम",
        "high": "🌧️🌧️🌧️ जास्त",

        "nitrogen": "नायट्रोजन (N)",
        "phosphorus": "फॉस्फरस (P)",
        "potassium": "पोटॅशियम (K)",
        "ph": "मातीचा pH",
        "temperature": "तापमान (°C)",
        "humidity": "आर्द्रता (%)",
        "rainfall": "पाऊस (mm)",

        "predict": "🌾 योग्य पीक शोधा",

        "recommendation": "🌾 पीक शिफारस",
        "recommended": "शिफारस केलेले पीक",
        "summary": "📋 इनपुट माहिती",
        "about": "🌱 शिफारस केलेल्या पिकाबद्दल",

        "soil_condition": "मातीची स्थिती",
        "climate_condition": "हवामानाची स्थिती",

        "suitable_soil": "🌍 योग्य माती",
        "water": "💧 पाण्याची गरज",
        "climate_info": "🌡️ हवामान",
        "season": "📅 सामान्य हंगाम",

        "feature": "📊 मॉडेलमधील फीचरचे महत्त्व",

        "note": (
            "⚠️ शेतकरी मोडमध्ये निवडलेल्या परिस्थितींवर आधारित "
            "अंदाजे मूल्यांचा वापर केला जातो. अधिक अचूक "
            "निकालांसाठी माती परीक्षण अहवाल वापरा."
        ),

        "pH_note": "मातीचा pH सामान्यतः 0 ते 14 दरम्यान असतो."
    }
}


t = translations[language]


# =========================================================
# TITLE
# =========================================================

st.title(t["title"])

st.subheader(t["subtitle"])

st.divider()


# =========================================================
# MODE SELECTION
# =========================================================

st.header(t["mode"])

mode = st.radio(
    "",
    [t["farmer"], t["expert"]],
    horizontal=True
)


st.divider()


# =========================================================
# VARIABLES
# =========================================================

N = 50.0
P = 50.0
K = 50.0
temperature = 25.0
humidity = 70.0
ph = 6.5
rainfall = 100.0


# =========================================================
# FARMER MODE
# =========================================================

if mode == t["farmer"]:

    st.header("👨‍🌾 " + t["farmer"])

    st.info(t["note"])


    # -----------------------------------------------------
    # SOIL TYPE
    # -----------------------------------------------------

    st.subheader(t["soil_type"])

    soil_option = st.radio(
        "",
        [
            t["black"],
            t["red"],
            t["sandy"],
            t["loamy"],
            t["unknown"]
        ],
        horizontal=True
    )


    # -----------------------------------------------------
    # APPROXIMATE VALUES BASED ON SOIL TYPE
    # -----------------------------------------------------

    if soil_option == t["black"]:

        N = 80.0
        P = 45.0
        K = 50.0
        ph = 7.0

    elif soil_option == t["red"]:

        N = 50.0
        P = 35.0
        K = 35.0
        ph = 6.0

    elif soil_option == t["sandy"]:

        N = 40.0
        P = 30.0
        K = 30.0
        ph = 6.5

    elif soil_option == t["loamy"]:

        N = 60.0
        P = 45.0
        K = 45.0
        ph = 6.5

    else:

        N = 50.0
        P = 40.0
        K = 40.0
        ph = 6.5


    # -----------------------------------------------------
    # SOIL MOISTURE
    # -----------------------------------------------------

    st.subheader(t["moisture"])

    moisture_option = st.radio(
        "",
        [
            t["dry"],
            t["normal"],
            t["wet"]
        ],
        horizontal=True
    )


    if moisture_option == t["dry"]:

        humidity = 45.0

    elif moisture_option == t["normal"]:

        humidity = 70.0

    else:

        humidity = 85.0


    # -----------------------------------------------------
    # WEATHER
    # -----------------------------------------------------

    st.subheader(t["weather"])

    weather_option = st.radio(
        "",
        [
            t["hot"],
            t["moderate"],
            t["cold"]
        ],
        horizontal=True
    )


    if weather_option == t["hot"]:

        temperature = 32.0

    elif weather_option == t["moderate"]:

        temperature = 25.0

    else:

        temperature = 18.0


    # -----------------------------------------------------
    # RAINFALL
    # -----------------------------------------------------

    st.subheader(t["rain"])

    rainfall_option = st.radio(
        "",
        [
            t["low"],
            t["medium"],
            t["high"]
        ],
        horizontal=True
    )


    if rainfall_option == t["low"]:

        rainfall = 50.0

    elif rainfall_option == t["medium"]:

        rainfall = 150.0

    else:

        rainfall = 250.0


# =========================================================
# EXPERT MODE
# =========================================================

else:

    st.header("🔬 " + t["expert"])


    # -----------------------------------------------------
    # SOIL PARAMETERS
    # -----------------------------------------------------

    st.subheader(t["soil"])

    col1, col2, col3 = st.columns(3)

    with col1:

        N = st.number_input(
            t["nitrogen"],
            min_value=0.0,
            value=50.0
        )

    with col2:

        P = st.number_input(
            t["phosphorus"],
            min_value=0.0,
            value=50.0
        )

    with col3:

        K = st.number_input(
            t["potassium"],
            min_value=0.0,
            value=50.0
        )


    col4, col5 = st.columns(2)

    with col4:

        ph = st.number_input(
            t["ph"],
            min_value=0.0,
            max_value=14.0,
            value=6.5
        )

    with col5:

        st.info(t["pH_note"])


    # -----------------------------------------------------
    # CLIMATE PARAMETERS
    # -----------------------------------------------------

    st.subheader(t["climate"])

    col6, col7, col8 = st.columns(3)

    with col6:

        temperature = st.number_input(
            t["temperature"],
            value=25.0
        )

    with col7:

        humidity = st.number_input(
            t["humidity"],
            min_value=0.0,
            max_value=100.0,
            value=70.0
        )

    with col8:

        rainfall = st.number_input(
            t["rainfall"],
            min_value=0.0,
            value=100.0
        )


# =========================================================
# PREDICTION BUTTON
# =========================================================

st.divider()

predict_button = st.button(
    t["predict"],
    use_container_width=True
)


# =========================================================
# PREDICTION
# =========================================================

if predict_button:

    # -----------------------------------------------------
    # CREATE MODEL INPUT
    # -----------------------------------------------------

    user_input = [[
        N,
        P,
        K,
        temperature,
        humidity,
        ph,
        rainfall
    ]]


    # -----------------------------------------------------
    # MODEL PREDICTION
    # -----------------------------------------------------

    prediction = model.predict(user_input)

    crop = prediction[0]


    # -----------------------------------------------------
    # RESULT
    # -----------------------------------------------------

    st.divider()

    st.header(t["recommendation"])

    st.success(
        f"{t['recommended']}: {crop.upper()}"
    )

    st.markdown(
        f"## 🌱 {crop.upper()}"
    )


    # -----------------------------------------------------
    # INPUT SUMMARY
    # -----------------------------------------------------

    st.subheader(t["summary"])

    summary_col1, summary_col2 = st.columns(2)


    with summary_col1:

        st.write(
            f"### 🧪 {t['soil_condition']}"
        )

        st.write(
            f"**{t['nitrogen']}:** {N}"
        )

        st.write(
            f"**{t['phosphorus']}:** {P}"
        )

        st.write(
            f"**{t['potassium']}:** {K}"
        )

        st.write(
            f"**{t['ph']}:** {ph}"
        )


    with summary_col2:

        st.write(
            f"### ☁️ {t['climate_condition']}"
        )

        st.write(
            f"**{t['temperature']}:** {temperature}"
        )

        st.write(
            f"**{t['humidity']}:** {humidity}"
        )

        st.write(
            f"**{t['rainfall']}:** {rainfall}"
        )


    # -----------------------------------------------------
    # CROP INFORMATION
    # -----------------------------------------------------

    crop_key = crop.lower()

    if crop_key in crop_info:

        info = crop_info[crop_key]

        st.divider()

        st.subheader(t["about"])

        st.write(
            info["description"]
        )


        info_col1, info_col2 = st.columns(2)


        with info_col1:

            st.write(
                f"**{t['suitable_soil']}**"
            )

            st.write(
                info["soil"]
            )


            st.write(
                f"**{t['water']}**"
            )

            st.write(
                info["water"]
            )


        with info_col2:

            st.write(
                f"**{t['climate_info']}**"
            )

            st.write(
                info["climate"]
            )


            st.write(
                f"**{t['season']}**"
            )

            st.write(
                info["season"]
            )


    # -----------------------------------------------------
    # FEATURE IMPORTANCE
    # -----------------------------------------------------

    st.divider()

    st.subheader(t["feature"])

    importance = pd.Series(
        model.feature_importances_,
        index=[
            "Nitrogen",
            "Phosphorus",
            "Potassium",
            "Temperature",
            "Humidity",
            "pH",
            "Rainfall"
        ]
    )

    importance = importance.sort_values(
        ascending=True
    )

    st.bar_chart(importance)