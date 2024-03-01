# Custom Byte Pair Encoding (BPE) Implementation

This repository contains a custom implementation of Byte Pair Encoding (BPE), a data compression technique used in natural language processing (NLP) and other fields. BPE is commonly used for subword tokenization, which breaks down words into smaller units based on their frequency in a corpus.
By : Nitin Kapoor

## Overview

Byte Pair Encoding (BPE) is a simple yet powerful algorithm for subword tokenization. It iteratively merges the most frequent pair of characters (or bytes) in a given corpus until a desired vocabulary size is reached. This allows the model to learn subword units that capture meaningful morphological and syntactic information, especially in morphologically rich languages.

## Implementation Details

The custom BPE implementation provided in this repository follows these main steps:

1. **Initialization**: Start with a vocabulary containing all unique characters (or bytes) in the corpus.
2. **Tokenization**: Apply the learned merges to tokenize input text into subword units.

## Usage

To use the custom BPE implementation, follow these steps:

1. Clone the repository:
   ```bash
   git clone git@github.com:nitkap01/byte_pair_tokenizer.git
