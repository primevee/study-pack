#include <Python.h>

/**
 * print_python_list_info - print list infor
 * @p: python object
 */
void print_python_list_info(PyObject *p)
{
	int i;
	int size = Py_SIZE(p);
	int alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
