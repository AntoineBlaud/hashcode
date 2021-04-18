
# source : Livre Programmation Efficace
# Sinon j'avais déja fais un algo ou j'utilisais la technique de Monte-Carlo pour estimer l'aire en mettant le polygone dans un carré plus grand ,
# puis pour un grand nombre de point je vérifiais si le point était à l'intérieur du polygone ou non en utilisant la technique de Ray casting prouvé par le théroreme de Jordan.
# Enfin le résultat s'obtenait en appliquant un rapport de points (inter/total)*aire du carré
def main():
    n = int(input())

    p = [tuple(map(int, input().split(" "))) for _ in range(n)]
    A = 0
    for i, _ in enumerate(p):
        A += p[i - 1][0] * p[i][1] - p[i][0] * p[i - 1][1]
    print(abs(A))

if __name__ == '__main__':
    main()
