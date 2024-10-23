################ Functions for Programs Engineering Civil by Eng. Mahammad Qassem ###############
############################

def Beamweightcement(Lenghtforbeam,WidthofAreafaceBeam,HightofAreafaceBeam,WeightofCementper1m3):
    wt=(float(WeightofCementper1m3)*1400*0.001*(float(WidthofAreafaceBeam)*float(HightofAreafaceBeam)*float(Lenghtforbeam)))
    return wt
def Beamweightcementcost(Lenghtforbeam,WeightofCementper1m3,WidthofAreafaceBeam,HightofAreafaceBeam,costper1ton):
    wt=(float(WeightofCementper1m3)*1400*0.001*(float(WidthofAreafaceBeam)*float(HightofAreafaceBeam)*float(Lenghtforbeam)))
    cw=float(wt)*float(costper1ton)
    return cw
def BeamvolumeSand(Lenghtforbeam,WidthofAreafaceBeam,HightofAreafaceBeam,VolofSandper1m3):
    vs=(float(VolofSandper1m3)*(float(WidthofAreafaceBeam)*float(HightofAreafaceBeam)*float(Lenghtforbeam)))
    return vs
def BeamvolumSandCost(Lenghtforbeam,WidthofAreafaceBeam,HightofAreafaceBeam,VolofSandper1m3,CostSandperm3):
    vs=(float(VolofSandper1m3)*(float(WidthofAreafaceBeam)*float(HightofAreafaceBeam)*float(Lenghtforbeam)))
    cs=float(vs)*float(CostSandperm3)
    return cs
def BeamvolumeGravel(Lenghtforbeam,WidthofAreafaceBeam,HightofAreafaceBeam,Volofgravelper1m3):
    vg=(float(Volofgravelper1m3)*(float(WidthofAreafaceBeam)*float(HightofAreafaceBeam)*float(Lenghtforbeam)))
    return vg
def BeamvolumeGravelCost(Lenghtforbeam,WidthofAreafaceBeam,HightofAreafaceBeam,Volofgravelper1m3,Costgravelperm3):
    vg=(float(Volofgravelper1m3)*(float(WidthofAreafaceBeam)*float(HightofAreafaceBeam)*float(Lenghtforbeam)))
    cg=float(vg)*float(Costgravelperm3)
    return cg
def Beamweightreinforcement(Lenghtforbeam,numberofbars,sizeofbarbeam):
    wq=(float(Lenghtforbeam)*((float(sizeofbarbeam)**2)/162)*0.001*float(numberofbars))
    return wq
def Beamweightreinforcementcost(Lenghtforbeam,sizeofbarbeam,numberofbars,reinforcementcostper1ton):
    wq=(float(Lenghtforbeam)*((float(sizeofbarbeam)**2)/162)*0.001*int(numberofbars))
    reinforcementcost=float(wq)*float(reinforcementcostper1ton)
    return reinforcementcost
def Beamweightreinforcementstrip(Lenghtforbeam,Lenghtofstrip,Widthofstrip,sizeofbarstrip):
    waa =((float(Lenghtforbeam)/0.2)*(2*float(Lenghtofstrip)+2*float(Widthofstrip))*(float(sizeofbarstrip)**2/162)*0.001)
    return waa
def Beamweightreinforcementstripcost(Lenghtforbeam,Lenghtofstrip,Widthofstrip,sizeofbarstrip,reinforcementcostper1tonforstrip):
    wa=((float(Lenghtforbeam)/0.2)*(2*float(Lenghtofstrip)+2*float(Widthofstrip))*(float(sizeofbarstrip)**2/162)*0.001)
    costreinforcementstrip=float(wa)*float(reinforcementcostper1tonforstrip)
    return costreinforcementstrip

##############################################
def bricksunderbase(Lenghtforwall):
    Vol_bricks_under=float(Lenghtforwall)*(0.48*0.07+0.36*0.07+0.25*0.5)
    No_bricks_under=400*Vol_bricks_under
    return No_bricks_under
