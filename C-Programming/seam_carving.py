# CS4102 Spring 2022 -- Unit C Programming
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 3 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the comment
# at the top of your java or python file. Do not seek published or online
# solutions for any assignments. If you use any published or online resources
# (which may not include solutions) when completing this assignment, be sure to
# cite them. Do not submit a solution that you are unable to explain orally to a
# member of the course staff.
#################################
# Your Computing ID: yh9vhg 
# Collaborators: N/A
# Sources: Introduction to Algorithms, Cormen
#################################
import math

class SeamCarving:
    def __init__(self):
        energy = 0
        seam = []
        return

    def diff_pixel_color(self, pixel, neighbor):
        return math.sqrt((pixel[0]-neighbor[0])**2+(pixel[1]-neighbor[1])**2+(pixel[2]-neighbor[2])**2)

    def calc_energy(self, array):
        energy_array = [[0 for j in range(len(array[0]))] for i in range(len(array))]
        for row in range(len(array)):
            for column in range(len(array[0])): 
                diff_color_sum = 0
                neighbor_count = 0 
                if row - 1 >= 0:
                    diff_color_sum += self.diff_pixel_color(array[row][column],array[row-1][column])
                    neighbor_count += 1 # top 
                    if column - 1 >= 0:
                        diff_color_sum += self.diff_pixel_color(array[row][column],array[row-1][column-1])
                        neighbor_count += 1 # top left
                    if column + 1 <= len(array[0])-1:
                        diff_color_sum += self.diff_pixel_color(array[row][column],array[row-1][column+1])
                        neighbor_count += 1 # top right 
                if row + 1 <= len(array)-1:
                    diff_color_sum += self.diff_pixel_color(array[row][column],array[row+1][column])
                    neighbor_count += 1 # bottom
                    if column - 1 >= 0:
                        diff_color_sum += self.diff_pixel_color(array[row][column],array[row+1][column-1])
                        neighbor_count += 1 # bottom left    
                    if column + 1 <= len(array[0])-1:
                        diff_color_sum += self.diff_pixel_color(array[row][column],array[row+1][column+1])
                        neighbor_count += 1 # bottom right 
                if column - 1 >= 0:
                    diff_color_sum += self.diff_pixel_color(array[row][column],array[row][column-1])
                    neighbor_count += 1 # left   
                if column + 1 <= len(array[0])-1:
                    diff_color_sum += self.diff_pixel_color(array[row][column],array[row][column+1])
                    neighbor_count += 1 # right           
                energy_measure = diff_color_sum/neighbor_count
                energy_array[row][column] = energy_measure
        
        return energy_array

    # This method is the one you should implement.  It will be called to perform
    # the seam carving.  You may create any additional data structures as fields
    # in this class or write any additional methods you need.
    # 
    # @return the seam's weight
    def run(self, image):
        energy_array = self.calc_energy(image)
        least_energy = energy_array.copy()
        for row in range(len(least_energy)-2,-1,-1): # bottom row cannot form sub-problems; start from second-last row
            for column in range(len(least_energy[0])):
                if column == 0:
                    least_energy[row][column] += min(least_energy[row+1][column],least_energy[row+1][column+1])
                elif column == len(least_energy[0])-1:
                    least_energy[row][column] += min(least_energy[row+1][column],least_energy[row+1][column-1])
                else:
                    least_energy[row][column] += min(least_energy[row+1][column],least_energy[row+1][column-1],least_energy[row+1][column+1])
        
        seam = []
        current_index = least_energy[0].index(min(least_energy[0]))
        seam.append(current_index)
        for row in range(len(least_energy)-1):
            if current_index == 0:
                if least_energy[row+1][current_index+1] == min(least_energy[row+1][current_index],least_energy[row+1][current_index+1]):
                    current_index += 1
            elif current_index == len(least_energy[0])-1:
                if least_energy[row+1][current_index-1] == min(least_energy[row+1][current_index],least_energy[row+1][current_index-1]):
                    current_index -= 1         
            else: 
                if least_energy[row+1][current_index+1] == min(least_energy[row+1][current_index],least_energy[row+1][current_index+1],least_energy[row+1][current_index-1]):
                    current_index += 1
                elif least_energy[row+1][current_index-1] == min(least_energy[row+1][current_index],least_energy[row+1][current_index-1],least_energy[row+1][current_index+1]):
                    current_index -= 1
            seam.append(current_index)   

        self.energy = min(least_energy[0])
        self.seam = seam 

        return self.energy

    # Get the seam, in order from top to bottom, where the top-left corner of the
    # image is denoted (0,0).
    # 
    # Since the y-coordinate (row) is determined by the order, only return the x-coordinate
    # 
    # @return the ordered list of x-coordinates (column number) of each pixel in the seam
    #         as an array
    def getSeam(self):
        return self.seam 

