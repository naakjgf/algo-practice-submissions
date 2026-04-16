class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        defDict = defaultdict(list)
        for row in board:
            items = []
            for i, item in enumerate(row):
                if item in items and item != ".":
                    return False
                else:
                    items.append(item)
                    defDict[i].append(item)

        desiredRows = [-3, -2, -1]
        while desiredRows[-1] < 8:
            desiredCol = [-3, -2, -1]
            desiredRows[0] += 3
            desiredRows[1] += 3
            desiredRows[2] += 3
            while desiredCol[-1] < 8:
                desiredCol[0] += 3
                desiredCol[1] += 3
                desiredCol[2] += 3
                items = []
                for k in desiredRows:
                    for i in desiredCol:
                        if board[k][i] not in items and board[k][i] != ".":
                            items.append(board[k][i])
                        elif board[k][i] in items:
                            return False

        for x in defDict.keys():
            items = []
            for item in defDict[x]:
                if item in items:
                    return False
                if item != ".":
                    items.append(item)

        return True