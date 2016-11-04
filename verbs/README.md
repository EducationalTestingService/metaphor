# Automatic Metaphor Classification for Verbs

This repository contains the software specifications, experimental feature types and values, as well as predictions of metaphor/non-metaphor classes at the word level as discussed in the reference paper. We also provide two other related papers that lay the foundation for our current research in the reference paper.

Main Dataset
---------
Our features are obtained by extraction, parsing and tagging of the [VU Amsterdam Metaphor Corpus](http://ota.ahds.ac.uk/headers/2541.xml). While replicating our results does not require repeating the above processes on the dataset, you will need to download a copy of the dataset to extract any additional features. There are altogether 117 texts covering four genres (academic, conversation, fiction, news) and organized into different folds for cross-validation. More information can be found under `Data Interpretation` below.

Software
---------
* [Stanford Thrift](https://github.com/EducationalTestingService/stanford-thrift/releases), 0.5-operational (Python 2.7) for creating parsing/tagging servers
* Tagger and Parser in [Stanford CoreNLP](http://stanfordnlp.github.io/CoreNLP/) 3.6.0
 * Tagger Model : english-bidirectional-distsim.tagger
 * Parser Model : edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz
 * Parser output representation : Universal dependencies, enhanced
* [Gensim](https://radimrehurek.com/gensim) 0.10.3 for topic modeling features
* [NLTK](http://www.nltk.org/) 3.0.3 for parsing VUA (Python 2.7); 3.2 for features generation (Python 3.4) through lemmatization and stopwords filtering
* [SciKit-Learn Laboratory](https://github.com/EducationalTestingService/skll) 1.1.1 for machine learning experiments


Text Preprocessing
---------
For stopword removal, we padded the `NLTK English` stopwords list with the following additional stopwords:
```python
AUXWORDS = ['am','be', 'is', 'was', 'been', 'being', 'were', 'are', 'have', 'has', 'had', 'having', 'do', 'did', 'does', 'done', 'doing', 'didnt','doesnt','dont','havent', 'hasnt','couldnt','wont','shouldnt', 'wouldnt','cant','cannot','hadnt','shant','arent','isnt','mightnt','mustnt','werent','wasnt', 'neednt','oughtnt','couldve','mightve', 'mustve','shouldve','would','wouldve']
```

Data Interpretation
---------
* Each instance in our data is indexed in a way that makes it easy to locate it in the original VUA distribution, as follows.
* Each text from VUA is processed in a manner consistent with the original annotation intentions. That means, a sentence is enclosed within a pair of `<s>..</s>` tags, and a word is enclosed within a pair of `<w>..</w>` tags, and extracted as such. There are cases where multiple tokens are enclosed as a word e.g. `<w lemma="that is to say" type="AV0">That is to say</w>`. In this case, we used tokens to denote the ordering of words in a multiword expression.
 * The `id` of an instance can be decomposed using the underscore as delimiter, and decoded as follows. For example, in `a3m-fragment02_85_41_28_1_head`:
  - `a3m-fragment02` is the text segment id
  - `85` is the original sentence number provided by VUA (continuous counting across texts)
  - `41` is the sentence offset we computed, starting with 1 for each new text, using <s>...</s> markups in the corpus.
  - `28` is the word offset we computed, starting with 1 for each new sentence, using <w>...</w> marksup in the corpus.
  - `1` is the sub-word offset, inside a single <w>...</w>. It always starts with 1 for unigram, and increases for multiword expressions
  - `head` is the actual verb
* `inputs/traintest_verbs` contains the training and testing feature files and values by genre
* `inputs/traintest_verbs_all/all_genres/train` contains the training feature files and values for all genres. Note that testing is still done on the `inputs/traintest_verbs` by genre
* `outputs/metaphor_labels_predictions.csv` contains the instance_id, true metaphor label (`y`), as well as predictions made by several systems: baseline (`soa`), lemma unigram + WordNet (`ul_wn`), lemma unigram + WordNet + Concreteness Difference (`ul_wn_dc`), lemma unigram + Corpus (`ul_corpus`) and lemma unigram + Corpus + Concreteness Difference (`ul_corpus_dc`)



Reference Paper
---------
[Semantic Classifications for Detection of Verb Metaphors](http://aclweb.org/anthology/P/P16/P16-2017.pdf)
([erratum](paper/metaphor_acl_2016_erratum.pdf))
Beata Beigman Klebanov, Ben Leong, E. Dario Gutierrez, Ekaterina Shutova and Michael Flor, in Proceedings of the 54th Meeting of the Association for Computational Linguistics (ACL), 2016

Related Papers
---------
[Supervised Word-Level Metaphor Detection: Experiments with Concreteness and Reweighting of Examples](https://aclweb.org/anthology/W/W15/W15-1402.pdf)
Beata Beigman Klebanov, Ben Leong, Michael Flor,
in Proceedings of the Third Workshop on Metaphor in NLP (NAACL-Meta4NLP), Denver, CO, 2015

Please note that the data used in the above paper has been released [here] (https://github.com/EducationalTestingService/metaphor/tree/master/content-words).


[Different Texts, Same Metaphors: Unigrams and Beyond](http://anthology.aclweb.org/W/W14/W14-2302.pdf)
Beata Beigman Klebanov, Ben Leong, Michael Heilman and Michael Flor,
in NLP (ACL-Meta4NLP), Baltimore, MD, 2014


