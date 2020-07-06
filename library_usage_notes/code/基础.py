
import torch
import numpy as np
from torch.autograd import Variable

# np_data = np.arange(6).reshape((2,3))
# torch_data = torch.from_numpy(np_data)
# tensor2array = torch_data.numpy()
#
# print(
#     '\nnumpy',np_data,
#     '\ntorch',torch_data,
#     '\ntensor2array',tensor2array
# )

#绝对值
# data = [-1, 1, -2, 2]
# tensor = torch.FloatTensor(data)
#
# print(
#     '\nnumpy:', np.abs(data),
#     '\ntorch:', torch.abs(tensor)
# )


# data = [[1,2], [3,4]]
# tensor = torch.FloatTensor(data)
#
# print(
#     '\nnumpy:',np.matmul(data,data),
#     '\ntorch:',torch.mm(tensor, tensor)
# )

data = [[1,2],[3,4]]
tensor = torch.FloatTensor(data)
variable = Variable(tensor, requires_grad=True)

t_out = torch.mean(tensor*tensor)
v_out = torch.mean(variable*variable)

print(t_out)
print(v_out)

v_out.backward()
print(variable.grad)
