import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(
    page_title="China Travel Preparation Checklist",
    page_icon="🇨🇳",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stCheckbox {
        margin-bottom: 0.5rem;
    }
    .section-header {
        color: #FF4B4B;
        font-size: 1.5rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .subsection-header {
        color: #1E88E5;
        font-size: 1.2rem;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.title("🇨🇳 China Travel Preparation Checklist 2025")
st.markdown("Use this interactive checklist to prepare for your trip to China!")

# Initialize session state for checkboxes if not exists
if 'checkboxes' not in st.session_state:
    st.session_state.checkboxes = {}

# Function to create a checkbox with state management
def create_checkbox(key, label):
    if key not in st.session_state.checkboxes:
        st.session_state.checkboxes[key] = False
    return st.checkbox(label, key=key, value=st.session_state.checkboxes[key])

# Visa and Entry Section
st.markdown('<div class="section-header">Visa and Entry Requirements</div>', unsafe_allow_html=True)
create_checkbox('visa_apply', 'Apply for tourist visa (L Visa) at least 1 month before travel')
create_checkbox('visa_docs', 'Prepare required documents (passport, photos, itinerary)')
create_checkbox('visa_check', 'Check if eligible for 144/240-hour transit visa exemption')
create_checkbox('visa_waiver', 'Verify if your nationality qualifies for visa-free entry')
create_checkbox('passport_valid', 'Ensure passport has >6 months validity and blank pages')

# Internet and Connectivity
st.markdown('<div class="section-header">Internet and Connectivity</div>', unsafe_allow_html=True)
create_checkbox('vpn_install', 'Install VPN on all devices before arrival')
create_checkbox('vpn_test', 'Test VPN connection and download multiple server configurations')
create_checkbox('sim_research', 'Research local SIM card options (China Mobile/Unicom/Telecom)')
create_checkbox('esim_check', 'Check if your phone supports eSIM for China')
create_checkbox('wechat_setup', 'Set up WeChat account before arrival')
create_checkbox('offline_maps', 'Download offline maps and translation packages')

# Money and Payments
st.markdown('<div class="section-header">Money and Payments</div>', unsafe_allow_html=True)
create_checkbox('cash_prep', 'Prepare some RMB cash (¥500-1000) for initial expenses')
create_checkbox('wechat_pay', 'Set up WeChat Pay with international card')
create_checkbox('alipay_setup', 'Set up Alipay with international card')
create_checkbox('bank_notify', 'Notify your bank about China travel')
create_checkbox('wise_setup', 'Consider setting up Wise/Revolut for better exchange rates')

# Transportation
st.markdown('<div class="section-header">Transportation</div>', unsafe_allow_html=True)
create_checkbox('train_book', 'Book high-speed train tickets in advance if needed')
create_checkbox('didi_setup', 'Install and set up DiDi ride-hailing app')
create_checkbox('metro_apps', 'Download city-specific metro apps')
create_checkbox('transit_cards', 'Research transit card options for your cities')

# Accommodation
st.markdown('<div class="section-header">Accommodation</div>', unsafe_allow_html=True)
create_checkbox('hotel_book', 'Book hotels with foreign guest license')
create_checkbox('airbnb_check', 'If using Airbnb, confirm registration process')
create_checkbox('hotel_address', 'Save hotel addresses in Chinese')
create_checkbox('check_in_docs', 'Prepare documents for hotel check-in')

# Health and Safety
st.markdown('<div class="section-header">Health and Safety</div>', unsafe_allow_html=True)
create_checkbox('meds_pack', 'Pack necessary medications and first aid kit')
create_checkbox('insurance', 'Purchase travel insurance with medical coverage')
create_checkbox('emergency_contacts', 'Save emergency numbers (Police: 110, Ambulance: 120)')
create_checkbox('embassy_info', 'Save embassy contact information')

# Apps and Digital Tools
st.markdown('<div class="section-header">Essential Apps and Digital Tools</div>', unsafe_allow_html=True)
create_checkbox('translate_apps', 'Install translation apps (Google Translate, Microsoft Translator)')
create_checkbox('map_apps', 'Download map apps (Google Maps, Baidu Maps)')
create_checkbox('weather_app', 'Install weather and air quality apps')
create_checkbox('offline_content', 'Download offline content for entertainment')

# Cultural Preparation
st.markdown('<div class="section-header">Cultural Preparation</div>', unsafe_allow_html=True)
create_checkbox('basic_phrases', 'Learn basic Chinese phrases')
create_checkbox('cultural_research', 'Research local customs and etiquette')
create_checkbox('dress_code', 'Pack appropriate clothing for the season and culture')
create_checkbox('gift_prep', 'Prepare small gifts from your country if visiting friends')

# Weather and Seasonal Preparation
st.markdown('<div class="section-header">Weather and Seasonal Preparation</div>', unsafe_allow_html=True)
create_checkbox('weather_check', 'Check weather forecast for your destinations')
create_checkbox('seasonal_clothes', 'Pack appropriate seasonal clothing')
create_checkbox('umbrella', 'Pack umbrella (for both rain and sun)')
create_checkbox('sun_protection', 'Pack sun protection (sunscreen, hat)')

# Progress tracking
total_items = len(st.session_state.checkboxes)
checked_items = sum(st.session_state.checkboxes.values())
progress = checked_items / total_items if total_items > 0 else 0

st.markdown("---")
st.progress(progress)
st.markdown(f"**Progress: {checked_items}/{total_items} items completed**")

# Reset button
if st.button("Reset Checklist"):
    st.session_state.checkboxes = {key: False for key in st.session_state.checkboxes}
    st.experimental_rerun()

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center'>
        <p>Made with ❤️ for travelers to China</p>
        <p>Remember: 一路平安 (yílù píng'ān) - Have a peaceful journey!</p>
    </div>
""", unsafe_allow_html=True) 