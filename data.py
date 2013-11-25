''' Sample data of various forms'''

# [begin generated data]
# data runs from x = 1 to 25 with N(0,1) error added unless otherwise stated
# all functions use real parameters, but scaled to get about 3-5% error

''' f(x) = x '''
identity = [1.78911, 0.62553, 2.01295, 5.00472, 5.33279, 6.99715, 8.56787,
7.61004, 8.81425, 9.42831, 9.79978, 10.1006, 11.3555, 12.6809,
14.3768, 14.8353, 16.7808, 16.0585, 19.5048, 20.0614, 21.8866,
21.4971, 23.3099, 26.9678, 25.1561]

# (-4.9*x^2 + 250*x)/100
''' trajectory of a bullet fired straight up at 250 m/s (in hundreds of meters) - no friction'''
bullet = [2.63506, 5.05142, 7.58814, 8.36867, 9.89025, 12.6742, 14.9608,
17.1504, 18.25, 19.6037, 21.9566, 22.7667, 24.1432, 24.437, 25.9185,
26.0995, 27.685, 28.1738, 28.8522, 30.8774, 29.6592, 30.8546,
30.6832, 32.2816, 31.9304]

#  E^(-t/10) * (10 Cos[t] + 21 Sin[t])
''' damped harmonic oscillator: initial position of x = 10 meters,
    initial velocity of 20 meters/second
    friction and spring coefficients that made a nice 'wavy' trajectory
'''
oscillator = [20.4388, 11.1238, -4.39306, -15.2666, -8.83603, 2.95402, 10.6062,
7.45964, 0.1444, -8.34118, -7.56731, -3.08952, 3.9061, 4.388,
1.12161, -3.26213, -5.39157, 0.578177, 3.57381, 3.07006, 2.1935,
-1.25449, -2.06437, -0.404703, 1.84]

# 35*E^(Log[2]/2*-t)
''' Half life of iodinated MRI contrast (2 hours, 35mL dose)'''
half_life = [25.4415, 18.4398, 11.4443, 9.24007, 7.12872, 5.06899, 2.16361,
2.63675, 1.94151, 1.95126, 1.40326, 0.608226, -1.17869, 0.413052,
1.25293, -0.239452, -0.306854, 0.866765, 2.29676, 0.540789, 0.448099,
1.94394, -1.06473, -0.650251, -0.0989802]

# 500*.14 x/(1.5 + x)
''' Enzyme kinematics in the Michaelis-Menten model (500 moles of Chymotrypsin)'''
enzyme = [26.4847, 40.5327, 46.0789, 49.2011, 52.8957, 55.7521, 58.6808,
60.4513, 60.7341, 62.8158, 61.3433, 63.3663, 61.8981, 64.8282,
64.0561, 66.5473, 62.2379, 66.023, 65.5182, 66.5476, 63.9284,
64.9167, 65.3217, 66.3098, 66.0502]

# (200 E^(t/2))/(100 + 2 (-1 + E^(t/2)))
''' logistic population growth; carrying capacity of 100, initial population 2, r=1/2'''
population = [0.93123, 2.74321, 4.8985, 7.8035, 11.3275, 20.4799, 27.5689, 41.563,
52.8436, 63.7758, 73.2494, 83.4251, 89.4056, 92.3097, 92.5954,
97.8716, 98.5626, 98.9755, 99.8215, 99.2332, 99.3806, 99.377,
98.2133, 98.2611, 99.4528, 99.5506]

# (8400. E^(-0.06 t))/(1 + 70 E^(-0.06 t))^2
''' Hubbert peak oil curve (using his actual 1956 prediction parameters) 1900-1999'''
hubbert = [2.47792, 1.66126, 1.29464, 1.45541, 1.91928, 1.7015, 1.76235,
4.30153, 1.97041, 2.10179, 1.81996, 3.04693, 2.62143, 3.30383,
3.79316, 1.92067, 2.82471, 5.59357, 4.40778, 3.93959, 5.39259,
6.37814, 5.35129, 5.40325, 7.37639, 7.4691, 5.38406, 7.84323,
6.74289, 7.62103, 8.37723, 9.33054, 10.2963, 11.6003, 11.2796,
10.397, 10.4913, 11.8025, 11.9236, 12.5397, 14.4816, 13.6076,
15.3405, 14.3081, 15.7918, 17.7835, 17.2168, 18.9163, 19.1872,
20.0249, 19.9648, 21.1897, 22.8019, 22.9909, 22.5857, 24.5689,
24.2836, 25.4936, 26.5273, 26.3809, 27.4156, 26.1805, 27.602,
27.5581, 30.7774, 31.1848, 28.5914, 28.4669, 30.3312, 28.8426,
28.6371, 29.5687, 29.8155, 28.7657, 29.9785, 30.1336, 29.7337,
28.2382, 29.3158, 30.1079, 28.3529, 27.7694, 27.8894, 26.0385,
26.7129, 23.8395, 25.9024, 23.076, 23.1135, 22.1821, 19.8199,
20.8983, 20.1177, 20.8961, 19.9535, 18.3276, 18.9358, 17.7117,
14.3427, 15.0427]

