import mlflow

remote_sever_uri = 'https://dagshub.com/Felix-Sam/'
mlflow.set_tracking_uri(remote_sever_uri)

mlflow.set_experiment("/my-experiment")
with mlflow.start_run():
    mlflow.log_param("a", 1)
    mlflow.log_metric("b", 2)
