# set shell buffer size to 4000 width for correct display

def getDimensions(claims):
    max_x = max_y = 0

    for claim in claims:
        claim_max_x = claim["left"] + claim["width"]
        claim_max_y = claim["top"] + claim["height"]
        if claim_max_x > max_x: max_x = claim_max_x
        if claim_max_y > max_y: max_y = claim_max_y

    return max_x, max_y


def getClaims():
    claims = []
    with open("input") as f:
        for line in f.readlines():
            line = line[1:].replace("\n", "")

            split_at = line.split(" @ ")
            split_colon = split_at[1].split(": ")

            claim_id = split_at[0]
            left, top = split_colon[0].split(",")
            width, height = split_colon[1].split("x")

            claims.append({
                "claim_id": int(claim_id),
                "left": int(left),
                "top": int(top),
                "width": int(width),
                "height": int(height)
            })
    return claims


def weaveClaims(fabric, claims):
    for claim in claims:
        for x in range(claim["left"], claim["left"] + claim["width"]):
            for y in range(claim["top"], claim["top"] + claim["height"]):
                if fabric[x][y] == "    ":
                    fabric[x][y] = ("0000" + str(claim["claim_id"]))[-4:]
                else:
                    fabric[x][y] = "XXXX"
    return fabric


def getNotOverlappingClaim(fabric, claims):
    for claim in claims:
        overlaps = False
        for x in range(claim["left"], claim["left"] + claim["width"]):
            for y in range(claim["top"], claim["top"] + claim["height"]):
                if fabric[x][y] == "XXXX":
                    overlaps = True
        if not overlaps:
            return claim["claim_id"]
    return False


def main():
    claims = getClaims()
    dim_x, dim_y = getDimensions(claims)
    fabric = [["    " for x in range(dim_x)] for y in range(dim_y)]
    fabric = weaveClaims(fabric, claims)
    print(getNotOverlappingClaim(fabric, claims))


if __name__ == '__main__':
    main()
