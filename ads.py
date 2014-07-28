#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
This is an example script for a typical ADS use case: a simple
institutional bibliography. It accepts as input a file containing 
author names. It then searches ADS for records and outputs a tsv 
of bibcodes, titles, publication and full author list
'''
import simplejson
import requests
import datetime

# base API search url
BASE_URL = 'http://adslabs.org/adsabs/api/search/'

# developer API access key
DEV_KEY = 'G5hXxZuEhqnTyFx5'

def get_refereed():

  #if os.environ.has_key("ADS_DEV_KEY"):
  #    DEV_KEY = os.environ['ADS_DEV_KEY']

  params = {}
          
  # basic author search
  author = "Elliott"
  params['q'] = "author:%s,database:astronomy" % author
  # the fields we want back
  params['fl'] = 'title,pub,author,aff,volume,year'
          
  # process 100 results at a time
  params['rows'] = '200'
          
  #include our access key
  params['dev_key'] = DEV_KEY

  # database?
  params['filter'] = 'property:refereed AND database:astronomy AND year:[2010 TO *]'
         
  # json is the default type, this is just for illustration purposes
  headers = {'content-type': 'application/json'}
          
  # sys.stderr.write("issuing query for author %s\n" % author)
          
  # for paginating through long results
  start = 0
  processed = 0

  refereed = 0

  while True:
    params['start'] = start
    r = requests.get(BASE_URL, params=params, headers=headers)
      
    # uncomment if you want to see the actual http request url
    # sys.stderr.write(r.url + "\n")
      
    if r.status_code != requests.codes.ok:
      # hopefully if something went wrong you'll get a json error message
      e = simplejson.loads(r.text)
      # sys.stderr.write("error retrieving results for author %s: %s\n" % (author, e['error']))

    data = simplejson.loads(r.text.decode('utf-8'))

    # number of search hits
    hits = data['meta']['hits']
    #print "You have: %d hits" % hits
    count = data['meta']['count']
    processed += count

    possible_author = ["Elliott"]
    possible_aff = ["MPE"]


    string_arr = []
    for paper in data['results']['docs']:
      # Collect relevant details
      author_list = paper['author']
      match_auth = [author for author in author_list if "Elliott, J" in author]
      match_auth2  = [author for author in author_list if "Greiner" in author]

      try:
        aff_list = paper['aff']
      except:
  	  	aff_list = []



      if match_auth and match_auth2:
        first_name = match_auth[0].split(", ")[1]
        if first_name in ["J.", "Jonathan", "Jonny"]:
          refereed+=1

          for k in range(len(author_list)):
            if "Elliott" in author_list[k]:
              author_list[k] = "<b>%s</b>" % (author_list[k])

          string_authors = " ".join(author_list)
          string_journal = "<u>%s</u>" % paper['pub']
          title = "%s" % "".join(paper['title'])
          year = "%s" % paper['year']
          vol = "<b>%s</b>" % paper['volume']
          bibcode = paper['bibcode']
        
          string_output = "<FONT COLOR=\"red\">%d</FONT>.\
                            <a href=\"http://cdsads.u-strasbg.fr/abs/%s\" target="_blank">%s</a><br>\
                            %s<br>\
                            %s %s<br><br>" % (refereed, bibcode, title, string_authors, string_journal, year)
          string_arr.append(string_output)

    # should I repeat the above?
    if processed < hits:
      start += count
    else:
      break


  output_file = open("templates/ads.html", "w")
  updated = " ".join(datetime.datetime.now().isoformat().split("T"))
  output_file.write("<h4><FONT COLOR=\"green\">Updated: %s</FONT></h4>" % updated)
  for i in range(len(string_arr)):
    output_file.write("%s<br>\n\n" % string_arr[i].encode('utf-8'))
  output_file.close()

def get_gcn():

  #if os.environ.has_key("ADS_DEV_KEY"):
  #    DEV_KEY = os.environ['ADS_DEV_KEY']

  params = {}
          
  # basic author search
  author = "Elliott"
  params['q'] = "author:%s,database:astronomy" % author
  # the fields we want back
  params['fl'] = 'title,pub,author,aff,volume,year'
          
  # process 100 results at a time
  params['rows'] = '200'
          
  #include our access key
  params['dev_key'] = DEV_KEY

  # database?
  params['filter'] = 'bibstem:GCN AND database:astronomy AND year:[2010 TO *]'
         
  # json is the default type, this is just for illustration purposes
  headers = {'content-type': 'application/json'}
          
  # sys.stderr.write("issuing query for author %s\n" % author)
          
  # for paginating through long results
  start = 0
  processed = 0

  refereed = 0

  while True:
    params['start'] = start
    r = requests.get(BASE_URL, params=params, headers=headers)
      
    # uncomment if you want to see the actual http request url
    # sys.stderr.write(r.url + "\n")
      
    if r.status_code != requests.codes.ok:
      # hopefully if something went wrong you'll get a json error message
      e = simplejson.loads(r.text)
      # sys.stderr.write("error retrieving results for author %s: %s\n" % (author, e['error']))

    data = simplejson.loads(r.text.decode('utf-8'))

    # number of search hits
    hits = data['meta']['hits']
    #print "You have: %d hits" % hits
    count = data['meta']['count']
    processed += count

    possible_author = ["Elliott"]
    possible_aff = ["MPE"]


    string_arr = []
    for paper in data['results']['docs']:


      # Collect relevant details
      author_list = paper['author']
      match_auth = [author for author in author_list if "Elliott, J" in author]
      match_auth2  = [author for author in author_list if "Greiner" in author]

      try:
        aff_list = paper['aff']
      except:
        aff_list = []



      if match_auth and match_auth2:
        first_name = match_auth[0].split(", ")[1]
        if first_name in ["J.", "Jonathan", "Jonny"]:
          refereed+=1

          for k in range(len(author_list)):
            if "Elliott" in author_list[k]:
              author_list[k] = "<b>%s</b>" % (author_list[k])

          string_authors = " ".join(author_list)
          string_journal = "<u>%s</u>" % paper['pub']
          title = "%s" % "".join(paper['title'])
          year = "%s" % paper['year']
          vol = "<b>%s</b>" % paper['volume']
          bibcode = paper['bibcode']
        
          string_output = "<FONT COLOR=\"red\">%d</FONT>.\
                            <a href=\"http://cdsads.u-strasbg.fr/abs/%s\" target="_blank">%s</a><br>\
                            %s<br>\
                            %s %s<br><br>" % (refereed, bibcode, title, string_authors, string_journal, year)
          string_arr.append(string_output)

    # should I repeat the above?
    if processed < hits:
      start += count
    else:
      break


  output_file = open("templates/gcn.html", "w")
  updated = " ".join(datetime.datetime.now().isoformat().split("T"))
  output_file.write("<h4><FONT COLOR=\"green\">Updated: %s</FONT></h4>" % updated)
  for i in range(len(string_arr)):
    output_file.write("%s<br>\n\n" % string_arr[i].encode('utf-8'))
  output_file.close()

if __name__ == "__main__":
  get_refereed()
  get_gcn()
