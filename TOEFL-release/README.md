# TOEFL dataset release

This repository contains 180 essays in the training partition of the dataset described in the paper [A Corpus of Non-Native Written English Annotated for Metaphor](http://www.aclweb.org/anthology/N18-2014), as well as feature sets used to generate predictions of metaphoricity for each verb/content-word in the essay.

Essays
---------
The essays are part of a larger dataset released in the [ETS Corpus of Non-Native Written English](https://catalog.ldc.upenn.edu/LDC2014T06). Moreover, each essay used in our experiment has been processed further to include only tokens containing `[A-Z0-9_-]` characters, and annotated metaphors are marked with a `M_` prefix, as exemplified in the text snippet below:

TODO: `There are other M_things he has , M_on his own M_admission , not fully investigated , like the value of the DRG properties , or which M_part of the DRG business he would M_keep M_after the break up .`

Please send us any essay in the corpus to provide proof that you have access rights to the LDC database, and we will provide you with the annotated 180 training essays via email.

Feature sets
---------
Our feature sets reported in the paper are combinations of constituent features conceived in earlier publications:

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

Specifically, these are the combinations described in our paper:

```
<b>all-15</b>: U, P, T, CUpDown, CCDB-BiasUpDown
<b>all-16</b>: UL, WordNet, CCDB-BiasUpDown
<b>v-16</b>: UL, WordNet, CCDB-BiasUpDown
```

Each combination is used to build a logistic classification model whose predictions are used to generate metaphoricity. The format of each feature file is:

```
{"y": LABEL, "x": {FEATURE_NAME : FEATURE_VALUE}, "id": TOKENID}
```

Note that when combining several feature sets, the `FEATURE_NAME` has to be unique across all feature files.

SKLL (OPTIONAL)
---------
This [section](https://github.com/EducationalTestingService/metaphor/blob/master/NAACL-FLP-shared-task/README.md#skll-optional) illustrates an example on using `SKLL` to execute experiments using the feature files we provided here.


For citation, please use the following reference:
---------
[A Corpus of Non-Native Written English Annotated for Metaphor](http://www.aclweb.org/anthology/N18-2014.pdf)
Beata Beigman Klebanov, Chee Wee Leong, and Michael Flor, in Proceedings of the Proceedings of 16th Annual Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL), New Orleans, Louisiana, 2018


Other Reference Papers
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
