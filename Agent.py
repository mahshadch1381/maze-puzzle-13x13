import colors
import Environment


class Agent:
    def __init__(self, board):
        self.actions = []
        self.position = board.get_agent_pos()
        self.current_state = board.get_current_state()
        self.havePath_dfs = False
        self.bfs_actions = 0
        self.dfs_actions = 0
        self.aStar_actions = 0

    def get_position(self):
        return self.position

    def set_position(self, position, board):
        self.position = position
        board.set_agent_pos(position)
        board.update_board(self.current_state)

    def percept(self, board):
        # perception :
        # sets the current state
        # Use get_current_state function to get the maze matrix. - make your state
        self.current_state = board.get_current_state()
        board.update_board(board.get_current_state())
        pass

    def move(self, direction, board=None):
        # make your next move based on your perception
        # check if the move destination is not blocked
        # if not blocked:
        # use red color to show visited tiles.
        self.percept(board)

        # something like :
        # current_pos = self.get_position()
        # x, y = current_pos[0], current_pos[1]
        board.colorize(direction.x, direction.y, colors.red)
        li = board.get_current_state()
        # board.update_board(board)
        self.percept(board)
        # direction.set_player_here()
        '''for i in range(len(li)):
            for j in range(len(li[i])):
                if direction.x == li[i][j].x and direction.y == li[i][j].y:
                    li[i][j].isVisited = True'''
        # then move to destination - set new position
        # something like :
        new_position = {'x': direction.x,
                        'y': direction.y}
        self.set_position(new_position, board)

        pass

    @staticmethod
    def get_actions(x, y, graph):
        node = (x, y)
        list_of_actions = graph[node]
        actions = []
        actions = list_of_actions
        return actions

    def creating_graph(self):
        graph = {}
        for j in range(13):
            for i in range(13):
                if i == 0 and j == 0:
                    n1 = (i, j + 1)
                    n2 = (i + 1, j)
                    graph[(i, j)] = [n1, n2]
                    continue
                elif i == 0 and 0 < j < 12:
                    n1 = (i + 1, j)
                    n2 = (i, j + 1)
                    n3 = (i, j - 1)
                    graph[(i, j)] = [n2, n1, n3]
                    continue
                elif i == 0 and j == 12:
                    n1 = (i, j - 1)
                    n3 = (i + 1, j)
                    graph[(i, j)] = [n3, n1]
                    continue
                elif 0 < i < 12 and j == 0:
                    n1 = (i, j + 1)
                    n2 = (i + 1, j)
                    n3 = (i - 1, j)
                    graph[(i, j)] = [n3, n1, n2]
                    continue
                elif 0 < i < 12 and 0 < j < 12:
                    n1 = (i, j + 1)
                    n2 = (i + 1, j)
                    n3 = (i - 1, j)
                    n4 = (i, j - 1)
                    graph[(i, j)] = [n3, n1, n2, n4]
                    continue
                elif 0 < i < 12 and j == 12:
                    n1 = (i, j - 1)
                    n2 = (i + 1, j)
                    n3 = (i - 1, j)
                    graph[(i, j)] = [n3, n2, n1]
                    continue
                elif i == 12 and j == 0:
                    n1 = (i, j + 1)
                    n3 = (i - 1, j)
                    graph[(i, j)] = [n3, n1]
                    continue
                elif i == 12 and 0 < j < 12:
                    n1 = (i - 1, j)
                    n2 = (i, j + 1)
                    n3 = (i, j - 1)
                    graph[(i, j)] = [n1, n3, n2]
                    continue
                elif i == 12 and j == 12:
                    n1 = (i, j - 1)
                    n3 = (i - 1, j)
                    graph[(i, j)] = [n3, n1]
                    continue
        return graph

    def finding_tile(self, node, board):
        b = board.get_current_state()
        x = node[0]
        y = node[1]
        tile = b[x][y]
        return tile

    def coloring(self, way, board):
        j=0
        for i in way:
            if (i[0] + i[1]) % 2 == 0:
                board.colorize(i[0], i[1], colors.green1)
                board.update_board(board.boardArray)
                j=j+1
            else:
                board.colorize(i[0], i[1], colors.green2)
                board.update_board(board.boardArray)
                j = j + 1
    ##############################################################################################################
    def bfs(self, environment):
        graph = self.creating_graph()
        close_list = []
        open_list = []
        node = environment.get_agent_pos()
        close_list.append(node)
        open_list.append(node)
        j=0
        while open_list:
            s = open_list.pop(0)
            for node in graph[s]:
                if node not in close_list:
                    tile = self.finding_tile(node, environment)
                    if not tile.isGoal and not tile.isBlocked:
                        close_list.append(node)
                        open_list.append(node)
                        self.bfs_actions=self.bfs_actions+1
                        tile.father = s
                        if (node[0] + node[1]) % 2 == 0:
                            environment.colorize(node[0], node[1], colors.red1)
                            environment.update_board(environment.boardArray)
                            j = j+1
                        else:
                            environment.colorize(node[0], node[1], colors.red2)
                            environment.update_board(environment.boardArray)
                            j = j + 1
                    if tile.isGoal:
                        tile.father = s
                        environment.update_board(environment.boardArray)
                        self.finding_way_bfs(environment, graph)
                        return

    def finding_way_bfs(self, board, graph):
        b = board.get_current_state()
        node = (12, 0)
        tile = self.finding_tile(node, board)
        way = []
        way.append(node)
        while True:
            if node[0] == 6 and node[1] == 0:
                break
            node = tile.father
            way.append(node)
            tile = self.finding_tile(node, board)
        way.pop(0)
        print('path of bfs:', len(way))
        print('complexity of bfs:', self.bfs_actions)
        self.coloring(way, board)

    ###############################################################################################################
    def dfs(self, environment):
        visited = []
        g=[]
        close_list = set()
        graph = self.creating_graph()
        result = False
        visited.append((6, 0))
        j=0
        node = (6, 0)
        finish=False
        con = False
        while True:
            list = graph[node]
            for i in list:
                tile= self.finding_tile(i,environment)
                if tile.isGoal:
                    self.havePath_dfs=True
                    finish=True
                    tile.father = node
                    break
                if not tile.isBlocked and i not in close_list:
                    visited.append(i)
                    close_list.add(i)
                    self.dfs_actions = self.dfs_actions+1
                    tile.father = node
                    node=i
                    con=True
                    break
            if finish:
                finish=False
                break
            if con :
                con=False
                continue
            if len(visited)>0:
               visited.pop()
            if len(visited) > 0:
                node = visited.pop()
                visited.append(node)
            if len(visited)==0:
                break
        # n = self.make_dfs(visited, graph, (6, 0), result, environment, close_list)
        j=0
        for i in close_list:
            if (i[0] + i[1]) % 2 == 0:
                environment.colorize(i[0], i[1], colors.red1)
                environment.update_board(environment.boardArray)
                j = j + 1
            else:
                environment.colorize(i[0], i[1], colors.red2)
                environment.update_board(environment.boardArray)
                j = j + 1
        if self.havePath_dfs:
            node = (12, 0)
            tile = self.finding_tile(node, environment)
            way = []
            way.append(node)
            while True:
                if node[0] == 6 and node[1] == 0:
                    break
                node = tile.father
                way.append(node)
                tile = self.finding_tile(node, environment)
            way.pop(0)
            print('path of dfs:', len(way))
            print('complexity of dfs:', self.dfs_actions)
            self.coloring(way, environment)


    ########################################################################################
    def a_star(self, environment):
        graph = self.creating_graph()
        node = environment.get_agent_pos()
        visited = []
        visited.append(node)
        list = graph[node]
        ff = False
        while True:
            #self.aStar_actions = self.aStar_actions + 1
            node = self.finding_best_a(list, environment, visited)
            if node is None:
                break
            tile = self.finding_tile(node, environment)
            if tile.isGoal:
                ff = True
                break

            visited.append(node)
            list.remove(node)
            list.extend(graph[node])
            last_node = node

        # now node is goal
        j=0
        for i in visited:
            if (i[0] + i[1]) % 2 == 0:
                environment.colorize(i[0], i[1], colors.red1)
                environment.update_board(environment.boardArray)
                j = j + 1
            else:
                environment.colorize(i[0], i[1], colors.red2)
                environment.update_board(environment.boardArray)
                j = j + 1
        if ff:
            way = []
            while True:
                path = self.finding_best_a_in_child(graph[node], environment, visited, way)
                if path is None:
                    visited.remove(node)
                    way.remove(node)
                    node = way.pop()
                    way.append(node)
                    continue
                if path[0] == 6 and path[1] == 0:
                    way.append(path)
                    break
                way.append(path)
                node = path
            environment.colorize(6, 0, colors.white)
            environment.update_board(environment.boardArray)
            print('path of A*:', len(way))
            print('complexity of A*:', self.aStar_actions)
            way.pop()
            self.coloring(way, environment)
        pass

    def finding_best_a(self, list, board, visited):
        near = 90000
        result = None
        x1 = 12
        y1 = 0
        for a in list:
            x2 = a[0]
            y2 = a[1]
            tile = self.finding_tile(a, board)
            dis = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
            if not tile.isBlocked:
                if dis < near:
                    if (x2, y2) not in visited:
                        near = dis
                        result = a
                        continue
        return result

    def finding_best_a_in_child(self, list, board, visited, way):
        near = 90000
        result = None
        x1 = 12
        y1 = 0
        for a in list:
            x2 = a[0]
            y2 = a[1]
            tile = self.finding_tile(a, board)
            dis = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
            if dis < near and not tile.isBlocked:
                self.aStar_actions = self.aStar_actions + 1
                if (x2, y2) in visited and (x2, y2) not in way:
                    near = dis
                    result = a
                    continue
        return result
