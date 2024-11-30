immutable_var = 1, 2, 'a', 'b'
print("Immutable tuple:", immutable_var)
# immutable_var[0] = 'Modified' # кортежи являются неизменяемыми структурами, в связи с этим невозможно внести изменения;
mutable_list = [1, 2, 'a', 'b', 'c']
mutable_list[4] = 'Modified'
print("Mutable list:", mutable_list)