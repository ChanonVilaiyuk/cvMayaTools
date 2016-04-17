# cv utils v.1.0

import maya.cmds as mc
import maya.mel as mm

def transferUvToOrig() :

    '''
    Transfer UVs from first selected object to orig shape of last selected object.
    '''

    sels = mc.ls( sl=True )

    targetShapes = mc.listRelatives( sels[-1] , f=True , s=True )

    origShapes = []

    for targetShape in targetShapes :
        if mc.getAttr( '%s.intermediateObject' % targetShape ) and 'Orig' in targetShape :
            origShapes.append( targetShape )

    if len( origShapes ) == 1 :

        origShape = origShapes[0]
        mc.setAttr( '%s.intermediateObject' % origShape , 0 )

        mc.select( sels[0] , r=True )
        mc.select( origShape , add=True )

        cmd = 'transferAttributes -pos 0 -nml 0 -uvs 2 -col 2 -spa 4 -suv "map1" -tuv "map1" -sm 3 -fuv 0 -clb 1;'
        mm.eval( cmd )
        mc.delete( origShape , ch=True )
        mc.setAttr( '%s.intermediateObject' % origShape , 1 )
        mc.select( sels , r=True )

    else :
        print '%s has none or more than 1 orig shape.' % sels[1]