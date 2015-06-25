__author__ = 'admin'

from kernel import *

au = AeonUtility();
train = au.load_wifi('./Data/Training/data.wp', './Data/Training/data.wifi')
test = au.load_wifi('./Data/Test/Bad_Attempt/data.wp', './Data/Test/Bad_Attempt/data.wifi', train.wifi_list)

print test.wifi_matrix.shape
print test.wp_pos.shape

print "> Loading Finished"
ak = AeonKernel();
# ak.train(train.wifi_matrix, arange(train.wifi_matrix.shape[0]))
print "> Training Finished"
# ak.save()
print "> Saved"
ak.load_clf()
print "> Load In"
import time
st = time.time()
ak.validate_test_accuracy(test.wifi_matrix, test.wp_pos, train.wp_pos)
ed = time.time()
print "> Validation Done"
print "> Time Comsumption for Test : %s, Average Time Comsumption : %s" %(ed-st, float(ed-st)/test.wifi_matrix.shape[0])
