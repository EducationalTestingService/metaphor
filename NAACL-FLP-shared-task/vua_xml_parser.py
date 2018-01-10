"""
NAACL 2018 Figurative Workshop Shared Task on Metaphor Detection
Script to parse VUA XML corpus to get text fragment, sentence id, sentence text tuples.

:author: Ben Leong (cleong@ets.org)

"""

import os
from os.path import join
import csv
import configparser
import re
import lxml.etree as ET


def read_config(configFilename):
  parser = configparser.ConfigParser()
  parser.read(configFilename)

  xml_file = parser['params']['xml_file']
  functions = set(parser['params']['functions'].split(','))
  types = set(parser['params']['types'].split(','))
  subtypes = set(parser['params']['subtypes'].split(','))
  function_override = bool(
      parser['params']['function_override'].lower() == 'true')

  return xml_file, functions, types, subtypes, function_override


def is_metaphor(seg, functions, types, subtypes, function_override):
  if seg is not None:
    if seg.get('function') in functions:
      if not function_override:
        return 1
      elif function_override and (seg.get('type') in types
                                  or seg.get('subtype') in subtypes):
        return 1
      else:
        return 0
    else:
      return 0
  else:
    return 0


def handle_anomaly(txt_id, sentence_id):
  if txt_id == 'as6-fragment01' and sentence_id == '26':
    return 'M_to'
  if txt_id == 'as6-fragment01' and sentence_id == '89':
    return 'M_sector'
  if txt_id == 'kb7-fragment48' and sentence_id == '13368':
    return 'like'


def extract_xml_tag_text(
    txt_id,
    sentence_id,
    namespace,
    t,
    functions,
    types,
    subtypes,
        function_override):

  final_token = None

  segs = t.findall('./' + namespace + 'seg')
  if len(segs) > 0:
    for seg in segs:
      if seg.text is None:
        return handle_anomaly(txt_id, sentence_id)

      flag = is_metaphor(seg, functions, types, subtypes, function_override)
      temp_token = seg.text.strip()
      temp_token = re.sub('[\[\]]', '', temp_token)  # replace non-word

      if flag == 1:
        temp_token = 'M_' + temp_token
        temp_token = re.sub(' +', ' M_', temp_token)

      prefix = t.text
      if prefix:
        temp_token = prefix.strip() + ' ' + temp_token

      suffix = seg.tail
      if suffix:
        temp_token = temp_token + ' ' + suffix.strip()

      temp_token = re.sub(' +', ' ', temp_token)
      if final_token:
        final_token += temp_token.strip()
      else:
        final_token = temp_token.strip()

  else:
    try:
      final_token = t.text.strip()
      # replace non-word
      final_token = re.sub('[\[\]]', '', final_token)
      final_token = re.sub(' +', ' ', final_token)

    except:
      pass

  if final_token and re.search(
          '-',
          final_token) and re.search(
          'M_',
          final_token):
    final_token = re.sub(' ', '', final_token)
    final_token = re.sub('M_', '', final_token)
    final_token = 'M_' + final_token

  if final_token and len(
          final_token.split()) > 1 and len(
          t.get('lemma').split()) == 1:
    final_token = re.sub(' ', '', final_token)


  # cleaning corrupted tokens due to annotator errors
  if final_token and re.search('^>[A-Za-z]+',final_token):
    final_token = re.sub('>','',final_token)
  if final_token and re.search('^<[A-Za-z]+',final_token):
    final_token = re.sub('<','',final_token)
  if final_token and re.search('^=[A-Za-z]+',final_token):
    final_token = re.sub('=','',final_token)
  if final_token and re.search('^/[A-Za-z]+',final_token):
    final_token = re.sub('/','',final_token)

  return final_token


def process_sentence(
        txt_id,
        sentence,
        tei_namespace,
        functions,
        types,
        subtypes,
        function_override):

  sentence_id = sentence.get('n')
  #print('sentence id : ' + sentence_id)
  tokens_lst = []
  tokens = sentence.findall('*')
  for t in tokens:
    # special handling of cases with embedded words/puncts within a
    # <hi></hi> pair of tags
    if t.tag == tei_namespace + 'hi':
      subTokens = t.findall('*')
      for st in subTokens:
        token_text = extract_xml_tag_text(
            txt_id, sentence_id,
            tei_namespace, st, functions,
            types, subtypes, function_override)

        if token_text is None or token_text == '':
          continue
        tokens_lst.append(token_text.strip())
      continue  # done for this tag pair, continue

    token_text = extract_xml_tag_text(
        txt_id, sentence_id,
        tei_namespace,
        t,
        functions,
        types,
        subtypes,
        function_override)

    # skips empty, non-meaningful tokens
    if token_text is None or token_text == '':
      continue

    tokens_lst.append(token_text.strip())

  return sentence_id, ' '.join(tokens_lst)


def extract_xml(
    xml_file,
    functions,
    types,
    subtypes,
        function_override):

  tei_namespace = '{http://www.tei-c.org/ns/1.0}'
  xml_namespace = '{http://www.w3.org/XML/1998/namespace}'

  tree = ET.parse(xml_file)
  root = tree.getroot()
  texts = root.findall(
      './' +
      tei_namespace +
      'text/' +
      tei_namespace +
      'group/' +
      tei_namespace +
      'text')

  output = []

  for txt in texts:
    txt_id = txt.attrib[xml_namespace + 'id']
    #print('txt id : ' + txt_id)
    sents = txt.findall('.//' + tei_namespace + 's')
    for s in sents:
      sentence_id, sentence_txt = process_sentence(
          txt_id, s, tei_namespace, functions, types, subtypes, function_override)
      output.append({'txt_id': txt_id,
                     'sentence_id': sentence_id,
                     'sentence_txt': sentence_txt})

  return output


def main():
  xml_file, functions, types, subtypes, function_override = read_config(
      'setup.cfg')

  output = extract_xml(
      xml_file,
      functions,
      types,
      subtypes,
      function_override)

  with open('vuamc_corpus.csv', 'w') as csvfile:
    fieldnames = [
        'txt_id',
        'sentence_id',
        'sentence_txt']

    writer = csv.DictWriter(
        csvfile,
        fieldnames=fieldnames,
        quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(output)


if __name__ == '__main__':
  main()
