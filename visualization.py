import graphlab as gl

url = "repos/8thSemProject/data/testing.csv"
leads = gl.SFrame.read_csv(url)

leads.show()
input()
