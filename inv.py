import tkinter as tk
from tkinter import messagebox
import pymysql


# DB 연결
def connect_db():
    return pymysql.connect(
        host = "localhost",
        user = "root",
        password = "tjwjddn0904@",
        database = "burger",
        charset = "utf8mb4",
        cursorclass = pymysql.cursors.DictCursor
    )


# 기능 함수
def read_data():
    listbox.delete(0, tk.END)
    conn = connect_db()
    with conn.cursor() as cur:
        cur.execute("select * from menu order by id")
        for row in cur.fetchall():
            listbox.insert(tk.END, f"{row['category']} | {row['id']} | {row['name']} | {row['price']} | {row['stock']}")

def add_data():
    name = entry_name.get()
    qty = entry_qty.get()
    if name and qty.isdigit():
        cur.execute("INSERT INTO menu (name, stock) VALUES (%s, %s)", (name, int('stock')))
        conn.commit()
        read_data()
    else:
        messagebox.showerror("에러", "상품명과 수량을 올바르게 입력하세요")

def delete_data():
    selected = listbox.curselection()
    if selected:
        item = listbox.get(selected[0])
        id = item.split(" | ")[0]
        cur.execute("DELETE FROM menu WHERE id=%s", (id,))
        conn.commit()
        read_data()
    else:
        messagebox.showerror("에러", "삭제할 항목을 선택하세요")

def update_data():
    selected = listbox.curselection()
    if selected:
        item = listbox.get(selected[0])
        item_id = item.split(" | ")[0]
        new_qty = entry_qty.get()
        if new_qty.isdigit():
            cur.execute("UPDATE menu SET inven=%s WHERE id=%s", (int(new_qty), item_id))
            conn.commit()
            read_data()
        else:
            messagebox.showerror("에러", "수량을 올바르게 입력하세요")
    else:
        messagebox.showerror("에러", "수정할 항목을 선택하세요")

# GUI 만들기
root = tk.Tk()
root.title("버거킹 재고관리 프로그램")

tk.Label(root, text="상품명").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="수량").grid(row=1, column=0)
entry_qty = tk.Entry(root)
entry_qty.grid(row=1, column=1)

tk.Button(root, text="추가", command=add_data).grid(row=2, column=0)
tk.Button(root, text="삭제", command=delete_data).grid(row=2, column=1)
tk.Button(root, text="수정", command=update_data).grid(row=2, column=2)
tk.Button(root, text="읽기", command=read_data).grid(row=2, column=3)

listbox = tk.Listbox(root, width=50)
listbox.grid(row=3, column=0, columnspan=4)

read_data()
root.mainloop()
