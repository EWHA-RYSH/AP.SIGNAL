import streamlit as st
import time

def render_landing():
    """
    Renders the Landing Page with a clean, B2B enterprise aesthetic.
    Features:
    - Hidden Sidebar (via CSS)
    - Centered Card with Title and 'Enter' button
    - Minimalist design (White on Gray)
    """
    
    # 1. Hide Sidebar CSS specifically for Landing Page
    hide_sidebar_style = """
        <style>
        [data-testid="stSidebar"] { display: none; }
        .stApp { background-color: #f1f3f5; } /* Slightly darker/cooler gray for B2B bg */
        </style>
    """
    st.markdown(hide_sidebar_style, unsafe_allow_html=True)

    # 2. Main Container (Vertically Centered)
    # Using columns to center horizontally
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown("<div style='height: 15vh;'></div>", unsafe_allow_html=True) # Top Spacer
        
        # Card Container
        with st.container():
            st.markdown(
                """
                <div style="
                    background-color: white; 
                    padding: 60px 40px; 
                    border-radius: 12px; 
                    border: 1px solid #e0e0e0;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
                    text-align: center;
                ">
                    <h1 style="
                        font-family: 'Arita-Sans-Bold', sans-serif; 
                        color: #111; 
                        font-size: 48px; 
                        margin-bottom: 10px;
                        font-weight: 700;
                    ">
                        AP<span style="color:#1F5795;">.Signal</span>
                    </h1>
                    <p style="
                        font-family: 'Arita-Sans-Medium', sans-serif;
                        color: #666; 
                        font-size: 18px; 
                        margin-bottom: 40px;
                        line-height: 1.6;
                    ">
                        콘텐츠 성과 분석 솔루션<br>
                        <span style="font-size: 14px; color: #999;">안전 • 신뢰 • 인사이트</span>
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            # Start Button (Streamlit widget need to be outside HTML block for state to work)
            # We use columns inside this container to center the button visually if needed, 
            # but st.button is full width by default in columns.
            
            # Additional Spacer inside the card logic visual separation
            st.markdown("<div style='margin-top: -30px; text-align: center;'>", unsafe_allow_html=True)
            
            if st.button("대시보드 시작", use_container_width=True, type="primary"):
                with st.spinner("인증 및 모듈 로딩 중..."):
                    time.sleep(1.0) # Fake loading effect for premium feel
                    st.session_state.page = "dashboard"
                    st.rerun()
            
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown(
                """
                <div style="text-align: center; margin-top: 30px; color: #ccc; font-size: 12px; font-family: 'Arita-Sans-Medium', sans-serif;">
                    © 2025 AP.Signal. All rights reserved.
                </div>
                """,
                unsafe_allow_html=True
            )
