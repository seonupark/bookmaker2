#%%
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilenames
from pyhwpx import Hwp

#os.chdir(os.getcwd()+'\★수학(상)')
# 이미지 선택
# 수치넣고
# root = Tk()
# 짧은문제이미지리스트 = askopenfilenames(
#     title="짧은문제이미지를 모두 선택해주세요.",
#     initialdir=os.getcwd(),
# )
# root.destroy()
#
# # 영상
# root = Tk()
# 긴문제이미지리스트 = askopenfilenames(
#     title="긴문제이미지를 모두 선택해주세요.",
#     initialdir=os.getcwd(),
# )
# root.destroy()



basepath = os.getcwd()
mathpath = os.path.join(os.getcwd(),'mathdata')
#os.chdir(mathpath)

def makehwp(짧은문제이미지리스트,긴문제이미지리스트,문제):
    hwp = Hwp(visible=False)
    hwp.open("워크북형식4단.hwp")
    hwp2 = Hwp(new=True,visible=False)
    hwp2.open("워크북형식2단.hwp")

    #%%
    복사할표갯수 = (len(짧은문제이미지리스트) - 4) // 4
    깍두기 = (len(짧은문제이미지리스트) - 4) % 4
    if (len(짧은문제이미지리스트) - 4) % 4:
        복사할표갯수 += 1

    복사할표갯수2 = (len(긴문제이미지리스트) - 2) // 2
    깍두기2 = (len(긴문제이미지리스트) - 2) % 2
    if (len(긴문제이미지리스트) - 2) % 2:
        복사할표갯수2 += 1


    #%%
    짧은문제 = [이미지.rsplit("_")[-1].replace(".png", "") for 이미지 in 짧은문제이미지리스트]
    긴문제 = [이미지.rsplit("_")[-1].replace(".png", "") for 이미지 in 긴문제이미지리스트]

    #%%
    tbl_content = hwp.get_into_nth_table(-1)
    hwp.move_pos(tbl_content.GetAnchorPos(1))
    hwp.SelectCtrlFront()

    #%%
    hwp.Copy()
    for i in range(복사할표갯수):  # 빈 칸 하나는 이미 있으니까
        hwp.Paste()




    #%%
    for idx, img in enumerate(짧은문제이미지리스트):
        hwp.move_to_field("번호", idx=idx)
        hwp.insert_text('   ' +str(idx+1))
        hwp.move_to_field('출처',idx=idx)
        hwp.insert_text(img.split("\\")[-1].split()[0]+" "+img.split("\\")[-1].split()[3])
        hwp.move_to_field("문제", idx=idx)
        hwp.insert_picture(img)

    hwp.put_field_text('단원명',img.split("\\")[-3])

    tbl_content2 = hwp2.get_into_nth_table(-1)
    hwp2.move_pos(tbl_content2.GetAnchorPos(1))
    hwp2.SelectCtrlFront()

    hwp2.Copy()
    for i in range(복사할표갯수2):  # 빈 칸 하나는 이미 있으니까
        hwp2.Paste()

    for idx, img in enumerate(긴문제이미지리스트):
        hwp2.move_to_field("번호", idx=idx)
        hwp2.insert_text(idx+1+len(짧은문제이미지리스트))
        hwp2.move_to_field("문제", idx=idx)
        hwp2.insert_picture(img)

    hwp.save_as('1.hwp')
    hwp2.save_as('2.hwp')


    hwp3 = Hwp(new=True,visible=False)
    hwp3.insert_file('1.hwp')
    hwp3.MoveDocEnd()
    hwp3.insert_file('2.hwp')
    hwp3.MoveDocBegin()
    hwp3.Delete()
    save_name = img.split("\\")[-3]+' '+문제+'.hwp'
    hwp3.save_as(save_name)
    hwp.quit()
    hwp2.quit()
    hwp3.quit()



book=[]
for a in os.listdir(mathpath):
    if a == 'desktop.ini':
        pass
    else:
        book.append(a)

for a in book:
    chapter = os.listdir(os.path.join(mathpath,a))
    for b in  chapter:
        짧은문제 = []
        긴문제 = []
        for c in os.listdir(os.path.join(mathpath,a,b,'short_question')):
            짧은문제.append(os.path.join(mathpath,a,b,'short_question',c))
            긴문제.append(os.path.join(mathpath, a, b, 'long_question', c))
            makehwp(짧은문제,긴문제,'학생용')
            #makehwp(os.listdir(os.path.join(mathpath, a, b, 'short_question_ans')), os.listdir(os.path.join(mathpath, a, b, 'long_question_ans')), '교사용')