def bricksunderbasecost(Lenghtforwall,costbricksper4000):
    Vol_bricks_under=float(Lenghtforwall)*(0.48*0.07+0.36*0.07+0.25*0.5)
    No_bricks_under=400*Vol_bricks_under
    costbricksuder=float(No_bricks_under)*float(costbricksper4000)
    return costbricksuder
def bricksupbase(Lenghtforwall,Volumeofdoorsandwindows):
    Vol_bricks_up=(0.25*3*float(Lenghtforwall))-float(Volumeofdoorsandwindows)
    No_bricks_up=400*Vol_bricks_up
    return No_bricks_up
def bricksupbasecost(Lenghtforwall,Volumeofdoorsandwindows,costbricksper4000):
    Vol_bricks_up=(0.25*3*float(Lenghtforwall))-float(Volumeofdoorsandwindows)
    No_bricks_up=400*Vol_bricks_up
    costbricksup=float(No_bricks_up)*float(costbricksper4000)
    return costbricksup
###################################
def Riftweightreinforcement(LenghtofRift,WidthofRift,sizsofbar):
    Riftweightreinf=(((float(sizsofbar))**2/162)*0.001*20*float(LenghtofRift)*float(WidthofRift))
    return Riftweightreinf
def Riftweightreinforcementcost(LenghtofRift,WidthofRift,sizsofbar,Riftreinforcementcostper1ton):
    Riftweightreinf=(((float(sizsofbar))**2/162)*0.001*20*float(LenghtofRift)*float(WidthofRift))
    riftreinforcementcost=float(Riftweightreinf)*float(Riftreinforcementcostper1ton)
    return riftreinforcementcost 
def RiftweightCement(LenghtforRift,WidthofAreafaceRift,HightofAreafaceRift,WeightofCementper1m3):
    Rwt=(float(WeightofCementper1m3)*1400*0.001*(float(WidthofAreafaceRift)*float(HightofAreafaceRift)*float(LenghtforRift)))
    return Rwt
def Riftweightcementcost(LenghtforRift,WeightofCementper1m3,WidthofAreafaceRift,HightofAreafaceRift,costper1ton):
    Rwt=(float(WeightofCementper1m3)*1400*0.001*(float(WidthofAreafaceRift)*float(HightofAreafaceRift)*float(LenghtforRift)))
    cw=float(Rwt)*float(costper1ton)
    return cw
def RiftvolumeSand(LenghtforRift,WidthofAreafaceRift,HightofAreafaceRift,VolofSandper1m3):
    vs=(float(VolofSandper1m3)*(float(WidthofAreafaceRift)*float(HightofAreafaceRift)*float(LenghtforRift)))
    return vs
def RiftvolumSandCost(LenghtforRift,WidthofAreafaceRift,HightofAreafaceRift,VolofSandper1m3,CostSandperm3):
    vs=(float(VolofSandper1m3)*(float(WidthofAreafaceRift)*float(HightofAreafaceRift)*float(LenghtforRift)))
    cs=float(vs)*float(CostSandperm3)
    return cs
def RiftvolumeGravel(LenghtforRift,WidthofAreafaceRift,HightofAreafaceRift,Volofgravelper1m3):
    vg=(float(Volofgravelper1m3)*(float(WidthofAreafaceRift)*float(HightofAreafaceRift)*float(LenghtforRift)))
    return vg
def RiftBeamvolumeGravelCost(LenghtforRift,WidthofAreafaceRift,HightofAreafaceRift,Volofgravelper1m3,Costgravelperm3):
    vg=(float(Volofgravelper1m3)*(float(WidthofAreafaceRift)*float(HightofAreafaceRift)*float(LenghtforRift)))
    cg=float(vg)*float(Costgravelperm3)
    return cg
