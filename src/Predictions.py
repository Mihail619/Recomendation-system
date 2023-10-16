# import Load_model, Load_sql

# model = Load_model.model
# data = Load_sql.load_features()

from pandas import DataFrame

# выполняем предсказания для user_id

def prediction_list(user_id: int, model, data: DataFrame, limit: int):
    # print(f'data: {data.head()}')
    user_data = data[data['user_id'] == user_id].drop(('timestamp'), axis=1)

    predicts = model.predict_proba(user_data)[:,1]
    print(f'predicts: {predicts}')
    user_data['predicts'] = predicts
    print(f'user_data: {user_data.head()}')
    user_data = user_data.sort_values('predicts', ascending=False)
    print(f'user_data sorted: {user_data}')

    return list(user_data.head(limit)['post_id'])