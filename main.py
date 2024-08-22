import numpy as np
from PIL import Image
import streamlit as st
import openai
import requests

openai.api_key = 'API-KEY'

def get_openai_response(prompt):
    """
    [TODO] OpenAI에게 프롬프트를 전달하고, 답변을 받아오는 함수를 구현합니다. 
    """
    message_history = [
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt}
                ]
    response = openai.ChatCompletion.create(
        model = "gpt-4o",
        messages=message_history,
        stream=False
        )

    return response['choices'][0]['message']['content']

def main():
    # 페이지 타이틀과 배너 이미지
    st.title('계절별로 자신에게 어울리는 코디를 추천받으세요!')
    st.image("fashion_banner.jpg", use_column_width=True)

    # 패션 아이콘 이미지 섹션
    st.markdown("## ✨ 나의 옷장을 완성해보세요! ✨")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("fashion_icon1.jpg", caption="캐주얼 룩", use_column_width=True)
    with col2:
        st.image("fashion_icon2.jpg", caption="비즈니스 룩", use_column_width=True)
    with col3:
        st.image("fashion_icon3.jpg", caption="파티 룩", use_column_width=True)

    # 사이드바에서 사용자 정보 입력
    st.sidebar.header("사용자 정보를 입력하세요:")
    
    age = st.sidebar.number_input("나이", min_value=1, max_value=100, step=1)
    gender = st.sidebar.selectbox("성별", ("남성", "여성"))
    height = st.sidebar.number_input("키 (cm)", min_value=100, max_value=250, step=1)
    weight = st.sidebar.number_input("몸무게 (kg)", min_value=30, max_value=200, step=1)
    style = st.sidebar.text_input("원하는 스타일이 있으신가요? (예: 비즈니스룩):")

    # 사용자 입력에 따른 코디 및 날씨 정보 요청
    if st.sidebar.button("추천 받기"):
        if style:
            with st.spinner('생성 AI로 코디를 추천받는 중입니다...'):
                # ChatGPT에게 전달할 프롬프트 생성
                prompt = (f"나는 {age}세 {gender}이고, 키는 {height}cm, 몸무게는 {weight}kg이야. "
                          f"나의 나이와 성별 그리고 체형에 맞는 {style}스타일로 계절별 코디를 추천해줘"
                          f"{style}스타일에서 절대 벗어나면 안 되고 두 가지에서 세 가지 정도의 선택지를 줬으면 좋겠어.")
                
            response = get_openai_response(prompt)
            st.markdown(f'**코디 추천:**\n{response}')
            
            # 추천된 코디를 더욱 돋보이게 하기 위한 이미지 배치
            st.image("outfit_suggestion.jpg", use_column_width=True)
            
        else:
            with st.spinner('생성 AI로 코디를 추천받는 중입니다...'):
                # ChatGPT에게 전달할 프롬프트 생성
                prompt = (f"나는 {age}세 {gender}이고, 키는 {height}cm, 몸무게는 {weight}kg이야. "
                          f"나의 나이와 성별 그리고 체형에 맞는 계절별 코디를 추천해줘")
                
            response = get_openai_response(prompt)
            st.markdown(f'**코디 추천:**\n{response}')
            
            # 추천된 코디를 더욱 돋보이게 하기 위한 이미지 배치
            st.image("outfit_suggestion.jpg", use_column_width=True)
    
        # 추가적인 패션 영감을 주는 이미지 섹션
        st.markdown("## 👗 패션 영감을 얻어보세요! 👠")
        st.image("fashion_collage.jpg", use_column_width=True)


if __name__ == '__main__':
    main()
