    if keys[K_a]:
            rend.angle -= 30 * deltaTime
        elif keys[K_d]:
            rend.angle += 30 * deltaTime

        if keys[K_w]:
            if rend.camPosition.y < 2:
                rend.camPosition.y += 5 * deltaTime
        elif keys[K_s]:
            if rend.camPosition.y > -2:
                rend.camPosition.y -= 5 * deltaTime