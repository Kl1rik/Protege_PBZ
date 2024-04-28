

from py2neo import Graph

# Подключение к Neo4j (замените URL, логин и пароль на ваши)
graph = Graph("bolt://localhost:7687", user="neo4j", password="testtest")

# Запрос на получение подграфа
query = """
MATCH (petr:node{name:"Пётр"})-[link:loves]->(o)-[*]->(x)
RETURN o, labels(x), x;
"""


def substructure_determination(node_name):
    substructure = """
        MATCH path = (startNode {name: $name})-[*]->()
        RETURN path
        """

    result = graph.run(substructure, name=node_name)
    for record in result:
        print(record)


def text_reader(text):

    #Делим сообщение на отдельные связи и вершины
    text_units = text.split(',')

    #Создаем массив, который будет на 0 элементе содержать название связи, а на 1 - название вершины
    link_and_node = []

    #Массив пар, содержит в себе все собранные пары (связь + вершина)
    array_of_pairs = []

    for unit in text_units:
        if '*' in unit:
            link_and_node = unit.split('*')
            array_of_pairs.append(link_and_node)

        elif 'is' in unit and 'ostis' not in unit:
            link_and_node = ['is', unit.split('is')[1]]
            array_of_pairs.append(link_and_node)

    for array in array_of_pairs:
        print(array)
    
    return array_of_pairs


def builder(array_of_pairs):
    done_arrays = []
    dict_of_tuples = {}
    tuple_indexes = []

    main_node = ''

    for index, array in enumerate(array_of_pairs):

        if 'основной идентификатор' in array[0].strip().lower():
            main_node = array[1]
            query = """
                            Create (:main {name: $name})
                            """
            result = graph.run(query, name=main_node)


    for array in array_of_pairs:
        target_link = array[0].strip().lower()
        target_counter = 0
        lost_index = 0

        # Массив картежа
        array_of_tuple = []

        for index, array in enumerate(array_of_pairs):
            if target_link in array[0]:
                target_counter += 1
                if target_counter == 1:
                    lost_index = index
                if target_counter == 2:
                    array_of_tuple.append(lost_index)
                    array_of_tuple.append(index)
                elif  target_counter > 2:
                    array_of_tuple.append(index)

        if array_of_tuple:
            dict_of_tuples[target_link] = array_of_tuple
            tuple_indexes += array_of_tuple
    tuple_indexes = set(tuple_indexes)

    print(dict_of_tuples)
    print(tuple_indexes)

    #Отдельное создание кортежей
    tuple_keys = list(dict_of_tuples.keys())

    for tuple_key in tuple_keys:
        array_of_indexes = dict_of_tuples[tuple_key]
        temp_array = []
        relation = ''

        for index in (array_of_indexes):
            temp_array.append(array_of_pairs[index][1])
            relation = array_of_pairs[index][0]

        relation = relation.strip().replace(' ', '_').replace('-', '_')

        tuple_ = 'tuple'
        #Создание запросов для кортежей вплоть до 5 вершин
        query_2 = """CREATE (:tuple {name: 'tuple', node_1: $node_1, node_2: $node_2})"""
        query_3 = """CREATE (:tuple {name: 'tuple', node_1: $node_1, node_2: $node_2, node_3: $node_3})"""
        query_4 = """CREATE (:tuple {name: 'tuple', node_1: $node_1, node_2: $node_2, node_3: $node_3, node_4: $node_4})"""
        query_5 = """CREATE (:tuple {name: 'tuple', node_1: $node_1, node_2: $node_2, node_3: $node_3, node_4: $node_4, node_5: $node_5})"""


        amount = len(temp_array)
        if amount == 2:
            node_1 = temp_array[0]
            node_2 = temp_array[1]

            query = query_2
            result = graph.run(query, node_1 = node_1, node_2 = node_2)

        elif amount == 3:
            node_1 = temp_array[0]
            node_2 = temp_array[1]
            node_3 = temp_array[2]

            query = query_3
            result = graph.run(query, node_1=node_1, node_2=node_2, node_3 = node_3)

        elif amount == 4:
            node_1 = temp_array[0]
            node_2 = temp_array[1]
            node_3 = temp_array[2]
            node_4 = temp_array[3]

            query = query_4
            result = graph.run(query, node_1=node_1, node_2=node_2, node_3=node_3, node_4 = node_4)

        elif amount == 5:
            node_1 = temp_array[0]
            node_2 = temp_array[1]
            node_3 = temp_array[2]
            node_4 = temp_array[3]
            node_5 = temp_array[4]

            query = query_5
            result = graph.run(query, node_1=node_1, node_2=node_2, node_3=node_3, node_4 = node_4, node_5 = node_5)

        print(relation,"Это элементы tuple")
        query_ = (
            f"MATCH (node1:tuple {{name: '{tuple_}'}}), "
            f"(node2:main {{name: '{main_node}'}})"
            f"create (node1)-[r:{relation}]->(node2) "
        )


        result = graph.run(query_)




    array_of_nodes_names = []
    dict_of_link_names = {}
    main_node = "основной_идентификатор"
    for index, array in enumerate(array_of_pairs):

        if 'основной идентификатор' in array[0].strip().lower():
            main_node = array[1]
            array_of_nodes_names.append(main_node)


        elif index not in tuple_indexes:
            name = array[1]
            name = name.strip().replace(' ', '_').replace('-', '_')
            relation = array[0]
            relation = relation.strip().replace(' ', '_').replace('-', '_')
            array_of_nodes_names.append(name)
            dict_of_link_names[name] = relation


            query = """
                    Create (:node {name: $name})
                    """
            result = graph.run(query, name=name)


    print(array_of_nodes_names,"Это список с tuple")

    relation_keys = list(dict_of_link_names)

    for index, node in enumerate(array_of_nodes_names):


        if node in relation_keys:
            relation = dict_of_link_names[node]
        else:
            relation = 'это'

        query = (
            f"MATCH (node1: node {{name: '{node}'}}), "
            f"(node2:main {{name: '{main_node}'}})"
            f"create (node1)-[r:{relation}]->(node2) "
        )

        result = graph.run(query)




            # result = graph.run(query).data(name)
            # print(result)



# substructure_determination("Щенок")


# query = """
# MATCH (petr:node{name:"Пётр"})-[link:loves]->(o)-[*]->(x)
# RETURN об x;
# """



# query = """MATCH (n) RETURN n"""


#
#
# query = """
# MATCH (petr:node{name:"Пётр"})-[link:loves]->(o)-[r]->(x)
# RETURN type(r)
# """
#
# print('='*20)
#
# result = graph.run(query).data()
# print(result)
#
#

# Вывод результата
# for record in result:
#     print(f"Узел 'petr': {record['petr']}")
#     print(f"Связанный узел: {record['owned']}")



if __name__ == "__main__":
    text = "декомпозиция sc-модели* Пользовательский интерфейс IMS, декомпозиция sc-модели* База знаний IMS, Is базовая декомпозиция* of Собственное Я, is ostis-система, основной идентификатор* IMS, декомпозиция sc-модели* Машина обработки знаний IMS, is sc-модель компьютерной системы, первый домен* дочерняя ostis-система*"
    array_of_pairs = text_reader(text)
    builder(array_of_pairs = array_of_pairs)




    # my_array = list(range(19, 75))
    # for num in my_array:
    #     query = (
    #         f"match(n) WHERE ID(n) = {num} "
    #         f"DETACH DELETE n; "
    #     )
    #
    #     result = graph.run(query)

