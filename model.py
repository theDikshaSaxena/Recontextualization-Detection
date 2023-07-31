# import spacy
# from fuzzywuzzy import fuzz
# from docx import Document

# # Load spaCy's pre-trained English model
# nlp = spacy.load("en_core_web_sm")

# def extract_entities(text):
#     doc = nlp(text)
#     return [(ent.text, ent.label_) for ent in doc.ents]

# def entity_matching(article_entities, post_entities):
#     matched_entities = []
#     for article_ent in article_entities:
#         for post_ent in post_entities:
#             if fuzz.ratio(article_ent[0].lower(), post_ent[0].lower()) >= 80:
#                 matched_entities.append((article_ent, post_ent))
#     return matched_entities

# def compare_facts(article_entity, post_entity):
#     # Implement fact comparison logic here, such as semantic similarity or keyword extraction.
#     # You can use deep learning models or other NLP techniques based on your requirements.
#     # For simplicity, let's assume the facts are considered the same if the entity label and text match.
#     return article_entity[1] == post_entity[1] and article_entity[0] == post_entity[0]

# def consistency_check(article_text, post_text):
#     article_entities = extract_entities(article_text)
#     post_entities = extract_entities(post_text)

#     matched_entities = entity_matching(article_entities, post_entities)

#     if not matched_entities:
#         return False  # No common entities found, not consistent

#     for article_entity, post_entity in matched_entities:
#         if not compare_facts(article_entity, post_entity):
#             return False  # Facts don't match, not consistent

#     return True  # All facts matched, consistent

# def read_word_file(filename):
#     doc = Document(filename)
#     full_text = ""
#     for para in doc.paragraphs:
#         full_text += para.text + "\n"
#     return full_text

# def print_ner_map(text):
#     doc = nlp(text)
#     for ent in doc.ents:
#         print(f"Entity: {ent.text}, Label: {ent.label_}")

# article_file = "/Users/dikshasaxena/Documents/2nd sem/Research-NLP- work/FinalModel/article_text.docx"
# post_file = "/Users/dikshasaxena/Documents/2nd sem/Research-NLP- work/FinalModel/post_file.docx"
# post_file1 = "/Users/dikshasaxena/Documents/2nd sem/Research-NLP- work/FinalModel/post_file1.docx"

# article_text = read_word_file(article_file)
# post_text = read_word_file(post_file)
# post_text1 = read_word_file(post_file1)

# result = consistency_check(article_text, post_text)
# print("Consistency Check Result (Post):", result)

# result1 = consistency_check(article_text, post_text1)
# print("Consistency Check Result (Post1):", result1)

# print("\nNER Map for Article:")
# print_ner_map(article_text)

# print("\nNER Map for Post:")
# print_ner_map(post_text)

# print("\nNER Map for Post1:")
# print_ner_map(post_text1)

