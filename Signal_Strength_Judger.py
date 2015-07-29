# coding = utf-8
__author__ = 'Xiaolong Shen'

from numpy import *
from kernel import *


class APInfo:
	def __init__(self):
		self.mac_add = None;
		self.name = None;
		self.wp_threshold = None;
		self.wp_threshold_count = 0;
		self.wifi_strength = None;

	def set(self, mac_add=None, name=None, wp_threshold=None, wp_threshold_count=None, wifi_strength=None,
	        wifi_pos=None):
		self.mac_add = mac_add;
		self.name = name;
		self.wp_threshold = wp_threshold;
		self.wp_threshold_count = wp_threshold_count;
		self.wifi_strength = wifi_strength;
		self.wifi_pos = wifi_pos;

	def setName(self, name):
		self.name = name;

	def setThreshold(self, wp_threshold, wp_threshold_count):
		self.wp_threshold = wp_threshold;
		self.wp_threshold_count = wp_threshold_count;


au = AeonUtility();

"""
train.wifi_list;
train.wifi_matrix
train.wifi_filepath
train.wp_filepath
train.wp_ind
train.wp_pos
"""


def getRes(wp_pos, wifi_vec):
	w_v = [];
	w_p = [];
	for i, ws in enumerate(list(wifi_vec)):
		if ws is not 0:
			w_v.append(ws);
			w_p.append(wp_pos[i, :]);
	return w_v, w_p


def extractRes(w_p, w_v, threshold):
	w_p_t = [];
	for i, ws in enumerate(w_v):
		if ws > threshold:
			w_p_t.append(w_p[i]);
	return w_p_t, len(w_p_t)


def getAnalysis(aeon_data):
	aeon_analysis = {}
	for i, mac in enumerate(aeon_data.wifi_list):
		t_ap = APInfo();
		w_v, w_p = getRes(aeon_data.wp_pos, aeon_data.wifi_matrix[:, i]);
		t_ap.set(mac, None, None, None, w_v, w_p);
		w_p_t, count = extractRes(w_p, w_v, -75);
		t_ap.setThreshold(w_p_t, count);
		aeon_analysis[mac] = t_ap
	return aeon_analysis


def output_format(data):
	file_name = "Aeon_" + (data.name if data.name else "EMPTY") + "_" + data.mac_add;
	f = open("./XML_AEON_SIGNAL/" + file_name + '.xml', 'w')
	bid = '10107993'
	fid = '101079930001'
	st_time = 1437991958349;
	ed_time = 1437991958349 + data.wp_threshold_count;
	st = time.strftime("%Y%m%d%H%M%S", time.localtime(st_time * 1e-3))
	ed = time.strftime("%Y%m%d%H%M%S", time.localtime(ed_time * 1e-3))
	f.write('<?xml version="1.0" encoding="GB2312"?>\n')
	f.write('<recode bid="%s" floorID="%s" startTime="%s" endTime="%s">\n' % (bid, fid, st, ed))
	f.write('\t<LocationPoints>\n')
	for i, x in enumerate(data.wp_threshold):
		t = time.localtime((st_time + i) * 1e-3)
		nt = time.strftime("%Y%m%d%H%M%S", t)
		f.write('\t\t<LoctP timestamp="%s" posX="%s" posY="%s"/>\n' % (nt, x[0], x[1]))
	f.write('\t</LocationPoints>\n')
	f.write('\t<RealPoints id="1">\n')
	f.write('\t\t<RealP timestamp="%s" posX="%s" posY="%s"/>\n' % (st, "0.0", "0.0"))
	f.write('\t\t<RealP timestamp="%s" posX="%s" posY="%s"/>\n' % (ed, "0.0", "0.0"))
	f.write('\t</RealPoints>\n')
	f.write('</recode>\n')
	f.close()

def _extract_wifi(file_path):
	wifi_info = {}
	for fn in os.listdir(file_path):
		if 'journal' in fn:
			continue
		wifi_path = os.path.join(file_path, fn)
		f = open(wifi_path)
		lines = f.readlines()
		f.close()
		for i, l in enumerate(lines):
			ls = l.split('#')
			if len(ls) is not 10:
				continue
			mac = ls[3]
			name = ls[2]
			if not mac in wifi_info:
				wifi_info[mac] = name;
	return wifi_info


def fillName(wifi_info, aeon_analysis):
	for mac in aeon_analysis.keys():
		try:
			aeon_analysis[mac].setName(wifi_info[mac]);
			print "got Mac"
		except:
			print "dont't have mac"
	return aeon_analysis



data = load('Aeon_Base_Data.npz');
# Data Format: savez('Aeon_Base_Data.npz', wifi_list=train.wifi_list, wp_pos=train.wp_pos, all_data=train)

# aeon_data = data['all_data'];

aeon_data = au.load_wifi('./Data/Training/data_new.wp', './Data/Training/data_new.wifi')

aeon_analysis = getAnalysis(aeon_data);

sample = APInfo();
sample.set("00:00:00:00:00:00", "MiaoPaSi", [[0,0],[1,1],[2,2],[3,3],[4,4]], 5, [-50,-50,-50,-50,-50], [[0,0],[1,1],[2,2],[3,3],[4,4]]);

output_format(sample);

wifi_info = _extract_wifi('./RawData/nextdirection')

aeon_analysis = fillName(wifi_info, aeon_analysis)

for x in aeon_analysis:
	output_format(aeon_analysis[x]);




