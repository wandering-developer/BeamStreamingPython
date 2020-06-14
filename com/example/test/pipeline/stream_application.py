import sys

import apache_beam as beam
from apache_beam import Pipeline
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import StandardOptions
import logging
from com.example.test.pipeline.simple_dofn import DecodeByteArray
from com.example.test.pipeline.stream_pipeline_options import StreamPipelineOptions
import os

cwd = os.getcwd()


def run_stream_pipeline(argv):
    logger = logging.getLogger("stream_application")
    stream_options = StreamPipelineOptions()
    print(argv)
    known_args, pipeline_args = stream_options.create_pipeline_options(argv)

    options = PipelineOptions(flags=pipeline_args)
    options.view_as(StandardOptions).streaming = True
    logger.info("[stream_application] - Pipeline options created")
    print(type(options))
    print(options)
    pipeline = beam.Pipeline(options=options)
    logging.info("[stream_application]- Pipeline Created Successfully")
    pubsub_messages = read_pubsub_messages(pipeline, known_args)
    get_pubsub_error_messages(pubsub_messages)
    pipeline.run().wait_until_finish()


def get_pubsub_error_messages(byte_collection):
    logging.info("[stream_application] - Extracting Error Codes")
    byte_collection | "Extract ErrorCodes" >> beam.ParDo(DecodeByteArray()).with_output_types(
        str)


def read_pubsub_messages(pipeline: Pipeline, known_args):
    # print("args : ", known_args)
    logging.info(
        "[stream_application:read_pubsub_messages] - Reading events from subsciption ")
    pubsub_messages = (pipeline | "Read Pubsub Messages" >> beam.io.ReadFromPubSub(
        subscription=known_args.input_topic).with_output_types(bytes))
    return pubsub_messages


if __name__ == '__main__':
    # sys.path.append('com/example/test/pipeline')
    run_stream_pipeline(argv=sys.argv)
