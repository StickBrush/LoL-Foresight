# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.api_response import ApiResponse  # noqa: E501
from openapi_server.models.score import Score  # noqa: E501
from openapi_server.test import BaseTestCase


class TestGameController(BaseTestCase):
    """GameController integration test stubs"""

    def test_predict_game(self):
        """Test case for predict_game

        Predict a game
        """
        score = {
  "firstBlood" : 0,
  "team2_rift_herald_kills" : 1,
  "team2_tower_kills" : 2,
  "team2_dragon_kills" : 7,
  "team2_baron_kills" : 1,
  "team1_dragon_kills" : 7,
  "firstDragon" : 5,
  "team1_rift_herald_kills" : 3,
  "team1_baron_kills" : 9,
  "team1_inhibitor_kills" : 2,
  "firstInhibitor" : 1,
  "firstTower" : 6,
  "team2_inhibitor_kills" : 4,
  "team1_tower_kills" : 5
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/predict',
            method='POST',
            headers=headers,
            data=json.dumps(score),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
