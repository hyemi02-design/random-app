import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="오늘 뭐 먹지?", page_icon="🍱", layout="centered")

# 제목 및 설명
st.title("🍱 오늘의 점심 메뉴 추천기")
st.write("결정 장애를 해결해 드립니다! 아래 버튼을 눌러 오늘의 메뉴를 골라보세요.")

# 카테고리별 메뉴 데이터
menus = {
    "한식": ["김치찌개", "된장찌개", "제육볶음", "비빔밥", "국밥", "불고기", "칼국수"],
    "중식": ["짜장면", "짬뽕", "탕수육", "마라탕", "볶음밥"],
    "일식": ["초밥", "돈까스", "라멘", "우동", "카레덮밥"],
    "양식": ["파스타", "피자", "햄버거", "스테이크", "리조또"],
    "분식/기타": ["떡볶이", "김밥", "쌀국수", "샌드위치", "타코"],
}

# 카테고리 선택 옵션 (전체 포함)
category_options = ["전체"] + list(menus.keys())
selected_category = st.selectbox("원하는 음식 종류를 선택하세요:", category_options)

st.divider()

# 추천 버튼
if st.button("🎲 오늘의 메뉴 추천받기!", use_container_width=True, type="primary"):
    if selected_category == "전체":
        # 모든 카테고리의 메뉴를 하나로 합침
        all_menus = [item for sublist in menus.values() for item in sublist]
        chosen_menu = random.choice(all_menus)
    else:
        chosen_menu = random.choice(menus[selected_category])

    # 결과 출력 및 풍선 애니메이션 효과
    st.balloons()
    st.success(f"오늘의 추천 점심 메뉴는 **{chosen_menu}** 입니다! 맛있게 드세요! 😋")
