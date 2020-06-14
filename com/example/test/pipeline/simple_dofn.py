import json
import logging
import os

import apache_beam

cwd = os.getcwd()


class SimpleDoFn(apache_beam.DoFn):
    @classmethod
    def print(cls):
        print("Hello")

    def process(self, data):
        print(data)
        return data


class DecodeByteArray(apache_beam.DoFn):
    def process(self, pubsub_data):
        # str_data = pubsub_data.decode('utf-8')
        # print("Data Is : ", pubsub_data)
        # print(type(pubsub_data))
        str_data: str = pubsub_data.decode('utf-8')
        print(str_data)
        logging.info("[simple_dofn] - Event Data :")
        global error_code
        try:
            json_object: json = json.loads(str_data)
            logging.info("Error JSON Payload Received is %s",json_object)
            error_code = json_object['DSABaseException']['ErrorCode']
            logging.info("successfully got ErrorCode data. %s",error_code)
        except:
            logging.error("Error while reading json key daya")
        finally:
            error_code = 'JSON_PARSE_EXCEPTION'

        logging.info("[simple_dofn] ErrorCode is : ", error_code)
        # error_code = 'RUNTIME_ERROR'
        print("Error Code is %s", error_code)
        return error_code
