import spacy
import tiktoken

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Parts of speech to remove (predictable grammar)
REMOVE_POS = {"DET", "ADP", "AUX", "PRON", "CCONJ", "SCONJ", "PART"}

# Optional low-information words to remove
REMOVE_LIKE = {"like", "just", "really", "basically", "literally"}

def tsc_compress(text: str) -> str:
    """Telegraphic Semantic Compression: remove predictable grammar, keep facts."""
    doc = nlp(text)
    chunks = []

    for sent in doc.sents:
        words = [
            token.lemma_
            for token in sent
            if (
                token.pos_ not in REMOVE_POS
                and token.text.lower() not in REMOVE_LIKE
                and not token.is_punct
            )
        ]
        if words:
            chunks.append(" ".join(words))

    return ". ".join(chunks) + "."

def count_tokens(text: str, model: str = "gpt-4") -> int:
    """Estimate the number of tokens using tiktoken."""
    enc = tiktoken.encoding_for_model(model)
    return len(enc.encode(text))


text = """
The Eiffel Tower, located in Paris, France, was built in 1889 for the Exposition Universelle.
"""

compressed = tsc_compress(text)

original_tokens = count_tokens(text)
compressed_tokens = count_tokens(compressed)
reduction = (original_tokens - compressed_tokens) / original_tokens * 100

print("Original Text:\n", text.strip())
print("\nCompressed Text:\n", compressed)
print(f"\nOriginal Tokens: {original_tokens}")
print(f"Compressed Tokens: {compressed_tokens}")
print(f"Token Reduction: {reduction:.1f}%")


text_long = """
The Amazon rainforest, often referred to as the lungs of the Earth, spans across nine countries in South America and is home to over 400 billion individual trees representing around 16,000 species. 
It plays a critical role in regulating the global climate by absorbing carbon dioxide and producing oxygen. 
In addition, the forest is home to countless animal species, many of which are endangered, and supports the livelihoods of millions of people who depend on it for food, shelter, and medicine. 
Deforestation, driven by logging, agriculture, and mining, poses a significant threat to this unique ecosystem.
"""
compressed_long = tsc_compress(text_long)

original_tokens_long = count_tokens(text_long)
compressed_tokens_long = count_tokens(compressed_long)
reduction_long = (original_tokens_long - compressed_tokens_long) / original_tokens_long * 100

print("Original Text:\n", text_long.strip())
print("\nCompressed Text:\n", compressed_long)
print(f"\nOriginal Tokens: {original_tokens_long}")
print(f"Compressed Tokens: {compressed_tokens_long}")
print(f"Token Reduction: {reduction_long:.1f}%")
