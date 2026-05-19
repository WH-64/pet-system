from db import get_conn
import streamlit as st

# =====================
# 新增宠物
# =====================
def new_pet():
    st.subheader("新增宠物信息")

    nick_name = st.text_input("昵称")
    age = st.text_input("年龄")
    sex = st.text_input("性别")
    weight = st.text_input("体重")

    if st.button("确认新增"):
        if not nick_name:
            st.warning("昵称不能为空")
            return

        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO pets (nick_name, age, sex, weight) VALUES (?, ?, ?, ?)",
            (nick_name, age, sex, weight)
        )
        conn.commit()
        conn.close()

        st.success(f"✅ 添加 {nick_name} 成功")


# =====================
# 显示全部宠物
# =====================
def shou_all():
    st.subheader("全部宠物信息")

    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nick_name, age, sex, weight FROM pets")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        st.warning("【当前没有任何宠物信息记录】")
        return

    for row in rows:
        st.write(
            f"ID:{row['id']} | "
            f"昵称:{row['nick_name']} | "
            f"年龄:{row['age']} | "
            f"性别:{row['sex']} | "
            f"体重:{row['weight']}"
        )


# =====================
# 搜索宠物
# =====================
def search_pet():
    keyword = st.text_input("请输入昵称关键字")

    if st.button("搜索"):
        if not keyword:
            st.warning("请输入关键字")
            return

        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, nick_name, age, sex, weight FROM pets WHERE nick_name LIKE %s",
            (f"%{keyword}%",)
        )
        rows = cursor.fetchall()
        conn.close()

        if not rows:
            st.warning("未找到匹配宠物")
            return

        st.subheader("搜索结果")
        for row in rows:
            st.write(
                f"ID:{row['id']} | "
                f"昵称:{row['nick_name']} | "
                f"年龄:{row['age']} | "
                f"性别:{row['sex']} | "
                f"体重:{row['weight']}"
            )


# =====================
# 修改宠物
# =====================
def update_pet():
    st.subheader("修改宠物信息")

    pet_id = st.number_input("请输入要修改的宠物ID", min_value=1)

    # 第一次点击：加载数据
    if st.button("加载宠物信息"):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT nick_name, age, sex, weight FROM pets WHERE id=?",
            (pet_id,)
        )
        pet = cursor.fetchone()
        conn.close()

        if not pet:
            st.error("未找到该宠物")
            return

        # ✅ 保存到 session_state
        st.session_state["pet"] = pet
        st.session_state["pet_id"] = pet_id

    # ✅ 如果已经加载过，就显示修改表单
    if "pet" in st.session_state:
        pet = st.session_state["pet"]

        new_name = st.text_input("昵称", value=pet['nick_name'])
        new_age = st.text_input("年龄", value=pet['age'])
        new_sex = st.text_input("性别", value=pet['sex'])
        new_weight = st.text_input("体重", value=pet['weight'])

        if st.button("确认修改"):
            conn = get_conn()
            cursor = conn.cursor()
            cursor.execute(
                """UPDATE pets 
                   SET nick_name=?, age=?, sex=?, weight=? 
                   WHERE id=?""",
                (new_name, new_age, new_sex, new_weight, st.session_state["pet_id"])
            )
            conn.commit()
            conn.close()

            # ✅ 清空状态
            del st.session_state["pet"]
            del st.session_state["pet_id"]

            st.success("✅ 修改成功")


# =====================
# 删除宠物
# =====================
def delete_pet():
    pet_id = st.number_input("请输入要删除的宠物ID", min_value=1)

    if st.button("确认删除"):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM pets WHERE id=?", (pet_id,))
        conn.commit()
        conn.close()
        st.success("✅ 删除成功")