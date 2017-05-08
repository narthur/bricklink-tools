from bricklink import api
import csv, os

class PartRepository:
    def __init__(self):
        secret = {}
        secretPath = os.path.dirname(__file__) + "/../secret"
        with open(secretPath, 'r') as csvfile:
            secretFile = csv.reader(csvfile, delimiter=',')
            for row in secretFile:
                secret[row[0]] = row[1]
        self.api = api.ApiClient(secret["ConsumerKey"],secret["ConsumerSecret"],secret["TokenValue"],secret["TokenSecret"])