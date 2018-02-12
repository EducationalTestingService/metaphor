# Shared Task on Metaphor Detection


This repository contains the dataset used in the [shared task on metaphor detection](https://competitions.codalab.org/competitions/17805) in the [First Workshop on Figurative Language Processing](https://sites.google.com/site/figlangworkshop/), co-located with NAACL 2018.

Main Dataset
---------
For the shared task, we are using the [VU Amsterdam Metaphor Corpus](http://ota.ahds.ac.uk/headers/2541.xml) (VUA). There are altogether 117 texts covering four genres (academic, conversation, fiction, news).

Task Details
---------
You can either participate in the metaphor prediction tracks for verbs only, all content part-of-speech only, or both. For a given text in VUA, and for each sentence, the task is to predict metaphoricity for each word.

Issues
----------
Should you have any difficulties with the shared task, please file an [issue](https://github.com/EducationalTestingService/metaphor/issues), and we will get back to you promptly.

Instructions
---------

1. Create a working directory, say `naacl_flp`

```
$ mkdir naacl_flp
$ cd naacl_flp
```

2. Download the [VUAMC.xml zip file](http://ota.ahds.ac.uk/text/2541.zip) and unzip it in the working directory.
```
$ unzip 2541.zip
Archive:  2541.zip
  inflating: 2541/VUAMC.odd
  inflating: 2541/VUAMC.rnc
  inflating: 2541/VUAMC.rng
  inflating: 2541/VUAMC.xml
  inflating: 2541.xml
```

3. Download the [starter kit](https://github.com/EducationalTestingService/metaphor/releases/download/v1.0/naacl_flp_starter_kit.zip) and unzip it in the working directory. Then, run it (using Python 3.x). The parser script uses [lxml](http://lxml.de/installation.html). If you do not have it, simply do `pip install lxml` before running it.
<pre>
$ unzip naacl_flp_starter_kit.zip
Archive:  naacl_flp_starter_kit.zip
  inflating: setup.cfg
  inflating: vua_xml_parser.py

$ python vua_xml_parser.py

$ ls
# vuamc_corpus_train.csv is generated
2541 2541.xml 2541.zip naacl_flp_starter_kit.zip setup.cfg vua_xml_parser.py <b>vuamc_corpus_train.csv</b>
</pre>

4. `vuamc_corpus_train.csv` has 12123 lines in the following format. The `txt_id` is the ID of each text provided in the VUAMC.xml, `sentence_id` is the ID of the sentence within a given text. Any token marked with `M_` denotes a metaphor, while the lack of which denotes a non-metaphor.

```
"txt_id","sentence_id","sentence_txt"
"a1e-fragment01","1","Latest corporate unbundler M_reveals laid-back M_approach : Roland Franklin , who is M_leading a 697m pound break-up bid for DRG , talks M_to Frank Kane"
"a1e-fragment01","2","By FRANK KANE"
"a1e-fragment01","3","IT SEEMS that Roland Franklin , the latest unbundler to appear in the UK , has M_made a M_fatal error M_in the preparation of his £697m break-up bid for stationery and packaging group DRG ."
"a1e-fragment01","4","He has not properly investigated the M_target 's dining facilities ."
"a1e-fragment01","5","The 63-year-old M_head of Pembridge Investments , M_through which the bid is being M_mounted says , ‘ M_rule number one M_in M_this business is : the more luxurious the luncheon rooms at M_headquarters , the more inefficient the business ’ ."
"a1e-fragment01","6","If he had M_taken his own rule seriously , he would have found out that DRG has a very M_modest self-service canteen at its Bristol M_head office ."
"a1e-fragment01","7","There are other M_things he has , M_on his own M_admission , not fully investigated , like the value of the DRG properties , or which M_part of the DRG business he would M_keep M_after the break up ."
...
```

5. Download and unzip the [training gold labels](https://github.com/EducationalTestingService/metaphor/releases/download/v1.0/naacl_flp_gold_labels.zip) for verbs and all part-of-speech tokens:

```
$ unzip naacl_flp_gold_labels.zip
Archive:  naacl_flp_gold_labels.zip
  inflating: all_pos_tokens.csv
  inflating: verb_tokens.csv

$ wc -l all_pos_tokens.csv verb_tokens.csv
  72611 all_pos_tokens.csv
  17240 verb_tokens.csv
```

Each token list has a format similar to the following, a <b>unique</b> token identifier followed by a binary gold label (0 for non-metaphor, 1 for metaphor):

```
...
a1e-fragment01_1_4,1
a1e-fragment01_1_13,1
a1e-fragment01_11_5,1
a1e-fragment01_12_3,1
a1e-fragment01_12_21,0
a1e-fragment01_12_33,1
...
```

For example, the token identifier `a1e-fragment01_1_4` denotes text `a1e-fragment01`, sentence `1`, word offset `4`. This corresponds to the token `M_reveals` by tokenizing the sentence below using a white space. Note that the word offset starts at 1, and token count includes punctuation as well.

```
>>> "Latest corporate unbundler M_reveals laid-back M_approach : Roland Franklin , who is M_leading a 697m pound break-up bid for DRG , talks M_to Frank Kane".split()
['Latest', 'corporate', 'unbundler', 'M_reveals', 'laid-back', 'M_approach', ':', 'Roland', 'Franklin', ',', 'who', 'is', 'M_leading', 'a', '697m', 'pound', 'break-up', 'bid', 'for', 'DRG', ',', 'talks', 'M_to', 'Frank', 'Kane']
```

5. During evaluation, token lists (without gold labels) for the test sets will be made available. The task will be to generate predictions for the test verb and all part-of-speech tokens in the same format as `verb_tokens.csv` and `all_pos_tokens.csv`, and submit it to CodaLab for evaluation.

Evaluation Phase
---------
1. Download the [testing kit](https://github.com/EducationalTestingService/metaphor/releases/download/v1.0/naacl_flp_testing_kit.zip) into the working directory and execute it like you would with the starter kit.

<pre>
$ unzip naacl_flp_testing_kit.zip
Archive:  naacl_flp_testing_kit.zip
  inflating: setup.cfg
  inflating: vua_xml_parser_test.py

$ python vua_xml_parser_test.py

$ ls vuamc*csv
# vuamc_corpus_test.csv is generated
vuamc_corpus_train.csv <b>vuamc_corpus_test.csv</b>
</pre>

Baseline (OPTIONAL)
---------
For the shared task, you are welcome to use any machine/deep learning toolkit to generate predictions for each target token. We have used the logistic classifier in [SKLL v1.5](https://github.com/EducationalTestingService/skll) to perform classification for the training and testing sets with published results, using a set of features outlined below.

```
feature (SKLL feature name), published venue
====================
1. unigram (U), Meta4NLP 2014
2. part-of-speech tags (P), Meta4NLP 2014
3. topical LDA (T), Meta4NLP 2014
4. concreteness (C-BiasUp, C-BiasDown, CCDB-BiasUpDown), Meta4NLP 2015 (CUpDown as C-BiasUp + C-BiasDown)
5. unigram lemmas (UL), ACL 2016
6. wordnet (WordNet), ACL 2016
7. verbnet (VN-Raw), ACL 2016
8. corpus (Corpus), ACL 2016
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

1. To start, download the [baseline features and SKLL configuration file](https://github.com/EducationalTestingService/metaphor/releases/download/v1.0/naacl_flp_skll_datasets.zip), then unzip it into the working directory.  <b>NOTE</b>: The extracted contents `toy_set`, `verbs`, `all_pos` and `toy_set.cfg` should be directly under the working directory.

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

Reference Papers
---------
[Semantic Classifications for Detection of Verb Metaphors](http://aclweb.org/anthology/P/P16/P16-2017.pdf)
([erratum](paper/metaphor_acl_2016_erratum.pdf))
Beata Beigman Klebanov, Ben Leong, E. Dario Gutierrez, Ekaterina Shutova and Michael Flor, in Proceedings of the 54th Meeting of the Association for Computational Linguistics (ACL), 2016

[Supervised Word-Level Metaphor Detection: Experiments with Concreteness and Reweighting of Examples](https://aclweb.org/anthology/W/W15/W15-1402.pdf)
Beata Beigman Klebanov, Ben Leong, Michael Flor,
in Proceedings of the Third Workshop on Metaphor in NLP (Meta4NLP), Denver, CO, 2015

[Different Texts, Same Metaphors: Unigrams and Beyond](http://anthology.aclweb.org/W/W14/W14-2302.pdf)
Beata Beigman Klebanov, Ben Leong, Michael Heilman and Michael Flor,
in Proceedings of the Second Workshop on Metaphor in NLP (Meta4NLP), Baltimore, MD, 2014


