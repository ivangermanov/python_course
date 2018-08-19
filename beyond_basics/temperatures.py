temperatures = [10,-20,-289,100]
def c_to_f(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"
    else:
        return c * 9/5 + 32

with open(r"C:\Users\ivang\Desktop\python_course\beyond_basics\temperatures.txt", "w") as temp_file:
    for t in temperatures:
        temp_file.write(str(c_to_f(t))+'\n')