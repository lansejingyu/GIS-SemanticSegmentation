# -*- coding: utf-8 -*-
# @Project : GIS-SemanticSegmentation
# @File : 639
# @IDE：PyCharm
# @Author : KT15
# @Time : 2022/10/26 15:21


import arcpy
import shapefile
from arcpy import env


def ClippingTool():
	def Workspace():  # 工作空间
		global workspace3
		workspace = input("请输入工作空间(如 E:\TIF\masaike):")
		slash = ("\\")
		env.workspace2 = r'' + workspace
		env.workspace3 = env.workspace2 + slash
		print("")

	def InputRaster():  # 选择栅格数据集
		global TifFile
		global Raster
		Raster = input('''-----选择的栅格数据集文件应在输入的工作空间文件夹内-----
请输入"输入栅格数据集"文件(如 K50F038012.tif):''')
		TifFile = r'' + env.workspace3 + Raster
		print("")

	def OutExtent():  # 选择的输出范围矢量文件
		global datasetShp
		ShpFile = input('''-----选择的用于定义裁剪所需的范围坐标文件应在输入的工作空间文件夹内-----
请输入"用于定义裁剪所需的范围坐标"矢量文件(如 test.shp)：''')
		datasetShp = shapefile.Reader(r'' + env.workspace3 + ShpFile)  # 使用shapefile库打开已有的shp文件
		print("")

	def Rectangle():  # 获取输出范围矢量文件的X 最小值、Y 最小值、X 最大值和 Y 最大值，即.shp范围(外包矩形)
		global datas
		print("当前用于定义裁剪所需的范围坐标:\n", datasetShp.bbox)
		datas = datasetShp.bbox
		print("")

	def OutFile():
		global filename
		name = input("请输入'输出栅格数据集'文件的名字(如 clip.tif):")
		filename = r'' + env.workspace3 + name
		print("")

	def ClipManagement():
		arcpy.Clip_management(TifFile, " ".join([str(i) for i in datas]), filename, "#", "#", "NONE")
		print("-----裁剪完成-----")
		print("")

	Workspace()
	InputRaster()
	OutExtent()
	Rectangle()
	OutFile()
	ClipManagement()
	ClippingTool()

ClippingTool()
