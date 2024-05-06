# Censorship of Twitter - Unsupervised Topic Modeling

This project focuses on topic modeling for censored tweets. In recent years, there has been an increasing amount of censorship on social media platforms such as Twitter. This has led to a need for methods to identify and understand the topics of censored tweets. In our case, we aim to discover topics that are prohibited by some countries.

## Approach

The project uses natural language processing (NLP) techniques to perform topic modeling on censored tweets. This involves a careful pre-processing of the text of the tweets and the use of different topic modeling algorithms. The algorithms used are the following: Latent Dirichlet Allocation (LDA), Biterm Topic Model (BTM), Gibbs Sampling Dirichlet Mixture Model (GSDMM) and BERTopic that uses sentence transformers.

Once the topics have been identified, we analyze and interpret the results to gain insights into the content of the censored tweets.


## Report

The report can be found [here](https://github.com/CS-433/ml-project-2-censoredml/blob/master/report.pdf).


## Requirements
To run this project, you will need Python 3 and the following libraries:

* bertopic
* bitermplus
* contractions
* deep_translator
* dict_replacement
* gensim
* gsdmm
* hdbscan
* json
* langcodes
* matplotlib
* nltk
* numpy
* pandas
* pickle
* pycountry
* pyLDAvis
* re
* seaborn
* sentence_transformers
* sklearn
* swifter
* textblob
* tmplot
* umap
* wordcloud

You can download the necessary package using the following command:

```pip install -r requirements.txt```

 
## Code organization

In the data folder, you can find all the preprocessed data used in this project. 
* ```censored_tweets``` are the original data
* ```translated_string.csv``` correspond to the original data where the processing before translation and the translation have been applied
* ```out_clean.csv``` correspond to the data with all the preprocessing and the translation
* ```to_be_clustered.csv``` is the same as out_clean with the exception that each tweet is censored in only one country. Tweets that were censored in multiple countries have been duplicated. Each duplicate is censored in a single and different country.
* ```saved_models``` are the parameters for our best models with BERTopic
* ```labelling``` are the labels for the 125 French tweets that have been manually labelled

In the ```Algorithms``` folder, you can find notebooks corresponding to all the algorithms that have been tested

The processing part can be found in the ```helpers``` folders

Here is an overview of the codebase:

```
.
├── Algorithms
│   ├── BERT-France.ipynb
│   ├── BERT-Germany.ipynb
│   ├── BERT-India.ipynb
│   ├── BERT-Russian_Federation.ipynb
│   ├── BERT-Turkey.ipynb
│   ├── BTM.ipynb
│   ├── GSDMM.ipynb
│   ├── LDA.ipynb
│   ├── bert_helpers.py
│   └── lda_helpers.py
├── EDA.ipynb
├── README.md
├── data
│   ├── censored_tweets.zip
│   ├── labelling
│   │   ├── France_final.csv.gz
│   │   └── France_labeled.xlsx
│   ├── out_clean.csv.gz
│   ├── saved_models
│   │   └── save_models_for_France.pkl
│   ├── to_be_clustered.csv.gz
│   └── translated_string.csv.zip
├── helpers_notebooks
│   ├── Labelling.ipynb
│   ├── processing_after_translation.ipynb
│   └── processing_before_translation.ipynb
├── helpers_python
│   ├── dict_replacement.py
│   ├── helpers.py
│   └── pre_processing.py
├── report.pdf
└── requirements.txt
```

## Results

The results of the topic modeling can be used to gain insights into the content of censored tweets. For example, the identified topics can be used to understand what types of content are being censored, and the top words for each topic can provide further information on the specific details of the censored tweets.

Our BERTopic best parameters for each country can be found in the following folder: ```data/saved_models```

## Authors

- Eva Luvison eva.luvison@epfl.ch
- Mathieu Desponds mathieu.desponds@epfl.ch
- Robin Jaccard robin.jaccard@epfl.ch