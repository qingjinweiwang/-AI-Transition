import torch

# x=torch.tensor([[1, 2, 3],[4,5,6]],dtype=torch.float32)

# print("x=")
# print(x)

# print("shape:",x.shape)
# print("dimension:",x.ndim)
# print("dtype:",x.dtype)
# print("device:",x.device)

# device = "cuda" if torch.cuda.is_available() else "cpu"

# y=torch.randn(2,3,device=device,dtype=torch.float32)

# print("\ny=")
# print(y)    

# print("shape:",y.shape)
# print("dimension:",y.ndim)  
# print("dtype:",y.dtype)
# print("device:",y.device)

# x=x.to(device)

# print("\nx after to(device):")
# print(x)
# print("device:",x.device)

# z=x+y

# print("\nz=x+y=")
# print(z)


# x=torch.tensor([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],dtype=torch.float32,device="cuda")
# 修正 x=torch.zero_s((4,5),dtype=torch.float32,device="cuda")
# print("shape=",x.shape)


# y=torch.tensor([[2,3,224,224]])
# 修正 y=torch.randn(2,3,224,224)
# print("shape:",y.shape)
# print("dimension:",y.ndim)
# print("dtype:",y.dtype)
# print("device:",y.device)

# a=torch.tensor([1,2,3],dtype=torch.float32)
# a=a.to("cuda")

# a,b不在同一区域，无法运算
#修正： a、b 不在同一个 device，无法直接运算

# torch.randn(2, 3, 224, 224) 创建了什么？
# 答：创建了一个形状为 (2, 3, 224, 224) 的张量，包含从标准正态分布中随机采样的浮点数。
# ndim 为什么是 4？
# 答：因为张量的形状是 (2, 3, 224, 224)，它有四个维度：第一个维度是批量大小（2），第二个维度是通道数（3），第三个和第四个维度是图像的高度和宽度（224x224）。
# dtype=torch.float32 是什么意思？
# 答：dtype=torch.float32 表示张量的数据类型是 32 位浮点数（float32），这是深度学习中常用的数据类型，适合表示连续值。
# cuda:0 是什么意思？
# 答：cuda:0 表示第一个 GPU 设备，用于指定张量在 GPU 上的存储位置。
# 为什么 CPU Tensor 和 GPU Tensor 不能直接相加？
# 答：因为 CPU Tensor 和 GPU Tensor 存储在不同的设备上，直接相加会导致设备不匹配的错误。
# torch.tensor([2,3,224,224]) 和 torch.randn(2,3,224,224) 有什么区别？
# 答：torch.tensor([2,3,224,224]) 创建了一个形状为 (4,) 的张量，包含指定的值；而 torch.randn(2,3,224,224) 创建了一个形状为 (2, 3, 224, 224) 的张量，包含从标准正态分布中随机采样的浮点数。