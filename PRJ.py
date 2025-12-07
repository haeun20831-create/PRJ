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
        # Treeview 데이터를 리스트로 변환
        students = []
        for row in self.tree.get_children():
            values = self.tree.item(row)["values"]
            students.append({
                "name": values[0],
                "id": values[1],
                "major": values[2]
            })
        try:
            # 파일 확장자에 따라 분기
            if file.endswith('.json'):
                # JSON으로 저장
                with open(file, "w", encoding="utf-8") as f:
                    json.dump(students, f, ensure_ascii=False, indent=4)
            elif file.endswith('.csv'):
                # CSV로 저장
                df = pd.DataFrame(students)
                df.to_csv(file, index=False, encoding='utf-8-sig') # Excel 한글 깨짐 방지
            elif file.endswith('.xlsx'):
                # Excel로 저장
                df = pd.DataFrame(students)
                df.to_excel(file, index=False)
            else:
                messagebox.showwarning("지원하지 않는 형식", "JSON, CSV, XLSX 파일 형식만 지원합니다.")
                return
            # 저장 완료 메시지
            messagebox.showinfo("저장 완료", f"{file.split('/')[-1]} 파일 저장 완료!")
        except Exception as e:
            # 저장 오류 메시지
            messagebox.showerror("저장 오류", f"파일을 저장하는 중 오류가 발생했습니다:\n{e}")
    # 파일 불러오기 함수 (JSON, CSV, Excel)
    def load_file(self):
        file = filedialog.askopenfilename(
            title="학생 정보 불러오기",
            filetypes=[
                ("Supported Files", "*.json *.csv *.xlsx"),
                ("JSON Files", "*.json"),
                ("CSV Files", "*.csv"),
                ("Excel Files", "*.xlsx"),
                ("All Files", "*.*")
            ]
        )
        # 불러오기 취소 시 종료
        if not file:
            return

        data_list = []
        try:
            # 파일 확장자에 따라 분기
            if file.endswith('.json'):
                # JSON 파일 로드
                with open(file, "r", encoding="utf-8") as f:
                    data_list = json.load(f)
            elif file.endswith('.csv'):
                # CSV 파일 로드
                df = pd.read_csv(file)
                data_list = df.to_dict('records') # DataFrame -> dict list
            elif file.endswith('.xlsx'):
                # Excel 파일 로드
                df = pd.read_excel(file)
                data_list = df.to_dict('records') # DataFrame -> dict list
            else:
                messagebox.showwarning("지원하지 않는 형식", "JSON, CSV, XLSX 파일 형식만 지원합니다.")
                return
        except Exception as e:
            # 불러오기 오류 메시지
            messagebox.showerror("불러오기 오류", f"파일을 읽는 중 오류가 발생했습니다:\n{e}")
            return
        # 기존 목록 초기화
        self.tree.delete(*self.tree.get_children())

        # 불러온 데이터를 테이블에 삽입
        for data in data_list:
            self.tree.insert("", "end", values=(data["name"], data["id"], data["major"]))

        # 불러오기 완료 메시지
        messagebox.showinfo("불러오기 완료", f"{file.split('/')[-1]} 파일 불러오기 성공!")