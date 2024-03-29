#%%
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilenames
from pyhwpx import Hwp

#os.chdir(os.getcwd()+'\★수학(상)')
# 이미지 선택
# 수치넣고
root = Tk()
짧은문제이미지리스트 = askopenfilenames(
    title="짧은문제이미지를 모두 선택해주세요.",
    initialdir=os.getcwd(),
)
root.destroy()

# 영상
root = Tk()
긴문제이미지리스트 = askopenfilenames(
    title="긴문제이미지를 모두 선택해주세요.",
    initialdir=os.getcwd(),
)
root.destroy()


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
#대상 = os.path.basename(짧은문제이미지리스트[0]).split("(")[0]

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
    hwp.insert_text(idx+1)
    hwp.move_to_field('출처',idx=idx)
    hwp.insert_text(img.split("/")[-1].split()[0]+" "+img.split("/")[-1].split()[3])
    hwp.move_to_field("문제", idx=idx)
    hwp.insert_picture(img)

hwp.put_field_text('단원명',img.split("/")[-3])




tbl_content2 = hwp2.get_into_nth_table(-1)
hwp2.move_pos(tbl_content2.GetAnchorPos(1))
hwp2.SelectCtrlFront()

hwp2.Copy()
for i in range(복사할표갯수2):  # 빈 칸 하나는 이미 있으니까
    hwp2.Paste()


#%%
#hwp.put_field_text("측점", 측점아이디)


#%%
for idx, img in enumerate(긴문제이미지리스트):
    hwp2.move_to_field("번호", idx=idx)
    hwp2.insert_text(idx+1+len(짧은문제이미지리스트))
    hwp2.move_to_field("문제", idx=idx)
    hwp2.insert_picture(img)

# 셀 병합하기
# i = 0
# while hwp.move_to_field("A1", idx=i):
#     hwp.TableLowerCell()
#     hwp.TableCellBlockExtendAbs()
#     hwp.TableColPageDown()
#     hwp.TableMergeCell()
#     hwp.Cancel()
#     i += 1


#%% 마무리3 : 35905 삽입(전부 동일하다고 가정)
#hwp.put_field_text("대상", 대상)
hwp.save_as('1.hwp')
hwp2.save_as('2.hwp')


hwp3 = Hwp(new=True,visible=False)
hwp3.insert_file('1.hwp')
hwp3.MoveDocEnd()
hwp3.insert_file('2.hwp')
hwp3.MoveDocBegin()
hwp3.Delete()
hwp3.save_as(img.split("/")[-3]+' 문제.hwp')
hwp.quit()
hwp2.quit()
hwp3.quit()

