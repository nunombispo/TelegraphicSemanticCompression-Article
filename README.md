# Telegraphic Semantic Compression

A Python implementation of Telegraphic Semantic Compression (TSC), a text compression technique that removes predictable grammar while preserving semantic information. This approach reduces token counts for LLM processing while maintaining the core meaning of the text.

If this script was useful to you, consider donating to support the Developer Service Blog: https://buy.stripe.com/bIYdTrggi5lZamkdQW

## Overview

Telegraphic Semantic Compression works by:

- Removing predictable grammatical elements (determiners, prepositions, auxiliaries, pronouns, conjunctions, particles)
- Filtering out low-information words (like "just", "really", "basically", etc.)
- Preserving content words (nouns, verbs, adjectives, adverbs) that carry semantic meaning
- Using lemmatization to normalize words

## Features

- **Semantic Preservation**: Keeps the essential meaning and facts of the text
- **Token Reduction**: Significantly reduces token counts for LLM processing
- **NLP-Based**: Uses spaCy for accurate part-of-speech tagging
- **Token Counting**: Includes token estimation using tiktoken

## Installation

1. Clone this repository:

```bash
git clone https://github.com/nunombispo/TelegraphicSemanticCompression-Article
cd TelegraphicSemanticCompression-Article
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Download the spaCy English model:

```bash
python -m spacy download en_core_web_sm
```

## Usage

Run the main script to see examples:

```bash
python main.py
```

### Example Output

The script demonstrates compression on two example texts:

1. A short text about the Eiffel Tower
2. A longer text about the Amazon rainforest

For each example, it shows:

- Original text
- Compressed text
- Token counts (original vs compressed)
- Percentage reduction

## How It Works

The compression algorithm:

1. **Parses the text** using spaCy's NLP pipeline
2. **Identifies parts of speech** for each token
3. **Filters tokens** by:
   - Removing tokens with predictable grammatical roles (DET, ADP, AUX, PRON, CCONJ, SCONJ, PART)
   - Removing low-information words from a predefined list
   - Removing punctuation
4. **Lemmatizes** remaining words to their base forms
5. **Reconstructs** the text by joining lemmatized words

## Configuration

You can customize the compression by modifying:

- `REMOVE_POS`: Set of parts of speech to remove (default: determiners, prepositions, auxiliaries, pronouns, conjunctions, particles)
- `REMOVE_LIKE`: Set of low-information words to filter out (default: "like", "just", "really", "basically", "literally")

## Requirements

- Python 3.7+
- spaCy
- tiktoken
- en_core_web_sm (spaCy English model)
