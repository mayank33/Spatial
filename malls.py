import math
#objective : find the distance between the nearest existing mall
result_malls = "open_spaces_commercial_sorted"
existing_malls = "malls_crs"

layers = iface.legendInterface().layers()

existm = 0
newm = 0

for i in layers:
    if i.name() == existing_malls:
        existm = i
    if i.name() == result_malls:
        newm = i

print "Existing Malls :" , existm.name()
print "Predicted Malls : " , newm.name()

ids = []
newm_features = newm.getFeatures()        
provider = existm.dataProvider()

spIndex = QgsSpatialIndex() #create spatial index object

feat = QgsFeature()
fit = provider.getFeatures() #gets all features in layer

# insert features to index
while fit.nextFeature(feat):
    spIndex.insertFeature(feat)
selection = []
rank = 1
dist_st = []
#print type(newm_features)
for i in newm_features:
    point = i.geometry()
    pt = point.asPoint()
    nearestIds = spIndex.nearestNeighbor(pt,1) # we need only one neighbour
    featureId = nearestIds[0]
    fit2 = existm.getFeatures(QgsFeatureRequest().setFilterFid(featureId))
    ftr = QgsFeature()
    fit2.nextFeature(ftr)
    mx = pt.x()
    my = pt.y()
    rx = ftr.geometry().asPoint().x()
    ry = ftr.geometry().asPoint().y()
    nx = mx - rx
    ny = my - ry
    dist = math.sqrt(nx**2 + ny**2)
    dist_st.append([dist,i.id()])
    rank += 1
    selection.append(ftr.id())

existm.setSelectedFeatures(selection)
num = 1
dist_st.sort(reverse=True)
for i in dist_st:
    newm.changeAttributeValue(i[1], 87, num)
    num += 1