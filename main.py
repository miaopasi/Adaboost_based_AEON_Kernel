__author__ = 'admin'

from kernel import *

# au = AeonUtility();
# train = au.load_wifi('./Data/Training/data.wp', './Data/Training/data.wifi')
# # savez('Aeon_Base_Data.npz', wifi_list=train.wifi_list, wp_pos=train.wp_pos, all_data=train)
# test = au.load_wifi('./Data/Test/Bad_Attempt/data.wp', './Data/Test/Bad_Attempt/data.wifi', train.wifi_list)
#
# print test.wifi_matrix.shape
# print test.wp_pos.shape
#
# print "> Loading Finished"
# ak = AeonKernel();
# # ak.train(train.wifi_matrix, arange(train.wifi_matrix.shape[0]))
# print "> Training Finished"
# # ak.save()
# print "> Saved"
# ak.load_clf()
# print "> Load In"
# import time
# st = time.time()
# ak.validate_test_accuracy_proba(test.wifi_matrix, test.wp_pos, train.wp_pos)
# ed = time.time()
# print "> Validation Done"
# print "> Time Comsumption for Test : %s, Average Time Comsumption : %s" %(ed-st, float(ed-st)/test.wifi_matrix.shape[0])


from kernel import *
import cPickle

# ae = Aeon()
# ae.load_config('Aeon_Adaboost_Classifier.pkl', 'Aeon_Base_Data.npz')
# res, res_cred = ae.process_route('./Raw_Data/Collect_File_Type/test')
# # res = {1:'miao',3:'si',2:'pa'}
#
# f = open('temp_res.pkl','w')
# cPickle.dump(res, f)
# f.close()
# f = open('temp_res_cred.pkl','w')
# cPickle.dump(res_cred, f)
# f.close()

f = open('temp_res.pkl')
res = cPickle.load(f)
f.close()
f = open('temp_res_cred.pkl')
res_cred = cPickle.load(f)
f.close()
# res_key = list(res.keys())
# res_key.sort()

ae = Aeon()
ae.output_format(res, res_cred, True);


# count = 0
# sx = res_key[0];
#
# for x in res_key:
# 	cred = res_cred[x]
# 	if cred[0] < 5:
# 		continue
# 	if (cred[0] - cred[1]) / cred[0] < 0.7:
# 		continue
# 	count += 1
# 	print "%s\t%s" % (res[x],(x-sx)/1000)
# 	sx = x
#
# print "Cand: %s, Pick : %s" %(len(res_key), count)