# 1200*E^(-(x - 100)^2/(2*15^2))/Sqrt[2*Pi*15^2]
''' sample of 1200 people; number of people with IQ = x (x from 50 to 149)'''
iq = [1.37566, -0.899212, 0.588958, 0.613957, 0.67308, -0.240921,
0.731746, -0.843862, 0.751699, 2.28214, 1.1486, 1.79116, 1.52875,
0.731629, 0.92356, 0.885134, 3.16097, 2.0485, 3.64488, 5.75456,
2.74511, 5.31514, 6.20542, 5.97012, 5.67394, 7.79638, 8.75234,
10.0676, 11.318, 11.2768, 13.3625, 15.3951, 15.9025, 16.107, 17.5867,
18.7222, 20.315, 22.2963, 22.4823, 23.189, 26.4283, 27.3979, 27.9506,
29.7377, 29.606, 31.2871, 30.71, 30.4486, 31.0699, 31.9716, 32.1896,
29.7381, 34.3681, 30.9706, 32.4324, 30.443, 30.3364, 27.4615,
29.8134, 26.7659, 24.6115, 23.9923, 22.0388, 22.2489, 20.6744,
19.4673, 17.7974, 14.4444, 15.4269, 13.9571, 11.2766, 12.2884,
12.5268, 10.2402, 8.29488, 8.5, 8.17637, 5.07055, 5.53863, 5.42583,
4.69913, 1.45667, 3.19444, 4.62804, 2.04399, 2.32917, 0.92009,
1.79705, 0.223042, 2.75132, 0.464375, -0.00995843, 0.0591558,
1.28974, -0.879947, -0.156615, 0.435686, 0.447098, -1.62389, 0.962722]

# [end generated data]; possible additional datasets: Gompertz_curve, ?

''' fibonacci sequence (no error) '''

fibonacci = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,
2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025]

'''US GDP (millions) 1900-1999'''
us_gdp = [
20567,
22269,
24062,
25930,
25681,
28788,
31037,
33851,
30133,
32229,
33423,
34343,
37384,
39140,
36479,
38675,
49638,
59702,
75835,
78333,
88393,
73603,
73432,
85414,
86947,
90575,
96949,
95544,
97365,
103600,
91200,
76500,
58700,
56400,
66000,
73300,
83800,
91900,
86100,
92200,
101400,
126700,
161900,
198600,
219800,
223000,
222200,
244100,
269100,
267200,
293700,
339300,
358300,
379300,
380400,
414700,
437400,
461100,
467200,
506600,
526400,
544800,
585700,
617800,
663600,
719100,
787700,
832400,
909800,
984400,
1038300,
1126800,
1237900,
1382300,
1499500,
1637700,
1824600,
2030100,
2293800,
2562200,
2788100,
3126800,
3253200,
3534600,
3930900,
4217500,
4460100,
4736400,
5100400,
5482100,
5800500,
5992100,
6342300,
6667400,
7085200,
7414700,
7838500,
8332400,
8793500,
9353500]

'''US population (millions) 1900-1999'''
us_pop = [
76.212,
77.68,
79.176,
80.701,
82.255,
83.839,
85.453,
87.099,
88.776,
90.486,
92.229,
93.523,
94.836,
96.167,
97.516,
98.885,
100.273,
101.68,
103.107,
104.554,
106.022,
107.626,
109.254,
110.908,
112.586,
114.29,
116.019,
117.775,
119.557,
121.366,
123.203,
124.071,
124.945,
125.825,
126.712,
127.605,
128.504,
129.41,
130.321,
131.24,
132.165,
133.966,
135.792,
137.643,
139.519,
141.421,
143.349,
145.303,
147.283,
149.291,
151.326,
153.917,
156.552,
159.232,
161.958,
164.731,
167.551,
170.42,
173.337,
176.305,
179.323,
181.588,
183.881,
186.204,
188.555,
190.937,
193.348,
195.79,
198.263,
200.766,
203.302,
205.515,
207.752,
210.013,
212.299,
214.609,
216.945,
219.307,
221.694,
224.107,
226.546,
228.67,
230.815,
232.979,
235.164,
237.369,
239.595,
241.842,
244.11,
246.399,
248.71,
251.802,
254.933,
258.103,
261.312,
264.561,
267.85,
271.18,
274.552,
277.966]