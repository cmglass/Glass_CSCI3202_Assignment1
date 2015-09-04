import queue
import unittest
TestIntegers=[1,2,3,5,8,10,20,30,1000,35];
TreeInts={1,1,2,2,10,100,30,5,8,100,5}

class int_Queue(queue.Queue):
	def __init__(self):
		queue.Queue.__init__(self)
	def put(self,item,*block,**timeout):
		if(isinstance(item,int)):
			queue.Queue.put(self,item,block,timeout)
		else:
			return("item is not of type int")

	def get(self,*block,**timeout):
		g=queue.Queue.get(self,block,timeout)
		print(g)
		return g

class stack():
	def __init__(self):
		self.L=[]
	def push(self,data):
		if(isinstance(data,int)):
			self.L.append(data)
	def pop(self):
		return self.L.pop()
	def checkSize(self):
		return len(self.L)

class node():

	def __init__(self,key,left,right,parent):
		self.key=key
		self.left=left
		self.right=right
		self.parent=parent

class binary_tree():

	def __init__(self):
		self.root=node(0,None,None,None)

	def _find(self,Value,N):
		if(N.key==Value):
			return N
		elif(N.left):
			out=self._find(Value,N.left)
			if(out!=0):
				return out
		elif(N.right):
			out=self._find(Value,N.right)
		else:
			return 0;
		return out;

	def add(self,value,parentValue):
		parent=self._find(parentValue,self.root);
		if(parent):
			N=node(value,None,None,parent)
			if(parent.left):
				if(parent.right):
					print("Parent already has Two children");
					return 0;
				else:
					parent.right=N
					return 1
			else:
				parent.left=N
				return 1


	def delete(self,value):
		D=self._find(value,self.root)
		if(D):
			if(D.left or D.right):
				print("Node has children NOT DELETED")
			else:
				if(D.parent.left==D):
					D.parent.left=none
				else:
					D.parent.rght=none
		else:
			print("Value not in tree")

	def recursive_print(self,n):
		if(n):
			print("[",n.key)
			self.recursive_print(n.left)
			self.recursive_print(n.right)
			print("]")

	def Print(self):
		self.recursive_print(self.root)




class graph:
	def __init__(self):
		self.verts={}

	def addVertex(self,V):
		self.verts.update({V:[]})

	def addEdge(self,V1,V2):
		r=0
		for x in self.verts.keys():
			if x==V1:
				self.verts[x].append(V2)
				r=1
			elif x==V2:
				self.verts[x].append(V1)
				r=1
		return r
			

	def findVertex(self,V):
		for x in self.verts.keys():
			if x==V:
				print("value found:",x)
				return self.verts
		return 0


class QueueTest(unittest.TestCase):
	def test_int(self):
		self.Q=int_Queue()
		self.assertEqual(self.Q.put("test"),"item is not of type int")
	def test_FuncTest(self):
		self.Q=int_Queue()
		for x in TestIntegers:
			self.Q.put(x)
		for x in TestIntegers:
			self.assertEqual(self.Q.get(),x);

class StackTest(unittest.TestCase):
	def setUp(self):
		self.S=stack()

	def test_Add(self):
		for x in TestIntegers:
			self.S.push(x)
		self.assertEqual(self.S.checkSize(),10)

	def test_Pop(self):
		if(not self.S.checkSize()):
			for x in TestIntegers:
				self.S.push(x)

		for x in reversed(TestIntegers):
			self.assertEqual(self.S.pop(),x)


class TreeTest(unittest.TestCase):
	def setUp(self):
		self.B=binary_tree()
		self.B.add(1,0)

	def test_Add(self):
		for x,y in zip(TestIntegers, TreeInts):
			self.B.add(x,y)
		#self.B.Print();

	def test_Delete(self):
		self.B.delete(2)
		self.B.delete(30)
		self.B.Print()


class GraphTest(unittest.TestCase):
	def setUp(self):
		self.G=graph()
		self.G.addVertex(8)
		self.G.addVertex(1)
		self.G.addVertex(2)
		self.G.addVertex(3)
		self.G.addVertex(4)
		self.G.addVertex(5)
		self.G.addVertex(10)
		self.G.addVertex(20)
		self.G.addVertex(25)
		self.G.addVertex(11)

	def test_Edge(self):
		self.assertTrue(self.G.addEdge(1,2))
		self.assertTrue(self.G.addEdge(1,3))
		self.assertTrue(self.G.addEdge(1,4))
		self.assertTrue(self.G.addEdge(2,5))
		self.assertTrue(self.G.addEdge(2,10))
		self.assertTrue(self.G.addEdge(10,20))
		self.assertTrue(self.G.addEdge(11,20))
		self.assertTrue(self.G.addEdge(11,25))
		self.assertTrue(self.G.addEdge(1,25))
		self.assertTrue(self.G.addEdge(10,25))
		self.assertTrue(self.G.addEdge(2,4))
		self.assertTrue(self.G.addEdge(4,20))
		self.assertTrue(self.G.addEdge(4,10))
		self.assertTrue(self.G.addEdge(10,8))
		self.assertTrue(self.G.addEdge(4,8))
		self.assertTrue(self.G.addEdge(2,4))
		self.assertTrue(self.G.addEdge(3,5))
		self.assertTrue(self.G.addEdge(5,25))
		self.assertTrue(self.G.addEdge(5,10))
		self.assertTrue(self.G.addEdge(1,11))
		self.assertTrue(self.G.addEdge(4,5))

	def test_Find(self):
		self.assertTrue(self.G.findVertex(1))
		self.assertTrue(self.G.findVertex(5))
		self.assertTrue(self.G.findVertex(10))
		self.assertTrue(self.G.findVertex(2))
		self.assertTrue(self.G.findVertex(4))

if __name__=='__main__':
	unittest.main()

print('done')
