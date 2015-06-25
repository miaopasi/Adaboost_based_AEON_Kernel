# coding: UTF-8
__author__ = 'Xiaolong Shen @ Nexd Tech'

'''
THIS IS THE UTILITY TOOLKIT FOR SDK GENERATED DATA.

TEMPORARILY DEVELOPED FOR AEON USAGE.

ADD-ON FUNCTION NEED TO BE FILLED.
'''


class ClfDataStorage:
	def __init__(self):
		self.wifi_matrix = None
		self.outlier_mac_count = None
		self.hit_mac_count = None
		self.total_mac_count = None


class SDKUtility:
	def __init__(self):
		pass
	"""
	PUBLIC FUNCTION:
		EXTRACT_WIFI    EXTRACTING WIFI FILE ONLY ACCORDING TO REFERENCE LIST FOR CLASSIFICATION USAGE
	"""
	def extract_wifi(self, wifi_path, ref_list=[]):
		"""
		:param wifi_path:
		:param ref_list:
		:return:
			miss_count
			hit_count
			wifi_matrix
		"""
		if ref_list:
			pass

		else:
			print "No Reference List Found"
			return


	"""
	PRIVATE FUNCTION
	"""
	def _extract_wifi(self, wifi_path, ref_list):
		"""
		Data Format:
			用户 ID#采集 ID#SSID#BSSID#Capability#Level#Frequency#扫描时间#强度（以100为准）#写入时间（毫秒

		:param wifi_path: path of wifi file(filepath)
		:param ref_list: reference wifi list
		:return:

		"""