import pandas as pd
from sentence_transformers import InputExample, models, SentenceTransformer, losses
from torch.utils.data import DataLoader

#Load CSV data
df = pd.read_csv('data/tech_company_triplets_mini.csv')

# Convert csv data into SBERT row format for triplet loss training
training_set = [
    InputExample(texts=["query: " + row['job_description'], "passage: " + row['resume_positive'], "passage: " + row['resume_negative']])
    for _, row in df.iterrows()
]

# Load a model variant from ConsultantBERT (MoritzLaurer/consultant-bert)
model = SentenceTransformer('intfloat/e5-large-v2')

# Create Dataloader
training_dataloader = DataLoader(training_set, shuffle=True, batch_size=8)

# Define Triplet Loss
training_triplet = losses.TripletLoss(model=model)

# Train the model
model.fit(train_objectives=[(training_dataloader, training_triplet)], epochs=3, warmup_steps=10, output_path='../app/model/output_new_one')

print('Training completed!')


