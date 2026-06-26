# import test_package
# # import test_package.module_a
# from test_package.module_a import Module_a, module_a_func, module_var_a
import test_package

def main():
    # print(test_package.module_a.Module_a())
    # print(test_package.module_a.module_var_a)
    # test_package.module_a.module_a_func()
    # print(test_package.module_b.Module_b())
    # print(test_package.module_b.module_var_b)
    # test_package.module_b.module_b_func()
    print(test_package.Module_a())
    print(test_package.module_var_a)
    test_package.module_a_func()
    print(test_package.Module_b())
    print(test_package.module_var_b)
    test_package.module_b_func()






if __name__ == "__main__":
        main()

