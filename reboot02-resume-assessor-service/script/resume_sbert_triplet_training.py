import pandas as pd
from sentence_transformers import InputExample, models, SentenceTransformer, losses
from torch.utils.data import DataLoader
import torch
import gc
# import os
# os.environ["PYTORCH_MPS_HIGH_WATERMARK_RATIO"] = "0.9"

from torch.xpu import device

# Load CSV data
df = pd.read_csv('data/tech_company_triplets_LTC.csv')

# Convert csv data into SBERT row format for triplet loss training
training_set = [
    InputExample(texts=["query: " + row['job_description'], "passage: " + row['resume_positive'],
                        "passage: " + row['resume_negative']])
    for _, row in df.iterrows()
]

def train_model(model):
    # model = SentenceTransformer('intfloat/e5-large-v2')

    # Create Dataloader
    training_dataloader = DataLoader(training_set, shuffle=True, batch_size=4)

    # Define Triplet Loss
    training_triplet = losses.TripletLoss(model=model)

    # Train the model
    model.fit(train_objectives=[(training_dataloader, training_triplet)], epochs=3, warmup_steps=10,
              output_path='../app/model/output_new_one')


try:
    print("Trying training on MPS...")
    torch.mps.empty_cache()
    gc.collect()
    # Load a model variant from ConsultantBERT (MoritzLaurer/consultant-bert)
    train_model(SentenceTransformer('intfloat/e5-large-v2'))
except RuntimeError as e:
    if "MPS backend out of memory" in str(e):
        print("MPS OOM occurred. Switching to CPU...")
        torch.mps.empty_cache()
        gc.collect()
        train_model(SentenceTransformer('intfloat/e5-large-v2',device='cpu'))
    else:
        raise e

print('Training completed!')


