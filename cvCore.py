import maya.cmds as mc
import maya.mel as mm

class MeshInfo() :
	def __init__(self, inputMesh) :

		self.inputMesh = inputMesh
		self.mesh = self.shape()

	def __repr__(self) :
		return self.inputMesh

	def __str__(self) :
		return self.inputMesh

	def shape(self) :
		objType = mc.objectType(self.inputMesh)
		mesh = str()

		if objType == 'mesh' :
			mesh = self.inputMesh

		if objType == 'transform' :
			result = mc.listRelatives(self.inputMesh, s = True)

			if result :
				mesh = result[0]

		return mesh

	def transform(self) :
		objType = mc.objectType(self.inputMesh)
		transform = str()

		if objType == 'mesh' :
			result = mc.listRelatives(self.inputMesh, p = True)

			if result :
				transform = result[0]

		if objType == 'transform' :
			transform = self.inputMesh

		return transform


	def orig(self) :
