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

        # 추가 버튼
        ttk.Button(input_frame, text="추가", command=self.add_student).grid(row=1, column=3, padx=5)

        # 목록 영역 프레임 (Treeview)
        list_frame = ttk.LabelFrame(self.root, text="학생 목록")
        list_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Treeview 테이블 생성
        columns = ("name", "id", "major")
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings")

        # 테이블 헤더 설정
        self.tree.heading("name", text="이름")
        self.tree.heading("id", text="학번")
        self.tree.heading("major", text="학과")

        self.tree.pack(fill="both", expand=True)

        # 버튼 영역 프레임
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=10)

        # 기능 버튼 생성
        ttk.Button(btn_frame, text="삭제", command=self.delete_student).grid(row=0, column=0, padx=10)
        ttk.Button(btn_frame, text="파일로 저장", command=self.save_file).grid(row=0, column=1, padx=10)
        ttk.Button(btn_frame, text="파일 불러오기", command=self.load_file).grid(row=0, column=2, padx=10)
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
