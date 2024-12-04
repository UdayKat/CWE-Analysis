import re
from nltk.translate.bleu_score import sentence_bleu

# Tokenization function for C++ code
def tokenize_cpp_code(code):
    """
    Tokenizes C++ code into meaningful units.
    This includes keywords, identifiers, symbols, and numbers.
    """
    token_pattern = r'[A-Za-z_][A-Za-z_0-9]*|[0-9]+|[{}()\[\],.;<>!=&|+\-*%/]'
    return re.findall(token_pattern, code)

# Function to compute BLEU score between two C++ code strings
def compute_bleu_score(code1, code2):
    """
    Computes the BLEU score between two C++ code strings.
    """
    # Tokenize both strings
    tokens1 = tokenize_cpp_code(code1)
    tokens2 = tokenize_cpp_code(code2)

    # Compute BLEU score
    return sentence_bleu([tokens1], tokens2)

# Example C++ code strings
code1 ="mask_colorspace = fz_device_gray(ctx);"


code2 ="mask_colorspace = fz_keep_colorspace(ctx, fz_device_gray(ctx));"

# Compute BLEU score
bleu_score = compute_bleu_score(code1, code2)
print(f"BLEU score: {bleu_score}")
