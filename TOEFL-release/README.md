# TOEFL dataset release

This repository contains 180 essays in the training partition of the dataset described in the paper [A Corpus of Non-Native Written English Annotated for Metaphor](http://www.aclweb.org/anthology/N18-2014), as well as feature sets used to generate predictions of metaphoricity for each verb/content-word in the essay.

Essays
---------
The essays are part of a larger dataset released in the [ETS Corpus of Non-Native Written English](https://catalog.ldc.upenn.edu/LDC2014T06). Moreover, each essay used in our experiment has been processed further to include only tokens containing `[A-Z0-9_-]` characters, and annotated metaphors are marked with a `M_` prefix, as exemplified in the text snippet below:

`There are other M_things he has , M_on his own M_admission , not fully investigated , like the value of the DRG properties , or which M_part of the DRG business he would M_keep M_after the break up .`

Please send us any essay in the corpus to provide proof that you have access rights to the LDC datasets, and we will provide you with the annotated 180 training essays.

Feature sets
---------

```
feature (SKLL feature name), published venue
====================
1. unigram (U), Meta4NLP 2014
2. part-of-speech tags (P), Meta4NLP 2014
3. topical LDA (T), Meta4NLP 2014
4. concreteness (C-BiasUp, C-BiasDown, CCDB-BiasUpDown), Meta4NLP 2015 (CUpDown as C-BiasUp + C-BiasDown)
5. unigram lemmas (UL), ACL 2016
6. wordnet (WordNet), ACL 2016
```

A combination of these features will be used to build a logistic classification model whose predictions will be used as the baseline during the evaluation phase. <b>NOTE</b>: You can download and use any of these features for building your model for the shared task, along with other interesting features you may conceive. The format of each SKLL feature file is:

```
{"y": LABEL, "x": {FEATURE_NAME : FEATURE_VALUE}, "id": TOKENID}
```

Note that when combining several feature sets, the `FEATURE_NAME` has to be unique across all feature files.

SKLL (OPTIONAL)
---------

To illustrate how SKLL can be used, we provided a toy example here.

SKLL can be installed via Conda. You can find installation instructions at the [anaconda](https://docs.anaconda.com/anaconda/install/) page.

1. To start, download the [baseline features and SKLL configuration file](https://github.com/EducationalTestingService/metaphor/releases/download/v1.0/naacl_flp_skll_train_datasets.zip), then unzip it into the working directory.  <b>NOTE</b>: The extracted contents `toy_set`, `verbs`, `all_pos` and `toy_set.cfg` should be directly under the working directory.

2. Next, run
```
# create a conda environment just for this shared task
$ conda create -n naacl_flp

# activate the conda environment
$ source activate naacl_flp
```

3. Install SKLL v1.5
```
(naacl_flp)$ conda install -c defaults -c conda-forge -c desilinguist python=3.6 skll
```

4. Navigate to the working directory, then type:
```
(naacl_flp)$ mkdir log results predictions models
(naacl_flp)$ export SKLL_MAX_CONCURRENT_PROCESSES=1
(naacl_flp)$ run_experiment toy_set.cfg
```

Once the experiment is completed, you should be able to look into `results` directory and get the following confusion matrix in the *results file. Note that the numbers reported here are based on a very small subset of data and for illustration purposes only. We will release our baseline results once the testing phase begins.

```
+---+------+-----+-----------+--------+-----------+
|   |    0 |   1 | Precision | Recall | F-measure |
+---+------+-----+-----------+--------+-----------+
| 0 | [74] |   9 |     0.851 |  0.892 |     0.871 |
+---+------+-----+-----------+--------+-----------+
| 1 |   13 | [4] |     0.308 |  0.235 |     0.267 |
+---+------+-----+-----------+--------+-----------+

```

If you need to cite, please use the following reference:
---------
[A Corpus of Non-Native Written English Annotated for Metaphor](http://www.aclweb.org/anthology/N18-2014.pdf)
Beata Beigman Klebanov, Chee Wee Leong, and Michael Flor, in Proceedings of the Proceedings of 16th Annual Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL), New Orleans, Louisiana, 2018


Reference Papers
---------
[Semantic Classifications for Detection of Verb Metaphors](http://aclweb.org/anthology/P/P16/P16-2017.pdf)
([erratum](https://github.com/EducationalTestingService/metaphor/blob/master/verbs/paper/metaphor_acl_2016_erratum.pdf))
Beata Beigman Klebanov, Ben Leong, E. Dario Gutierrez, Ekaterina Shutova and Michael Flor, in Proceedings of the 54th Meeting of the Association for Computational Linguistics (ACL), 2016

[Supervised Word-Level Metaphor Detection: Experiments with Concreteness and Reweighting of Examples](https://aclweb.org/anthology/W/W15/W15-1402.pdf)
Beata Beigman Klebanov, Ben Leong, Michael Flor,
in Proceedings of the Third Workshop on Metaphor in NLP (Meta4NLP), Denver, CO, 2015

[Different Texts, Same Metaphors: Unigrams and Beyond](http://anthology.aclweb.org/W/W14/W14-2302.pdf)
Beata Beigman Klebanov, Ben Leong, Michael Heilman and Michael Flor,
in Proceedings of the Second Workshop on Metaphor in NLP (Meta4NLP), Baltimore, MD, 2014
