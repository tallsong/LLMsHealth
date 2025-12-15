import pandas as pd
import bibtexparser # Used to read .bib files
import re
pd.set_option("display.max_columns", None)


ieee_df = pd.read_csv("dataset/IEEE.csv")
print(f"Columns: {ieee_df.columns}, \n\nLength: {len(ieee_df)}")


# Read the ACM .bib file
with open("dataset/acm.bib", encoding="utf-8") as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# Convert entries to a pandas DataFrame
acm_df = pd.DataFrame(bib_database.entries)
print(f"acm Columns: {acm_df.columns}, \n\nLength: {len(acm_df)}")
print(acm_df.count)

# springer_df = pd.read_csv("dataset/springer.csv")
# print(f"Columns: {springer_df.columns}, \n\nLength: {len(springer_df)}")



# pubmed_df = pd.read_csv("dataset/Pubmed.csv")
# pubmed_df["abstract"] = ""
# print(f"Columns: {pubmed_df.columns}, \n\nLength: {len(pubmed_df)}")


# # pubmed_abstracts = pd.read_csv("./medical_dialogue_summarization/pubmed_abstracts_medical_dialogue_summarization_v2.csv")

# # # Merge on PMID
# # pubmed_df = pubmed_df.merge(pubmed_abstracts.rename(columns={"Abstract Text": "abstract"}), 
# #                              on="PMID", how="left")






# with open("dataset/ScienceDirect_citations_1762954648570.bib", encoding="utf-8") as bibtex_file:
#     bib_database = bibtexparser.load(bibtex_file)
# elsevier_df_l = pd.DataFrame(bib_database.entries)

# with open("dataset/ScienceDirect_citations_1762954661482.bib", encoding="utf-8") as bibtex_file:
#     bib_database = bibtexparser.load(bibtex_file)
# elsevier_df_s = pd.DataFrame(bib_database.entries)

# elsevier_df = pd.concat([elsevier_df_l, elsevier_df_s])
# print(f"Columns: {elsevier_df.columns}, \n\nLength: {len(elsevier_df)}")


# # Assessing Duplicate Values with Title
# # Using title because the formats of DOI are all different :/
# # 1. Create a list of tuples: (dataframe_name, title_series)
# df_sources = [
#     ("ACM", acm_df["title"]),
#     ("Elsevier", elsevier_df["title"]),
#     ("IEEE", ieee_df["Document Title"]),
#     ("PubMed", pubmed_df["Title"]),
#     ("Springer", springer_df["Item Title"])
# ]

# # 2. Create a combined DataFrame with source information
# combined_data = []
# for source_name, title_series in df_sources:
#     # Create a temporary DataFrame with title and source
#     temp_df = pd.DataFrame({
#         'title': title_series.str.lower(),  # Normalize to lowercase
#         'source': source_name
#     })
#     combined_data.append(temp_df)

# # Combine all into one DataFrame
# all_titles_df = pd.concat(combined_data, ignore_index=True)

# # 3. Remove rows with missing titles
# all_titles_df = all_titles_df.dropna(subset=['title'])

# # 4. Find titles that appear more than once
# title_counts = all_titles_df['title'].value_counts()
# duplicate_titles = title_counts[title_counts > 1].index.tolist()

# # 5. Filter to show only duplicates and group by title
# if not duplicate_titles:
#     print("No duplicate titles found across the DataFrames.")
# else:
#     duplicates_df = all_titles_df[all_titles_df['title'].isin(duplicate_titles)]
    
#     print(f"Found {len(duplicate_titles)} duplicate titles across datasets")
#     print(f"Total duplicate entries: {len(duplicates_df)}")
#     print("=" * 80)
#     # Group by title and show which sources contain each duplicate
#     for title in sorted(duplicate_titles):
#         title_data = duplicates_df[duplicates_df['title'] == title]
#         sources = title_data['source'].tolist()
#         count = len(sources)
        
#         print(f"\nTitle: {title}")
#         print(f"   Total occurrences: {count}")
#         print(f"   Found in: {', '.join(sources)}")



# acm_df["library"] = "acm"
# acm_df = acm_df.rename(columns={
#     "ID": "id", "title": "title", "abstract": "abstract", "author": "authors",
#     "doi": "doi", "journal": "journal"
# })
# acm_df["date"] = acm_df["year"].astype(str) + "-" + acm_df["month"].astype(str)
# acm_df = acm_df[["id", "title", "abstract", "library", "authors", "doi", "journal", "date"]]

# # Elsevier
# elsevier_df["library"] = "elsevier"
# elsevier_df = elsevier_df.rename(columns={
#     "ID": "id", "title": "title", "abstract": "abstract", "author": "authors",
#     "doi": "doi", "journal": "journal", "year": "date"
# })
# elsevier_df["date"] = elsevier_df["date"].astype(str)
# elsevier_df = elsevier_df[["id", "title", "abstract", "library", "authors", "doi", "journal", "date"]]

# # IEEE
# ieee_df["library"] = "ieee"
# ieee_df = ieee_df.rename(columns={
#     "ISBNs": "id", "Document Title": "title", "Abstract": "abstract", "Authors": "authors",
#     "DOI": "doi", "Publication Title": "journal", "Online Date": "date"
# })
# ieee_df = ieee_df[["id", "title", "abstract", "library", "authors", "doi", "journal", "date"]]

# # PubMed
# pubmed_df["library"] = "pubmed"
# pubmed_df = pubmed_df.rename(columns={
#     "PMID": "id", "Title": "title", "abstract": "abstract", "Authors": "authors",
#     "DOI": "doi", "Journal/Book": "journal", "Create Date": "date"
# })
# pubmed_df = pubmed_df[["id", "title", "abstract", "library", "authors", "doi", "journal", "date"]]

# combined_df = pd.concat([acm_df, elsevier_df, ieee_df, pubmed_df], ignore_index=True)
# print(len(combined_df))


# print(combined_df.head())
# combined_df.to_csv("./cm.csv", index=False)
# print("Saved combined DataFrame to ./cm.csv")
