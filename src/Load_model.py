import os
import pickle
from catboost import CatBoostClassifier


def get_model_path(path: str) -> str:
    if os.environ.get("IS_LMS") == "1":  # проверяем где выполняется код в лмс, или локально. Немного магии
        MODEL_PATH = '/workdir/user_input/model'
    else:
        MODEL_PATH = path
    return MODEL_PATH

def load_models():
    model_path = get_model_path("model_test")
    # new_model = pickle.load(open(model_path, 'rb')) # пример как можно загружать модели
    model = CatBoostClassifier()  # здесь не указываем параметры, которые были при обучении, в дампе модели все есть
    model.load_model(model_path, format='cbm')
    return model


model = load_models()

if __name__== "__main__":
    print(model)








