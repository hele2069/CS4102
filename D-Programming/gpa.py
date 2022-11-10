import numpy as np


exam = [84.5,82,89,94]
coding = [100,100,100,100]
basic = [100,100,100,100]
advanced = [83,93,100,100]

gpa = np.mean(exam)*0.52 + np.mean(basic)*0.08 + np.mean(advanced)*0.2 + np.mean(coding)*0.2 
print(gpa)