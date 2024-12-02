v = int(input("Velocity = "))
V = str(input(" m/s or km/h : "))
s = int(input("Distance = "))

def jetfighter(v, V, s):
    if v != 0 and s != 0:
        if V == "m/s":
            t = ( 2 * s ) / v
            a = v / t
            t = str(t)
            a = str(a)
            t = "t = " + t + " s"
            a = "a = " + a + " m/s2"
            print(t)
            return a
        elif V == "km/h":
            v *= 1000 / 3600
            t = ( 2 * s ) / v
            a = v / t
            t = str(t)
            a = str(a)
            t = "t = " + t + " s"
            a = "a = " + a + " m/s2"
            print(t)
            return a
       

result = jetfighter(v, V, s)
print(f"{result}")
