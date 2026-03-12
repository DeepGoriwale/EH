# Documents
documents = {
    1: "apple banana orange",
    2: "apple banana",
    3: "banana orange",
    4: "apple"
}

# Build inverted index
def build_index(docs):
    index = {}
    for doc_id, text in docs.items():
        for term in set(text.lower().split()):
            index.setdefault(term, set()).add(doc_id)
    return index

# Boolean operations
def boolean_and(terms, index):
    sets = [index.get(t, set()) for t in terms]
    return sorted(set.intersection(*sets)) if sets else []

def boolean_or(terms, index):
    sets = [index.get(t, set()) for t in terms]
    return sorted(set.union(*sets)) if sets else []

def boolean_not(term, index, total_docs):
    all_docs = set(range(1, total_docs + 1))
    return sorted(all_docs - index.get(term, set()))

# Build index
inverted_index = build_index(documents)

# Queries
print("Documents containing 'apple' AND 'banana':", boolean_and(["apple", "banana"], inverted_index))
print("Documents containing 'apple' OR 'orange':", boolean_or(["apple", "orange"], inverted_index))
print("Documents NOT containing 'orange':", boolean_not("orange", inverted_index, len(documents)))
print("Performed by 740_Pallavi & 743_Deepak")
