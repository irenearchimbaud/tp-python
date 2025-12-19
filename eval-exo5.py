def swap_et_statistiques(nombres):
    mini, maxi = min(nombres), max(nombres)
    mini, maxi = maxi, mini
    moyenne = sum(nombres)/len(nombres)
    return (mini, maxi, moyenne, len(nombres))

print(swap_et_statistiques([1,2,3,4,5]))

points = [(1,2,3), (4,5,6), (7,8,9), (10,11,12)]

#on sé pare en 3 listes
xs, ys, zs = zip(*points)
print(xs, ys, zs)

# on crée des tuples x et y en ignorant z
xy = [(x,y) for x,y,_ in points]
print(xy)

# on fait la somme
somme_x = sum(xs)
somme_y = sum(ys)
somme_z = sum(zs)
print(somme_x, somme_y, somme_z)