import torch
import numpy
from torch.autograd import Variable

tensor = torch.FloatTensor ([[1,2],[3,4]])
variable = Variable (tensor,requires_grad=True)

t_out = torch.mean (tensor*tensor) # mean 为均值
v_out = torch.mean (variable*variable)

v_out.backward ()

print (variable.grad)

print (variable)
print (variable.data)

print (variable.data.numpy)
# print (tensor)
# print (t_out)
# print (v_out)