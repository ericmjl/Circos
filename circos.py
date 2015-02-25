import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.patches as patches
import math

from matplotlib.path import Path

class CircosPlot(object):
	def __init__(self, nodes, edges, radius):
		self.nodes = nodes # Dictionary of nodes
		self.edges = edges # Dictionary of Edges
		self.radius = radius
		self.fig = plt.figure(figsize=(8,8))
		self.ax = self.fig.add_subplot(111)
		self.node_radius = self.radius*0.05
		self.ax.set_xlim(-radius*1.05, radius*1.05)
		self.ax.set_ylim(-radius*1.05, radius*1.05)
		self.ax.xaxis.set_visible(False)
		self.ax.yaxis.set_visible(False)
		for k in self.ax.spines.keys():
			self.ax.spines[k].set_visible(False)


	def draw(self):
		self.add_nodes()
		self.add_edges()

	def add_nodes(self):
		r = self.radius
		node_r = self.node_radius
		for node in self.nodes:
			theta = self.node_theta(node)
			x, y = get_cartesian(r, theta)
			node_patch = patches.Ellipse((x,y), node_r, node_r, facecolor='red')
			self.ax.add_patch(node_patch)


	def draw_edge(self, node1, node2):
		start_theta = self.node_theta(node1)
		end_theta = self.node_theta(node2)
		middle_theta = float((start_theta + end_theta))/2.0

		verts = [get_cartesian(self.radius, start_theta), (0,0), get_cartesian(self.radius,end_theta)]
		codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4]

		path = Path(verts, codes)

		patch = patches.PathPatch(path, lw=1, facecolor='none')
		self.ax.add_patch(patch)


	def node_theta(self, node):
		''' Maps node to Angle '''
		i = self.nodes.index(node)
		theta = i*2*np.pi/len(self.nodes)

		return theta

	def add_edges(self):
		for start, end in self.edges:
			self.draw_edge(start, end)


def get_cartesian(r, theta):
	x = r*np.sin(theta)
	y = r*np.cos(theta)

	return x, y