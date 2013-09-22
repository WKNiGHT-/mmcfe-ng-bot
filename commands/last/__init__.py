import urllib
import logging
import json

def last_run_cmd(line, config):
    logger = logging.getLogger()
    logger.debug('Running command cmd.last')
    url = urllib.urlopen(config['api_url'] + '&action=getblocksfound&api_key=' + config['api_key'] + '&limit=1')
    jsonData = json.loads(url.read())
    return 'PRIVMSG ' + config['channel'] + ' :' + 'Last Block: #' + str(jsonData['getblocksfound']['data'][0]['height']) + ' | Shares: ' + str(jsonData['getblocksfound']['data'][0]['shares']) + ' | Confirmations: ' + str(jsonData['getblocksfound']['data'][0]['confirmations']) + ' | Solved By: ' + str(jsonData['getblocksfound']['data'][0]['finder'])