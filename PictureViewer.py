import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("600x400")

imgpass=tk.StringVar(value='')

# 画像を表示
def open_file():
  # ファイルダイアログ
  typ = [('画像ファイル', '*.jpg;*.png;*.bmp;*.gif;*.tiff')]
  imgpass.set(filedialog.askopenfilenames(filetypes = typ))
  if imgpass.get()=="":
    return 0
  # 表示するイメージを用意
  global img
  spass=str(imgpass.get())
  spass=spass[2:len(spass)-3] #謎の文字処理 
  rimg = Image.open(spass)
  img = ImageTk.PhotoImage(rimg)
  canvas.create_image(0,0,image=img,tag="illust",anchor=tk.NW)
  # Canvasのスクロール範囲を設定
  canvas.config(scrollregion=(0,0,rimg.width,rimg.height))

# アプリケーションを終了
def close_disp():
  root.quit()

# メニューを作成
men = tk.Menu(root) 
root.config(menu=men)
menu_file = tk.Menu(root)
men.add_cascade(label='ファイル', menu=menu_file)
menu_file.add_command(label='開く', command=open_file) 
menu_file.add_separator() 
menu_file.add_command(label='終了する', command=close_disp)

# Canvas Widget を生成して配置
canvas = tk.Canvas(root)
canvas.grid(row=0,column=0,sticky=tk.W + tk.E + tk.N + tk.S)
root.grid_columnconfigure(0,weight=1)
root.grid_rowconfigure(0,weight=1)

# Scrollbar を生成して配置
barX = tk.Scrollbar(root, orient=tk.HORIZONTAL)
barX.grid(row=1, column=0, sticky="ew")
barY = tk.Scrollbar(root, orient=tk.VERTICAL)
barY.grid(row=0, column=1, sticky="ns")

# Scrollbarを制御をCanvasに通知する処理を追加
barY.config(command=canvas.yview)
barX.config(command=canvas.xview)

# Canvasの可動域をScreoobarに通知する処理を追加
canvas.configure(yscrollcommand=barY.set, xscrollcommand=barX.set)
canvas.configure(xscrollcommand=barX.set, yscrollcommand=barY.set) 

# マウスホイールに対応
barY.bind('<MouseWheel>', lambda e:canvas.yview_scroll(-1*(1 if e.delta>0 else -1),tk.UNITS))
barY.bind('<Enter>',lambda e:barY.focus_set())
canvas.bind('<MouseWheel>', lambda e:canvas.yview_scroll(-1*(1 if e.delta>0 else -1),tk.UNITS))
canvas.bind('<Enter>',lambda e:barY.focus_set())
barX.bind('<MouseWheel>', lambda e:canvas.xview_scroll(-1*(1 if e.delta>0 else -1),tk.UNITS))
barX.bind('<Enter>',lambda e:barX.focus_set())

# Canvas上に適当な図形を書いておく
#id = canvas.create_oval(0, 0, 400, 400)
#canvas.itemconfigure(id, fill = 'red')

root.mainloop()
