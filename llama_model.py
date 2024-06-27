import os
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

def interact_with_llama_model(input_text):
    model_name = "../llama/Meta-Llama-3-8B/"  # Path to the local model directory
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    
    generator = pipeline('text-generation', model=model, tokenizer=tokenizer)
    response = generator(input_text, max_length=150, num_return_sequences=1)
    return response[0]['generated_text']

if __name__ == "__main__":
    import sys
    input_text = sys.argv[1]
    print(interact_with_llama_model(input_text))
