# coding: UTF-8
__author__ = 'Xiaolong Shen @ NEXD'

import sys
from numpy import *
from sklearn.externals import joblib
# import imp

sys.path.append('./RefCode/')

from loadfile import LoadWifiData
from Adaboost_Classification_Class import *


class AeonUtility:
	"""
	Including Utility Functions for Aeon Usage

	DataStorage Content:
		self.wp_filepath = wp_filepath
		self.wifi_filepath = wifi_filepath
		self.wifi_list = wifi_list
		self.wp_pos = wp_pos
		self.wp_ind = wp_ind
		self.wifi_matrix = wifi_matrix

	"""
	def __init__(self):
		self.loader = LoadWifiData()
		self.map_ratio = 10

	def load_wifi(self, wp_path, wifi_path, ref_list = []):
		if ref_list:
			wifi = self.loader.extract_with_ref(wp_path, wifi_path, ref_list)
		else:
			wifi = self.loader.extract(wp_path, wifi_path)
		return wifi

	def _extract(self,wifi_path):
		"""

		用户 ID#采集 ID#SSID#BSSID#Capability#Level#Frequency#扫描时间#强度（以100为准）#写入时间（毫秒
		"""

		pass

	def accuracy(self, res, test_pos, train_pos):
		RMSE = []
		for i,n in enumerate(res):
			pos_res = array(train_pos[n]);
			pos_tar = array(test_pos[i]);
			pos_diff = pos_res
			se = sqrt(((pos_tar - pos_diff) ** 2).sum()) / self.map_ratio
			RMSE.append(se)
		return RMSE

class AeonKernel(AdaboostClassification):
	"""

	"""
	def __init__(self):
		AdaboostClassification.__init__(self)
		# clf is the classifier trained out
		self.clf = None
		self.util = AeonUtility()

	def train(self, train_data, train_tar):
		self.clf = self.learn_clf(train_data, train_tar)

	def save(self, save_path = 'Aeon_Adaboost_Classifier.pkl'):
		# savez(save_path, clf=self.clf)
		joblib.dump(self.clf, save_path, compress=9)

	def load_clf(self, load_path = 'Aeon_Adaboost_Classifier.pkl'):
		ref = joblib.load(load_path)
		self.clf = ref

	def test(self, test_data):
		res = self.clf.predict(test_data)
		return res

	def validate_test_accuracy(self, test_data, test_pos, train_pos):
		res = self.test(test_data)
		RMSE = self.util.accuracy(res, test_pos, train_pos)
		print "RMSE:%s\n Average Mean Error: %s" %(RMSE, array(RMSE).mean())
		return array(RMSE).mean()

