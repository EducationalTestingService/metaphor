# Shared Task on Metaphor Detection


This repository contains the dataset used in the [shared task on metaphor detection](https://competitions.codalab.org/competitions/17805) in the [First Workshop on Figurative Language Processing](https://sites.google.com/site/figlangworkshop/), co-located with NAACL 2018. We provide a script to parse VUAMC.xml, the main dataset used in the competition, a set of features used to construct the baseline classification model for prediction of metaphor/non-metaphor classes at the word level, and instructions on how to replicate our published results. As additional information, we also provide software specifications used to generate our baseline feature types and values.

Main Dataset
---------
Our features are obtained by extraction, parsing and tagging of the [VU Amsterdam Metaphor Corpus](http://ota.ahds.ac.uk/headers/2541.xml) using this set of [software](https://github.com/EducationalTestingService/metaphor/tree/master/content-words#software). While replicating our results does not require repeating the above processes on the dataset, you will need to download a copy of the dataset to extract any additional features. There are altogether 117 texts covering four genres (academic, conversation, fiction, news).

Task Details
---------
You can either participate in the metaphor prediction task for verbs only, all part-of-speech only, or both.

Parsing VUAMC.XML for additional features
---------
To participate in the shared tasks, you can either use our baseline feature sets as a starting point, or generate your own feature sets by parsing the original VUAMC.xml.

To parse the VUAMC.xml, first download the [VUAMC.xml zip file](http://ota.ahds.ac.uk/text/2541.zip), then unzip it. You should get the file `2541/VUAMC.xml`. After that, run the following command (in Python 3.x):

```
python vua_xml_parser.py
```

This will generate `vuamc_corpus.csv` with 16203 lines in the following format:

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

The `txt_id` is the ID of each text provided in the VUAMC.xml, `sentence_id` is the ID of the sentence within a given text. Any token marked with `M_` denotes a metaphor, while the lack of which denotes a non-metaphor.


Data Interpretation
---------
In our baseline feature sets, each token has a <b>unique</b> identifier. For example, the token ID `a1e-fragment01_1_4_reveals` denotes `a1e-fragment01` text, sentence `1`, word offset `4`. To cross-reference this token ID in vuamc_corpus.csv, simply space tokenize the sentence_txt and count starting from the first word.

```
>>> "Latest corporate unbundler M_reveals laid-back M_approach : Roland Franklin , who is M_leading a 697m pound break-up bid for DRG , talks M_to Frank Kane".split()
['Latest', 'corporate', 'unbundler', 'M_reveals', 'laid-back', 'M_approach', ':', 'Roland', 'Franklin', ',', 'who', 'is', 'M_leading', 'a', '697m', 'pound', 'break-up', 'bid', 'for', 'DRG', ',', 'talks', 'M_to', 'Frank', 'Kane']
```


We provide a 1-1 mapping between our feature tokens and those that are extracted from the original XML file.


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


