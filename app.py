import os
import pandas as pd
import streamlit as st
from config import Config


def menu():
    st.sidebar.title("Navigation")
    st.sidebar.page_link("app.py", label="Home")
    st.sidebar.page_link("pages/data_analysis.py", label="Data Analysis")
    st.sidebar.page_link("pages/input_records.py", label="Input Records")
    st.sidebar.page_link("pages/prediction.py", label="Prediction")


def load_overview_metrics(csv_path: str):
    if not os.path.exists(csv_path):
        return None
    df = pd.read_csv(csv_path)
    total_songs = len(df)
    total_producers = df["Producer"].nunique() if "Producer" in df.columns else 0
    total_genres = df["Genre"].nunique() if "Genre" in df.columns else 0
    return total_songs, total_producers, total_genres


if __name__ == "__main__":
    st.set_page_config(
        page_title="Virtual Singer Data Analysis",
        page_icon="🎤",
        layout="centered",
        initial_sidebar_state="expanded",
    )

    menu()

    st.title("🎤 Virtual Singer Data Analysis")
    st.caption("Khám phá dữ liệu bài hát, trực quan hóa xu hướng và dự đoán chỉ số bằng mô hình hồi quy tuyến tính.")

    metrics = load_overview_metrics(Config.TRAIN_PATH)
    if metrics is not None:
        songs_cnt, prod_cnt, genre_cnt = metrics
        c1, c2, c3 = st.columns(3)
        c1.metric("Số bài hát", songs_cnt)
        c2.metric("Số Producer", prod_cnt)
        c3.metric("Số thể loại", genre_cnt)
    else:
        st.info("Chưa tìm thấy file dữ liệu huấn luyện. Hãy kiểm tra lại đường dẫn trong `Config.TRAIN_PATH`.")

    st.divider()
    st.subheader("Chức năng chính")

    col_a, col_b, col_c = st.columns(3)
    with col_a:
        with st.container(border=True):
            st.markdown("**📊 Data Analysis**")
            st.write("Thống kê mô tả, lọc dữ liệu và xem biểu đồ trực quan.")
            st.page_link("pages/data_analysis.py", label="Mở phân tích →")

    with col_b:
        with st.container(border=True):
            st.markdown("**➕ Input Records**")
            st.write("Thêm bản ghi bài hát mới để mở rộng tập dữ liệu.")
            st.page_link("pages/input_records.py", label="Thêm dữ liệu →")

    with col_c:
        with st.container(border=True):
            st.markdown("**📈 Prediction**")
            st.write("Dự đoán biến mục tiêu bằng mô hình Linear Regression.")
            st.page_link("pages/prediction.py", label="Chạy dự đoán →")

    st.divider()
    st.caption("Xây dựng bằng Streamlit • Dữ liệu phục vụ đồ án phân tích dữ liệu.")