'''
The current plan to building this algorithm

Based on architecture proposed in https://arxiv.org/pdf/2104.01778.pdf
'''

# Step 1 - Convert audio (preferably the whole song) into vector representations
# Convert to audio spectogram (log-mel spectogram?)
# Could also use a CNN as a feature encoder and feed directly through (might be more general and better?)
# Split into patches (test with and without overlap)
# Add positional embedding
# Don't add classification token, find how to get an output for similarity not classification

# Step 2 - Feed song embeddings through transformer
# Try to use a viT model architecture (maybe pretrained on ImageNet?)
# Could also try architecture proposed in https://arxiv.org/pdf/2105.00335.pdf (Using average pooling layers)
# Find a way to combine all outputs for each patch into one embedding to store in a vector database

# Step 3 - Store "similarity score" into vector database
# Open-source or commercial?
# To get a song recommendation based on a song, get songs closest to the given song's vector


# Start on very small dataset of songs and test and make sure similarity scores are consistent
# Scale up and optimize algorithm