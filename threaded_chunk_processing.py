import threading
import together
import time
from requests.exceptions import HTTPError

together.api_key = "a66ca7b7091cd606df07d72d5f103a61a3f62762312437bcdf5304211e9f558e"

def inference(question: str, max_tokens=512) -> str:
    prompt = f"<human>: {question}\n<bot>:"
    output = together.Complete.create(
        prompt=prompt,
        model="lmsys/vicuna-13b-v1.5",
        max_tokens=max_tokens,
        temperature=0.7,
        top_k=10,
        top_p=0.7,
        repetition_penalty=1,
        stop=["<human>:"],
    )

    return output["output"]["choices"][0]["text"]


def process_chunks_in_parallel(chunks, question):
    relevant_info = []

    # Define a function to process a single chunk
    def process_chunk(chunk):
        prompt = chunk
        prompt += "\n**From the content above, summarize everything that may be relevant to the question: "
        prompt += f'"{question}"**'
        try:
            result = inference(prompt, max_tokens=512)
            relevant_info.append(result)
        except HTTPError:
            pass

    # Create a list to hold thread objects
    threads = []

    # Start a thread for each chunk
    for chunk in chunks:
        thread = threading.Thread(target=process_chunk, args=(chunk,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    return relevant_info