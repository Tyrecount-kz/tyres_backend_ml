from rest_framework import generics,status
from rest_framework.decorators import api_view
from ml_predict.models import Prediction
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
import numpy as np
from .serializers import PredictionSerializer
import pickle
import pandas as pd
from sklearn import preprocessing
from django.conf import settings
from sklearn.preprocessing import StandardScaler
import os
from shop.models import Car

BASE_DIR = settings.BASE_DIR

@api_view(["POST"])
def make_prediction(request):
    if request.method == 'POST':
        serializer = PredictionSerializer(data=request.data)
        print(request.data["year"])
        if serializer.is_valid():
            print(BASE_DIR)
            workpath = os.path.dirname(os.path.abspath(__file__)) #Returns the Path your .py file is in
            data = pd.read_csv(os.path.join(workpath,'FinalData.csv'))

            def DroppingAllOutliers(data):
                data.drop(data[data['Mileage'] >= 0.1 * 10**7].index, inplace=True)
                data.drop(data[data['Price'] >= 0.2 * 10**8].index, inplace=True)
                data.drop(data[data['Volume'] >= 4.7].index,inplace=True)
                data.drop(data[data['Year'] <= 1985].index, inplace=True)

                data.drop(data[data['Price'] >= 1.22 * 10**7].index, inplace=True)
                data.drop(data[data['Mileage'] >= 0.48 * 10**6].index, inplace=True)
                data.drop(data[(data['Volume'] >= 3.7) | (data['Volume'] < 0.3)].index, inplace=True)
                return data
            data = DroppingAllOutliers(data)

            df = data
            df = df.append(pd.Series([request.data["city"],request.data["year"],request.data["shell"],float(request.data["volume"]),int(request.data["mileage"]),request.data["transmisson"],
                                      request.data["rudder"],request.data["gear"],request.data["custom_cleared"],request.data["type_engine"],
                                      request.data["company"],request.data["model"],0], index=df.columns ), ignore_index=True)

            # Numerical columns names
            num_cols = data.select_dtypes(include=np.number).columns

            # Categorical columns names
            cat_cols = data.select_dtypes(exclude=np.number).columns

            def SS(data):
                norm = StandardScaler()
                data['Price'] = np.log(data['Price'])
                data['Mileage'] = norm.fit_transform(np.array(data['Mileage']).reshape(-1, 1))
                data['Year'] = norm.fit_transform(np.array(data['Year']).reshape(-1, 1))
                data['Company'] = norm.fit_transform(np.array(data['Company']).reshape(-1, 1))
                data['Model'] = norm.fit_transform(np.array(data['Model']).reshape(-1, 1))
                data['City'] = norm.fit_transform(np.array(data['City']).reshape(-1, 1))

                # scaling target variable
                q1, q3 = (data['Price'].quantile([0.25, 0.75]))
                o1 = q1 - 1.5 * (q3 - q1)
                o2 = q3 + 1.5 * (q3 - q1)
                data = data[(data.Price >= o1) & (data.Price <= o2)]
                return data

            le = preprocessing.LabelEncoder()
            data[cat_cols] = data[cat_cols].apply(le.fit_transform)

            data = SS(data)

            new_data = data[-1:]
            model = pickle.load(open(os.path.join(workpath,'betaV1.pkl'),'rb'))
            #'Year','Volume','Mileage','Model','CustomsCleared','Transmission','Company'
            p = model.predict([new_data['Year'],new_data['Volume'],new_data['Mileage'],new_data['Model'],new_data['CustomsCleared'],new_data['Transmission'],new_data['Company']])
            
            answer = round(np.e**p[0])
            print(round(np.e**p[0]))
            
            return Response(answer)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        