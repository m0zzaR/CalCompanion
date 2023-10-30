import together
from math import ceil
from threaded_chunk_processing import process_chunks_in_parallel


MAX_CHUNK_SIZE = 20_000  # characters
together.api_key = ""


def inference(prompt: str, max_tokens=512) -> str:
    output = together.Complete.create(
        prompt=prompt,
        model="lmsys/vicuna-13b-v1.5",
        max_tokens=max_tokens,
        temperature=0.7,
        top_k=50,
        top_p=0.7,
        repetition_penalty=1,
        stop=["<human>:"],
    )

    return output["output"]["choices"][0]["text"]


with open("compressed_posts.txt", "r", encoding="utf-8") as data_file:
    compressed_data = data_file.read()


chunks = [
    compressed_data[MAX_CHUNK_SIZE * i : MAX_CHUNK_SIZE * (i + 1)]
    for i in range(ceil(len(compressed_data) / MAX_CHUNK_SIZE))
]

def ask_question(question: str) -> str:
    relevant_info = process_chunks_in_parallel(chunks, question)

    # Ask question
    prompt = "\n".join(relevant_info)
    prompt += "\n**Using the information above answer the following question "
    "in a knolwedgable tone of voice. Refrain from using any vulgar or inappropriate "
    "language. If conflicting views are present respond with the majority view, whilst "
    "acknowledging the views of the larger minorities. Respond like a knowledgeable third party, do not mention data above, commentors, posters, etc.\n"
    prompt += f'Question: "{question}"**'

    return inference(prompt)


if __name__ == "__main__":
    print(ask_question("Is CS 61A hard?"))
