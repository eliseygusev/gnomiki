x, y = map(float, input().split())
is_land_successfull  = (0.5 * x**2 + y**2 < 1) and (y < 0.5 * abs(x) + 0.5) and \
                       ((x - 0.5)**2 + y**2 > 0.3) and ((x + 0.5)**2 + y**2 > 0.3) 
print('YES' if is_land_successfull else 'NO')
