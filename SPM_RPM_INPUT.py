###直径80~130[mm]のタイヤを使用することを想定###
###速度5~13[m/s](18~46.8[km/s])を実現するモータに必要な回転数[SPM, RPM]と動力[W]を求める###

#インポート

import math

#初期設定

Distance = 100000 #[mm]

######## 関数群 ########

#円周　Circumference
def Circumference(Diameter):
    Circumference = Diameter * math.pi
    return Circumference

#100m到達できる回転数 Complete_Rotation_Speed
def Complete_Rotation_Speed(Circumference):
    Complete_Rotation_Speed = 100000 / Circumference
    return Complete_Rotation_Speed

#一回転にかかる時間
def One_Rotation_Speed(END_TIME, Complete_Rotation_Speed):
    One_Rotation_Speed = END_TIME / Complete_Rotation_Speed
    return One_Rotation_Speed

#SPM
def SPM(One_Rotation_Speed):
    SPM = 1 / One_Rotation_Speed
    return SPM

#RPM
def RPM(SPM):
    RPM = SPM * 60
    return RPM

#トルク
def Torque(Radius):
    Torque = (25 * 9.81) * Radius / 1000 #ここだけmになおす
    return Torque

#動力
def Power(Radius, RPM):
    Power = (25 * 9.81 * Radius * RPM) / 9549
    return Power

#接線力
def Tangential_Force(Torque, Radius):
    Tangential_Force = Torque / Radius
    return Tangential_Force

#加速度
def Acceleration(Tangential_Force):
    Acceleration = Tangential_Force / m - g
    return Acceleration

########## MAIN ##########

print("静止状態(0m)から頂点まで(100m)のぼるとき")
print("注：モーターがひとつの場合")
Diameter = float(input("車輪直径[mm]を入力してください"))
Circumference1 = Circumference(Diameter)
Complete_Rotation_Speed1 = Complete_Rotation_Speed(Circumference1)
Radius = Diameter / 2
Torque1 = Torque(Radius)
print("ーーータイヤ直径", Diameter, "[mm] 必要最低トルク", Torque1, "[N・m]の場合ーーー")

V = float(input("目標速度[m/s]を入力してください")) * 1000
END_TIME = Distance / V
One_Rotation_Speed1 = One_Rotation_Speed(END_TIME, Complete_Rotation_Speed1)
SPM1 = SPM(One_Rotation_Speed1)
RPM1 = RPM(SPM1)
print("V", V / 1000, "[m/s]", "SPM", SPM1, "[回転/秒]", "RPM", RPM1, "[回転/分]")
P = Power(Radius, RPM1)
print("必要最低動力", P, "[W]")
