import requests
import yaml
import os

inteltype = ['INTEL_ADDR']
path = os.environ["WORKDIR"]
with open(path + "/enrichment_plugins/feodotracker/dnifconfig.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)


def import_ip_intel():
    try:
        source = cfg['enrichment_plugin']['FEODOTRACKER_IP_SOURCE']
        response = requests.get(source)
    except Exception, e:
        print 'Api Request Error %s' % e
    try:
        lines = []
        for line in response.iter_lines():
            line = line.strip()
            s = str(line)
            s = s.strip()
            if not s.startswith("#") and s != '':
                tmp_dict = {}
                tmp_dict["EvtType"] = "IPv4"
                tmp_dict["EvtName"] =s
                tmp_dict2 = {}
                tmp_dict2["IntelRef"] = ["FEODOTRACKER"]
                tmp_dict2["IntelRefURL"] = [source]
                b_lst = []
                b_lst.append("Feodo botnet C&C ")
                tmp_dict2["ThreatType"] = b_lst
                tmp_dict["AddFields"] = tmp_dict2
                lines.append(tmp_dict)
    except:
        lines = []
    return lines, 'INTEL_ADDR'

