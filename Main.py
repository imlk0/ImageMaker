#coding:utf-8

'''
Created on 2017年7月2日

@author: KB5201314
'''

from PIL import Image
import sys



class main(object):


    def get_first_img(self):
        str = raw_input("表面图片：")
        
        self.fim = Image.open(str).convert('L')
        self.fim_size = self.fim.size
        
        print "(宽度，高度)",self.fim.size
        #self.fim.show()
    
    def get_next_img(self):
        str = raw_input("隐藏图片：")
        
        self.nim = Image.open(str).convert('L')
        self.nim_size = self.nim.size
        
        print "(宽度，高度)",self.nim.size

    
    def make_new_img(self):
        
        mx = int(raw_input("生成文件宽度："))
        my = int(raw_input("高度："))
        self.new_size = (mx,my)
        self.new = Image.new("RGBA",self.new_size,(255,255,255,0))
        
        
    
    def write_new_img(self):
        for y in range(0,self.new_size[1]):#每一行
            
            i = int((y*100.0)/self.new_size[1] )
            sys.stdout.write("[" + ("#" * int(i/2) ) + (" " * (50-int(i/2))) +"]" + str(i) + "%" +"\r")
            sys.stdout.flush()
            
            for x in range(0,self.new_size[0]):
                
                if ((x + y)% 2) == 0:#取第一张图
                    p = self.fim.getpixel( (  int(x * self.fim_size[0] /self.new_size[0]) ,  int(y * self.fim_size[1] /self.new_size[1]) ) )
                    self.new.putpixel((x,y), (0,0,0,(255-p)))
                    
                else:#取第二张图片
                    p = self.nim.getpixel( (  int(x * self.nim_size[0] /self.new_size[0]) ,  int(y * self.nim_size[1] /self.new_size[1]) ) )
                    self.new.putpixel((x,y), (255,255,255,p))
                    
        
        
        
        

if __name__ == "__main__":
    
    m = main()
    
    m.get_first_img()
    
    m.get_next_img() 
    
    
    m.make_new_img()
    m.write_new_img()
    m.new.save("aim.png", 'png')
    
