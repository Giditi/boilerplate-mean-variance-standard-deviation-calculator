import numpy as np

def calculate(list):
    try:
        arr=np.array(list)
        arr_3=arr.reshape(3,3)
        arr_fl=arr_3.flatten()

        arr_sumr=np.sum(arr_3, axis=0).tolist()
        arr_sumc=np.sum(arr_3, axis=1).tolist()
        arr_sum=np.sum(arr_fl).tolist()

        arr_minr=np.min(arr_3, axis=0).tolist()
        arr_minc=np.min(arr_3, axis=1).tolist()
        arr_min=np.min(arr_fl).tolist()

        arr_maxr=np.max(arr_3, axis=0).tolist()
        arr_maxc=np.max(arr_3, axis=1).tolist()
        arr_max=np.max(arr_fl).tolist()

        arr_meanr=np.mean(arr_3, axis=0).tolist()
        arr_meanc=np.mean(arr_3, axis=1).tolist()
        arr_mean=np.mean(arr_fl).tolist()

        arr_sdevr=np.std(arr_3, axis=0).tolist()
        arr_sdevc=np.std(arr_3, axis=1).tolist()
        arr_sdev=np.std(arr_fl).tolist()

        arr_varr=np.var(arr_3, axis=0).tolist()
        arr_varc=np.var(arr_3, axis=1).tolist()
        arr_var=np.var(arr_fl).tolist()

        l_sum =[arr_sumr, arr_sumc, arr_sum]
        l_min =[arr_minr, arr_minc, arr_min]
        l_max =[arr_maxr, arr_maxc, arr_max]
        l_var =[arr_varr, arr_varc, arr_var]
        l_mean =[arr_meanr, arr_meanc, arr_mean]
        l_sdev =[arr_sdevr, arr_sdevc, arr_sdev]
        
        calculations={
            'mean': l_mean,
            'variance': l_var,
            'standard deviation': l_sdev,
            'max': l_max,
            'min': l_min,
            'sum': l_sum
            }
        return calculations
    
    except ValueError:
        raise ValueError('List must contain nine numbers.')
