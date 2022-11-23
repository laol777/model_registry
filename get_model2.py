import dvc.api

with dvc.api.open(
    'pytorch_model.bin',
    repo='https://github.com/laol777/model_registry',
    mode='rb'
) as f:
    model = f.read()
