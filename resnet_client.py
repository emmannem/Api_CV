#from _future_ import print_function

import json

import numpy as np
import requests

# The server URL specifies the endpoint of your server running the ResNet
# model with the name "resnet" and using the predict interface.
#SERVER_URL = 'http://localhost:8500/v1/models/resnet:predict'
SERVER_URL = 'http://localhost:8080/header'


def main():
  # Send few requests to warm-up the model.
  for _ in range(10):
    response = requests.get(SERVER_URL)
    response.raise_for_status()

  # Send few actual requests and report average latency.
  total_time = 0
  num_requests = 1000
  index = 0
  for _ in range(num_requests):
    response = requests.get(SERVER_URL)
    response.raise_for_status()
    total_time += response.elapsed.total_seconds()
    prediction = response.json()
#    prediction = response.json()
    print (prediction)
    #index = index + 1


#  print (prediction)
  print('Prediction class: {}, avg latency: {} ms'.format(
      np.argmax(prediction), (total_time * 1000) / num_requests))


main()
