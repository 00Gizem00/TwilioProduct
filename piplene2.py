from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import torch

model_name = "meta-llama/Meta-Llama-3-8B"
use_auth_token = "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"

# Tokenizer ve model yükleme
tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=use_auth_token)
model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token=use_auth_token, torch_dtype=torch.bfloat16, device_map="auto")

# Pipeline oluşturma
generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

product_name = "blue shirt"

prompt = f"Generate category and color tags for suitable clothing combinations for a {product_name}."

# Text generation
response = generator(
    prompt,
    max_length=50,
    num_return_sequences=1,
    truncation=True,
    pad_token_id=tokenizer.eos_token_id,
    do_sample=True
)

print(response[0]['generated_text'])
