import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel, pipeline
import re



def enhanced_response_filtering(response_text, threshold=0.5):

    # Load a more robust classifier
    zero_shot_classifier = pipeline(
        "zero-shot-classification", 
        model="facebook/bart-large-mnli",
        device_map="auto"
    )

    # Expanded and more specific categories
    candidate_labels = [
        "instructions for illegal activities",
        "promoting violence or physical harm",
        "generating malicious code or malware",
        "fraudulent schemes or scams",
        "instructions for vaolating rules",

    ]
    
    # Additional pattern-based checks for common jailbreak indicators
    jailbreak_patterns = [
        #r"ignore (previous|your) instructions",
        r"pretend (to be|you are)",
        r"roleplay as",
        r"hypothetically speaking",
        r"for educational purposes only",
        r"this is just fiction",
        r"developer mode",
        r"jailbreak",
        #r"DAN mode"
    ]
    
    # Check for obvious jailbreak attempts
    text_lower = response_text.lower()
    for pattern in jailbreak_patterns:
        if re.search(pattern, text_lower):
            return "I cannot provide that type of content."
    
    # Zero-shot classification
    result = zero_shot_classifier(response_text, candidate_labels)
    
    # Check results with dynamic threshold adjustment
    for label, score in zip(result["labels"], result["scores"]):
        # Lower threshold for high-risk categories
        adjusted_threshold = threshold
        if any(keyword in label.lower() for keyword in ["illegal", "harm", "malware", "fraud", "violation"]):
            adjusted_threshold = 0.5
            
        if score > adjusted_threshold:
            return f"I cannot provide content that may involve {label.replace('_', ' ')}."
    
    return response_text