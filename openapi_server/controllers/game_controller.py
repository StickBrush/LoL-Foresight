import connexion
import six

from openapi_server.models.api_response import ApiResponse  # noqa: E501
from openapi_server.models.score import Score  # noqa: E501
from openapi_server import util
from openapi_server.machine_learning.predictions import Predictor


def predict_game():  # noqa: E501
    """Predict a game

     # noqa: E501

    :param score: Objective score
    :type score: dict | bytes

    :rtype: ApiResponse
    """
    if connexion.request.is_json:
        try:
            pr = Predictor()
            data = pr.dict2data(connexion.request.get_json())
            dct = {'winner': pr.predict(data)[0]}
            return dct, 200
        except Exception:
            return {}, 405
    else:
        return {}, 405
