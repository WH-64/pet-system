"""
这是宠物信息管理系统的主程序
"""
from pet_tools import *


def main():
	while True:
		#  1.显示系统菜单
		shou_menu()
		#2.根据用户输入，调用不同的功能（函数）
		action = input("请选择需要执行的操作：")
		if action in ["1","2","3"]:
			if action == "1":
				new_pet()
			#  1.新增宠物信息
			elif action == "2":
				shou_all()
			#  2.显示宠物信息
			elif action == "3":
				search_pet()
			# TODO 3.搜索宠物信息
		elif action == "0":
			print("欢迎再次使用【宠物管理系统】")
			break
		else:
			print("【您输入的不正确，请重新选择】")
		#3.不断执行上述操作（循环）
if __name__ == "__main__":
	main()


import streamlit as st

st.title("宠物信息管理系统")

if st.button("显示全部宠物"):
	st.write("这里显示宠物列表")











