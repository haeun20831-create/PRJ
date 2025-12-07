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


    # 위젯 생성 및 배치
    def create_widgets(self):
        # 입력 영역 프레임
        input_frame = ttk.LabelFrame(self.root, text="학생 정보 입력")
        input_frame.pack(fill="x", padx=10, pady=10)

        
        # 이름, 학번, 학과 입력 필드
        ttk.Label(input_frame, text="이름").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(input_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(input_frame, text="학번").grid(row=0, column=2, padx=5, pady=5)
        self.id_entry = ttk.Entry(input_frame)
        self.id_entry.grid(row=0, column=3, padx=5, pady=5)
        ttk.Label(input_frame, text="학과").grid(row=1, column=0, padx=5, pady=5)
        self.major_entry = ttk.Entry(input_frame)
        self.major_entry.grid(row=1, column=1, padx=5, pady=5)
