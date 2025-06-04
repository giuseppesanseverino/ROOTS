from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F
import numpy as np
import pandas as pd

raw_data = pd.read_csv("/content/drive/MyDrive/across_hackathon_data/arxiv_dataset.csv")
embeddings = np.load("/content/drive/MyDrive/across_hackathon_data/arxiv_scibert_embeddings.npy")
metadata_file = "/content/drive/MyDrive/across_hackathon_data/arxiv_scibert_embeddings.csv"
df = pd.read_csv(metadata_file)

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

promt_string = "Self-adaptive Operating system"

inputs = tokenizer(promt_string, return_tensors="pt", max_length=512, truncation=True, padding="max_length")

with torch.no_grad():
  outputs = model(**inputs)

token_embddings = outputs.last_hidden_state

attention_mask = inputs["attention_mask"]
input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embddings.size()).float()
token_embeddings = token_embddings * input_mask_expanded

sum_embeddings = torch.sum(token_embeddings, 1)

sum_mask = torch.clamp(input_mask_expanded.sum(1), min=1e-9)
sentence_embedding = sum_embeddings / sum_mask

results = []
for idx in embeddings:
  cos_sim = F.cosine_similarity(sentence_embedding, torch.from_numpy(idx))
  results.append(cos_sim)

results = sorted(results)
best_results = results[-5:]

out = []
for idx in topk.indices:
    title = df.iloc[idx.item()].get("title", "N/A")
    out.append(title + "\n")

print(out)