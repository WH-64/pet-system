#!/bin/bash
# 1. 切换到你真实的路径（注意：我把路径改成了你终端显示的 PIMS 路径）
cd "/Users/wanghao/PycharmProjects/PIMS"

# 2. 激活你的虚拟环境（看你终端有 base，所以要加这一句）
conda activate base

# 3. 启动程序
streamlit run app.py