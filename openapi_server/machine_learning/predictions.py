import pickle
import numpy as np
from singleton_decorator import singleton

@singleton
class Predictor:
    def __init__(self):
        with open('LoLModel.sklearn', 'rb') as infile:
            self.__model = pickle.load(infile)
    
    def predict(self, X):
        return self.__model.predict(X)
    
    def dict2data(self, dikt):
        data_list=[dikt['firstBlood'], dikt['firstTower'], dikt['firstInhibitor'], dikt['firstDragon'],
              dikt['team1_tower_kills'], dikt['team1_inhibitor_kills'], dikt['team1_baron_kills'], dikt['team1_dragon_kills'],
              dikt['team1_rift_herald_kills'],
               dikt['team2_tower_kills'], dikt['team2_inhibitor_kills'], dikt['team2_baron_kills'], dikt['team2_dragon_kills'],
              dikt['team2_rift_herald_kills']]
        return np.array(data_list).reshape(1, -1)