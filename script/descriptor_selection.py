from sklearn.model_selection import KFold
kfold = KFold(n_splits=10,shuffle=True)
def get_descriptor_selection(des,lable,model,des_len,tem_des_sel,all_num):
    all_pearsr = []
    all_mae = []
    des_rank=[]
    all_r2=[]
    try_index=list(set(list(range(des_len)))-set(tem_des_sel))
    for tem_des_index in try_index:
        tem_des_sel_=tem_des_sel+[tem_des_index]
        tem_des=des[:,tem_des_sel_]
        desc=tem_des
        lable=lable
        pearsr = []
        mae = []
        for i in range(1):
            all_pred = []
            all_test = []
            for train_index_tep,test_index_tep in kfold.split(desc):
                train_x,test_x = desc[train_index_tep],desc[test_index_tep]
                train_y,test_y = lable[train_index_tep],lable[test_index_tep]
                model = model#
                model.fit(train_x,train_y)
                test_pred = model.predict(test_x)
                all_pred.append(test_pred)
                all_test.append(test_y)
            all_pred = np.concatenate(all_pred)
            all_test = np.concatenate(all_test)
            r2 = r2_score(all_test,all_pred)
            pearsr.append(pearsonr(all_test,all_pred)[0])
            mae.append(mean_absolute_error(all_test,all_pred))
        r2=np.mean(np.array(r2))
        pearsr=np.mean(np.array(pearsr))
        mae=np.mean(np.array(mae))
        all_r2.append([r2])
        all_pearsr.append([pearsr])
        all_mae.append(mae)
    all_r2=np.array(all_r2)    
    max_r2=all_r2[np.argmax(all_r2)]
        
    all_pearsr=np.array(all_pearsr)    
    max_pear=all_pearsr[np.argmax(all_pearsr)]
    
    all_mae=np.array(all_mae)    
    max_mae=all_mae[np.argmax(all_mae)]    
    tem_des_sel_max=tem_des_sel+[try_index[np.argmax(all_pearsr)]]
    return max_pear,max_r2,max_mae,tem_des_sel_max



train_index=list(set(list(range(69))))
des_sel_max=108
tem_des_sel=[]
max_pear,max_r2,max_mae,tem_des_sel_max=get_descriptor_selection(des[train_index],lable=ddg[train_index],model=RandomForestRegressor(n_jobs=60),des_len=108,tem_des_sel=tem_des_sel,all_num=69)
print(max_pear,max_r2,max_mae,tem_des_sel_max)
result=[]
while True:
    tem_des_sel=tem_des_sel_max
    max_pear,max_r2,max_mae,tem_des_sel_max=get_descriptor_selection(des[train_index],lable=ddg[train_index],model=RandomForestRegressor(n_jobs=60),des_len=108,tem_des_sel=tem_des_sel,all_num=69)
    result.append([max_pear,max_r2,max_mae,tem_des_sel_max])
    print(max_pear,max_r2,max_mae,tem_des_sel_max)
    if len(tem_des_sel_max) ==des_sel_max:
        break
    else:
        continue
