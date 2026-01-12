# import numpy as np
# import time
# SIZE=100000
# L1=range(SIZE)
# L2=range(SIZE)
# A1=np.arenge(SIZE)
# A2=np.arenge(SIZE)
# satar=time.time()
# result=[(x,y

import pandas as pd 
import numpy as np
dict={'first score':[100,90,np.nan,95],
      'second score':[30,45,56,np.nan],
      'thired score':[np.nan,40,80,98]}
df=pd.DataFrame(dict)
df.isnull()