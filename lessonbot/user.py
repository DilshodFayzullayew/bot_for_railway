import pandas as pd
from base import get_user_table_number,get_file_names,get_salary, finished_work, generate_graph

class User:
    def __init__(self):
        return


    def get_information(self, telegram_id):
       return get_user_table_number(telegram_id)

    def get_file(self,telegram_id,path):
        return get_file_names(telegram_id,path)

    def get_salary(self,date,path):
        return get_salary(date,path)

    def finished(self, date):
        return finished_work(date)

    def graph(self, list1, list2):
        return generate_graph(list1, list2)