'''
1   2   3   4
1   0   4   7
2   3   0   1
4   0   2   0
'''

class SpatialFilters(object):
    def read_image(self, filename):
        '''
        ret: a list extended with 0
        '''
        pic_list = open(filename, 'r', encoding='utf-8').readlines()
        self.image = [line.split() for line in pic_list]
        self.rownum = len (self.image)
        self.colnum = len (self.image[0])
        for row in range(self.rownum):
            for col in range (self.colnum):
                self.image[row][col] = int (self.image[row][col])
            self.image[row].insert (0, 0)
            self.image[row].append (0)
        self.image.append([0 for i in range (self.rownum + 2)])
        self.image.insert(0, [0 for i in range (self.rownum + 2)])

        #for x in range (self.rownum + 2):
        #    print (self.image[x])

    def get_avg(self, x, y):
        '''
        x, y: origin position
        ret: M(x, y)
        '''
        x += 1
        y += 1
        pSum = 0
        for i in range (-1, 2):
            for j in range (-1, 2):
                pSum += self.image[x + i][y + j]
        return pSum / 9.0

    def print_avg(self, x, y):
        print ("g(%d, %d) = (%d+%d+%d+%d+%d+%d+%d+%d+%d) / 9 = %.2f" % (x, y,
            self.image[x][y],self.image[x+1][y],self.image[x+2][y],
            self.image[x][y+1],self.image[x+1][y+1],self.image[x+2][y+1],
            self.image[x][y+2],self.image[x+1][y+2],self.image[x+2][y+2],
            self.get_avg (x, y)))

    
    def get_robert(self, x, y):
        x += 1 # has insterted a line
        y += 1
        return (abs (self.image[x+1][y+1]-self.image[x][y])\
                + abs (self.image[x+1][y]-self.image[x][y+1]))

    def print_robert(self, x, y):
        print ("M(%d, %d) = |%d - %d| + |%d - %d| = %d" % (x, y, 
                self.image[x+2][y+2], self.image[x+1][y+1], self.image[x+2][y+1], self.image[x+1][y+2],
                self.get_robert (x, y)))
        

    def get_sobel(self, x, y):
        '''
        ret: M(x, y)
        '''
        x += 1
        y += 1
        return (abs ((self.image[x+1][y-1] + self.image[x+1][y]*2 + self.image[x+1][y+1])\
                - (self.image[x-1][y-1] + self.image[x-1][y]*2 + self.image[x-1][y+1]))\
                + abs ((self.image[x+1][y+1] + self.image[x][y+1]*2 + self.image[x-1][y+1])\
                - (self.image[x+1][y-1] + self.image[x][y-1]*2 + self.image[x-1][y-1])))

    def print_sobel(self, x, y):
        print ("M(%d, %d) = |(%d + 2*%d + %d) - (%d + 2*%d + %d)| + |( %d + 2*%d + %d) - (%d + 2*%d + %d)| = %d"\
                % (x, y, 
                self.image[x+1][y-1], self.image[x+1][y], self.image[x+1][y+1],
                self.image[x-1][y-1], self.image[x-1][y], self.image[x-1][y+1],
                self.image[x+1][y+1], self.image[x][y+1], self.image[x-1][y+1],
                self.image[x+1][y-1], self.image[x][y-1], self.image[x-1][y-1],
                self.get_sobel (x, y)))

    def proc(self, output_file, get_func, print_func):
        '''
        output: image                     
        '''
        result_image = [[get_func (x, y) for y in range (self.colnum)] for x in range (self.rownum)]
        # print process...
        for x in range (self.rownum):
            for y in range(self.colnum):
                print_func(x, y)
        with open(output_file, 'w', encoding='utf-8') as f:
            for line in result_image:
                s_line = list(map (lambda num : "%.2f" % num, line))
                f.write("\t".join (s_line))
                f.write("\r\n")
    
    def process(self, output_file, name):
        name = name.lower()
        if name == "robert":
            self.proc(output_file, self.get_robert, self.print_robert)
        elif name == "sober":
            self.proc(output_file, self.get_sobel, self.print_sobel)
        else:
            self.proc(output_file, self.get_avg, self.print_avg)

    

















