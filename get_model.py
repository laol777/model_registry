import dvc
import dvc.api

with dvc.api.open('pytorch_model.bin', mode='rb') as f:
    model = f.read()
