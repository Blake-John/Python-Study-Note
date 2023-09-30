import torch
import numpy
import random
import numpy as np


# tensor1 = torch.tensor (range (12))
# print (tensor1)

# tensor2 = tensor1.view (2,3,2)
# print (tensor2)

# tensor3 = tensor1.view (3,4,1)
# print (tensor3)

a = torch.randn (3,2,2,requires_grad=True)
print (a)