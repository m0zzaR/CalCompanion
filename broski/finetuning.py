import sys
import together

together.api_key = "f2458062d03be3ce2e26da297a5cb6208a47aeaaeb04f6bad7e83388bf296beb"
def preTrain():
  resp = together.Files.upload(file="./finaloutput.jsonl")
  return resp['id']

def train():

  resp = together.Finetune.create(
    training_file = preTrain(),
    model = 'togethercomputer/llama-2-13b',
    n_epochs = 2,
    n_checkpoints = 1,
    batch_size = 4,
    learning_rate = 1e-5,
    suffix = 'broski',
    wandb_api_key = '95cabb2f0d82c34f322d7a8964f79ceb67267928',
  )
  return resp