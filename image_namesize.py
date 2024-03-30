import os
from PIL import Image
import shutil

# 현재 스크립트가 위치한 디렉토리를 가져옵니다.
# current_directory = os.path.dirname(os.path.abspath(__file__))

def seonu():
    file_names = []
    image_info = {}
    long_question = []
    long_question_ans= []

    [ff for ff in os.listdir() if 'png' in ff]
    # 폴더가 존재하는지 확인합니다.
    if os.path.exists(photo_folder_path) and os.path.isdir(photo_folder_path):
        file_names = os.listdir(photo_folder_path)
        if 'desktop.ini' in file_names:
            file_names.remove('desktop.ini')

        for file_name in file_names:
            file_path = os.path.join(photo_folder_path, file_name)



            try:
                with Image.open(file_path) as img:
                    width, height = img.size
                    image_info[file_name] = {"size": (width, height)}

                    if ("답" not in file_name and height > 350) or ("답" not in file_name and "서술" in file_name):
                        long_question.append(file_name)
                        corresponding_answer_file = file_name.replace("번", "번답")
                        if corresponding_answer_file in file_names:
                            long_question_ans.append(corresponding_answer_file)
                    # if "서술" in file_name :
                    #     long_question.append(file_name)
                    #     corresponding_answer_file = file_name.replace("번", "번답")
                    #     if corresponding_answer_file in file_names:
                    #         long_question_ans.append(corresponding_answer_file)

            except Exception as e:
                print(f"Error processing {file_name}: {str(e)}")

        # Exclude long questions from file_names
        # short_question = [name for name in file_names if ("답" and name) not in long_question]
        #
        # # Create short_question_ans based on the remaining file names
        # short_question_ans = [name.replace("번", "번답") for name in short_question]

    file_names_with_answer = [name for name in file_names if "답" in name]
    file_names_without_answer = [name for name in file_names if "답" not in name]

    short_question = [name for name in file_names_without_answer if name not in long_question]
    short_question = [name for name in short_question if "png" in name]
    short_question_ans = [name for name in file_names_with_answer if name not in long_question_ans]


    folder_name = ['short_question','short_question_ans','long_question','long_question_ans']

    # os.chdir(os.getcwd()+'\★수학1')
    for destination_directory in folder_name:
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)

    for file_name in [ff for ff in os.listdir() if 'png' in ff]:
        # 파일이 이동할 목록에 있는지 확인합니다.
        if file_name in short_question:
            # 소스 파일의 전체 경로를 가져옵니다.
            source_file_path = os.path.abspath(file_name)
            # 대상 파일의 전체 경로를 가져옵니다.
            destination_file_path = os.path.join(os.getcwd(),'short_question', file_name)
            # 파일을 대상 디렉토리로 이동합니다.
            shutil.move(source_file_path, destination_file_path)

    for file_name in [ff for ff in os.listdir() if 'png' in ff]:
        if file_name in short_question_ans:
            source_file_path = os.path.abspath(file_name)
            destination_file_path = os.path.join(os.getcwd(),'short_question_ans', file_name)
            shutil.move(source_file_path, destination_file_path)

    for file_name in [ff for ff in os.listdir() if 'png' in ff]:
        if file_name in long_question_ans:
            source_file_path = os.path.abspath(file_name)
            destination_file_path = os.path.join(os.getcwd(),'long_question_ans', file_name)
            shutil.move(source_file_path, destination_file_path)
    for file_name in [ff for ff in os.listdir() if 'png' in ff]:
        if file_name in long_question:
            source_file_path = os.path.abspath(file_name)
            destination_file_path = os.path.join(os.getcwd(),'long_question', file_name)
            shutil.move(source_file_path, destination_file_path)




# 디렉토리만 수정할것
current_directory = 'E:\\★시험지 만들기'
# 현재 디렉토리와 "photo" 폴더를 결합합니다.
photo_folder_path = os.path.join(current_directory, "★수학1",'002_02_삼각함수')
os.chdir(photo_folder_path)
seonu()