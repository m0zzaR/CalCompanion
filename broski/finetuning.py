import sys
import together

def preTrain():
  resp = together.Files.upload(file="./output.jsonl")
  return resp['id']

def train():

  resp = together.Finetune.create(
    training_file = preTrain(),
    model = 'togethercomputer/llama-2-7b',
    n_epochs = 4,
    n_checkpoints = 0,
    batch_size = 4,
    learning_rate = 1e-5,
    suffix = 'finetune',
    wandb_api_key = '95cabb2f0d82c34f322d7a8964f79ceb67267928',
  )
  return resp