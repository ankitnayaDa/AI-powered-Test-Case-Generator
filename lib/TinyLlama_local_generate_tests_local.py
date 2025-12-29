#AutoTokenizer : Converts text → numbers (tokens) the model understands | Also converts numbers → text when decoding the output
#AutoModelForCausalLM : Loads a causal language model | “Causal” = predicts the next token based on previous tokens (GPT-style)
from transformers import AutoModelForCausalLM, AutoTokenizer
#PyTorch is the deep learning framework the model runs on | Handles tensors, CPU/GPU execution, memory, etc.
import torch

#Chooses a free, public, chat-tuned model | Smaller models may run on CPU, larger models may require a GPU
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

#Load the tokenizer | Downloads tokenizer files (first run only)
tokenizer = AutoTokenizer.from_pretrained(model_name)
#Load the model
#from_pretrained(model_name) | Downloads model files (first run only)
#device_map="auto" | GPU if available Otherwise CPU
#torch_dtype=torch.float32 | Uses standard precision Safer on CPU
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    torch_dtype=torch.float32
)

with open("prompts/telecom_ipv6_cups_tests.txt") as f:
    template = f.read()

feature_desc = """
The system introduces IPv6 support in 4G CUPS architecture,
allowing UEs to obtain IPv6 addresses and establish data
sessions over IPv6 via SGW-U and PGW-U while control plane
functions remain on SGW-C and PGW-C using PFCP signaling.
The feature supports dual-stack IPv4/IPv6 subscribers and
ensures session continuity during control or user plane
failures
"""

prompt = template.replace("{{FEATURE_DESCRIPTION}}", feature_desc)

#Takes a text prompt | Returns generated text
def get_completion(prompt: str) -> str:
    #Prompt construction
    full_prompt = prompt + f"""
{prompt}
"""
    #tokenizer Converts text → token IDs | Returns PyTorch tensors
    #return_tensors="pt" | Returns PyTorch tensors
    #.to(model.device) | Moves tensors to the same device as the model (CPU or GPU)
    inputs = tokenizer(full_prompt, return_tensors="pt").to(model.device)
    #Generate output tokens | Text generation (the “thinking” step)
    outputs = model.generate(
        **inputs,
        max_new_tokens=300,
        temperature=0.3,
        do_sample=True,
        top_p=0.9,
    )
    #Decode tokens back to text
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

if __name__ == "__main__":
    prompt = "Generate test cases"
    print(get_completion(prompt))
