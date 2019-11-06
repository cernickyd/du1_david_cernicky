def vypis_ahoj(pocet):
    for i in range(pocet):
        print("Ahoj!")
vypis_ahoj(1)

def sestiuhelnik(a,r):
    from turtle import left, right, forward, exitonclick, speed
    speed('fastest')
    #   pocitadlo
    k = 1

    for k in range(r):
        k = k + 1
        print(k)
        for j in range(r):
            for i in range(8):
                forward(a)
                left(60)
            right(120)
        right(120)
        if k == r:
            break
        for l in range(r):
            forward(a)
            right(60)
            forward(a)
            left(60)
        for m in range(2):
            forward(a)
            left(60)

    exitonclick()
#   a = delka strany
#   r = počet opakování cyklu
sestiuhelnik(20,10)