#1
x = [100,110,120,130,140,150]
newlist=[]
for a in x:
   if x in a:
      newlist.append(x)

print(newlist)

#2
def divisible_by_three(n):
    if n==3:
     print("it is divisible_by_three")
    else:
        divisible_by_three(n==3)
#3
def flatten():
    x = [[1,2],[3,4],[5,6]]
new_list=[]
for new_list in x:
    for x in new_list:
        new_list.append(x)
print(new_list)

def smallest():
    y=[3,6,8,2,4,1,5,7]
    y.sort()
    print(y)
smallest()
##6
def divisible_by_seven():
 k=(100,200)
 if k==7:
     return(k)
divisible_by_seven()


#

#5
def list():
  x = ['a','b','a','e','d','b','c','e','f','g','h']
final_x={}
{final_x.append(n) for n in x if n not in final_x}
print(final_x)
list()



#7
def greeting():
             students = [
         {"age": 19, "name": "Eunice"},
          {"age": 21, "name": "Agnes"},
          {"age": 18, "name": "Teresa"}, 
         {"age": 22, "name": "Asha"}
         ]
      
    


 
# #8
class Rectangle():

    def __init__(self, length, width):
        self.length = length
        self.width  = width

    def area(self):
        return self.length*self.width
rectangle = Rectangle(34, 18)
print(rectangle.area())

def P(self):
         return self.length+self.width

perimeter = Rectangle(34, 18)
print(perimeter.p())




   


