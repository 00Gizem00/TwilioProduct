from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM


model_name = "Qwen/Qwen2-72B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

def generate_combination_tags(product_name):
    prompt = f"Generate category and color tags for suitable clothing combinations for a {product_name}."
    response = generator(
        prompt,
        max_length=50,
        num_return_sequences=1,
        truncation=True,
        pad_token_id=tokenizer.eos_token_id,

    )
    tags = response[0]['generated_text'].strip().split(', ')
    combinations = [tag.split()[:2] for tag in tags] 
    return combinations

def generate_message(product_name, tags):
    combination_text = '\n'.join([f"- {category} {color}" for category, color in tags])
    prompt = f"Write a positive message for a customer who just bought a {product_name} and suggest the following matching combinations:\n{combination_text}"
    response = generator(
        prompt,
        max_length=100,
        num_return_sequences=1,
        truncation=True,
        pad_token_id=tokenizer.eos_token_id,
    )
    message = response[0]['generated_text'].strip()
    return message

# deneme
product_name = "blue shirt"
combinations = generate_combination_tags(product_name)
print(combinations)
