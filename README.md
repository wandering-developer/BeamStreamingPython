# BeamStreamingPython
Example apache beam streaming job using Python SDK

# Run the beam streaming job using DatafloeRunner as follows :

python -m  com.ingka.test.pipeline.stream_application --runner=DataflowRunner --input_topic=projects/<GCP_PROJECT_ID>/subscriptions/subscription-test --project=<GCP_PROJECT_ID> --job_name=test-python-job  --region=europe-west1 --autoscaling_algorithm=THROUGHPUT_BASED --max_num_workers=1 --temp_location=<GCS_TEMP_LOCATION_FOLDER_PATH> --gcpTempLocation=<GCS_TEMP_LOCATION_FOLDER> --streaming --staging_location=<GCS_STAGING_FOLDER_PATH> --setup_file=/c/Users/onpat/PycharmProjects/first-beam-project/setup.py

# Run the streaming job using DirectRunner as follows :

python -m com.ingka.test.pipeline.stream_application --runner=DirectRunner --input_topic=projects/<GCP_PROJECT_ID>/subscriptions/subscription-test --project=<GCP_PROJECT_ID>  --streaming --setup_file=/c/Users/onpat/PycharmProjects/first-beam-project/setup.py
