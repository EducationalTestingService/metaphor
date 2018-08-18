# TOEFL dataset release


This repository contains 180 essays in the training partition of the dataset described in the paper [A Corpus of Non-Native Written English Annotated for Metaphor](http://www.aclweb.org/anthology/N18-2014), as well as feature sets used to generate predictions of metaphoricity.

Main Dataset
---------
For the shared task, we are using the [VU Amsterdam Metaphor Corpus](http://ota.ahds.ac.uk/headers/2541.xml) (VUA). There are altogether 117 texts covering four genres (academic, conver


3. (Optional) If you would like to use our test partition baseline features, you may do so by downloading the [SKLL test baseline features](https://github.com/EducationalTestingService/metaphor/releases/download/v1.0/naacl_flp_skll_test_datasets.zip) and use them by setting `task` type to [predict](http://skll.readthedocs.io/en/latest/run_experiment.html#predict) when running experiments. Below is an example of the parameters you should change, marked by `<---` comments:

```
[General]
experiment_name = news-UL-WordNet-AutoWeighting <--- this should be changed for each new experiment
task = evaluate # <--- change this to predict for making predictions

[Input]
train_directory = news/train # <--- SKLL training features for a specific genre
test_directory = news/test # <--- SKLL test features for a specific genre. Note that test features do not have y labels populated when used in the prediction mode
featuresets = [["UL","WordNet"]] <--- feature set you want to use for training and making prediction
featureset_names = ["expt"]
learners = ["LogisticRegression"] <--- you can try other learners available
suffix = .jsonlines
fixed_parameters = [{'class_weight':'balanced'}]

[Tuning]
grid_search = true
objective = f1_score_least_frequent

[Output]
probability = false
log = log
models = models
predictions = predictions
```
Assuming that the above configration is named 'example.cfg' and that you already have trained models previously stored in the `models` directory, you can choose to reuse those models by running `run_experiment -k example.cfg`. After running the experiments, you will find binary predictions generated for each token under the `predictions` output directory. You can format these predictions into the format required for CodaLab submission. More details on how to run SKLL can be found in the [Baseline optional section](https://github.com/EducationalTestingService/metaphor/tree/master/NAACL-FLP-shared-task#baseline-optional) below.

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
