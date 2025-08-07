import streamlit as st

# MBTI 데이터 (간단 예시)
mbti_info = {
    "ISTJ": {
        "직업": ["회계사", "공무원", "엔지니어"],
        "취미": ["독서", "퍼즐 맞추기", "정리하기"]
    },
    "ENFP": {
        "직업": ["마케터", "작가", "디자이너"],
        "취미": ["여행", "그림 그리기", "사람 만나기"]
    },
    "INFJ": {
        "직업": ["상담가", "교사", "연구원"],
        "취미": ["글쓰기", "명상", "예술 감상"]
    },
    "ESTP": {
        "직업": ["영업", "기업가", "스포츠 트레이너"],
        "취미": ["스포츠", "게임", "드라이브"]
    }
    # 필요 시 더 많은 MBTI 유형 추가 가능
}

# 제목
st.title("💡 MBTI 맞춤 직업 & 취미 추천")

# 사용자 입력: MBTI 선택
mbti_list = list(mbti_info.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_list)

# 결과 출력
if selected_mbti:
    st.subheader(f"✨ {selected_mbti} 유형을 위한 추천")

    jobs = mbti_info[selected_mbti]["직업"]
    hobbies = mbti_info[selected_mbti]["취미"]

    st.markdown("**추천 직업:**")
    for job in jobs:
        st.write(f"- {job}")

    st.markdown("**추천 취미:**")
    for hobby in hobbies:
        st.write(f"- {hobby}")
