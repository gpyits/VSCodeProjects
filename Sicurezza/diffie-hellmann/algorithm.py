p=209345123859120219439234012846
g=17263812

#segreto di alice
a=123321

#segreto di bob
b=321123

#alice calcolo
A=pow(g, a, p)

#bob calcolo
B=pow(g, b, p)

#alice fornisce A a bob, e viceversa

#bob ora con A
kbob=pow(A, b, p)

#alice ora con B
kali=pow(B, a, p)