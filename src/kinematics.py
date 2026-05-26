import numpy as np
from src.transformations import Rx, Ry, Rz, Trans


def T_base(x, y, z):
    return Trans(x, y, z)


def T_joint(rx, ry, rz, x, y, z):
    R = Rz(rz) @ Ry(ry) @ Rx(rx)
    T = Trans(x, y, z)
    return R @ T

if __name__ == "__main__":
    from src.transformations import Trans
    print(Trans(1,2,3))
