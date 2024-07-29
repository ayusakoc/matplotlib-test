import matplotlib.pyplot as plt
import numpy as np
age_list=[10,20,30]
weight=[40,50,60]
age_np=np.array(age_list)
weight_np=np.array(weight)

plt.plot(age_np,weight_np,"r")
plt.show()
