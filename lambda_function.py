import json
import codecs
  
def lambda_handler(event, context):
    print("Hello kinkoman", file=codecs.open('hello.txt', 'w', 'utf-8'))
    return event


