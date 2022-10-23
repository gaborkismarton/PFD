import random

def data_zsofi(long):
    data = []
    hour = 60
    day = 24 * hour
    week = 7 * day

    for w in range(long):
        r = random.randrange(3)
        for d in range(7):
            # hóeleje
            if (w % 4 == 0 and r == d):
                rdn = random.randrange(3*hour) - 1.5*hour
                data.append([w * day + day * d + 17 * hour + 30 + rdn, [47.492244201495176, 19.05949322903217], 10000])

            if(d < 5): #munkanap
                rdn = random.randrange(20) - 10
                data.append([w * day + day * d + 7 * hour + 30 + rdn,  [47.50112086068873, 19.081786817112395],
                             500])
                rdn = random.randrange(40) - 20
                data.append([w * day + day * d + 12 * hour + 30 + rdn, [47.509147171858096, 19.095228672303605],
                             random.randrange(1000, 2200)])
                rdn = random.randrange(100)
                if (rdn > 79):
                    rdn = random.randrange(50) - 25
                    data.append([w * day + day * d + 17 * hour + rdn, [47.53396742483766, 19.10579921136512],
                                 random.randrange(10000, 20000)])
                elif (rdn > 69):
                    rdn = random.randrange(50) - 25
                    data.append([w * day + day * d + 18 * hour + 30 + rdn,
                                 random.choice([[47.55525430551007, 19.141013516794708], [47.51326928333116, 19.051623527751605], [47.504609403652566, 19.065667014706825
    ]]),                   random.randrange(15000, 35000)]
                                )
                elif (rdn > 65):
                    rdn = random.randrange(90) - 45
                    data.append([w * day + day * d + 20 * hour + 15 + rdn, [47.50274445224853, 19.136399813593794],
                                 random.randrange(5000, 12000)])
            else: # hétvége
                if (rdn > 69):
                    rdn = random.randrange(9*hour) - 4.5*hour
                    data.append([w * day + day * d + 14.5 * hour + rdn, [47.50274445224853, 19.136399813593794],
                                 random.randrange(20000, 40000)])
                elif (rdn > 54):
                    rdn = random.randrange(9*hour) - 4.5*hour
                    data.append([w * day + day * d + 14.5 * hour + rdn,
                                 random.choice([[47.55525430551007, 19.141013516794708], [47.51326928333116, 19.051623527751605], [47.504609403652566, 19.065667014706825
    ]]), random.randrange(20000, 40000)])
                elif (rdn > 14):
                    rdn = random.randrange(9*hour) - 4.5*hour
                    data.append([w * day + day * d + 14.5 * hour + rdn, [47.68598714220247, 16.58446680377768],
                                 random.randrange(15000, 25000)])
    return(data)

def data_jeff(long):
    data = []
    hour = 60
    day = 24*hour
    week = 7*day
    bp = [47.492244201495176, 19.05949322903217]

    for w in range(long):
        r = random.randrange(3)
        place = random.choice([[48.19151115713141, 16.36106226325922],
                            [50.06954758804355, 14.421844249507618],
                            [52.62971526405194, 12.122980902981277],
                            [49.31882539652234, 2.206035828924941],
                            [51.7737029040451, 0.06434816034939822],
                            [40.577829466968566, -3.7162825088908136],
                            [40.860547216020855, -73.88303548232227],
                            [37.97832990634181, -122.14096946186609],
                            [-33.343339180217406, 19.124783230165182],
                            [38.874502470526465, 128.73239621138316],
                            [22.274998156712208, 88.42833588454488],
                            [25.53570825001538, 55.322276185585550],
                            [56.414573152199814, 37.378327645284195],
                            [36.444287386405335, 51.15868670878957]])
        for d in range(7):
            # hóeleje
            if (w % 4 == 0 and r == d):
                rdn = random.randrange(3*hour) - 1.5*hour
                data.append([w * day + day * d + 10 * hour + 30 + rdn, [47.492244201495176, 19.05949322903217],
                            120000 + random.randrange(70000, 90000)])

            if(d < 5): #munkanap
                rdn = random.randrange(60)
                data.append([w * day + day * d + 8 * hour + rdn,
                            [place[0] + random.randrange(-100, 100, 5) / 10000, place[1] + random.randrange(-100, 100, 5) / 10000],
                            random.randrange(800, 1500)])
                rdn = random.randrange(120)
                data.append([w * day + day * d + 11 * hour + rdn,
                            [place[0] + random.randrange(-100, 100, 5) / 10000, place[1] + random.randrange(-100, 100, 5) / 10000],
                            random.randrange(1500, 2500)])
                rdn = random.randrange(100)
                if (rdn > 79):
                    rdn = random.randrange(60)
                    data.append([w * day + day * d + 18 * hour + rdn,
                            [place[0] + random.randrange(-100, 100, 5) / 10000, place[1] + random.randrange(-100, 100, 5) / 10000],
                                random.randrange(2000, 3000)])
                elif (rdn > 69):
                    rdn = random.randrange(120)
                    data.append([w * day + day * d + 19 * hour + rdn,
                                [place[0] + random.randrange(-100, 100, 5) / 10000, place[1] + random.randrange(-100, 100, 5) / 10000],
                                random.randrange(10000, 12000)]
                                )
            else: # hétvége
                if (rdn > 69):
                    rdn = random.randrange(4*hour)
                    data.append([w * day + day * d + 10 * hour + rdn,
                            [bp[0] + random.randrange(-100, 100, 5) / 10000, bp[1] + random.randrange(-100, 100, 5) / 10000],
                                random.randrange(10000, 20000)])
                elif (rdn > 49):
                    rdn = random.randrange(4*hour)
                    data.append([w * day + day * d + 10 * hour + rdn,
                                [bp[0] + random.randrange(-100, 100, 5) / 10000, bp[1] + random.randrange(-100, 100, 5) / 10000],
                                random.randrange(3000, 5000)])
                elif (rdn > 9):
                    rdn = random.randrange(9*hour) - 4.5*hour
                    data.append([w * day + day * d + 14.5 * hour + rdn,
                            [bp[0] + random.randrange(-100, 100, 5) / 10000, bp[1] + random.randrange(-100, 100, 5) / 10000],
                                random.randrange(5000, 9000)])
    return data