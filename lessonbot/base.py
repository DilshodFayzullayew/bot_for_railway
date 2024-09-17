import pandas as pd
import os
import io
import matplotlib.pyplot as plt

file_path = "C:\\Users\\Hp\\Desktop\\admin\\IshcilarPassword\\Ishchilar.xlsx"
file_path1 = "C:\\Users\\Hp\\Desktop\\admin\\ishchilarMalumoti\\Ischilarmalumotnoma.xlsx"
file_path2 = "C:\\Users\\Hp\\Desktop\\admin\\user_check\\user_check.xlsx"

df = pd.read_excel(file_path)
df1 = pd.read_excel(file_path1)
df2 = pd.read_excel(file_path2)
def is_user_exist(userdata, user_id):
    user_splited = userdata.split(" ")
    if len(user_splited) == 1:
        return "notTrue"
    table_number = int(user_splited[0])
    password = int(user_splited[1])
    if table_number == 32134 and password != 32134:
        return "admpass"

    if table_number == 32134 and password == 32134:
        return "admin"

    if table_number in df['table_number'].values:
        index_of_table_number = df.index[df['table_number'] == table_number].tolist()[0]
        index_of_password = df.index[df['password'] == password].tolist()[0]
        if index_of_password == index_of_table_number:
            df.loc[index_of_table_number,'user_telegram_id'] = user_id
            df.to_excel(file_path, index=False)

            return "user"


    else:
        return "userNotexists"





def get_user_table_number(user_telegram_id):
    index = df.index[df['user_telegram_id'] == user_telegram_id].tolist()[0]
    res = df.loc[index,'table_number']
    index_table_number = df1.index[df1['table_number'] == res].tolist()[0]
    info = df1.loc[index_table_number]
    return info

def get_file_names(user_telegram_id, path):
    file_path = "C:\\Users\\Hp\\Desktop\\admin\\"+path
    list_file_name = []
    for file in os.listdir(file_path):
        if file.endswith('.xlsx') or file.endswith('.xls'):
            filename = file[:-5]
            list_file_name.append(filename)
    return list_file_name

def get_salary(date,path):
    file_path = "C:\\Users\\Hp\\Desktop\\admin\\"+path
    for file in os.listdir(file_path):
        if file.endswith('.xlsx') or file.endswith('.xls'):
            filename = file[:-5]
            if filename == date:
                file_salary = file_path + f"\\{filename}.xlsx"
                df_salary = pd.read_excel(file_salary)
                response = df_salary.iloc[0]
                return response





def finished_work(date):
    file_path = "C:\\Users\\Hp\\Desktop\\admin\\BajarilganIshlar"
    for file in os.listdir(file_path):
        if file.endswith('.xlsx') or file.endswith('.xls'):
            filename = file[:-5]
            if filename == date:
                file_done = file_path + f"\\{filename}.xlsx"
                df_work_done = pd.read_excel(file_done)
                response = df_work_done.iloc[0:]
                print(response)


def generate_graph(list1, list2):
    x = list1
    y = list2

    plt.plot(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Grafig')

    # Save the plot to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Clear the plot
    plt.clf()

    return buffer


