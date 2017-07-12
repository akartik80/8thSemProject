import graphlab as gl

file = "repos/8thSemProject/data/testing.csv"
leads = gl.SFrame.read_csv(file)

leads.show()
input()
