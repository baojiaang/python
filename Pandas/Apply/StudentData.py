import pandas as pd

data = pd.read_csv('./student-mat.csv')
student_data = data.loc[:, "school":"guardian"]

f = lambda x: str(x) + "aaa"

# apply, 所有数据都应用这个函数, 原来的数据并不会改变，需要赋值给新的数据才能改变数据
print(student_data['school'].apply(f))


def bigger_than_eighteen(age):
    if age > 18:
        return True
    else:
        return False
student_data['adult'] = student_data['age'].apply(bigger_than_eighteen)
print(student_data.head())