# Shared Task on Metaphor Detection


This repository contains the dataset used in the [shared task on metaphor detection](https://competitions.codalab.org/competitions/17805) in the [First Workshop on Figurative Language Processing](https://sites.google.com/site/figlangworkshop/), co-located with NAACL 2018. We provide a script to parse VUAMC.xml, the main dataset used in the competition, a set of features used to construct the baseline classification model for predictions of metaphor/non-metaphor classes at the word level, and instructions on how to replicate our published results. As additional information, we also provide software specifications, experimental feature types and values.

Main Dataset
---------
Our features are obtained by extraction, parsing and tagging of the [VU Amsterdam Metaphor Corpus](http://ota.ahds.ac.uk/headers/2541.xml). While replicating our results does not require repeating the above processes on the dataset, you will need to download a copy of the dataset to extract any additional features. There are altogether 117 texts covering four genres (academic, conversation, fiction, news) and organized into different folds for cross-validation. More information can be found under `Data Interpretation` below.

NOTE: Please download the datasets from the [release](https://github.com/EducationalTestingService/metaphor/releases/tag/v1.0) page.

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
  - `head` is the actual token (a verb in this case)
* `inputs/traintest` contains the training and testing feature files and values by genre
* `inputs/traintest_all/all_genres/train` contains the training feature files and values for all genres. Note that testing is still done on the `inputs/traintest` by genre
* `inputs/xvals/*/train` contains the training AND testing feature files and values, grouped by genres.
* `outputs/metaphor_labels_predictions_traintest.csv` contains the instance_id, true metaphor label (`y`), as well as predictions made by different weighting regimes i.e. AutoWeighting (`uptc_auto`) and OptimizedWeighting (`uptc_optimized`) of the feature set: unigram + pos + topic + concreteness binning bias-up/down + concreteness difference binning bias-up/down. Similarly, `outputs/metaphor_labels_predictions_traintest_all.csv` is generated for the scenario where training is done using data from all genres, but testing is performed on individual genres. For `outputs/metaphor_labels_predictions_xvals.csv`, the predicted label for each instance is a result of cross-validation within each genre by training on (n-1)th folds and testing on the nth fold.



Reference Paper
---------
[Supervised Word-Level Metaphor Detection: Experiments with Concreteness and Reweighting of Examples](https://aclweb.org/anthology/W/W15/W15-1402.pdf)
Beata Beigman Klebanov, Ben Leong, Michael Flor,
in Proceedings of the Third Workshop on Metaphor in NLP (Meta4NLP), Denver, CO, 2015

Please have a look at the [Release Note with Up-To-Date Benchmarks](paper/meta_2015_release_note.pdf).


Related Papers
---------
[Different Texts, Same Metaphors: Unigrams and Beyond](http://anthology.aclweb.org/W/W14/W14-2302.pdf)
Beata Beigman Klebanov, Ben Leong, Michael Heilman and Michael Flor,
in Proceedings of the Second Workshop on Metaphor in NLP (Meta4NLP), Baltimore, MD, 2014


