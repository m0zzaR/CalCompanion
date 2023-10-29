import sys
import together

together.api_key ="f2458062d03be3ce2e26da297a5cb6208a47aeaaeb04f6bad7e83388bf296beb"

def ask():
  print("Say 'exit' in order to leave chat bot")

  inp = ""
  while True:
    inp = input('AMA: ')
    if inp == "exit":
      sys.exit()
    output = together.Complete.create(
      prompt = "\n<bot>:", 
      model = "lmsys/vicuna-13b-v1.5", 
      max_tokens = 256,
      temperature = 0.8,
      top_k = 60,
      top_p = 0.6,
      repetition_penalty = 1.1,
      stop = ['<human>', '\n\n']
    )

    # print generated text
    print(output['prompt'][0]+output['output']['choices'][0]['text'])