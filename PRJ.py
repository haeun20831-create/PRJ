# 필요한 라이브러리 임포트
import tkinter as tk
from tkinter import ttk, messagebox, filedialog # GUI 위젯, 메시지 박스, 파일 대화상자
import json # JSON 데이터 처리
import pandas as pd # CSV, Excel 데이터 처리
# 학생 정보 관리 앱 메인 클래스
class StudentManagerApp:
    # 초기화 메서드
    def __init__(self, root):
        self.root = root  # 메인 윈도우
        self.root.title("학생 정보 관리 프로그램") # 윈도우 제목 설정
        self.root.geometry("600x420") # 윈도우 크기 설정
        self.create_widgets() # 위젯 생성 함수 호출

# 학생 추가 함수
    def add_student(self):
        # 입력값 가져오기
        name = self.name_entry.get().strip()
        sid = self.id_entry.get().strip()
        major = self.major_entry.get().strip()

        # 입력값 유효성 검사
        if not name or not sid or not major:
            messagebox.showwarning("입력 오류", "모든 항목을 입력하세요.")
            return

        # 목록에 학생 추가
        self.tree.insert("", "end", values=(name, sid, major))

        # 입력 필드 초기화
        self.name_entry.delete(0, tk.END)
        self.id_entry.delete(0, tk.END)
        self.major_entry.delete(0, tk.END)

    # 학생 삭제 함수
    def delete_student(self):
        selected = self.tree.selection() # 선택된 항목 가져오기
        if not selected:
            messagebox.showwarning("선택 오류", "삭제할 학생을 선택하세요.")
            return
        
        # 선택된 항목 삭제
        for item in selected:
            self.tree.delete(item)