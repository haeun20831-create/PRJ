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

    # 파일 저장 함수 (JSON, CSV, Excel)
    def save_file(self):
        file = filedialog.asksaveasfilename(
            title="학생 정보 저장",
            defaultextension=".json",
            filetypes=[
                ("JSON Files", "*.json"),
                ("CSV Files", "*.csv"),
                ("Excel Files", "*.xlsx"),
                ("All Files", "*.*")
            ]
        )
        # 저장 취소 시 종료
        if not file:
            return