import argparse
import sys
from apache_beam.options.pipeline_options import PipelineOptions
import os
cwd = os.getcwd()


class StreamPipelineOptions(PipelineOptions):
    @classmethod
    def create_pipeline_options(cls,argv:sys.argv):
        print(argv)
        parser = argparse.ArgumentParser()
        parser.add_argument('--input_topic', required=True, help='input pubsub topic name',
                            default='projects/topic_name')
        known_args, pipeline_args = parser.parse_known_args(argv)
        return known_args, pipeline_args
