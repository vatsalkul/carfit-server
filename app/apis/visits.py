from flask import request, Response
import json
from flask_restplus import Api, Resource, Namespace
import datetime

api = Namespace('visits', description='Car visits')


@api.route('/latest')
class Visits(Resource):
    def get(self):
        
        dates = ['2020-06-29T07:30:00']
        t = datetime.datetime.today().date()
        today = str(datetime.datetime.today().date())
        yesterday = str(t - datetime.timedelta(days=1))
        tomorrow = str(t + datetime.timedelta(days=1))
        day_after = str(t + datetime.timedelta(days=2))
        next_month = str(t + datetime.timedelta(days=30))
        print(next_month)
        
        
        with open('./content/latests.json') as f:
            data = json.load(f)
            all_visits = data["data"]
            
            dates = [yesterday, yesterday, yesterday, 
                    today, today, today, today, today,
                    tomorrow, tomorrow, tomorrow,
                    day_after, day_after, day_after, day_after,
                    next_month, next_month
                    ]
            count = 0
            for visit in all_visits:
                
                
                start = visit["startTimeUtc"]
                start = start.split("T")
                time = start [1]
                visit["startTimeUtc"] = dates[count] + "T" + time
                count = count + 1
                
        return {
                "success": True,
                "message": "Got visits successfully",
                "data": all_visits,
                "code": 200
                }
