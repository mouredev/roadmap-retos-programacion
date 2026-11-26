"""
SETS
"""

data = ["Claude", "GPT-4", "Gemini"]
print(f"Initial list: {data}")

# Add element at the end
data.append("Llama")
print(f"Append at end: {data}")

# Add element at the beginning
data.insert(0, "Mistral")
print(f"Insert at start: {data}")

# Add multiple elements at the end
data.extend(["Grok", "Copilot"])
print(f"Extend at end: {data}")

# Add multiple elements at a specific position
data[2:2] = ["Perplexity", "DeepSeek"]
print(f"Insert block at index 2: {data}")

# Remove element at a specific position
del data[3]
print(f"Delete at index 3: {data}")

# Update element at a specific position
data[1] = "GPT-4o"
print(f"Update at index 1: {data}")

# Check if an element exists
print(f"'Claude' in list: {'Claude' in data}")
print(f"'Gemini' in list: {'Gemini' in data}")

# Clear the list
data.clear()
print(f"After clear: {data}")


"""
    EXTRA EXERCISE
"""

anthropic = {"Claude 3 Opus", "Claude 3.5 Sonnet", "Claude 3 Haiku"}
openai = {"GPT-4o", "GPT-4 Turbo", "Claude 3.5 Sonnet", "o1"}
google = {"Gemini Ultra", "Gemini Pro", "Claude 3 Haiku"}

print(f"\nAnthropic models : {anthropic}")
print(f"OpenAI models    : {openai}")
print(f"Google models    : {google}")

# Union — all elements from both sets, without duplicates
print(f"\nUnion (all models)                        : {anthropic.union(openai, google)}")
print(f"Union (all models)                        : {anthropic | openai | google}")

# Intersection — only elements present in both sets
print(f"\nIntersection (Anthropic ∩ OpenAI)         : {anthropic.intersection(openai)}")
print(f"Intersection (Anthropic ∩ OpenAI)         : {anthropic & openai}")

# Difference — elements in the first set but not in the second
print(f"\nDifference (Anthropic - Google)           : {anthropic.difference(google)}")
print(f"Difference (Anthropic - Google)           : {anthropic - google}")

# Symmetric difference — elements in either set, but not in both
print(f"\nSymmetric difference (Anthropic △ OpenAI) : {anthropic.symmetric_difference(openai)}")
print(f"Symmetric difference (Anthropic △ OpenAI) : {anthropic ^ openai}")
