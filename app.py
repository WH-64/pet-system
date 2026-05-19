import streamlit as st
from pet_tools import (
    new_pet,
    shou_all,
    search_pet,
    update_pet,
    delete_pet
)

st.set_page_config(page_title="宠物信息管理系统", layout="wide")
st.title("🐾 宠物信息管理系统")

menu = [
    "显示全部宠物",
    "新增宠物",
    "搜索宠物",
    "修改宠物",
    "删除宠物"
]

choice = st.sidebar.selectbox("请选择操作", menu)

if choice == "显示全部宠物":
    shou_all()
elif choice == "新增宠物":
    new_pet()
elif choice == "搜索宠物":
    search_pet()
elif choice == "修改宠物":
    update_pet()
elif choice == "删除宠物":
    delete_pet()