######## Mixing Cement and Sand and Gravel ####
######## M5     >>> 1:5:10 >>> 5 N/mm2 ########
Mix5WeightCementper1m3 = 0.093
Mix5VolofSandper1m3 = 0.465
Mix5Volofgravelper1m3 = 0.93
######## M7.5 >>> 1:4:8  >>> 7.5 N/mm2 ########
Mix7_5WeightCementper1m3 = 0.114
Mix7_5VolofSandper1m3=0.456
Mix7_5Volofgravelper1m3=0.912
######## M10  >>> 1:3:6  >>> 10 N/mm2 ########
Mix10WeightCementper1m3=0.149
Mix10VolofSandper1m3=0.447
Mix10Volofgravelper1m3=0.894
######## M15  >>> 1:2:4  >>> 15 N/mm2 ########
Mix15WeightCementper1m3=0.213
Mix15VolofSandper1m3=0.42
Mix15Volofgravelper1m3=0.85
######## M20  >>> 1:1.5:3 >> 20 N/mm2 ########
Mix20WeightCementper1m3=0.271
Mix20VolofSandper1m3=0.4065
Mix20Volofgravelper1m3=0.813
##############################################
###### Volumes ###############################
def VolofConc(hightofConc,widhtofConc,LenghtofConc):
    v=float(hightofConc)*float(widhtofConc)*float(LenghtofConc)
    return v
##############################################
####### Types of Slab ########################
########### Checking for Types of Slab #######
def Check_Type_of_Slabs(LenghtforLongSide,LenghtforShortSide):
    check=(LenghtforLongSide/LenghtforShortSide)
    if check == 2 and check >= 2 :
        a="One Way Slab"
    if check < 2 :
        a="Two Way Slab" 
    return a
######################################################
####### Found The Thickness of One Way Slab When Fy=420 Mpa ##########
def ThicknessMinimum_One_Way_Solid_Slab_Simply_Support(LenghtofOneWaySlab):
    sump=LenghtofOneWaySlab/20
    return sump
def ThicknessMinimum_One_Way_Solid_Slab_OneEnd_Continuous(LenghtofOneWaySlab):
    sump=LenghtofOneWaySlab/24
    return sump
def ThicknessMinimum_One_Way_Solid_Slab_BothEnd_Continuous(LenghtofOneWaySlab):
    sump=LenghtofOneWaySlab/28
    return sump
def ThicknessMinimum_One_Way_Solid_Slab_Cantilever(LenghtofOneWaySlab):
    sump=LenghtofOneWaySlab/10
    return sump
def ThicknessMinimum_One_Way_BeamOrRibbed_Slab_Simply_Support(LenghtofOneWaySlab):
    sump=LenghtofOneWaySlab/16
    return sump
def ThicknessMinimum_One_Way_BeamOrRibbed_Slab_OneEnd_Continuous(LenghtofOneWaySlab):
    sump=LenghtofOneWaySlab/18.5
    return sump
def ThicknessMinimum_One_Way_BeamOrRibbed_Slab_BothEnd_Continuous(LenghtofOneWaySlab):
    sump=LenghtofOneWaySlab/21
    return sump
def ThicknessMinimum_One_Way_BeamOrRibbed_Slab_Cantilever(LenghtofOneWaySlab):
    sump=LenghtofOneWaySlab/8
    return sump
######################################################
###### AREAS OF STEEL ########################

def AreaOfSteelSingleBar(Bar):
    A=(3.14/4)*(float(Bar)**2)
    return A
def AreaOfSteelMultBar(Bar,NumofBars):
    A=float(NumofBars)*((3.14/4)*(float(Bar)**2))
    return A
##############################################

def Spacing_layers_ReinforcementMin(Spacing_layers_Reinforcement_Min,maxSizeofAgg):
    db= 25 
    agg=(4/3)*maxSizeofAgg
    if Spacing_layers_Reinforcement_Min >= db :
        Sc= Spacing_layers_Reinforcement_Min
    if Spacing_layers_Reinforcement_Min >= agg :
        Sc= Spacing_layers_Reinforcement_Min
    elif Spacing_layers_Reinforcement_Min <= db  :
        Sc=25
    
    return Sc

######################
