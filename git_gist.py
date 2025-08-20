import pprint
import requests

pprint.pprint(requests.get("https://gist.githubusercontent.com/viplavdube/cd085f915b332a072690505aab86f5d9/raw/75b063a2b861e33720e97bde3c44671b1acc964c/viplav-dube-scrapping.json").json())