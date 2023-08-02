from prefect.deployments import Deployment

from training import train, preprocess

if __name__ == '__main__':

    deployment_processor = Deployment.build_from_flow(
        flow=preprocess.preprocessor_flow, name='pre-processor'
    )

    deployment_train = Deployment.build_from_flow(flow=train.train_flow, name='train')

    deployment_processor.apply()
    deployment_train.apply()

    # preprocess.preprocessor_flow()
    # train.train_flow()
